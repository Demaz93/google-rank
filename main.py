from google import google
from terminaltables import SingleTable
import sys

ricerche = ["cuscino per bancale","cuscino per pallet","cuscini mobili divano pallet"]
results = [["Keyword","Page","Index on page","Index","Link"]]
site = sys.argv[1]

for search in ricerche:
    ris = google.search(search, 4)

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
