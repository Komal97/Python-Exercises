from nltk.tokenize import word_tokenize, sent_tokenize

text = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

print(sent_tokenize(text))
print(word_tokenize(text))

