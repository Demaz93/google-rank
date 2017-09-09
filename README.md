# Google Rank
Check site's google ranking

# Requirements
This script is created with Python 2.7 because of libraryes.
To use this script you need to install two libraryes: Google-Search-API to search on google and terminaltables to show results in a beautiful table.

To install Google-Search-API use this command:
```
pip install Google-Search-API
```
To install terminaltables use this command:
```
pip install terminaltables 
```
# How To Use it
To use this script create a file in the same folder of script called keywords.txt .
The file keywords.txt must contain one keyword per line.

Run the script with this command
```
python google-rank.py <domain-to-check> <number of page to check>
```
ex. python google-rank.py mysite.com 10

You can omit 'number of page to check', default value is 5.
With this examle you can chek the domain "mysite.com" in the first 10 pages of google results.

# How To Read results
The table showed at the end of the script is split in 5 columns.

* **Keyword:** The keyword linked to the result showed
* **Page:** The number of Google's page you can find your site
* **Index on page:** The position you can find your site in the Google's page
* **Index:** The number of results before you can find this link to your site
* **Link:** The link to your site related to the given keyword
