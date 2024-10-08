# -*- coding: utf-8 -*-
"""Copy of Email spam.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10SVDcgpGtl7lEgQygvYg-TWWH-xg3TFz
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('/content/spam.csv', encoding="ISO-8859-1")
data

data.columns

data.info()

data.isnull().sum()

data.isnull().mean()*100

data.drop(columns=data[['Unnamed: 2','Unnamed: 3','Unnamed: 4']],axis=1,inplace=True)
data.head()

# visualizing the data - swarm plot
sns.swarmplot(x='v1', y='v2', data=data)
plt.xlabel('Email Type')
plt.ylabel('length')
plt.title('Swarm plot of length with spam/Ham Differentiation')
plt.show()

sns.boxplot(x='v1', y='v2', data=data)
plt.xlabel('Email Type')
plt.ylabel('length')
plt.title('Box plot of length with spam/Ham Differentiation')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report,confusion_matrix

x_train, x_test, y_train, y_test = train_test_split(data['v2'], data['v1'], test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
x_train_vectorized = vectorizer.fit_transform(x_train)
x_test_vectorized = vectorizer.transform(x_test)

classifier = MultinomialNB()
classifier.fit(x_train_vectorized, y_train)

y_pred = classifier.predict(x_test_vectorized)

accuracy = accuracy_score(y_test, y_pred)
confusion_matrix = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Confusion Matrix:")
print(confusion_matrix)
print("Classification Report:")
print(classification_rep)m