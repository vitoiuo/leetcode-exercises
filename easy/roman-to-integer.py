# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000


def romanToInt(s):
    roman_symbols_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    previous_match_map = {'I':['V','X'], 'X':['L','C'], 'C':['D','M']}

    integer_correspondence = 0
    for index, symbol in enumerate(list(s)):
        previous_symbol = list(s)[index-1] if index > 0 else ''
        if previous_symbol in previous_match_map and symbol in previous_match_map[previous_symbol]:
            integer_correspondence = integer_correspondence + roman_symbols_map[symbol] - 2*roman_symbols_map[previous_symbol]
        else:
            integer_correspondence+=roman_symbols_map[symbol]
    return integer_correspondence
