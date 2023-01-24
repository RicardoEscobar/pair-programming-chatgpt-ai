"""
2023-01-24 13:45:15
This module contains the get_response function.
"""
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_response(prompt: str = None) -> str:
    """
    This function receives a promt to be sent to OpenAI.
    Returns a str containing the response.
    """
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0,
            max_tokens=2047  # Max 4097
        )
        response_text = response.choices[0].text
    except openai.error.InvalidRequestError as error:
        with open('error.log', 'a', encoding='utf-8') as file:
            file.write(f'Error: {error}\n')

    return response_text


if __name__ == '__main__':
    print(get_response('What time is it?'))
