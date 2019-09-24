import xml.etree.ElementTree as ET

string = '''
<person>
    <name>Max</name>
    <age>27</age>
</person>'''

data = ET.fromstring(string)
print(data.find('age').text)
