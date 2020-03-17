from gtts import gTTS
import os

fh = open('test.txt', 'r')
myText = fh.read().replace("\n", " ")
#myText = "Text to speech conversion using python"

language = 'en'

#output = gTTS(text=myText, lang=language, slow=False)
#output.save('output.mp3')
#os.system("start output.mp3")

output_file = gTTS(text=myText, lang=language, slow=False)
output_file.save('output_file.mp3')
fh.close()
os.system("start output_file.mp3")

