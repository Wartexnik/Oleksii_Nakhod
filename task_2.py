from collections import Counter

def first_non_repeating_letter(str):
    str_lower = str.lower()
    c = Counter(str_lower)
    for letter in c:
        if c[letter] == 1:
            return str[str_lower.find(letter)]
    return ""