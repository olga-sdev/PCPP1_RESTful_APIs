"""
XML -> eXtensible Markup Language https://www.w3schools.com/xml/default.asp
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
    
"""
Title: Antibodies IgG to SARS-CoV-2, Price: 25 eur
Title: Antibodies to HIV, Price: 20 eur
Title: Determination of calprotectin in feces, Price: 35 eur
Title: Bacteriological diagnostic study on Legionel, Price: 20 eur
"""
