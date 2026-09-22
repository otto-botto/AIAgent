import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse


def main():
    parser = argparse.ArgumentParser(description="ChatBot")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to the LLM")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output.")
    args = parser.parse_args() # now can use args.user_prompt and args.verbose
    
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    
    if (api_key == None):
        raise RuntimeError("openrouter apoi key did not work, check .env file")
   
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages = [{"role": "user", "content": args.user_prompt}]
    response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
    )
    if(response.usage == None):
        raise RuntimeError("could not get usage statistics")

    if(args.verbose == True):
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    
    print("Response:")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
