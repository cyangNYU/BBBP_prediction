import sys, os
import time, random, pickle
import numpy as np
import pandas as pd
from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score
from hyperopt import STATUS_OK, Trials, fmin, hp, tpe

## Feature set
features = pickle.load(open('data/features.pickle','rb'))

## Dataset
df = pd.read_csv('data/train_set_2.csv')

X_train = np.c_[df[features]]
y_train = np.c_[df['BBclass']]



space={'max_depth': hp.choice('max_depth', [4, 6,8,10,12]),
       "criterion": hp.choice("criterion", ["gini"]),
       'min_samples_split' : hp.choice('min_samples_split', [2,3,4]),
       'min_samples_leaf' : hp.choice('min_samples_leaf', [1,2,3]),
       'max_features' : hp.choice('max_features', [4,6,8,10,12]),
       'n_estimators': hp.choice('n_estimators', [400,500,600])}

def objective(space):
    clf=BalancedRandomForestClassifier(
        n_estimators =space['n_estimators'], criterion = space['criterion'],
        max_depth = space['max_depth'],min_samples_split=space['min_samples_split'],
        min_samples_leaf = space['min_samples_leaf'],
        max_features = space['max_features'], random_state = 10,
        oob_score=True, n_jobs=-1)
    
    clf.fit(X_train, y_train[:,0])
    # y_oob_predict = np.argmax(clf.oob_decision_function_, axis=1)
    # acc = accuracy_score(y_train, y_oob_predict)
    # print ("Accuracy:", acc)
    y_scores = clf.oob_decision_function_[:, 1]
    auc = roc_auc_score(y_train, y_scores)
    print ("AUC:", auc )
    
    return {'loss': -auc, 'status': STATUS_OK }

trials = Trials()
best_hyperparams = fmin(fn = objective, space = space, algo = tpe.suggest, max_evals = 500, trials = trials)
print("The best hyperparameters are : ","\n")
print(best_hyperparams)

