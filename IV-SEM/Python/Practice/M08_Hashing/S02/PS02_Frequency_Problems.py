# 1.count frequency of each elements(using dictionary and using counter)
# a = [1,2,2,1,2,1]
# freq={}
# for i in a:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)

# 2. count distinct elements

# 3. find elemet with maximum frequency
a = [1,2,2,1,2,1]
freq={}
for x in a:
    freq[x]=freq.get(x,0)+1
    max_ele=max(freq, key=freq.get)
print(max_ele)
# 4. first non-repeating element


# # 5.count Occurance of each character in String
# 6.Check if two arrays have same frequency
# 7.elements appearing more than n/2 times(majority elements)``


