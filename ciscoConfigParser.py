#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

# Select all interfaces with configuration
interfaceConfigRegex = re. compile(r'''(
    ^interface                          # matched text should start with a string "interface" with preceding spaces
    .*?                                 # there should be a configuration of the interface
    \!                                  # interface configuration section should end '!' sign at the end
)''', re.VERBOSE|re.DOTALL|re.MULTILINE)

# Select all interfaces (only names)
allInterfaceRegex = re. compile(r'''(
    ^interface                         # matched text should start with a string "interface" with preceding spaces
    .*                                 # there should type and name of the interface
)''', re.VERBOSE|re.MULTILINE)

# Select necessary interfaces (only names)
interfaceRegex = re. compile(r'''(
    ^interface.*                                            # matched text should start with a string "interface" with preceding spaces
    (Bundle-Ether\d+\s|GigabitEthernet\d+/\d+/\d+/\d+\s|TenGigE\d+/\d+/\d+/\d+\s|HundredGigE\d+/\d+/\d+/\d+\s)   # select specific interfaces
    .*
 )''', re.VERBOSE|re.MULTILINE)


# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []

for groups in interfaceRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No interfaces found.')