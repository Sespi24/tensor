import xml.etree.ElementTree as ET

tree = ET.parse('dict.xml')
root = tree.getroot()
print(root)
 
print(root[0].attrib)
print(root[5][0].text)