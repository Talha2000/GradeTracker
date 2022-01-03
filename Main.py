import xlsxwriter
workbook = xlsxwriter.Workbook('c:\\temp\\Welocme.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Welcome to Python')
workbook.close()
