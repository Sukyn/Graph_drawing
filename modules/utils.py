def remove_all(l, x):
    try:
        while(True):
            l.remove(x)
    except ValueError:
        pass
