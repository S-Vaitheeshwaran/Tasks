from dotenv import load_dotenv
import os

load_dotenv()

DIRECTUS_URL = os.getenv("DIRECTUS_URL")
DIRECTUS_TOKEN = os.getenv("DIRECTUS_TOKEN")

if not DIRECTUS_URL or not DIRECTUS_TOKEN:
    raise RuntimeError("Missing Directus configuration in .env")
