# def isValid(s):
#     valid = []
#     end_tags_map = {'[':']','{':'}','(':')'}
#     for index,char in enumerate(s):
#         if(char in end_tags_map.keys()):
#             valid = end_tags_map[char] in s[index+1:-1] and s.index(end_tags_map[char])

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

print(isValid(")(){}"))


#a partir do bracket, precisa ter algo que o feche, porém, não pode haver nenhuma outro tipo de bracket de fechamento no caminho 