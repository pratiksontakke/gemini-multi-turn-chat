import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment variables.")
        return

    client = genai.Client(api_key=api_key)

    model_name = "gemini-2.0-flash"

    try:
        temp_input = input(f"Enter desired temperature (0.0 to 1.0, default 0.9 for creativity): ")
        temperature = float(temp_input) if temp_input else 0.9
        if not (0.0 <= temperature <= 1.0):
            print("Temperature must be between 0.0 and 1.0. Using default 0.9.")
            temperature = 0.9
    except ValueError:
        print("Invalid temperature input. Using default 0.9.")
        temperature = 0.9

    chat = client.chats.create(
        model=model_name,
        config=types.GenerateContentConfig(
            max_output_tokens=500,
            temperature=temperature
        )
    )


    print("🔵 Gemini Chat is running. Type your messages below.")
    print("Type 'exit', 'quit', or 'q' to end the chat.\n")

    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ["exit", "quit", "q"]:
            print("🔚 Chat ended.")
            break

        response = chat.send_message(user_input)
        print("Gemini:", response.text)

    # # Optional: Print conversation history
    # print("\n📝 Conversation Summary:")
    # for message in chat.get_history():
    #     print(f"{message.role.capitalize()}: {message.parts[0].text}")

if __name__ == "__main__":
    main()
