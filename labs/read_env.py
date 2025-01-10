import os
import dotenv

# Load environment vars from .env file
dotenv.load_dotenv()

tenant_id = os.environ.get("TENANT_ID")
client_id = os.environ.get("CLIENT_ID")

print(f"Azure SP Tenant Id : {tenant_id}")
print(f"Azure SP Client Id : {client_id}")
