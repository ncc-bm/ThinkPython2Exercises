#! python3
# readCensusExcel.py - Tabulates population and number of census tracts for
# each country.

import openpyxl, pprint

print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

# TODO: Fill in countryData with each country's  population and tracts.
print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # Make shure the key for this state exists.
    countyData.setdefault(state, {})

    # Make shure the key for this country in this state exists.
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # Each row represents one census tract, so increment by one.
    countyData[state][county]['tracts'] += 1
    # Increase the country pop by the pop in this censys tract.
    countyData[state][county]['pop'] += int(pop)

# Open a new text file and write the contents of countryData to it.
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData =' + pprint.pformat(countyData))
resultFile.close()
print('Done.')
