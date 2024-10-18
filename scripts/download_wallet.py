# Python script run in terminal to download wallet from private endpoint Object Storage Bucket
import oci

# Path to the OCI configuration file
config_path = "/home/datascience/.oci/config"

# Initialize the OCI configuration
config = oci.config.from_file(file_location=config_path)

# Create a service client for Object Storage
object_storage_client = oci.object_storage.ObjectStorageClient(config)

# Get the namespace
namespace = object_storage_client.get_namespace().data

# List all compartments accessible by the user
identity_client = oci.identity.IdentityClient(config)
compartment_id = config["tenancy"]  # Root compartment (tenancy)

compartments = oci.pagination.list_call_get_all_results(
    identity_client.list_compartments,
    compartment_id,
    compartment_id_in_subtree=True
).data

# Add root compartment to the list of compartments
compartments.append(oci.identity.models.Compartment(id=compartment_id))

# Define the compartment and bucket names
compartment_name = "Data_Engineering_Project"
bucket_name = "bucket-wallet"
object_name = "wallet_adw.zip"  # Name of the object to download
destination_path = "/home/datascience/wallet/wallet_adw.zip"  # Local path to save the downloaded file

# Find the specified compartment
compartment = next((c for c in compartments if c.name == compartment_name), None)
if not compartment:
    raise ValueError(f"Compartment {compartment_name} not found")

# List buckets in the specified compartment
buckets = oci.pagination.list_call_get_all_results(
    object_storage_client.list_buckets,
    namespace,
    compartment.id
).data

# Check if the specified bucket exists
bucket = next((b for b in buckets if b.name == bucket_name), None)
if not bucket:
    raise ValueError(f"Bucket {bucket_name} not found in compartment {compartment_name}")

# Download the specified object from the bucket
try:
    get_obj = object_storage_client.get_object(namespace, bucket_name, object_name)
    with open(destination_path, 'wb') as f:
        for chunk in get_obj.data.raw.stream(1024 * 1024, decode_content=False):
            f.write(chunk)
    print(f"Downloaded {object_name} to {destination_path}")
except oci.exceptions.ServiceError as e:
    print(f"Service error: {e}")
