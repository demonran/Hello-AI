import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import joblib

def leaning():
    # 加载数据集
    data = pd.read_csv('reviews.csv')

    # 分离特征和标签
    X = data['review']
    y = data['sentiment']

    # 创建TF-IDF向量化器
    vectorizer = TfidfVectorizer()

    # 在整个数据集上拟合向量化器并转换文本数据为特征向量
    X_vectorized = vectorizer.fit_transform(X)

    # 创建线性支持向量机分类器
    classifier = LinearSVC()

    # 在整个数据集上训练分类器
    classifier.fit(X_vectorized, y)

    # 保存模型权重和向量化器
    joblib.dump(classifier, 'sentiment_model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')


if __name__ == '__main__':
    leaning()
