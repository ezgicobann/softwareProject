import requests
import pandas as pd
import re
from datetime import datetime 
from bs4 import BeautifulSoup
import csv

def get_match_data(country):

    url_mapping = {
        "England": "https://www.rsssf.org/tablese/eng-intres.html#c",
        "Spain": "https://www.rsssf.org/tabless/span-intres.html",
        "Turkey": "https://www.rsssf.org/tablest/turk-intres.html",
        "France": "https://www.rsssf.org/tablesf/fran-intres.html",
        "Germany": "https://www.rsssf.org/tablesd/duit-intres.html",
        "Italy": "https://www.rsssf.org/tablesi/ital-intres.html",
        "Belgium": "https://www.rsssf.org/tablesb/belg-intres.html"
    }

    url = url_mapping.get(country, None)

    # not required after iu implementation since will use dropdown menu
    if not url:
        print("Selected country is not available")

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        pre_elements = soup.find_all('pre')

        # Germany match data is in the second <pre> 
        if pre_elements:
            if country == "Germany":
                pre_text = pre_elements[1].get_text()
            else:
                pre_text = pre_elements[0].get_text()
            return pre_text
        else:
            print(f"No data found for {country}")

    # no error so far / take notes if encountered
    except requests.RequestException as e:
        print(f"An error occured: {e}")


# placeholder country / will fetch from ui later
country = "Belgium"
data = get_match_data(country)

france_filtered_data = []
germany_filtered_data = []
turkey_filtered_data = []
spain_filtered_data = []
england_filtered_data = []
italy_filtered_data = []
belgium_filtered_data = []

if country == "France":
    france_filtered_data.append("Date,Location,Opponent,Score,League"+"\n")
    for line in data.splitlines():
        char = '-'
        index = line.find(char)
        if index:
            year_str = line[index+4:index+8]
            try:
                year = int(year_str)
                if year >= 2000:
                    date = line[6:16].strip()
                    location = line[18:38].strip()
                    opponent = line[38:56].strip()
                    score = line[56:59]
                    league = line[59:].strip()
                    if not league.strip():
                        league = "Friendly"
                    france_filtered_data.append(date+","+
                                                location+","+
                                                opponent+","+
                                                score+","+
                                                league+
                                                "\n")
            except ValueError:
                pass

if country == "Germany":
    germany_filtered_data.append("Date,Location,Opponent,Score,League"+"\n")
    for line in data.splitlines():
        char = '/'
        index = line.find(char)
        if index:
            year_str = line[index+4:index+8]
            try:
                year = int(year_str)
                if year >= 2000:
                    date = line[6:16].strip()
                    location = line[17:37].strip()
                    location_abvr = location.find(',')
                    if location_abvr:
                        location = location[:location_abvr].strip()
                    opponent = line[37:54].strip()
                    score = line[54:59].strip()
                    league = line[59:].strip()
                    if not league.strip():
                        league = "Friendly"
                    germany_filtered_data.append(date+","+
                                                location+","+
                                                opponent+","+
                                                score+","+
                                                league+
                                                "\n")
            except ValueError:
                pass

if country == "Turkey":
    turkey_filtered_data.append("Date,Location,Opponent,Score,League"+"\n")
    for line in data.splitlines():
        char = '.'
        index = line.find(char)
        if index:
            year_str = line[index+4:index+8]
            try:
                year = int(year_str)
                if year >= 2000:
                    date = line[6:16].strip()
                    location = line[17:32].strip()
                    opponent = line[32:64].strip()
                    score = line[64:67]
                    league = line[67:].strip()
                    if not league.strip():
                        league = "Friendly"
                    turkey_filtered_data.append(date+","+
                                                location+","+
                                                opponent+","+
                                                score+","+
                                                league+
                                                "\n")
            except ValueError:
                pass

if country == "Spain":
    spain_filtered_data.append("Date,Location,Opponent,Score,League"+"\n")
    for line in data.splitlines():
        char = '/'
        index = line.find(char)
        if index:
            year_str = line[index+4:index+8]
            try:
                year = int(year_str)
                if year >= 2000:
                    date = line[4:14].strip()
                    location = line[16:29].strip()
                    opponent = line[29:52].strip()
                    score = line[52:57].strip()
                    league = line[57:].strip()
                    if not league.strip():
                        league = "Friendly"
                    spain_filtered_data.append(date+","+
                                                location+","+
                                                opponent+","+
                                                score+","+
                                                league+
                                                "\n")
            except ValueError:
                pass

if country == "England":
    england_filtered_data.append("Date,Location,Opponent,Score,League"+"\n")
    for line in data.splitlines():
        char = '-'
        index = line.find(char)
        if index:
            year_str = line[index+4:index+8]
            try:
                year = int(year_str)
                if year >= 2000:
                    date = line[6:16].strip()
                    location = line[17:33].strip()
                    opponent = line[33:52].strip()
                    score = line[52:56].strip()
                    league = line[56:].strip()
                    if not league.strip():
                        league = "Friendly"
                    england_filtered_data.append(date+","+
                                                location+","+
                                                opponent+","+
                                                score+","+
                                                league+
                                                "\n")
            except ValueError:
                pass

# two seperate for loops / finding the line number with the year data / writing the data between the years.
"""
if country == "Italy":
    year_lines = []
    year_list = []
    for i,line in enumerate(data.splitlines()):
        year_str = line[0:1] + line[2:3] + line[4:5] + line[6:7]
        try:
            year = int(year_str)
            if year >= 2000 and not year in year_lines:
                year_list.append(year)
                year_lines.append(i)        
        except ValueError:
            pass
        if "Italy's International Record -- countrywise performance" in line:
            year_lines.append(i)

    for i in range(len(year_lines) - 1):
        start = year_lines[i]
        end = year_lines[i + 1]
        for line in data.splitlines()[start+2:end-2]:
            italy_filtered_data.append(str(year_list[i]) + " " + line[7:80] + "\n")

    txt_file = "{}_filtered_data.txt".format(country)
    with open(txt_file, "w", encoding="utf-8") as file:
            for line in italy_filtered_data:
                file.write(line)
    print(f"Filtered data saved to {txt_file}")
"""

if country == "Belgium":
    belgium_filtered_data.append("Date,Location,Opponent,Score,League"+"\n")
    for line in data.splitlines():
        char = '-'
        index = line.find(char)
        if index:
            year_str = line[index+4:index+8]
            try:
                year = int(year_str)
                if year >= 2000:
                    date = line[6:15].strip()
                    location = line[17:32].strip()
                    opponent = line[32:51].strip()
                    score = line[51:54]
                    league = line[59:].strip()
                    if not league.strip():
                        league = "Friendly"
                    belgium_filtered_data.append(date+","+
                                                location+","+
                                                opponent+","+
                                                score+","+
                                                league+
                                                "\n")
            except ValueError:
                pass

class matches:
    dates = []
    locations = []
    opponents = []
    scores = []
    competitions = []

country_data_mapping = {
    "England": england_filtered_data,
    "Spain": spain_filtered_data,
    "Turkey": turkey_filtered_data,
    "France": france_filtered_data,
    "Germany": germany_filtered_data,
    "Italy": italy_filtered_data,
    "Belgium": belgium_filtered_data   
}
filtered_data = country_data_mapping.get(country)

csv_file = "{}_matches_standardized.csv".format(country)
with open(csv_file, mode='w',  encoding="utf-8") as file:
    for line in filtered_data:
        file.write(line)
print(f"Data has been standardized and saved to '{country}_matches_standardized.csv'.")
