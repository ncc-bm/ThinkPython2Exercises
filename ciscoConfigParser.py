#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

# All sections wich starts with the string "interface" and ends with '!' regex
interfaceConfigRegex = re. compile(r'''(
    ^interface                       # matched text should start with a string "interface" with preceding spaces
    .*?                                 # there should be a configuration of the interface
    \!                                  # interface configuration section should end '!' sign at the end
)''', re.VERBOSE|re.DOTALL|re.MULTILINE)


# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []

for groups in interfaceConfigRegex.findall(text):
    matches.append(groups)

# Copy results to the clipboard.
if len(matches) > 0:
   pyperclip.copy('\n'.join(matches))
   print('Copied to clipboard:')
   print('\n'.join(matches))
else:
    print('No interfaces found.')