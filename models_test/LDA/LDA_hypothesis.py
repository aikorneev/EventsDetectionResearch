import csv
import sys
from gensim import corpora, models
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import LdaModel, LdaMulticore

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

    src_file = "1page_text_token.csv"
    source_f = open(src_file, "r", newline='', encoding='cp1251')
    f = csv.reader(source_f, delimiter=';')

    documents = dict()
    for row in f:
        if row[0] not in documents:
            print('new cat ', row[0])
            documents[row[0]] = row[1].strip('[').strip(']').replace("'","").replace(",","")

    #Using LDA algorithm for each pair of categories
    #Trying to get words, which describe category to show that it is possible to obtain category from descriptions
    #Save all models to the file and prepare summary file lda_out
    topic_count = len(documents.keys())
    topics = list(documents.keys())
    lda_out = open('LDA_'+src_file+'.txt', 'w')
    i = 0
    j = 0
    for i in range(0, topic_count):
        for j in range(i, topic_count):
            if i == j:
                continue
            print('topics: ', i, j, ': ', topics[i], topics[j])
            new_documents = dict()
            new_documents[topics[i]] = documents[topics[i]]
            new_documents[topics[j]] = documents[topics[j]]

            texts = list(new_documents.values())

            # creation of dictionary
            texts_token = [d.split() for d in texts]

            print('Creation of dictionary')
            mydict = corpora.Dictionary(texts_token)

            # creation of simple corpus
            print('Creation of corpus')
            corpus = [mydict.doc2bow(d.split()) for d in texts]

            # creation of corpus (with tfidf)
            print('tfidf start: creation of corpus')
            tfidf = models.TfidfModel(corpus, smartirs='ntc')

            # Show the TF-IDF weights and saving the model
            #for doc in tfidf[corpus]:
            #    print([[mydict[id], np.around(freq, decimals=2)] for id, freq in doc])
            tfidf.save('tfidf_'+src_file+'.model')

            # second variant of tf-idf
            #print('tfidf2 start: creation of corpus')
            #print(corpus)
            #tfidf_vectorizer = TfidfVectorizer()
            #values = tfidf_vectorizer.fit_transform(documents.values())
            #feature_names = tfidf_vectorizer.get_feature_names()
            #print(pd.DataFrame(values.toarray(), columns=feature_names))
            #print(tfidf_vectorizer)

            # LDA training
            print('LDA start:')
            keys = list(new_documents.keys())
            topic_number = len(keys)
            print('Topic number', topic_number, keys)
            lda_model = LdaMulticore(corpus=tfidf[corpus],
                                     id2word=mydict,
                                     random_state=100,
                                     num_topics=topic_number,
                                     passes=10,
                                     chunksize=1000,
                                     batch=False,
                                     alpha='asymmetric',
                                     decay=0.5,
                                     offset=64,
                                     eta=None,
                                     eval_every=0,
                                     iterations=100,
                                     gamma_threshold=0.001,
                                     per_word_topics=True)
            # save the lda model
            lda_model.save('lda_results/models/LDAmod_'+topics[i]+'_'+topics[j]+'.model')

            # Debug for topics
            print(topics[i]+' and '+topics[j], file=lda_out)
            for idx, topic in lda_model.print_topics(-1):
                print('Topic: {} Word: {}'.format(idx, topic), file=lda_out)
