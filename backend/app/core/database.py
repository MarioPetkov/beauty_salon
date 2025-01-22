from supabase import create_client
from app.core.config import SUPABASE_URL, SUPABASE_ANON_KEY

# Initialize Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

def get_supabase_client():
    return supabase
