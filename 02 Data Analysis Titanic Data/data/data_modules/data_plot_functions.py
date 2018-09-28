import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_distribution(data_frame, ax=None, color=None):
    '''
    Plots a distribution chart from data frame series
    '''
    ax_order = ax or None
    color_name = color or None
    return sns.distplot(data_frame, kde=False, ax=ax_order, color=color_name)

def get_means_of(data_frame):
    '''
    From data frame returns its mean, median and mode
    '''
    return {'mean': data_frame.mean(), \
            'median': data_frame.median(), \
            'mode': data_frame.mode().get_values()[0]}

def draw_means_lines(data_frame, distribution=None):
    mean, median, mode = get_means_of(data_frame).values()
    format_2_decimals = lambda number: f'{float(number):.2f}'
    plot = distribution if distribution else data_frame
    plot.axvline(mean, color='#000000', linestyle='-', label=f'mean {format_2_decimals(round(mean, 2))}')
    plot.axvline(median, color='#555555', linestyle='--', label=f'median {format_2_decimals(round(median, 2))}')
    plot.axvline(mode, color='#777777', linestyle=':', label=f'mode {format_2_decimals(round(mode, 2))}')
    
def plot_distribution_with_means(data_frame, ax=None, color=None, title=None):
    ''''
    Plots a seaborn distribution chart with mean, median and mode mark line
    '''
    distribution_plot = plot_distribution(data_frame, ax=ax, color=color)
    draw_means_lines(data_frame, distribution=distribution_plot)    
    distribution_plot.legend()
    distribution_plot.set_title(title.upper())

    return distribution_plot
    
def set_title(data_frame_plot, title):
    '''
    Sets a title to a plot
    '''
    data_frame_plot.set_title(title.upper(), fontdict={'verticalalignment': 'bottom'})

def set_plot_by(rows, columns, figsize, sharex=None, sharey=None):
    '''
    Sets basic structure to show charts
    '''
    sharex, sharey = sharex if sharex else 'none', sharey if sharey else 'none'

    figure, ax = plt.subplots(rows, columns, sharex=sharex, sharey=sharey, figsize=figsize)
    figure.show()
    
def apply_all_texts_color(axis, color):
    '''
    Sets chosen color in all texts of a plot
    '''
    for text in axis.texts:
        text.set_color(color)