import re

def test(x):
    if(x):
        print("Pass")
    else:
        print("Not pass")

def cleanword(w):
    return re.sub('[^A-Za-z]', '', w)

def has_dashdash(w):
    return "--" in w

def lower(w):
    return w.lower()

def extract_words(s):
    cleanString = map(cleanword,s.replace("--", " ").split())
    return map(lower, cleanString)

def wordcount(w,v):
    return v.count(w)

def wordset(v):
    myList = list(dict.fromkeys(v))
    return sorted(myList)

def length(w):
    return len(w)

def longestword(v):
    if(len(v) == 0):
        return 0
    return max(map(length,v))