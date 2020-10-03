
import re
data = input('Input data :');
digit = re.findall('[0-9]',data)
text = re.findall('[a-zA-Z]',data)
print('LETTERS '+ str(len(text)))
print('DIGITS '+ str(len(digit)))