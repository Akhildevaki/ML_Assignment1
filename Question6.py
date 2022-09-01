#Finding unique words in a sentence

str = "I am a teacher and I love to inspire and teach people"

s = set(str.split())
print(s)
print("The unique words used in the sentence is : " ,len(s))

