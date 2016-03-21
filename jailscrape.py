# import syntax is a little more specific in this case
import urllib2, csv, mechanize
from bs4 import BeautifulSoup
# get a piece of the library rather than the whole thing


# Get the output file ready
output = open('output.csv', 'w')
writer = csv.writer(output)
# Don't need input because URL is the input

# Get the HTML of the page
# br is short for browser
br = mechanize.Browser() #set up
br.open('https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500') #performing action
html = br.response().read()


# Set up is done
# Now need to use Beautiful Soup to take our diagnosis and use it to pull information

#END OF CLASS MARCH 16


# Transform the HTML into a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Find the main table using both the "align" and "class" attributes
main_table = soup.find('table',
	{'align': 'center',
	'class': ['collapse', 'shadow', 'BCSDTable']
})
# Lines 29-32 are one line of code broken down for readability

# Now get the data from each table row
for row in main_table.find_all('tr'):
	data = [cell.text for cell in row.find_all('td')] #on the right we have the loop
	#print data
	writer.writerow(data)
	
