'''numbers = [1,2,3,4] #lists of nums
print(numbers)

triples = [1,2,3,4 ] *3 #  printing the list trice
print(triples)

Alist = [11, 22 ,33 , 44, 55]
Alist = Alist[::-1]
print(Alist, "\n")'''
'''
L= [1,2,4,3,6,4,9,4,5,3]
print("original list: ", L)

count = 0

for i in L:
    count += i

avg = count/len(L) 

print("sum=", count)
print("Average=", avg)

L.sort()

print("smallest number is: ", L[0])
print("largest number is: ", L[-1])'''

def match_words(words):
    ctr = 0
    lst = []
    for word in words:
       if len(word) > 1 and word[0] == word[-1]:
        ctr += 1
        lst.append(word)

    print("list of words with first and last character being same are ", lst )
    return ctr

count = match_words(["bob", "mom", "dad", "cfc" , "father" , "noon", "3333", "300003", "29383", "tit", "tat", "5678"])



