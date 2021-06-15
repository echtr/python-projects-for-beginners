def unique_in_order(iterable):
    list = []
    last_char = ""
    c = 0
    for i in iterable:
        if c == 0:
            list.append(i)
            c = 1
            last_char = i
        else:
            if i == last_char:
                pass
            else:
                list.append(i)
                last_char = i
    return list
                
