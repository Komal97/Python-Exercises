import re

# 1. Find Name and age in a string
NameAge = "Janice is 22 and Theon is 33 Gabreil is 44 and Joey is 21"

ages = re.findall(r'\d{1,3}', NameAge)
names = re.findall(r'[A-Z][a-z]*', NameAge)
 
ageDict = {}
x = 0
for eachname in names:
    ageDict[eachname] = ages[x]
    x+=1
    
print(ageDict)

# 2. Find a word in a sentence
# a) if need to check only occurance
if re.search("inform", "We need to inform him with the latest information"):
    print("There is inform")
    
# b) print all occurances of a word
allwords = re.findall("inform", "We need to inform him with the latest information")
for i in allwords:
    print(i)

# c) Find starting and ending index of 'inform' keyword
str = "We need to inform him with the latest information"
for i in re.finditer("inform", str):
    loctup = i.span()
    print(loctup)
    
# 3. Find a pattern in a string ends with 'at' and start ith 's/h/m/p'
str = "Sat, mat, hat, pat"
allstr = re.findall("[shmp]at", str)

for i in allstr:
    print(i)
    
# 4. Series of range of characters
str = "Sat, mat, hat, pat"
str_in_range = re.findall("[h-m]at", str)
for i in str_in_range:
    print(i)
str_except_range = re.findall("[^h-m]at", str)
for i in str_except_range:
    print(i)
    
# 5. Replace 'rat' with 'food'
food = "hat mat rat pat"
regex = re.compile("[r]at")         #compile this regex into pattern objects
food = regex.sub("food", food)
print(food)

# 6. Remove newline characters
randstr = '''Keep the blue flag 
flying high 
Chelsea'''
print(randstr)
regex = re.compile("\n")
randstr = regex.sub(" ", randstr)
print(randstr)

# 7. Replace a single character in string
num = "123 1234 12345 123456 1234567"
print("Matches: ", len(re.findall("\d{5,7}", num)))


    