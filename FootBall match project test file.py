from bs4 import BeautifulSoup
import requests
import csv

url = requests.get('https://en.wikipedia.org/wiki/Spain_national_football_team')

soup = BeautifulSoup(url.text, 'html.parser')

table = soup.find("table", class_ ="wikitable sortable")

file = open("scrape_test.csv", "w")
writer = csv.writer(file)
writer.writerow(["YEAR", "C", "c", "5"])

for text in table:
    print(text.text)

file.close()
