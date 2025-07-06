import requests
import json

def test_api():
    base_url = "http://localhost:8000"
    
    # Test health check
    print("Testing health check...")
    try:
        response = requests.get(f"{base_url}/api/health")
        print(f"Health check status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Health check failed: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Test organize endpoint
    print("Testing organize endpoint...")
    test_activity = "I want to learn TypeScript for 2 hours tomorrow"
    
    payload = {
        "activity": test_activity
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/organize",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"Organize endpoint status: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"Response: {result['response']}")
            print("✅ API test successful!")
        else:
            print(f"Error: {response.text}")
            
    except Exception as e:
        print(f"Organize endpoint failed: {e}")

if __name__ == "__main__":
    test_api() 