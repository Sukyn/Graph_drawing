def remove_all(l, x):
    try:
        while(True):
            l.remove(x)
    except ValueError:
        pass

def count_occurence(l, x):
    return l.count(x)
