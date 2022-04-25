# coding=utf-8
import os, re
import requests
import synonyms
from jieba import posseg as pseg

def get_text(text):
    data = {
        "text": text
    }
    # data = json.dumps(data)

    headers = {"content-type": "application/json"}

    return requests.post("http://127.0.0.1:5000/wyc", json=data, headers=headers).text

def words_change(words):  # 传入句子，变形返回
    words_tuple = pseg.lcut(words)
    print(words_tuple)
    word_list = []
    for word, flag in words_tuple:
        if flag == 'a' or flag == 'ad' or flag == 'v':  # 词性判断
            seg_list = (synonyms.nearby(word))[0]
            if len(seg_list) <= 1:
                word = word
            else:
                word = seg_list[1]
        word_list.append(word)
    return "".join(word_list)


print(words_change("外贸网站运营必备技能(一):Python实现英文文案批量伪原创 ..."))