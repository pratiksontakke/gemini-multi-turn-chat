
# Gemini Multi-Turn Chat

A simple Python script that enables interactive chat conversations with Google's Gemini AI model. The script maintains conversation context across multiple messages and allows you to customize the AI's creativity level through temperature settings.

## What the script does

- **Interactive Chat**: Start a conversation with Google's Gemini 2.0 Flash model
- **Temperature Control**: Adjust the AI's creativity level (0.0 for focused responses, 1.0 for maximum creativity)
- **Multi-turn Conversations**: The AI remembers previous messages in the conversation
- **Easy Exit**: Type 'exit', 'quit', or 'q' to end the chat
- **Error Handling**: Graceful handling of invalid inputs and missing API keys

## Features

- 🤖 Uses Google's latest Gemini 2.0 Flash model
- 🌡️ Customizable temperature settings for response creativity
- 💬 Maintains conversation context throughout the session
- ⚡ Fast and responsive chat interface
- 🔒 Secure API key management through environment variables

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- A Google AI Studio account and API key

### Step 1: Clone or Download

Download the script file to your local machine.

### Step 2: Install Dependencies

Install the required Python packages:

```bash
pip install google-genai python-dotenv
```

### Step 3: Get Your Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the API key for the next step

### Step 4: Set Up Environment Variables

Create a `.env` file in the same directory as your script:

```
GEMINI_API_KEY=your_actual_api_key_here
```

**Important**: Replace `your_actual_api_key_here` with your actual Gemini API key.

## How to Run

1. Open your terminal/command prompt
2. Navigate to the directory containing the script
3. Run the script:

```bash
python your_script_name.py
```

4. When prompted, enter your desired temperature (0.0 to 1.0) or press Enter for default (0.9)
5. Start chatting with Gemini!

## Usage Example

```
$ python gemini_chat.py
Enter desired temperature (0.0 to 1.0, default 0.9 for creativity): 0.7

🔵 Gemini Chat is running. Type your messages below.
Type 'exit', 'quit', or 'q' to end the chat.

You: My name is Pratik
Gemini: Okay, Pratik. It's nice to meet you! How can I help you today?

You: What's my name?
Gemini: Your name is Pratik.

You: q
🔚 Chat ended.
```

## Temperature Settings

- **0.0**: Very focused and deterministic responses
- **0.5**: Balanced creativity and focus
- **0.9**: High creativity (default)
- **1.0**: Maximum creativity and randomness

## Troubleshooting

### "GEMINI_API_KEY not found" Error
- Make sure your `.env` file is in the same directory as the script
- Verify that your API key is correctly set in the `.env` file
- Check that there are no extra spaces around the API key

### "Invalid temperature input" Warning
- Enter a number between 0.0 and 1.0
- Press Enter to use the default temperature (0.9)

### Import Errors
- Make sure you've installed the required packages:
  ```bash
  pip install google-genai python-dotenv
  ```

## Security Notes

- Never commit your `.env` file to version control
- Keep your API key confidential
- Add `.env` to your `.gitignore` file if using Git

## Dependencies

- `google-genai`: Official Google Generative AI Python SDK
- `python-dotenv`: For loading environment variables from .env file
- `os`: Built-in Python module for environment variables

## License

This script is provided as-is for educational and personal use.
