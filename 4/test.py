sentence = ['this','is','a','sentence']
sent_str = ""
for i in sentence:
    sent_str += str(i) + "-"
sent_str = sent_str[:-1]
print (sent_str)

x = 'hello world'
y = list(x)
y.reverse()
print(y)