import matplotlib.pyplot as plt
import numpy
import pandas
from pandas.tools.plotting import scatter_matrix

OUTPUT_FILE = 'users_w_similarity_w_biometric.csv'
names = ['dwell_disp', 'dwell_time', 'flight_disp', 'flight_time', 'mouse_distance', 'mouse_points', 'bot_score']
data = pandas.read_csv(OUTPUT_FILE, names=names)


# Univariate Histograms
def histogram():
    data.hist()
    plt.show()


# Density Plots
def density():
    data.plot(kind='density', subplots=True, layout=(3, 3), sharex=False)
    plt.show()


# Correction Matrix Plot
def correlation():
    correlations = data.corr()
    # plot correlation matrix
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(correlations, vmin=-1, vmax=1)
    fig.colorbar(cax)
    ticks = numpy.arange(0, 9, 1)
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(names)
    ax.set_yticklabels(names)
    plt.show()


# Scatterplot Matrix
def scatter():
    scatter_matrix(data)
    plt.show()


# Box and Whisker Plots
def box_whisker():
    data.plot(kind='box', subplots=True, layout=(3, 3), sharex=False, sharey=False)
    plt.show()


switch = {
    histogram: histogram,
    density: density,
    correlation: correlation,
    scatter: scatter,
    box_whisker: box_whisker,
}

switch[histogram]()