import xlwt
import xlrd

book = xlwt.Workbook()
ws = book.add_sheet('First Sheet')  # Add a sheet

f = open('testsvc.txt', 'r+')

data = f.readlines() # read all lines at once
for i in range(len(data)):
  row = data[i].split()  # This will return a line of string data, you may need to convert to other formats depending on your use case

  for j in range(len(row)):
    ws.write(i, j, row[j])  # Write to cell i, j

book.save('TESTSVC' + '.xls')
f.close()