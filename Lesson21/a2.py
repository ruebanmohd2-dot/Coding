def match_words(x):
    Y = []
    for i in x:
        if i[0] == i[-1]:
            Y.append(i)
    return Y


X = ["Hi", "Hello", "How", "Are", "You", "Im",
     "Fine", "Thanks", "cfc", "aba", "dfd"]
Xyz = match_words(X)
print(Xyz)
print(len(Xyz))
