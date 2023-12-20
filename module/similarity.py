import math
import cv2
import pandas as pd
import torch
import matplotlib.pyplot as plt
from tqdm import tqdm
from PIL import Image
from pathlib import Path
import clip



def get_text_embedding(model, text_query):
    with torch.no_grad():
        text_embedding = model.encode_text(clip.tokenize(text_query).to(device))
        text_embedding = text_embedding / text_embedding.norm(dim=-1, keepdim=True)
    return text_embedding.cpu().numpy()

def find_best_matches(text_embeddings, image_embeddings, images_files, results_count):
    similarities = (image_embeddings @ text_embeddings.T).squeeze(1)
    best_match_image_idx = (-similarities).argsort()
    return [images_files[i] for i in best_match_image_idx[:results_count]], similarities[best_match_image_idx]

def text_query_image(model, text_query, image_embeddings, images_files, result_count=3):
    text_embeddings = get_text_embedding(model, text_query)
    # 根據圖片與文字的embeddings計算相似度，並且找到前n名
    best_image_ids, best_similarities = find_best_matches(text_embeddings, image_embeddings, images_files, result_count)

    # 將找到的圖片繪製出來
    plt.figure(figsize = (20, 10))
    for i, path in enumerate(best_image_ids):
        print(path)
        plt.subplot(1, len(best_image_ids), i+1)
        plt.imshow(Image.open(path))
        plt.title(f"similarity : {best_similarities[i]}")
    # plt.tight_layout()
    # plt.show()
    return path