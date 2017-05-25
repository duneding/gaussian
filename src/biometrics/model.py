from numpy import array
from scipy.cluster.vq import vq, kmeans, whiten
from time import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
import pandas as pd
from mpl_toolkits.mplot3d import axes3d
from sklearn.cluster import KMeans
from numpy import genfromtxt
from sklearn.preprocessing import scale
import seaborn as sns
import sklearn
import pandas
from sklearn.preprocessing import normalize

def plot_correlation_map( df ):
    corr = df.corr()
    _ , ax = plt.subplots( figsize =( 12 , 10 ) )
    cmap = sns.diverging_palette( 220 , 10 , as_cmap = True )
    _ = sns.heatmap(
        corr,
        cmap = cmap,
        square=True,
        cbar_kws={ 'shrink' : .9 },
        ax=ax,
        annot = True,
        annot_kws = { 'fontsize' : 12 }
    )


from pandas.tools.plotting import scatter_matrix



#my_data = genfromtxt('output.csv', delimiter=',')
#df = pd.read_csv('output.csv', parse_dates=[0], header=None, names=['duration', 'flying_avg'])
#stacked = df.pivot(index='duration', columns='duration', values='flying_avg').fillna(0).stack()

tracks = pd.read_csv('output.csv', names=['duration', 'flying_avg', 'pattern'])
tracks.pop('pattern')
tracks_norm = (tracks - tracks.mean()) / (tracks.max() - tracks.min())
scatter_matrix(tracks, alpha=0.2, figsize=(6, 6), diagonal='kde')
#plot_correlation_map(tracks_norm)

import numpy
import scipy.cluster.hierarchy as hcluster

# clustering
'''
thresh = 3
clusters = hcluster.fclusterdata(tracks_norm, thresh, criterion="distance")
# plotting
plt.scatter(tracks_norm.duration, tracks_norm.flying_avg, c=clusters, edgecolors='g')
plt.axis("equal")
title = "threshold: %f, number of clusters: %d" % (thresh, len(set(clusters)))
plt.title(title)
plt.show()
'''

print 1
# do unsupervised clustering
# =============================================
'''
estimator = KMeans(n_clusters=3, random_state=0)
X = stacked.values.reshape(len(stacked), 1)
cluster = estimator.fit_predict(X)

# check the mean value of each cluster
X[cluster==0].mean()  # Out[53]: 324.73175293698534
X[cluster==1].mean()  # Out[54]: 6320.8504071851467
X[cluster==2].mean()  # Out[55]: 1831.1473140192766
'''