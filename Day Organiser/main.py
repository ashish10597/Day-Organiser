from llm_client import LLMClient

def main():
    client = LLMClient()
    while True:
        prompt = input("Enter your prompt (or 'exit' to quit): ")
        if prompt.lower() == 'exit':
            break
        response = client.get_response(prompt)
        print(f"LLM Response: {response}")

if __name__ == "__main__":
    main() 