#https://stackoverflow.com/questions/2136556/in-python-how-do-i-split-a-string-and-keep-the-separators?lq=1 

def splitkeep(s, delimiter):
    split = s.split(delimiter)
    return [substr + delimiter for substr in split[:-1]] + [split[-1]]
