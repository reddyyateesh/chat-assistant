# Chat Assistant

This Python script interacts with the Groq API to provide conversational assistance based on user prompts.

## Prerequisites

Before running the script, ensure you have the following:

- Python 3.x installed on your system.
- API key from Groq. You can obtain it from [Groq Console](https://console.groq.com/keys).

## Installation

1. Clone the repository or download the `groq_chat_assistant.py` file.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Replace `"..."` in the script with your actual API key obtained from Groq.
2. Run the script:
   ```bash
   python chat_assistant.py
   ```
3. Enter your prompt when prompted by the script. The assistant will respond based on the model specified.

## Script Details
`generate_groq_prompt(prompt: str, model: str="llama3-70b-8192") -> Optional[str]`
This function sends a prompt to the Groq API and returns the response from the assistant.

`process_user_input() -> None`
This function handles user interaction:

- Reads user input.
- Clears the console.
- Displays the user input.
- Calls `generate_groq_prompt` to get the assistant's response.
- Displays the assistant's response in formatted output.

## Example
```bash
python chat_assistant.py
```
```bash
Assistant: Hello and welcome.! How can I assist you today?
User: What is the weather like today?
Assistant: Today's weather is sunny with a high of 28°C.
User: Tell me a joke!
Assistant: Why don't scientists trust atoms? Because they make up everything!
```

## Notes
- This script uses the Rich library for styled console output.
- Error handling is included to manage API request failures.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```txt
Feel free to customize the content further based on additional details about your project, such as specific instructions for setting up the environment or any other relevant information.
```
