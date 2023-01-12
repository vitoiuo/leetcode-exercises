# Problem: https://leetcode.com/problems/valid-parentheses/

def isValid(s):
    stock = []
    valid = False
    end_tags_map = {'[':']','{':'}','(':')'}
    key_list = list(end_tags_map.keys())
    val_list = list(end_tags_map.values())
    for char in s:
        if(char in end_tags_map.keys()):
            stock.append(char)
        elif(bool(stock) and key_list[val_list.index(char)] == stock[-1]):
            valid=True 
            stock.pop()
        else:
            valid=False
            return valid
    return stock == [] and valid
