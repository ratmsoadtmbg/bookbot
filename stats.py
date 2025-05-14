def word_count(t):
    words = t.split()
    return len(words)

def letter_count(text):
    letters = {}
    for l in text:
        ll = l.lower()
        if ll in letters:
            letters[ll] += 1
        else:
            letters[ll] = 1
    return letters

def sort_on(dict):
    return dict["num"]

def list_sort(list):
    results = []
    for l in list:
        if l.isalpha() == True:
            results.append({"char":l, "num":list[l]})
    results.sort(reverse=True, key=sort_on)
    return results


    