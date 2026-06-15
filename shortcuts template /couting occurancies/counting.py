num = [1,2,3,1,5,7,2,8,9,1]
freq ={}

for x in num:
    freq[x] = freq.get(x,0)+1

print(freq) 