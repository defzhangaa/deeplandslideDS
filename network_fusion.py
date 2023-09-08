'''
Source code of interpretability improved three branched evidential fusion model. 
Author: Jiaxu Zhang
'''

import numpy as np
import pandas as pd
from pyds_ import MassFunction
import copy
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, roc_auc_score, confusion_matrix, classification_report

ntw = 'repvgg'

# data1 = pd.read_csv(ntw + '/'+'original.csv')
# data1.index = data1['File']
# data1 = data1[['True_label', 'non-landslide', 'landslide']]
# data1 = data1.sort_index()

data2 = pd.read_csv(ntw + '/'+'h.csv')
data2.index = data2['File']
data2 = data2[['True_label', 'non-landslide', 'landslide']]
data2 = data2.sort_index()

data3 = pd.read_csv(ntw + '/'+'s.csv') 
data3.index = data3['File']
data3 = data3[['True_label', 'non-landslide', 'landslide']]
data3 = data3.sort_index()

data4 = pd.read_csv(ntw + '/'+'v.csv') # hornet换成h2
data4.index = data4['File']
data4 = data4[['True_label', 'non-landslide', 'landslide']]
data4 = data4.sort_index()

element = ['a', 'b', 'ab']

def ebetp_generation(m):
    me = copy.deepcopy(m)
    me[0] = m[0] + m[2]/2
    me[1] = m[1] + m[2]/2
    me[2] = m[2]
    me = me*me
    me = me/np.sum(me)
    return me

alpha = 0.5
def renyi_entropy(m):
    return np.log2(np.sum(m**alpha))/(1-alpha)

def deng_entropy(m):
    s = 0
    for i in range(len(m)):
        s +=  -m[i]*np.log2(m[i]/(2**len(element[i]) -1))
    return s
        
        
def jensen_renyi_divergence(m1_, m2_):
    # 默认权值相等
    d = renyi_entropy((m1_+m2_)/2) - (renyi_entropy(m1_) + renyi_entropy(m2_) )/2
    d = np.exp(d)
    return d



# 只fuse data2-4
tar = np.zeros((data2.shape[0], 2))
for i in range(data2.shape[0]):
# for i in range(69, 70):
    # m1 = np.array([data1.iloc[i, 1], data1.iloc[i, 2], (1-np.abs(data1.iloc[i, 1]-data1.iloc[i, 2]))/np.e]) + 1e-13
    m2 = np.array([data2.iloc[i, 1], data2.iloc[i, 2], (1-np.abs(data2.iloc[i, 1]-data2.iloc[i, 2]))/np.e]) + 1e-13
    # m2 = m1
    m3 = np.array([data3.iloc[i, 1], data3.iloc[i, 2], (1-np.abs(data3.iloc[i, 1]-data3.iloc[i, 2]))/np.e]) + 1e-13
    m4 = np.array([data4.iloc[i, 1], data4.iloc[i, 2], (1-np.abs(data4.iloc[i, 1]-data4.iloc[i, 2]))/np.e]) + 1e-13
    # m1 /= np.sum(m1)
    m2 /= np.sum(m2)
    m3 /= np.sum(m3)
    m4 /= np.sum(m4)
    
    # ebetp1 = ebetp_generation(m1)
    ebetp2 = ebetp_generation(m2)
    ebetp3 = ebetp_generation(m3)
    ebetp4 = ebetp_generation(m4)


    # d1 = jensen_renyi_divergence(ebetp2, ebetp3, ebetp4)
    # d2 = jensen_renyi_divergence(ebetp1, ebetp3, ebetp4)
    # d3 = jensen_renyi_divergence(ebetp1, ebetp2, ebetp4)
    # d4 = jensen_renyi_divergence(ebetp1, ebetp2, ebetp3)
    d2 = jensen_renyi_divergence(ebetp3, ebetp4)
    d3 = jensen_renyi_divergence(ebetp2, ebetp4)
    d4 = jensen_renyi_divergence(ebetp2, ebetp3)
    
    # s = d1 + d2 + d3 +d4
    s = d2 + d3 +d4
    # sup1 = d1/s
    sup2 = d2/s
    sup3 = d3/s
    sup4 = d4/s
    
    
    
    # deng1 = deng_entropy(ebetp1)
    deng2 = deng_entropy(ebetp2)
    deng3 = deng_entropy(ebetp3)
    deng4 = deng_entropy(ebetp4)
    # s = deng1 + deng2 + deng3 + deng4
    s = deng2 + deng3 + deng4
    # ivd1 = deng1/s
    ivd2 = deng2/s
    ivd3 = deng3/s
    ivd4 = deng4/s


    # renyi1 = renyi_entropy(ebetp1)
    renyi2 = renyi_entropy(ebetp2)
    renyi3 = renyi_entropy(ebetp3)
    renyi4 = renyi_entropy(ebetp4)

    # s = renyi1 + renyi2 + renyi3 + renyi4
    s = renyi2 + renyi3 + renyi4
    # ivr1 = renyi1/s
    ivr2 = renyi2/s
    ivr3 = renyi3/s
    ivr4 = renyi4/s

    # w1 = sup1 * ivd1 * ivr1
    w2 = sup2 * ivd2 * ivr2
    w3 = sup3 * ivd3 * ivr3
    w4 = sup4 * ivd4 * ivr4

    # s_ = w1 + w2 + w3 + w4
    s_ = w2 + w3 + w4
    s = copy.deepcopy(s_)
    # w1 = w1/s
    w2 = w2/s
    w3 = w3/s
    w4 = w4/s

    
    new_ebetp = w2*ebetp2 + w3*ebetp3 + w4*ebetp4
    new_ebetp = MassFunction({'a': new_ebetp[0], 'b': new_ebetp[1], 'ab': new_ebetp[2]})
    ebetp = new_ebetp & new_ebetp
    ebetp = ebetp & new_ebetp
    # ebetp = ebetp & new_ebetp
    print(ebetp)
    tar[i, 0] = ebetp['a']+0.5*ebetp['ab']
    tar[i, 1] = ebetp['b']+0.5*ebetp['ab']
    
y_pred = tar[:, 0] < tar[:, 1]
y_true = data1['True_label']=='landslide'
y_true = y_true.values

acc_score = accuracy_score(y_true, y_pred)
pre_score = precision_score(y_true, y_pred)
rec_score = recall_score(y_true, y_pred)
f_score = f1_score(y_true, y_pred)
matrix = confusion_matrix(y_true, y_pred)
rep = classification_report(y_true, y_pred, digits=4)
print('network name: '+ntw)
print('acc:', acc_score)
print('pre:', pre_score)
print('rec:', rec_score)
print('f-measure:', f_score)
print('confusion matrix: \n', matrix)
print(rep)
# tar = pd.DataFrame(tar)
# tar.to_csv('y_pred.csv')
# y_true = pd.DataFrame(y_true)
# y_true.to_csv('y_true.csv')
