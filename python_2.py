'''Question 2: -
Consider a string to be valid if all characters of the string appear the same number of times. It is also valid if
he can remove just one character at the index in the string, and the remaining characters will occur the same
number of times. Given a string, determine if it is valid. If so, return YES , otherwise return NO .'''
s=input()
def isValid(s):
    
    length = 0
    
    record_lst = [] #unique alphabet
    record_num = [] #each alphabet occur times
    for i in range(len(s)):
        if s[i] not in record_lst:
            record_lst.append(s[i])
            record_num.append(1)
            length += 1
        else:
            index = record_lst.index(s[i])
            record_num[index] += 1
    
    unique = []
    occur_min = 0 #count minimum occur times in each alphabet occur times
    occur_max = 0 #count maximum occur times in each alphabet occur times
    for i in record_num:
        if i == min(record_num):
            occur_min += 1
        if i == max(record_num):
            occur_max += 1
        if i not in unique: # unique occur times
            unique.append(i)
    
    print(unique)      
    print(record_lst) 
    print(record_num)
    
    # Every alphabet has same occur time is a valid string
    if len(unique) == 1:
        return "YES"  