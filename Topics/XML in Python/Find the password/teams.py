from lxml import etree


xml_path = "C:\Users\cjmea\AppData\Roaming\JetBrains\PyCharm2021.2\scratches\scratch_1.xml"
root = etree.parse(xml_path).getroot()
members = root[0]
for member in members:
    print(member)

