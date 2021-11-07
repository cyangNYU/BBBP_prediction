### BBBP prediction

(Blood-Brain-Barrier-Permeability prediction)

#### Prepared datasets

|             Train set              |                          Test sets                           |
| :--------------------------------: | :----------------------------------------------------------: |
| train_set.csv (LightBBB train set) |               test_set.csv (LightBBB test set)               |
|   train_set_2.csv (MoleculeNet)    | test_set.csv (LightBBB test set) \| test_set_combined.csv (LightBBB train_test set) \| test_set_2.csv (LightBBB test set more) \| test_set_3.csv (B3DB dataset) \| test_set_4.csv (B3DB dataset with logBB) \| test_set_5.csv (B3DB dataset with \|logBB\| >=1) |

#### Available trained model: 

Balanced Random Forest Classifier 

| Balanced RF Classifier |        model/RF_model.pickle.dat        |
| :--------------------: | :-------------------------------------: |
|   Number of features   |     743 (model/RF_features.pickle)      |
|  Number of estimators  |                   400                   |
|       Train set        | dataset/feature_set_all/train_set_2.csv |

#### Performance

1. Test_set.csv

|    Model    |  tp  |  tn  |  fp  |  fn  | accuracy | precision | recall |  f1  | roc_auc | avg_precision |
| :---------: | :--: | :--: | :--: | :--: | :------: | :-------: | :----: | :--: | :-----: | :-----------: |
| Balanced RF |  16  |  16  |  1   |  0   |   0.97   |   0.94    |  1.00  | 0.97 |  0.97   |     0.94      |
|  LightBBB   |  16  |  13  |  1   |  3   |   0.88   |   0.93    |  0.81  | 0.87 |  0.88   |     0.85      |

2. Test_set_combined.csv

|    Model    |  tp  |  tn  |  fp  |  fn  | accuracy | precision | recall |  f1  | roc_auc | avg_precision |
| :---------: | :--: | :--: | :--: | :--: | :------: | :-------: | :----: | :--: | :-----: | :-----------: |
| Balanced RF | 1452 | 683  | 189  | 239  |   0.83   |   0.88    |  0.86  | 0.87 |  0.82   |     0.85      |

3. Test_set_2.csv

|    Model    |  tp  |  tn  |  fp  |  fn  | accuracy | precision | recall |  f1  | roc_auc | avg_precision |
| :---------: | :--: | :--: | :--: | :--: | :------: | :-------: | :----: | :--: | :-----: | :-----------: |
| Balanced RF |  17  |  23  |  2   |  2   |   0.91   |   0.89    |  0.89  | 0.89 |  0.91   |     0.85      |

4. Test_set_3.csv

|    Model    |  tp  |  tn  |  fp  |  fn  | accuracy | precision | recall |  f1  | roc_auc | avg_precision |
| :---------: | :--: | :--: | :--: | :--: | :------: | :-------: | :----: | :--: | :-----: | :-----------: |
| Balanced RF | 3001 | 2044 | 482  | 556  |   0.83   |   0.86    |  0.84  | 0.85 |  0.83   |     0.82      |

5. Test_set_4.csv

|    Model    |  tp  |  tn  |  fp  |  fn  | accuracy | precision | recall |  f1  | roc_auc | avg_precision |
| :---------: | :--: | :--: | :--: | :--: | :------: | :-------: | :----: | :--: | :-----: | :-----------: |
| Balanced RF | 518  |  65  |  34  | 154  |   0.76   |   0.94    |  0.77  | 0.85 |  0.71   |     0.92      |
