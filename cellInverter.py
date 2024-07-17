import sys, openpyxl, os.path

fileName = ''

if len(sys.argv) > 2:
    print('Usage python cellInverter.py Excel_File_Name')
elif len(sys.argv) < 2:
    fileName = input('Enter File Name: ')
else:
    fileName = sys.argv[1]

# print(fileName)
if not (os.path.isfile(fileName)):
    print('%s file does not exists. Please enter valid file name!' % fileName)

wb_org = openpyxl.load_workbook(fileName)

sheet_org = wb_org.active

print('Total number of columns in the active sheet %s ' % sheet_org.max_column)
print('Total number of rows in the active sheet %s ' % sheet_org.max_row)

wb_inverted = openpyxl.Workbook()
sheet_inverted = wb_inverted.active

for row in range(1, sheet_org.max_row+1):
    for column in range(1, sheet_org.max_column+1):
        sheet_inverted.cell(row=column, column=row).value = sheet_org.cell(row=row, column=column).value

wb_inverted.save('invertedCells.xlsx')
#wb_inverted.close
#wb_org.close