#import xml library for parsing xml
import xml.etree.Elementtree as ET

#input data string inside triple quotation save it to variable
input = '''
<stuff>
	<users>
		<user x="2">
			<id>001</id>
			<name>Nicholas</name>
		</user>
			<user x="7">
			<id>009</id>
			<name>Brent</name>
		</user>
	</users>
</stuff>'''

#get input string, pass it to ET.fromstring, pass it inside stuff = tree object
#outside world to inside world
stuff = ET.fromstring(input)

#findall user tags below users <users><user x="2"></user></users>
#list of dom tags
lst = stuff.findall('users/user')

#print how many there are in lst
print('User count:', len(lst))

#start definite loop on the list lst
for item in lst:

	#find the <name></name>, then get the text inside it, then print it
	print('Name', item.find('name').text)

	#find the <id></id>, then get the text inside it, then print it
	print('Id', item.find('id').text)

	#from <user ="7"></user>, get the value of attribute "x"
	print('Attribute', item.get("x"))
