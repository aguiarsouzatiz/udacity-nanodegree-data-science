def get_percent_of(amount_reference, total):
    '''
    Calculates percentage between a given part of total
    '''    
    return (amount_reference / total) * 100


def condition_to_check_by(condition):
    '''
    Executes for each described condition (key) a verification lambda function (value)
    that accepts data frame or series and returns True or False
    '''
    to_apply = {'null': lambda data: data.isnull().any(),
                'duplicated': lambda data: data.duplicated().any()}
    return to_apply[condition]


def get_column_names(data_frame, condition_in):
    ''''
    Verifies condition and returns column names case condition is True
    '''
    return [column for column in data_frame.columns if condition_in(data_frame[column])]


def check_data_frame(by_method):
    '''
    Executes for each verification data frame type (key) a lambda function:
    - key extract_column_names check data frame and returns columns names
    - key check_conditions check data frame or series and returns data frame column True or False
    '''    
    to_apply = {'extract_column_names': lambda data_frame, condition: 
                                               get_column_names(data_frame, condition),
                'check_conditions': lambda data, condition_in: condition_in(data)}
    return to_apply[by_method]


def get_data_by_condition_from(data_frame):
    '''
    Verifies some given condition in data frame by the 
    funcions condition_to_check_by and check_data_frame
    '''
    def get_data_frame_with(condition, by_method):
        get_from = check_data_frame(by_method)
        has_condition = condition_to_check_by(condition)
        return get_from(data_frame, has_condition)
    return get_data_frame_with


def adjust_column_by(criteria_to_adjust, to_lower=True):
    '''
    Returns a function description to manipulate data rows. 
    It is to be used in data frame apply method
    '''
    format_string = lambda value: str(value).lower() if to_lower else str(value)
    def get_adjusted(value):
        initial_value = str(value).lower() if type(value) == str else value
        if criteria_to_adjust.get(initial_value):
            return format_string(criteria_to_adjust[initial_value]) 
        else: 
            return initial_value
    return get_adjusted