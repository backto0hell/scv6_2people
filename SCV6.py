def pasteStringIntoList(list, string):
    if len(list) % 2:
        list.insert(int((len(list) - 1) /2), string)
    else:
        list.insert(int(len(list) / 2) , string)
        
def Func2(a:list, b:str, c:int):
    if len(a) > c and c >= 0:
        a.insert(c, b)
    else:
        return "paste operation is not possible"