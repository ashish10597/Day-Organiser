from llm_client import LLMClient

def main():
    client = LLMClient()
    print("🤖 Day Organiser LLM Agent")
    print("=" * 50)
    print("Enter activities to organize (or 'exit' to quit):")
    print("Example: 'I want to learn TypeScript for 2 hours tomorrow'")
    print("=" * 50)
    
    while True:
        activity = input("\nActivity: ")
        if activity.lower() == 'exit':
            break
        try:
            response = client.get_response(activity)
            print(f"\n📋 Organization Result:\n{response}")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main() 