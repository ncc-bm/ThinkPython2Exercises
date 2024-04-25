import re
import pyinputplus as pyip

dataFile = open('mad-libs.txt')

fileContent = dataFile.read()
newFileContent = ''

words = fileContent.split()
for word in words:
#    print(re.sub('\W+', '', word))
    pureWordWithoutPunktuation = re.sub('\W+', '',word)
    if pureWordWithoutPunktuation in ['ADJECTIVE', 'NOUN', 'VERB', 'ADVERB']:
        newWord = pyip.inputStr(f'Enter {word.lower()}:', blank=False)
        newWord = word.replace(pureWordWithoutPunktuation, newWord)
#        print(f'Substitue the word {word} with the new word {newWord}')
        newFileContent += newWord + ' '
    else:
        newFileContent += word + ' '

print((newFileContent).rstrip())

dataFile.close()