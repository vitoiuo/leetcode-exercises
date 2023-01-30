# Problem: https://leetcode.com/problems/integer-to-roman/submissions/876220835/

class Solution(object):
    def intToRoman(self, num):
        roman_symbols_map = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V',4:'IV', 1:'I'}
        roman_correspondence = ''

        for key, value in roman_symbols_map.items():
            if(num == 0):
                break
            if(num // key >= 1):
                roman_correspondence+=value*(num // key)
                num %= key

        return roman_correspondence