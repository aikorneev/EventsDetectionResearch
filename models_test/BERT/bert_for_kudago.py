import csv
import math
import numpy as np
import sys
from sklearn.feature_extraction.text import CountVectorizer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

if __name__ == '__main__':
    maxInt = sys.maxsize

    while True:
        # decrease the maxInt value by factor 10
        # as long as the OverflowError occurs.
        try:
            csv.field_size_limit(maxInt)
            break
        except OverflowError:
            maxInt = int(maxInt / 10)

    #src_file = "C:\\Users\\Aleksei\\Desktop\ITMO\\nir\crawler\\text_token_example.csv"
    src_file = "C:\\Users\\Aleksei\\Desktop\\ITMO\\nir\\data\\kudago\\1-1653_documents.csv"
    source_f = open(src_file, "r", newline='', encoding='cp1251')
    f = csv.reader(source_f, delimiter=';')

    #read documents
    documents = dict()
    temp_str = ""
    temp_cat = ""
    for row in f:
        if "'" not in row[0]:
            if temp_cat:
                #print('new cat finished')
                documents[temp_cat] = temp_str.strip('[').strip(']').replace("'", "").replace(",", "")
                temp_cat = ""
                temp_str = ""
            #print('new cat ', row[0])
            temp_cat = row[0]
            temp_str += row[1]
        else:
            #print('continue cat', row[0])
            temp_str += row[0]
        #documents[row[0]] = row[1].strip('[').strip(']').replace("'","").replace(",","")
    documents[temp_cat] = temp_str.strip('[').strip(']').replace("'", "").replace(",", "")

    #create bert vetors for each multilingual model and save them to files
    #these vetors will represent the average vector of concantenated event decriptions

    model_names = ['paraphrase-xlm-r-multilingual-v1',
    'stsb-xlm-r-multilingual',
    'quora-distilbert-multilingual',
    'paraphrase-multilingual-MiniLM-L12-v2',
    'paraphrase-multilingual-mpnet-base-v2',
    'distiluse - base - multilingual - cased - v1',
    'distiluse-base-multilingual-cased-v2']

    for model_name in model_names:
        print('for model', model_name)
        model = SentenceTransformer(model_name)
        calculated_vectors = dict()

        #check keywords for each document
        for keys in documents:
            doc = documents[keys]
            print(keys)

            # bounds for keyword(s) word amount
            n_gram_range = (1, 1)

            count = CountVectorizer(ngram_range=n_gram_range).fit([doc])
            #we don't use candidates here, because the aim is not to find keywords
            #candidates = count.get_feature_names()
            #print(candidates)

            # using bert finally
            doc_embedding = model.encode([doc])
            calculated_vectors[keys] = doc_embedding
            #print(doc_embedding, len(doc_embedding[0]))


            #candidate_embeddings = model.encode(candidates)

            # check similarity with straight method
            #top_n = 5
            #distances = cosine_similarity(doc_embedding, candidate_embeddings)
            #keywords = [candidates[index] for index in distances.argsort()[0][-top_n:]]
            #print('for ', keys, len(candidates), ' keywords:', keywords)

        # save vectors
        f_write = csv.writer(open(model_name+"_vectors.csv", "w+", newline='', encoding='cp1251'), delimiter=';')
        for key in calculated_vectors.keys():
            print('print', key)
            f_write.writerow([key, calculated_vectors[key]])