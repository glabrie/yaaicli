from email import message
import os
import sys
from userflags import Flags
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

user_args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
user_flags = [arg for arg in sys.argv[1:] if arg.startswith("-")]

if len(user_args) == 0 or len(user_args) >= 2:
    print('No prompt passed or multiple prompts detected. Please pass your prompt enclosed in "quotation marks"')
else:
    user_prompt = user_args[0]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages)
    print(response.text)
    if any(v in user_flags for v in Flags.VERBOSE.value):
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
