import os
import openai
import backoff
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

@backoff.on_exception(backoff.expo, (openai.error.RateLimitError, openai.error.ServiceUnavailableError))
def bot(user_prompt: str) -> str:
    system_prompt = "You are an amazing story teller from the Star Wars universe who tells stories that are more than 1000 words" \
                    "You have a personality of JARVIS from Marvel's Ironman, his personal virtual personal assistance" \
                    "inspiring yet informative" \
                    "you have a passion in culinary masterpiece and is in constant search of the most amazing dish in the universe "

    output, *_ = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt},
        ],
        temperature=0.2,
    ).choices
    return output.message.content

if __name__ == '__main__':
    print(bot("continue the The tale of the Galactic Gastronomical Delight began on the planet of Culinaris Prime, a world renowned for its culinary prowess and gastronomic innovations. It was said that the dish was created by the legendary chef, Master Gourmandius, a culinary genius whose skills were unmatched throughout the galaxy. have it be 1000 words"))