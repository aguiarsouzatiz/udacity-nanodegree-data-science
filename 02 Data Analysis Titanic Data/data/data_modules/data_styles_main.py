# estilos para cada tipo de dado
color_single = '#8e3e96'
color_family = '#a05da7'
color_survivors = '#28b14e'
color_survivors_light = '#5ec17a'
color_victims = '#b12885'
color_victims_light = '#bd589d'
palette_destiny = {'yes': color_survivors, 'no': color_victims}
palette_classes = {'first': '#8a6d3b','second': '#7e888a', 'third': '#8e5753'}
palette_gender = {'male': '#2798de','female': '#de8f27'}
palette_companion = {'single': color_single, 'with_family': color_family}
palette_destiny_classes = {**palette_destiny,**palette_classes}
palette_destiny_gender = {**palette_destiny,**palette_gender}
palette_maturity = {'child': '#ccbf00', 'adult': '#777777'}