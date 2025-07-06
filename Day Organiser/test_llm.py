from llm_client import LLMClient

def test_llm():
    client = LLMClient()
    
    # Test activity organization
    test_activity = "I want to learn TypeScript for 2 hours tomorrow"
    print(f"Test activity: {test_activity}")
    
    try:
        response = client.get_response(test_activity)
        print(f"Organization Response:\n{response}")
        print("✅ Day organization test successful!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_llm() 