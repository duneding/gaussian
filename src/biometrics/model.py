import scipy.cluster.hierarchy as hcluster
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.tools.plotting import scatter_matrix
import numpy
from numpy import inf

def plot_scatter(x, y, clusters):
    # plotting
    plt.scatter(x, y, c=clusters, edgecolors='g')
    plt.axis("equal")
    title = "threshold: %f, number of clusters: %d" % (thresh, len(set(clusters)))
    plt.title(title)
    plt.show()

tracks = pd.read_csv('output.csv', names=['start_time', 'end_time', 'avg_pressure', 'avg_dwell_time', 'avg_flight_time', 'pattern'])
tracks.pop('pattern')
tracks_norm = (tracks - tracks.mean()) / (tracks.max() - tracks.min())
tracks = numpy.log10(tracks_norm)
tracks[tracks == -inf] = 0
tracks_norm = tracks

# clustering
thresh = 3
clusters = hcluster.fclusterdata(tracks_norm, thresh, criterion="distance")
plot_scatter(tracks_norm.end_time, tracks_norm.avg_pressure, clusters)
plot_scatter(tracks_norm.end_time, tracks_norm.start_time, clusters)
plot_scatter(tracks_norm.avg_pressure, tracks_norm.avg_dwell_time, clusters)
plot_scatter(tracks_norm.avg_dwell_time, tracks_norm.avg_flight_time, clusters)

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