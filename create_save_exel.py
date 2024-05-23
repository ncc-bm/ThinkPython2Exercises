import openpyxl

wb = openpyxl.Workbook() # create a blank workbook
print(wb.sheetnames)

sheet = wb.active
print(sheet.title)

sheet.title = 'Spam Bacon Eggs Sheet' # Change title
print(wb.sheetnames)