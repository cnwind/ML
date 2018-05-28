# -*- coding: utf-8 -*-
"""
Created on Mon May 28 14:13:17 2018

@author: Administrator
"""

from math import log

"""
输入数据集，计算香农熵
"""
def calShannonEnt(dataset):
    numEntries = len(dataset)
    labelCounts={}
    for featVec in dataset:
       # print("featVec"+featVec)
        currentLabel = featVec[-1]
        print("currentLabel"+currentLabel)
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        print("labelCounts[key]:"+str(labelCounts[key])+", prob:"+str(prob))
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt
"""
生成测试数据集
"""
def createDataSet():
    dataSet=[[1,1,'yes'],
             [1,1,'yes'],
             [1,0,'no'],
             [0,1,'no'],
             [0,1,'no']]
    labels= ['no surfacing', 'flippers']
    return dataSet, labels


def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        print("featVec:"+str(featVec))
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            print("reducedFeatVec:"+str(reducedFeatVec))
            reducedFeatVec.extend(featVec[axis+1:1])
            print("reducedFeatVec extends:"+str(reducedFeatVec))
            retDataSet.append(reducedFeatVec)
    return retDataSet

myDat, labels = createDataSet()

#print(calShannonEnt(myDat))

print(splitDataSet(myDat, 1, 1))