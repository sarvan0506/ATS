import datetime
import requests
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.externals import joblib
import nltk
nltk.download("stopwords")
nltk.download('wordnet')
from nltk.corpus import stopwords
from textblob import Word


import logging
app = Flask(__name__)

logging.basicConfig(filename='/logs/profiler.log', filemode='w+',
                   format='%(asctime)s:: %(levelname)s:: %(message)s',
                   datefmt='%d-%b-%y %H:%M:%S',
                   level='INFO')

stop = stopwords.words('english')
tfidf_vect = joblib.load("tfdf_vector.sav")
model = joblib.load("ATS_linear.sav")


def l_print(obj, printtoconsole=True, code="PROF", level="info"):
   if level ==  'debug':
       logging.debug(code)
       logging.debug(obj)
   elif  level ==   'info':
       logging.info(code)
       logging.info(obj)
   elif  level ==   'warning':
       logging.warning(code)
       logging.warning(obj)
   elif  level ==   'error':
       logging.error(code)
       logging.error(obj)
   elif  level ==   'critical':
       logging.critical(code)
       logging.critical(obj)
   else:
       logging.debug(code)
       logging.debug(obj)
   if printtoconsole:
       print(code)
       print(obj)

@app.route('/', methods=['POST', 'GET'])
def predict():
   
    if request.method == 'POST':
        print("In Post")
        data = request.json

        sample = pd.Series(data["description"])
        sample = sample.apply(lambda x: " ".join(x.lower() for x in str(x).split()))
        sample = sample.str.replace('[^\w\s]','')
        sample = sample.apply(lambda x: " ".join(x for x in str(x).split() if x not in stop))
        sample = sample.apply(lambda x: " ".join([Word(word).lemmatize() for word in str(x).split()]))
        
        tfidf = tfidf_vect.transform(sample)

        d = model.predict(tfidf.toarray())

        print("Group: ", str(d[0]))

        return { "Group" : str(d[0])}

    elif request.method == 'GET':
        return { "status" : "Ok" }

if __name__ == '__main__':
    app.run(host = '0.0.0.0' , port = 8011, debug="ON")