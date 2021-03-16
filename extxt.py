from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import pandas as pd


def process(InputPath):
    file_object = open(InputPath, encoding="utf-8")
    text = file_object.read()
    tokens = word_tokenize(text)
    swords = stopwords.words('english')

    wnl = WordNetLemmatizer()

    re1 = list()
    for word in tokens:
        temp = str.lower(wnl.lemmatize(word))
        if temp not in swords and wordnet.synsets(temp) != [] and temp not in re1:
            re1.append(temp)
    file_object.close()
    return re1
def processout(datafile,outputpath,date):
    df1=pd.read_csv(datafile)
    words=list(df1[df1['Date']==date]['TEXT'])
    text=''
    for i in words:
        text=text+i+"#"
    file_write_obj = open(outputpath, 'w')
    file_write_obj.writelines(text)
    file_write_obj.close()
    print('Done')

