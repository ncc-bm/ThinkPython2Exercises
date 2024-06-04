import sys, openpyxl

if (len(sys.argv) < 4) or (len(sys.argv) > 4):
    print('Usage python blankRowInserter.py starti_row row_num_to_insert file_name')

wb = openpyxl.load_workbook(sys.argv[3])
sheet = wb.active
sheet.insert_rows(int(sys.argv[1]), int(sys.argv[2]))

wb.save('produceSales_newRows.xlsx')