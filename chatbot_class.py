from __future__ import annotations

import argparse
import os
from typing import List, Optional

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class ChatBot:
    def __init__(self, api_key: Optional[str] = None, model: str = 'gpt-4o-mini', temperature: float = 0.5):
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError('OpenAI API key is required. Set OPENAI_API_KEY in .env or pass --api-key.')

        self.model = model
        self.temperature = temperature
        self.client = OpenAI(api_key=self.api_key)

    def ask(self, user_message: str, system_message: Optional[str] = None) -> str:
        messages = []
        if system_message:
            messages.append({'role': 'system', 'content': system_message})

        messages.append({'role': 'user', 'content': user_message})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
        )

        return response.choices[0].message.content

    def chat(self, messages: List[dict]) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
        )
        return response.choices[0].message.content


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Chat with OpenAI using the ChatBot class')
    parser.add_argument('--prompt', '-p', help='Question or prompt to send')
    parser.add_argument('--system', '-s', help='Optional system prompt')
    parser.add_argument('--model', '-m', default=os.getenv('OPENAI_MODEL', 'gpt-4o-mini'), help='Model name to use')
    parser.add_argument('--temperature', '-t', type=float, default=float(os.getenv('OPENAI_TEMPERATURE', '0.7')), help='Sampling temperature')
    parser.add_argument('--api-key', '-k', help='OpenAI API key; falls back to OPENAI_API_KEY env var')
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    bot = ChatBot(api_key=args.api_key, model=args.model, temperature=args.temperature)

    if args.prompt:
        print(bot.ask(args.prompt, system_message=args.system))
        return

    print('Enter prompts interactively (Ctrl+C to quit).')
    while True:
        try:
            prompt = input('> ').strip()
            if not prompt:
                continue
            print(bot.ask(prompt, system_message=args.system))
        except KeyboardInterrupt:
            print('\nGoodbye!')
            break


if __name__ == '__main__':
    main()