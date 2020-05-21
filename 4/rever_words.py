x = 'hello world'
print(list(x))

# total reverse
def rev (word):
    word_lists = list(word)
    word_lists.reverse()
    return word_lists

def word_rev(rev):
    sent_str = ""
    for i in rev:
        sent_str += str(i)
    return sent_str

new_rev= rev(x)
print(word_rev(new_rev))

#another approach
def reverseW(sentence): 
  
    return ' '.join(word[::-1] for word in sentence.split(" ")) 

print(reverseW(x))

#You need to write a function that reverses the words in a given string. A word can also fit an empty string. If this is not clear enough, here are some examples:

def reverse(st):
    
    return ' '.join(st.split()[::-1])

print(reverse(x))

        


