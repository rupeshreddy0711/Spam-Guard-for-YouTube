from flask import Flask, render_template, request, url_for
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])

def predict():
    path=r'D:\RUPESH\PYTHONBASICS\project\SPAMDETECTOR\data.csv'
    data_fram = pd.read_csv(path)
    df_data = data_fram[["CONTENT","CLASS"]]
    df_x = df_data['CONTENT']
    df_y = df_data.CLASS
    corpus = df_x
    cv = CountVectorizer()
    X = cv.fit_transform(corpus)
    X_train, X_test, y_train, y_test = train_test_split(X, df_y, test_size=0.33, random_state=42)
    clf = MultinomialNB()
    clf.fit(X_train,y_train)
    clf.score(X_test,y_test)
    
    if request.method == 'POST':
        comment = request.form['comment']
        data = [comment]
        vect = cv.transform(data).toarray()
        my_prediction = clf.predict(vect)
    
    return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
    app.run(debug=True)