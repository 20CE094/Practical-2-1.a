#Name-Nehal Patel
#ID- 20CE094
#Write a Python script to check whether a given key already exists in a dictionary.
#Github link: https://github.com/20CE094/Practical-2-1.a.git

dict = {1:'50', 2:'180', 3:'9'}
a=int(input("Enter a value: "))
if a in dict:
    print("key is present in dictionary")
else:
        print("key is not present in dictainary")