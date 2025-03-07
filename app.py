import streamlit as st
import pickle
import string
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
nltk.download('punkt')


tfidf = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("model2.pkl", "rb"))

st.title("Email/SMS Spam Classifier")

input_sms=st.text_area("Enter the message")


def transform(text):
    text = text.lower()  # Lower case
    text = nltk.word_tokenize(text)  # Tokenization

    y = []

    for i in text:
        if i.isalnum():  # Remove special chars
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:  # remove stop words and puncs
            y.append(i)

    text = y[:]
    y.clear()

    ps = PorterStemmer()
    for i in text:  # stemming
        y.append(ps.stem(i))

    return " ".join(y)

# 4 steps
if st.button('Predict'):
    #preprocess
    transformed_sms=transform(input_sms)
    #vectorize
    vector_input=tfidf.transform([transformed_sms])
    #precict
    result=model.predict(vector_input)[0]
    #Display:
    if result==1:
        st.header("Spam")
    else:
        st.header("Not Spam")