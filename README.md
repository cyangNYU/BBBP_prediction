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

