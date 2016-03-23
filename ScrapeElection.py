import csv, mechanize
from bs4 import BeautifulSoup

# Get the output file ready
# output = open('output.csv', 'w')
# w wipes out the old file and replaces it
# a means appending and will add to the bottom of the file

#output = open('ElectionResults.csv', 'w')
#writer = csv.writer(ElectionResults)

br = mechanize.Browser() #set up
br.open('http://enr.sos.mo.gov/EnrNet/') #performing action

# Fill out the form
br.select_form(nr=0)

br.form['ct100$MainContent$cboElectionNames'] = ['750003566']


# Submit the form (Press the "submit" button)
br.submit('ct100$MainContent$btnElectionType')

# The result is basically the same code from jailscrape.py, just isolating different parts
# Paste stuff after "Get HTML"
