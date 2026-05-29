def first_non_repeating_char(string):
    freq = {}
    for x in string:
        freq[x] = freq.get(x,0) + 1
    for i in string :
        if freq[i] == 1:
            return i
    return -1
print(f"the first non-repeating char is: {first_non_repeating_char("leetcode")}")

