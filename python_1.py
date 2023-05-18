#Question 1: -
'''Write a program that takes a string as input, and counts the frequency of each word in the string, there might
be repeated characters in the string. Your task is to find the highest frequency and returns the length of the
highest-frequency word.'''

import string  
text = input() 
words = [] 

# Store all the words from the input
for word in text.split():     
    words.append(word.strip(string.punctuation).lower())  
# Initialize max frequency to 0
maxFrequency = 0 
maxWord = '' 
# Iterate every word 
for word in words:
    count = 0 
    # Count for every word    
    for w in words:         
        if w == word:             
            count += 1   
    # if count greater than max frequency than replace the word with max maxFrequency  
    if count > maxFrequency:         
        maxFrequency = count         
        maxWord = word  
print(maxWord)