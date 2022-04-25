# coding=utf-8
import synonyms
from jieba import posseg as pseg


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
