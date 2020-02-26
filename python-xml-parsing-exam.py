#this is the link to use and the answer sum should be 2520
# http://py4e-data.dr-chuck.net/comments_373681.xml

# import urllib library
import urllib.request, urllib.parse, urllib.error
# import xml library
import xml.etree.ElementTree as ET

# program will prompt for a url and will save it inside url variable
url = input("Enter location: ")

# if length of url is less than 1, the url will be automatically set
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_373681.xml"

# will print Retrieving url
print("Retrieving " + url)

# FILE HANDLER
# this line will get url and read it and save it to xml variable as file handler
xml = urllib.request.urlopen(url).read()

# printing how many length of characters are retrieved from xml file handler
print("Retrieved: " + str(len(xml)) + " characters")

# PARSING WILL RETURN A LIST
# this will parse values from xml variable
tree = ET.fromstring(xml)

# this will find all count tags then save it to counts variable
# this will tree.findall will return a list
counts = tree.findall('.//count')
print("Count: " + str(len(counts)))

# variable for total
totalsum = 0

# will start indefinite loop 
for count in counts:

	# total sum will be equal to previous totalsum + current text in count tag
    totalsum += int(count.text)

# print the total sum
print("Sum:" + str(totalsum))