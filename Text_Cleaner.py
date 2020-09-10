import numpy as np
import pandas as pd
import re
import os
import json
import sys


with open('Num2Txt.json', 'r') as f:
    Num2Txt = json.load(f)
print("1 for String \n2 for filename (add .txt)")
input_option= input()

flag=0

if input_option=="1":
    print("Please enter a sentence/paragraph to clean")
    input_string=sys.stdin.read()
elif input_option=="2":
    print("please enter the name of file\n")
    input_string=input()
    with open(input_string,'r') as txt:
        input_string=str(txt.readlines())
        flag=1
        
#input_string="""20 The English Wikipedia is the English-language edition of the free online encyclopedia Wikipedia. Founded on 15 January 2001, it is the first edition of Wikipedia and, as of April 2019, has the most articles of any edition.[2] As of September 2020, 11% of articles in all Wikipedias belong to the English-language edition. This share has gradually declined from more than 50 percent in 2003, due to the growth of Wikipedias in other languages.[3] As of 9 September 2020, there are 6,155,427 999 0987 articles and &&**21230000))((&&@#*$&))"""

input_string=re.sub('[^A-Za-z0-9\s.]+', ' ', input_string)
word_list=input_string.split(" ")

print("Input String:\n\n",input_string)

clean_txt=""

for i in word_list:
    num_word=""
    if i.isnumeric():
        num_word = Num2Txt.get(i)
        if num_word:
            clean_txt+=" "+num_word
        else:
            clean_txt+=" "+"<"+str(i)+">"
            
    else:
        clean_txt+=" "+i

print("\nOutput String:\n\n",clean_txt)

out_file="./CleanedTxt.txt"

fp = open(out_file, 'w')
fp.write(clean_txt)


f.close()
fp.close()

if flag==1:
    txt.close()

print("\n Cleaned text is stored in CleanedTxt.txt file")



