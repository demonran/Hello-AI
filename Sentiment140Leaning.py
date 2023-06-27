import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import joblib


def leaning():
    # 读取 Sentiment140 数据集
    data = pd.read_csv('sentiment140.csv', encoding='latin-1', header=None)


    # 设置列名
    data.columns = ['target', 'id', 'date', 'flag', 'user', 'text']

    # 只选择目标（情感标签）和文本列
    data = data[['target', 'text']]

    print(data)

    # 将情感标签映射为 0（消极）和 1（积极）
    data['target'] = data['target'].replace({0: 'negative', 4: 'positive'})
    print(data)


    # 数据集拆分为训练集和测试集
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

    # 特征提取器
    vectorizer = CountVectorizer()

    # 在训练集上拟合并转换特征向量
    train_features = vectorizer.fit_transform(train_data['text'])

    # 在测试集上转换特征向量
    test_features = vectorizer.transform(test_data['text'])

    # 创建 LinearSVC 分类器
    classifier = LinearSVC()

    # 在训练集上训练模型
    classifier.fit(train_features, train_data['target'])

    # 保存模型权重和向量化器
    joblib.dump(classifier, 'sentiment_model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')

    # 在测试集上进行预测
    predictions = classifier.predict(test_features)

    # 计算准确率
    accuracy = accuracy_score(test_data['target'], predictions)
    print("模型在测试集上的准确率：", accuracy)


if __name__ == '__main__':
    leaning()
