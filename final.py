import tkinter as tk
import pygame as pg
import threading
from io import BytesIO
import numpy as np
import pandas as pd
import requests
from PIL import Image, ImageTk
# from translate import Translator
from module.image_generate import ImageGenerate2
from module.similarity import text_query_image
from module.text_to_audio import generate_and_play_speech
from module.voice_to_text import voice_to_text
import clip
import torch



image_embeddings = np.genfromtxt('embedding.csv', delimiter=',')
final = pd.read_csv('final_des.csv')
ims_path = list(final.iloc[:,-1])
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device, jit=False)

# def translate_text(text, target_language='en', source_language='zh-TW'):
#     translator= Translator(to_lang=target_language, from_lang=source_language)
#     translation = translator.translate(text)
#     return translation


def show_image(path):
    img = Image.open(path)
    # Resize the image 
    (x, y) = img.size
    x_s = 300
    y_s = int(y * x_s / x)
    img = img.resize((x_s, y_s), Image.Resampling.LANCZOS)
    tk_img = ImageTk.PhotoImage(img)
    label.config(image=tk_img)
    label.image = tk_img
    
    
def update_label():
    recorded_text = voice_to_text()
    label.config(text=recorded_text)
    if recorded_text == '無法翻譯':
        return 'shut down'
    button.config(text='正在為您查詢...')
    audio_thread = threading.Thread(target=generate_and_play_speech, args=("正在為您查詢"+recorded_text,)) #label跟聲音同時執行
    audio_thread.start()
 
    label.update_idletasks()
    button.pack_forget()
    # search_query = translate_text(recorded_text)
    search_query = recorded_text
    img_path = text_query_image(model, search_query, image_embeddings, ims_path, 1)
    result_row = final.loc[final['path'] == img_path]
    res = list(result_row.iloc[0, :8])
    des = ImageGenerate2(res)
    show_image(img_path)
    audio_thread = threading.Thread(target=generate_and_play_speech, args=(des,)) #label跟聲音同時執行
    audio_thread.start()
    
    
def record_button(text:str):
    global button
    button = tk.Button(root, text=text, command=update_label)
    button.pack(fill="both", expand="y")
    
#step1 -> 建立螢幕
pg.mixer.init()
root = tk.Tk()
root.title("visual.studio")
root.geometry('300x580')

#step2 開啟 > 輸入語音
label = tk.Label(root, text="請說出您想要的衣服款式", font=30, bg='white', pady=20, padx=100, relief="groove")
label.pack(ipadx=100)
audio_thread = threading.Thread(target=generate_and_play_speech, args=("請說出您想要的衣服款式",)) #label跟聲音同時執行
audio_thread.start()
record_button("點擊錄製")

root.mainloop()