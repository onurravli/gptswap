import os
import requests
import argparse
from dotenv import load_dotenv
import sys
import re

load_dotenv()
OPENAI_API_KEY = ""

if os.getenv("OPENAI_API_KEY"):
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
else:
    print("Please set OPENAI_API_KEY environment variable.")
    exit(1)


def parse(inp: str):
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Input file path", required=True)
    parser.add_argument("-o", "--output", help="Output file path", required=True)
    args = parser.parse_args(inp.split())
    input_ext = args.input.split(".")[-1]
    output_ext = args.output.split(".")[-1]
    return {
        "input_file": args.input,
        "output_file": args.output,
        "input_ext": input_ext,
        "output_ext": output_ext,
    }


def remove_backtick(code: str) -> str:
    return re.sub(r"```.*\n", "", re.sub(r"\n```", "", code))


def convert(message: dict) -> str:
    with open(message["input_file"], "r") as input_file:
        input_code = input_file.read()
    url = "https://api.openai.com/v1/chat/completions"
    json = {
        "messages": [
            {
                "role": "system",
                "content": "You are a chatbot which can convert programming languages to other programming languages."
                f"I'm will give you a code and you will convert it to another programming language."
                f"The source code's extension is ${message['input_ext']} "
                f"and the target code will be written in ${message['output_ext']} extension."
                f"Don't describe the code, just convert it."
                f"Don't use backtick (`) character. Also, don't use markdown. Write code as plain text."
                f"Just write the converted code, write nothing if you can't convert it."
                f"Don't be a highbrow, just be a simple bot.",
            },
            {
                "role": "user",
                "content": f"The code will be converted is below:\n{input_code}",
            },
        ],
        "model": "gpt-3.5-turbo",
        "temperature": 0,
    }
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    try:
        res = requests.post(url, json=json, headers=headers)
        output_code = res.json()["choices"][0]["message"]["content"]
        output_file = open(message["output_file"], "w")
        output_file.write(remove_backtick(output_code))
        output_file.close()
        print("Success")
    except Exception as e:
        print("Failed: ", e)
        return "Failed"
    return "Success"


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            args = parse(" ".join(sys.argv[1:]))
            convert(args)
        else:
            print("Usage: python gptswap.py -i <input_file_path> -o <output_file_path>")
    except FileNotFoundError:
        print("File not found.")
    except KeyboardInterrupt or EOFError:
        print("Interrupted.")
