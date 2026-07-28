import time
import requests

# ⚠️ PASTE YOUR SECURE CREDENTIALS HERE:
SUPABASE_URL = "https://supabase.co"
SUPABASE_KEY = "PASTE_YOUR_LONG_ANON_PUBLIC_KEY_HERE"
"PASTE_YOUR_LONG_ANON_PUBLIC_KEY_HERE"
def monitor_cloud_database():
    print("==================================================")
    print("🛰️  STARTING LIVE CLOUD INFRASTRUCTURE MONITOR...")
    print("==================================================")
    
    # The database endpoint where our site stats live
    api_url = f"{SUPABASE_URL}/rest/v1/site_stats?select=clicks"
    
    # Security headers required by the cloud server
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}"
    }

    try:
        # Send a secure network request to Supabase over the internet
        response = requests.get(api_url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            if data and len(data) > 0:
                current_clicks = data[0]['clicks']
                print(f"✅ CONNECTION STATUS: Healthy (Code 200)")
                print(f"📊 LIVE CLOUD DATABASE COUNTER: [ {current_clicks} ] clicks recorded.")
                print(f"🕒 TIMESTAMP: {time.strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                print("⚠️ ALERT: Database connected, but the site_stats table is empty!")
        else:
            print(f"❌ ERROR: Cloud rejected connection. Status Code: {response.status_code}")
            
    except Exception as e:
        print(f"🚨 CRITICAL ERROR: Could not reach the cloud server. Details: {e}")
    
    print("==================================================")

if __name__ == "__main__":
    monitor_cloud_database()
