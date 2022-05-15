def pasteStringIntoList(list, string):
    if len(list) % 2:
        list.insert(int((len(list) - 1) /2), string)
    else:
        list.insert(int(len(list) / 2) , string)