# anscombe.py
"""View the graphs of the Anscombe Quartet."""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def anscombe_quartet():
    # load the dataset for Anscombe's quartet
    df = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/datasets/anscombe.csv')

    # apply the theme ticks
    sns.set_theme(style="ticks")

    # create the 'Figure' and 'Axes Objects
    figure, axes = plt.subplots(2, 2, figsize=(10, 10))

    # show the results of a linear regression within each dataset
    graph1 = sns.regplot(x=df.x1, y=df.y1, ci=None, scatter_kws={"s": 80}, ax=axes[0][0])
    graph2 = sns.regplot(x=df.x2, y=df.y2, ci=None, scatter_kws={"s": 80}, ax=axes[0][1])
    graph3 = sns.regplot(x=df.x3, y=df.y3, ci=None, scatter_kws={"s": 80}, ax=axes[1][0])
    graph4 = sns.regplot(x=df.x4, y=df.y4, ci=None, scatter_kws={"s": 80}, ax=axes[1][1])

    # set the axis label for each chart
    graph1.set(xlabel=r'$x_1$', ylabel=r'$y_1$')
    graph2.set(xlabel=r'$x_2$', ylabel=r'$y_2$')
    graph3.set(xlabel=r'$x_3$', ylabel=r'$y_3$')
    graph4.set(xlabel=r'$x_4$', ylabel=r'$y_4$')

    # adds a main title to the chart
    plt.subplots_adjust(top=0.9)
    plt.suptitle("Anscombe's quartet", fontsize=25)

    # view the plot
    plt.show()
    
    
if __name__ == '__main__':
    anscombe_quartet()
    