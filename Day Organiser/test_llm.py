from llm_client import LLMClient

def test_llm():
    client = LLMClient()
    
    # Test prompt
    test_prompt = "What is the capital of France?"
    print(f"Test prompt: {test_prompt}")
    
    try:
        response = client.get_response(test_prompt)
        print(f"LLM Response: {response}")
        print("✅ LLM test successful!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_llm() 