#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 02:37:52 2019

@author: root
"""

# '% reset' to clear variables
import tensorflow as tf
import tensorflow.contrib.learn as skflow
from sklearn import datasets, metrics

iris = datasets.load_iris()

#classifier = skflow.DNNClassifier(hidden_units=[10,20,10],n_classes=3)
feature_columns = [tf.contrib.layers.real_valued_column("", dimension=1)]
classifier = skflow.LinearClassifier(feature_columns=feature_columns, n_classes=3)
classifier.fit(iris.data, iris.target)

score = metrics.accuracy_score(iris.target,classifier.predict(iris.data))
print("Accuracy : %f" % score)













#https://stackoverflow.com/questions/41372375/attributeerror-module-tensorflow-contrib-learn-has-no-attribute-tensorflowdn
#https://stackoverflow.com/questions/46037627/tensorflow-contrib-learn-dnnclassifier-missing-1-required-positional-argument