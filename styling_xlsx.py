import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb['Sheet']
italic24Font = Font(size=24, italic=True) # Create a font
sheet['A1'].font = italic24Font # Apply the font to A1.
sheet['A1'] = 'Hello world!'
wb.save('styles.xlsx')

fontObj1 = Font(name='Times New Roman', bold=True)
sheet['B1'].font = fontObj1
sheet['B1'] = 'Bold Time New Roman'

fontObj2 = Font(size=24, italic=True)
sheet['B3'].font = fontObj2
sheet['B3'] = '24 pt Italic'

sheet['A4'] = 200
sheet['A5'] = 300
sheet['A6'] = '=SUM(A4:A5)' # Set the formula

wb.save('styles.xlsx')