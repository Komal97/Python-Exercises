programming_languages = ("Java", "Python", "C++")

print(type(programming_languages))

# -- shows error as tuple is immutable --
# programming_languages[0] = "hi"

print("\n")
for language in programming_languages:
    print(language)

print("\n")
l = [1, 2, 3, 4, 5]
print(l[1])

#works as slice method
print(l[1:3])

#dictionary
dictionaries = {"key1" : 15, "key2" : "Komal"}
print(dictionaries["key1"])

dictionaries["key3"] = "Hi"
print(dictionaries)