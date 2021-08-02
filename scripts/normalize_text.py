import json
import requests as req
import csv
import math
import re
import nltk
from nltk.corpus import stopwords
import pymorphy2

def CleanStopWords(stopWords3, line):
    stopWords = stopwords.words("russian")
    stopWords2 = stopwords.words("english")
    return [word for word in line if word not in stopWords and word not in stopWords2 and word not in stopWords3]

def CleanDigits(line):
    return [word for word in line if not word.isdigit()]

def Normalize(line):
    morph = pymorphy2.MorphAnalyzer()
    return [morph.parse(word)[0].normal_form for word in line if len(word) > 2 and
            morph.parse(word)[0].tag.POS != 'PREP' and
            morph.parse(word)[0].tag.POS != 'CONJ' and
            morph.parse(word)[0].tag.POS != 'PRCL' and
            morph.parse(word)[0].tag.POS != 'INTJ']

def Clean_Normalize(str):
    #additional stop list
    with open("stopwords.txt") as file:
        stopWords3 = [row.strip() for row in file]

    new_str1 = re.sub(r'\<[^>]*\>', '', str)
    new_str1 = new_str1.lower()
    new_str1 = re.sub(r'[^\w\d\s]', ' ', new_str1)
    tokenline = nltk.word_tokenize(new_str1)
    tokenline = CleanStopWords(stopWords3, tokenline)
    tokenline = Normalize(tokenline)
    tokenline = CleanDigits(tokenline)
    return tokenline

if __name__ == '__main__':

    f_write = csv.writer(open("1page_normalized_more.csv", "w+", newline='', encoding='cp1251'), delimiter=';')
    f = csv.reader(open("1page_notags.csv", "r", newline='', encoding='cp1251'), delimiter=';')

    i = 0
    for row in f:
        i += 1

        f_write.writerow([row[0],
                    row[1],
                    Clean_Normalize(row[2]),
                    Clean_Normalize(row[3]),
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                    row[9]])

        if (i % 10 == 0):
            print(' ',i)
        #print(' ',i)
    print('end')