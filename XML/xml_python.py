"""
XML -> eXtensible Markup Language https://www.w3schools.com/xml/default.asp

for updating data in xml apply 'SubElement' and 'set' methods then write data in a new file
"""
import xml.etree.ElementTree as ET

# Parse XML data
xml_data = """
<prices>
    <item title="Antibodies IgG to SARS-CoV-2" price="25 eur"/>
    <item title="Antibodies to HIV" price="20 eur"/>
    <item title="Determination of calprotectin in feces" price="35 eur"/>
    <item title="Bacteriological diagnostic study on Legionel" price="20 eur"/>
</prices>
"""
root = ET.fromstring(xml_data)

# Iterate through book elements and print attributes
for item in root.findall('item'):
    title = item.get('title')
    price = item.get('price')
    print(f"Title: {title}, Price: {price}")


new_item = ET.SubElement(root, "item")
new_item.set('title', 'Cortisol')
new_item.set("price", '30 eur')

tree = ET.ElementTree(root)
tree.write("output.xml")


"""
Title: Antibodies IgG to SARS-CoV-2, Price: 25 eur
Title: Antibodies to HIV, Price: 20 eur
Title: Determination of calprotectin in feces, Price: 35 eur
Title: Bacteriological diagnostic study on Legionel, Price: 20 eur
"""
