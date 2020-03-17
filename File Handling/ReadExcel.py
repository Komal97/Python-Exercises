import pandas as pd

file = pd.ExcelFile("sales.xlsx")
print(file.sheet_names)

sheet = file.parse('sales')

#print data of sales sheet
print(sheet)

#print type of sheet
print(type(sheet))

#print Date column
print(sheet.Date)

#print sum of values in Amount column
print(sheet.Amount.sum())

#locate first row data
print(sheet.loc[0])

#locate 'amount' of first row data
print(sheet.loc[0,"Amount"])

#set index
sheet.set_index("Customer", inplace = True)
sheet.loc["MMC Inc."]

#reset index
sheet = sheet.reset_index()

print(sheet.loc[sheet["Invoice"] == 99])

#return row with max amount value
print(sheet.loc[sheet["Amount"].idxmax()])

#return specific column with max amount value
print(sheet.loc[sheet["Amount"].idxmax()]["Customer"])

#return unique customer names having amount>1800
print(sheet.loc[sheet["Amount"]>1800]["Customer"].unique())