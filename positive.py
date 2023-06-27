import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import joblib


def action():

    # 加载训练好的模型权重和特征向量
    model = joblib.load('sentiment_model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')

    # 输入句子
    sentence = input("请输入一句话: ")

    # 使用向量化器将输入句子转换为特征向量
    sentence_vectorized = vectorizer.transform([sentence])

    # 使用模型进行情感预测
    prediction = model.predict(sentence_vectorized)

    # 打印情感预测结果
    if prediction[0] == 'positive':
        print("积极")
    else:
        print("消极")


if __name__ == '__main__':
    action()
