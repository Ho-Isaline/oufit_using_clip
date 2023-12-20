import time
import csv
from openai import OpenAI
import configparser
from pathlib import Path
import pandas as pd


config = configparser.ConfigParser()
relative_path = "../config/config.ini"
file_path = (Path(__file__).parent / relative_path).resolve()
config.read(file_path)
# OpenAI API Key
api_key = config['API_KEYS']['IMG_VIOSION_KEY']

def ImageGenerate2(descriptions):
    client = OpenAI(api_key=api_key)
    generated_descriptions = []
    desc_response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": f"整合{descriptions}成一個完整的句子 全中文"
            }
        ],
        max_tokens=200,
    )
    # print(translate_text)
    wear_desc = desc_response.choices[0].message.content
    print(wear_desc)
    return wear_desc