import re
def numsum():
    summ=0
    with open('abc.txt') as file: 
      for line in file:
           array=[]
           array = re.findall(r'[0-9]+',line)
           for i in array:
              summ+=int(i)
    return summ



print(numsum())