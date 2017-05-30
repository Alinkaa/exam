import urllib
import xml.etree.ElementTree as ET

serviceurl = raw_input('Enter location: ')
if not serviceurl: serviceurl = 'comments_283746.xml'

print 'Retrieving', serviceurl
uh = urllib.urlopen(serviceurl)
data = uh.read()
stuff = ET.fromstring(data)

cou = stuff.findall('comments/comment/count')
cou2=stuff.findall('comments/comment/name')
for i in cou:
        for b in cou2:
                print i.text
                print b.text

#TODO
#Make dictionary from elements in xml file where: key - name, value - count


#print dictionary
