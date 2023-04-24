import re
file = open('row.txt','r')

text = file.read()

BINPattern = "\nБИН\s+(?P<BIN>[0-9]{12})"
KassaPattern = "\nКасса\s+(?P<Kassa>.+)"

BINValue = re.search (BINPattern, text).group("BIN")
KassaValue = re.search (KassaPattern, text).group("Kassa")

print(BINValue)
print(KassaValue)
