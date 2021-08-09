from bs4 import BeautifulSoup
import json
import re
import jieba
import time
import os
import pickle
from rank_bm25 import BM25Okapi

documents = [] # = urls

list_search_result = []
   
list_URL_sport = []

INDEX = 'INDEX'

stopwords = []

index_obj = {}


def stop_words_list():
    stopwords = [line.strip() for line in open('stop2.txt',encoding='UTF-8').readlines()]
    return stopwords

def walk_file(file):
    for root, dirs, files in os.walk(file):
        for f in files:
            f_s = os.path.join(root, f);
            if f_s.endswith('html'):
                list_URL_sport.append(f_s)
        
def crawler(list_URL):
    corpus = []
    for i, url in enumerate(list_URL):
        print("网页爬取:", url, "...")
        with open(url, 'r') as f:
            page = f.read()
        result_chinese = url + bs4_page_clean(page)
        corpus.append(jieba_create_index(result_chinese))
        documents.append(url)
    index_obj['d'] = documents
    bm25 = BM25Okapi(corpus)
    index_obj['b'] = bm25
    with open(INDEX, 'wb') as index_file:
        pickle.dump(index_obj, index_file)
    return bm25


def bs4_page_clean(page):
    print("正则表达式：清除网页标签等无关信息...")
    soup = BeautifulSoup(page, "html.parser")
    [script.extract() for script in soup.findAll('script')]
    [style.extract() for style in soup.findAll('style')]
    reg1 = re.compile("<[^>]*>")
    content = reg1.sub('', soup.prettify())
    return str(content)

def jieba_create_index(string):
    list_word = jieba.lcut_for_search(string)
    dict_word_temp = []
    for word in list_word:
        if word in stopwords:
            continue
        dict_word_temp.append(word)
    return dict_word_temp



if __name__ == "__main__":

    time_start_crawler = time.time()
    
    if os.path.exists(INDEX):
        with open(INDEX, 'rb') as index_file:
            index_obj = pickle.load(index_file)
            documents = index_obj['d']
            bm25Model = index_obj['b']
                       
    else:
        stopwords = stop_words_list();        
        walk_file('./')
        bm25Model = crawler(list_URL_sport)
        
    time_end_crawler = time.time()
    print("载入OR网页爬取和分析时间：", time_end_crawler - time_start_crawler)
    word = input("请输入查询的关键词：")
    time_start_search = time.time()
    
    query = jieba.lcut_for_search(word)
    scores = bm25Model.get_top_n(query, documents, n=1)

    time_end_search = time.time()
    print("检索时间：", time_end_search - time_start_search)
    for url in scores:
        print(url)
