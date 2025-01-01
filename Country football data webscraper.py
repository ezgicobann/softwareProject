import requests
import pandas as pd
import re
from datetime import datetime 
from bs4 import BeautifulSoup

def get_match_data(country):

    url_mapping = {
        "England": "https://www.rsssf.org/tablese/eng-intres.html#c",
        "Spain": "https://www.rsssf.org/tabless/span-intres.html",
        "Turkey": "https://www.rsssf.org/tablest/turk-intres.html",
        "France": "https://www.rsssf.org/tablesf/fran-intres.html",
        "Germany": "https://www.rsssf.org/tablesd/duit-intres.html",
        "Italy": "https://www.rsssf.org/tablesi/ital-intres.html"
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

            # txt file is to view the data
            txt_file = "{}_data.txt".format(country)
            with open(txt_file, "w", encoding="utf-8") as file:
                file.write(pre_text)
            return pre_text
        else:
            print(f"No data found for {country}")

    # no error so far / take notes if encountered
    except requests.RequestException as e:
        print(f"An error occured: {e}")


# placeholder country / will fetch from ui later
country = "Italy"
data = get_match_data(country)

france_filtered_data = []
germany_filtered_data = []
turkey_filtered_data = []
spain_filtered_data = []
england_filtered_data = []
italy_filtered_data = []


# Filtering for France data
if country == "France":
    for line in data.splitlines():
        char = '-'
        index = line.find(char)
        if index:
            year_str = line[index+4:index+8]
            try:
                year = int(year_str)
                if year >= 2000:
                    france_filtered_data.append(line[index-2:index+80]+"\n")
            except ValueError:
                pass
    txt_file = "{}_filterd_data.txt".format(country)
    with open(txt_file, "w", encoding="utf-8") as file:
            for line in france_filtered_data:
                file.write(line)
    print(f"Filtered data saved to {txt_file}")

if country == "Germany":
    for line in data.splitlines():
        char = '/'
        index = line.find(char)
        if index:
            year_str = line[index+4:index+8]
            try:
                year = int(year_str)
                if year >= 2000:
                    germany_filtered_data.append(line[index-2:index+80]+"\n")
            except ValueError:
                pass
    txt_file = "{}_filterd_data.txt".format(country)
    with open(txt_file, "w", encoding="utf-8") as file:
            for line in germany_filtered_data:
                file.write(line)
    print(f"Filtered data saved to {txt_file}")

if country == "Turkey":
    for line in data.splitlines():
        char = '.'
        index = line.find(char)
        if index:
            year_str = line[index+4:index+8]
            try:
                year = int(year_str)
                if year >= 2000:
                    turkey_filtered_data.append(line[index-2:index+80]+"\n")
            except ValueError:
                pass
    txt_file = "{}_filterd_data.txt".format(country)
    with open(txt_file, "w", encoding="utf-8") as file:
            for line in turkey_filtered_data:
                file.write(line)
    print(f"Filtered data saved to {txt_file}")

if country == "Spain":
    for line in data.splitlines():
        char = '/'
        index = line.find(char)
        if index:
            year_str = line[index+4:index+8]
            try:
                year = int(year_str)
                if year >= 2000:
                    spain_filtered_data.append(line[index-2:index+80]+"\n")
            except ValueError:
                pass
    txt_file = "{}_filterd_data.txt".format(country)
    with open(txt_file, "w", encoding="utf-8") as file:
            for line in spain_filtered_data:
                file.write(line)
    print(f"Filtered data saved to {txt_file}")

if country == "England":
    for line in data.splitlines():
        char = '-'
        index = line.find(char)
        if index:
            year_str = line[index+4:index+8]
            try:
                year = int(year_str)
                if year >= 2000:
                    england_filtered_data.append(line[index-2:index+80]+"\n")
            except ValueError:
                pass
    txt_file = "{}_filterd_data.txt".format(country)
    with open(txt_file, "w", encoding="utf-8") as file:
            for line in england_filtered_data:
                file.write(line)
    print(f"Filtered data saved to {txt_file}")


# two seperate for loops / finding the line number with the year data / writing the data between the years.
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

    txt_file = "{}_filterd_data.txt".format(country)
    with open(txt_file, "w", encoding="utf-8") as file:
            for line in italy_filtered_data:
                file.write(line)
    print(f"Filtered data saved to {txt_file}")

 
matches = []

match_numbers = []
dates = []
locations = []
opponents = []
scores = []
competitions = []

   
df = pd.DataFrame({
"Match Number": match_numbers,
"Date": pd.to_datetime(dates, format = '%d-%m-%Y', errors="coerce"),
"Location": locations,
"Opponent": opponents,
"Score": scores,
"Competition": competitions
})

csv_file = "{}_matches_standardized.csv".format(country)
df.to_csv(csv_file, index=False)
print(f"Data has been standardized and saved to '{country}_matches_standardized.csv'.")
