from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn import metrics, cluster
import matplotlib.pyplot as plt
from sklearn import svm
import pandas as pd


data = pd.read_csv("raw_data/crime_processed_neighbourhood.csv").as_matrix()
print len(data[0])
X = data[:, [0,1,2,3,4,5,6,7,9]]
Y = data[:, 8]


#--------------------------------USING an RBF kernel--------------------------------


print "Data split into training and testing:"


print "Generating clusters....."

k_means = cluster.KMeans(n_clusters=2)

k_means.fit(X)

preds = k_means.labels_

z = Y > 0
z = z.astype(int)
print "ROC_AUC: ", metrics.roc_auc_score(z,preds)

