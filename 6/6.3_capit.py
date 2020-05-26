#Write a function taking in a string like WOW this is REALLY amazing and returning Wow this is really amazing. String should be capitalized and properly spaced. Using re and string is not allowed.



def filter_words(st):
    # Your code here.
    text = " ".join(st.split())
    return text.capitalize()
    

print(filter_words("HELLO world"))

#text = "HELLO world"
#text1 = " ".join(text.split())
#print(text1.capitalize())