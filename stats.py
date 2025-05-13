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


    