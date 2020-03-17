import docxpy

file = "Artificial Intelligence- Machine Learning Senior Engineer Job?? Description (1).docx"

#extract text
text = docxpy.process(file)
print(text)
a = text.split("\n")
print("Line 1: ", a[0])
b = a[0]
b = b.split(":")
print("Profile: ", b[1].strip())
# if you want the hyperlinks
# doc = docxpy.DOCReader(file)
# doc.process()
# hyperlinks = doc.data['links']
# print(hyperlinks)

