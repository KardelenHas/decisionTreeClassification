import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from openpyxl import Workbook,load_workbook
import math

trainDATA = pd.read_csv('trainDATA.csv')

def calculationEntropy(column):
    count = np.bincount(column)
    probabilities = count / len(column)
    entropy = 0

    for probablity in probabilities:
        if probablity > 0:
            entropy += probablity * math.log(probablity, 2)
    return -entropy

def calculationInfoGain(data, split, target):
    firstEntropy = calculationEntropy(data[target])
    values = data[split].unique()
    subset = [data[data[split] == value] for value in values]
    remove = 0

    for subset in subset:
        probablity = (subset.shape[0] / data.shape[0]) 
        remove += probablity * calculationEntropy(subset[target])

    return firstEntropy - remove

columns = ['Price', 'MaintPrice', 'NoofDoors', 'Persons', 'Lug_size', 'Safety']

def highestInfoGain(columns):
    gainInfo = {}

    for column in columns:
        infoGain = calculationInfoGain(trainDATA, column, 'Car Acceptibility')                                       
        gainInfo[column] = infoGain        

    print(gainInfo)

    return max(gainInfo, key=gainInfo.get)

print("\nHighest gain= " + highestInfoGain(columns))