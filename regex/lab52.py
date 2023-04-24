import re
import csv

result =[["Order", "Name", "Total"]]

file = open('row.txt','r')

text = file.read()

BINPattern = "\nБИН\s+(?P<BIN>[0-9]{12})"
KassaPattern = "\nКасса\s+(?P<Kassa>.+)"

BINValue = re.search (BINPattern, text).group("BIN")
KassaValue = re.search (KassaPattern, text).group("Kassa")

print(BINValue)

ItemPatternText = r"\n(?P<Order>.*)\n(?P<Name>.*)\n(?P<Count>.*)x(?P<Price>.*)\n(?P<Subtotal>.*)\nСтоимость\n(?P<Total>.*)\n"
ItemPattern = re.compile(ItemPatternText)
items = re.finditer(ItemPattern, text)
for match in items:
    row = [match.group("Order"), match.group("Name"), match.group("Total")]
    result.append(row)
    
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)