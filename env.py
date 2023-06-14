import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "14202110").strip()
API_HASH = os.getenv("API_HASH", "45f3a3ac8effd88e42aeabe3cfe4f520").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "6114656337:AAFwEQG7sKz8i-OHBQ-Pn1GbW_UpHnl1e1I").strip()
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "5956803759").split()))
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://eusbhunz:sMAFOIhfF3hB6CVT4Ri09wRIJLJcUh7x@hansken.db.elephantsql.com/eusbhunz").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "Its_Venom_family")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
