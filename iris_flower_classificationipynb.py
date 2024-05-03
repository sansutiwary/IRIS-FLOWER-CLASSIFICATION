# -*- coding: utf-8 -*-
"""IRIS_FLOWER_CLASSIFICATIONipynb.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/sansutiwary/IRIS-FLOWER-CLASSIFICATION/blob/main/IRIS_FLOWER_CLASSIFICATIONipynb.ipynb
"""

!git clone https://github.com/sansutiwary/IRIS-FLOWER-CLASSIFICATION.git

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv('Iris.csv')
df

# Commented out IPython magic to ensure Python compatibility.
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.svm import SVC
import warnings
warnings.simplefilter('ignore')
# %matplotlib inline

df.info()

df.describe()

df['Species'].value_counts()

df.isna().sum()

"""Data Visualization

"""

df1 = df.drop('Id', axis=1)
g = sns.pairplot(df, hue='Species', markers='+')
plt.show()

fig = df1[df1.Species=='Iris-setosa'].plot(kind='scatter',x='SepalLengthCm',y='SepalWidthCm',color='orange', label='Setosa')
df1[df1.Species=='Iris-versicolor'].plot(kind='scatter',x='SepalLengthCm',y='SepalWidthCm',color='blue', label='versicolor',ax=fig)
df1[df1.Species=='Iris-virginica'].plot(kind='scatter',x='SepalLengthCm',y='SepalWidthCm',color='green', label='virginica', ax=fig)
fig.set_xlabel("Sepal Length")
fig.set_ylabel("Sepal Width")
fig.set_title("Sepal Length VS Width")
fig=plt.gcf()
fig.set_size_inches(12,8)
plt.show()

fig = df1[df1.Species=='Iris-setosa'].plot.scatter(x='PetalLengthCm',y='PetalWidthCm',color='orange', label='Setosa')
df1[df1.Species=='Iris-versicolor'].plot.scatter(x='PetalLengthCm',y='PetalWidthCm',color='blue', label='versicolor',ax=fig)
df1[df1.Species=='Iris-virginica'].plot.scatter(x='PetalLengthCm',y='PetalWidthCm',color='green', label='virginica', ax=fig)
fig.set_xlabel("Petal Length")
fig.set_ylabel("Petal Width")
fig.set_title(" Petal Length VS Width")
fig=plt.gcf()
fig.set_size_inches(12,8)
plt.show()

df1.hist(edgecolor='black')
fig=plt.gcf()
fig.set_size_inches(12,6)
plt.show()

plt.figure(figsize=(10,8))
fig, ax = plt.subplots(figsize=(12,9))
sns.heatmap(df1.corr(),annot=True,ax=ax)

label = df['Species']
df.drop(['Species'],inplace=True,axis=1)

df.drop(['Id'] ,inplace =True , axis =1)

df

from sklearn.svm import SVC #import svm as classifier
from sklearn.model_selection import train_test_split

Xtrain,Xtest,ytrain,ytest=train_test_split(df,label,test_size=0.25)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df

svm = SVC(class_weight='balanced') # create new svm classifier with default parameters
svm.fit(Xtrain,ytrain)

from sklearn.metrics import confusion_matrix, accuracy_score
predictions = svm.predict(Xtest) # test model against test set
print("Model Acurracy in testing = {}".format(accuracy_score(ytest, predictions))) # print accuracy

!git clone https://github.com/sansutiwary/IRIS-FLOWER-CLASSIFICATION.git