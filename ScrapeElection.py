import csv, mechanize
from bs4 import BeautifulSoup

# Get the output file ready
# output = open('output.csv', 'w')
# w wipes out the old file and replaces it
# a means appending and will add to the bottom of the file

output = open('ElectionResults.csv', 'w')
writer = csv.writer(output)

br = mechanize.Browser() #set up
br.open('http://enr.sos.mo.gov/EnrNet/') #performing action

# Fill out the form
br.select_form(nr=0)

br.form['ctl00$MainContent$cboElectionNames'] = ['750003566']
#Grabbing select item on left side and setting it equal to that element

# Submit the form (Press the "submit" button)
br.submit('ctl00$MainContent$btnElectionType')
#This essentially clicks the submit the button

html = br.response().read()

# The result is basically the same code from jailscrape.py, just isolating different parts
# Paste stuff after "Get HTML"
# Transform the HTML into a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Find the main table using both the "align" and "class" attributes
main_table = soup.find('table',
		{'id': 'MainContent_dgrdResults'
})

# Now get the data from each table row
for row in main_table.find_all('tr'):
	#data = [cell.text for cell in row.find_all('td')]
	data = [cell.text.replace(u'\xa0', ' ') for cell in row.find_all('td')] #on the right we have the loop
	#print data
	writer.writerow(data)



