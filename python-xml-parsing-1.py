#clever import statment that will do the work for parsing XML
#import a library xml, as means alias, we do not need to type that long
#we just have to type ET
import xml.etree.ElementTree as ET

#triple-quoted string = potentially multi-lined string then save it inside data
data = '''
<person>
	<name>Nicholas</name>
	<phone type="intl">
	+1 234 567 8910
	</phone>
	<email hide="yes"/>
</person>'''

#get string data from "data",  pass it to ET.fromstring so it will return a tree(DOM)
tree = ET.fromstring(data)

#with that tree data, find me the tag <name> then get the text then print
#example <name>Nicholas</name> to Nicholas
#.text is the attribute of the node name tag
print('Name:',tree.find('name').text)

#go find me the email tag, then get me the attribute hide = yes
#example <email hide="yes"/>
print('Attr:',tree.find('email').get('hide'))