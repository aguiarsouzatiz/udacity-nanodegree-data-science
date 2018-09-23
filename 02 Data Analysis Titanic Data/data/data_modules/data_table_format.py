def set_template_positions():
    return {'left':[], 'right': [], 'center': []}


def get_column_names_position(data_frame, names):
    adjust_index = 2
    return [(data_frame.columns.get_loc(name) + adjust_index) for name in names]


def get_column_alignments_positions(data_frame, alignments=None):
    alignments = alignments or set_template_positions()
    positions = set_template_positions()
    for align in alignments:
        align_names = alignments[align]
        positions[align] = get_column_names_position(data_frame, align_names)
    
    return positions
 
    
def get_column_name_by_type(data_frame, type_list):
    '''
    Given a type and data frame returns a list with corresponding column names
    '''
    return list(data_frame.select_dtypes(include=type_list).columns.values)
    
    
def get_series_alignment_styles(position, align):
    return [dict(selector=f'{tag}:nth-child({position})', props=[('text-align', f'{align}')]) 
            for tag in ['th','td']]


def append_each_style_of(table_styles, styles=None):
    styles = styles or []
    mutate_append = lambda table_styles, style: table_styles.extend(style)
    for style in styles:
        mutate_append(table_styles, style)
    
    return table_styles


def get_table_style_by(align_styles_positions):
    table_styles = append_each_style_of([])
    for align in align_styles_positions:
        positions = align_styles_positions[align]
        align_styles = [get_series_alignment_styles(position, align) for position in positions]
        append_each_style_of(table_styles, align_styles)
    
    return table_styles


def set_default_alignments(data_frame):
    string_alignments = get_column_name_by_type(data_frame, ['object'])
    return {'left': string_alignments}
    

def format_table(data_frame, alignments=None):
    alignments = alignments or set_default_alignments(data_frame)
    align_styles_positions = get_column_alignments_positions(data_frame, alignments)
    styles = get_table_style_by(align_styles_positions)
    
    return data_frame.style.set_table_styles(styles)