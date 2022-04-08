#!/usr/bin/env python
"""
Positional parameters:

1. number of df row to begin with
2. number of last df row to clean
3. path to df for cleaning
4. file name to save labels
"""

import os
import time
import numpy as np
import pandas as pd
import sys
from scipy.spatial import distance
from sklearn.metrics import classification_report
import transformers
from transformers import pipeline
import sentence_transformers 
from sentence_transformers import SentenceTransformer

def classifier_semantic(text, targets, model):
    target_emb = model.encode(targets)
    text_emb = model.encode(text)
    
    probs = [ 1 - distance.cosine(text_emb, t) for t in target_emb]
    probs = probs / sum(probs)
    
    response = dict()
    for p, t in zip(probs, targets):
        response[t] = p 
    
    temp = dict(sorted(response.items(), key=lambda item: item[1], reverse=True))
    response = dict()
    response['sequence'] = text
    response['scores'] = list(temp.values())
    response['labels'] = list(temp.keys())
    
    return response

def clean_dataset(df, candidate_labels, classifier, cand_adv_index, debug = 100000, threshold = 0):
    labels = list() # объединяем все нерекламные классы в один, реклама в другой
    semantic_classifier_model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
    for index, row in df.iterrows():
        if index % debug == 0:
            print('index = ', index)    
        res = classifier(row['caption'], candidate_labels, semantic_classifier_model)
        #print(res)
        if res['scores'][0] > threshold:
            val = 0
            for ind in cand_adv_index:
                if res['labels'][0] == candidate_labels[ind]: # равен лейблу, который относится к рекламному (food, ...)
                    val = 1
                    break
            labels.append(val)
        else:
            labels.append(1) # не хватило уверенности в классификации события, помечаем как реклама
    return labels

if __name__ == '__main__':
    start_time = time.time()
    try:
        start = int(sys.argv[1])
        finish = int(sys.argv[2])
            
        data_path = sys.argv[3] + str(start) + '_' + str(finish) + '.csv'
        save_path = sys.argv[4]
        
        print('Start', start)
        print('Finish', finish)
        print('Path to data:', data_path)
        print('File to save:', save_path)
    except:
        print('Bad parameters')
        sys.exit(1)
        
    df = pd.read_csv(data_path, lineterminator='\n')
    df = df.dropna(subset = ['caption']).reset_index(drop=True)
    df.caption = df.caption.apply(lambda x: x.replace('\n', ' ') if type(x) != float else print(x))
    print('Dataset is read')

    candidate_labs = [
        'other',
        'food',
        'advertisement',
        'spam',
        'promotion',
        'music concert', 
        'exhibition', 
        'festival',
        'conference',
        'calendar holiday',
        'sport event',
        'flashmob', 
        'accident',
        'stroll walking',
        'wedding birthday',
        'private event',
        'public event']
    
    print('Cleaning')
    y_pred = clean_dataset(df, candidate_labs, classifier_semantic,[0, 1, 2, 3, 4])
    print('Finished')
    
    np.save(save_path + str(start) + '_' + str(finish), np.array(y_pred))
    print('Saved')
    print(f"Clean data:--- {(time.time() - start_time)/60} minutes ---")
