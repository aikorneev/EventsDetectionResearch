import csv

if __name__ == '__main__':

    source_f = open("1page_normalized_more.csv", "r", newline='', encoding='cp1251')
    f = csv.reader(source_f, delimiter=';')

    #creation of documemts according to the category of text
    i = 0
    documents = dict()
    event_count = dict()
    for row in f:
        i += 1
        if i == 1:
            continue
        #parse multiple categories
        cats = row[8].replace(',', ' ').split()
        for cat in cats:
            str1 = row[2].strip('[').strip(']').replace("'","").replace(",","")
            str2 = row[3].strip('[').strip(']').replace("'","").replace(",","")
            if cat not in documents:
                print('new cat ',cat)
                event_count[cat] = 1
                documents[cat] = str1 + ' ' + str2
            else:
                #print('old cat ', cat)
                event_count[cat] = event_count[cat] + 1
                documents[cat] = documents[cat] + ' ' + str1 + ' ' + str2
        #print(' ',i)


    #filter for categories with amount of events > 3
    #temp_doc = dict(documents)
    #for cat in temp_doc:
    #    if event_count[cat] < 3:
    #        print('delete:', cat)
    #        del documents[cat]

    texts = list(documents.values())

    # creation of dictionary
    texts_token = [d.split() for d in texts]
    f_write = csv.writer(open("1page_text_token.csv", "w+", newline='', encoding='cp1251'), delimiter=';')

    j = 0
    print(documents.keys())

    for key in documents.keys():
        print(key)
        f_write.writerow([key, texts_token[j]])
        j = j + 1

    print('end')


