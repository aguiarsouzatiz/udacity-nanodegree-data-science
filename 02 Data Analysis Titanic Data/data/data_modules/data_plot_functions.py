import seaborn as sns

def plot_distribution(data_frame, ax=None):
    '''
    Plots a distribution chart from data frame series
    '''
    ax_order = ax or None
    return sns.distplot(data_frame, kde=False, ax=ax_order)

def get_means_of(data_frame):
    '''
    From data frame returns its mean, median and mode
    '''
    return {'mean': data_frame.mean(), \
            'median': data_frame.median(), \
            'mode': data_frame.mode().get_values()[0]}

def plot_distribution_with_means(data_frame, ax=None, title=None):
    ''''
    Plots a seaborn distribution chart with mean, median and mode mark line
    '''
    ax_order = ax or None
    distribution = plot_distribution(data_frame, ax_order)
    mean, median, mode = get_means_of(data_frame).values()
    format_2_decimals = lambda number: f'{float(number):.2f}'
    
    distribution.set_title(title)
    distribution.axvline(mean, color='r', linestyle='-', label=f'mean {format_2_decimals(round(mean, 2))}')
    distribution.axvline(median, color='b', linestyle='--', label=f'median {format_2_decimals(round(median, 2))}')
    distribution.axvline(mode, color='g', linestyle='-.', label=f'mode {format_2_decimals(round(mode, 2))}')
    distribution.legend()
    
def set_title(data_frame_plot, title):
    '''
    Sets a title to plot
    '''
    data_frame_plot.set_title(title, fontdict={'fontsize':16, 'fontweight': 'bold', 'verticalalignment': 'bottom'})