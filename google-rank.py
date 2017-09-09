from google import google
from terminaltables import SingleTable
import sys

keywords = []
results = [["Keyword","Page","Index on page","Index","Link"]]

#Check the first argument to get the domain to check
try:
    site = sys.argv[1]
except:
    print "Google rank\n"
    print "Use:\n"
    print "python google-rank.py <domain-to-check> <number of page to check>\n"
    print "Default value of 'number of page to check' is 5\n"
    print "Ex. python google-rank.py mysite.com 5\n"
    sys.exit(0)

#Check the second argument to get the number of page to check
try:
    num_page = int(sys.argv[2])
except:
    num_page = 5

#Get keywords list
f_keywords = open("keywords.txt", "r")

for item in f_keywords:
    keywords.append(item)

f_keywords.close()

#Search in google results domain given
for search in keywords:
    ris = google.search(search, num_page)
    for elem in ris:
        list_row = []
        if site in elem.link:
            list_row.append(search)
            list_row.append(elem.page+1)
            list_row.append(elem.index+1)
            list_row.append(elem.page*10+elem.index+1)
            list_row.append(elem.link)

            results.append(list_row)

tab_to_print = SingleTable(results,title=site)

print tab_to_print.table
