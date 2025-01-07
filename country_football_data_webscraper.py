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
    if not url:
        print(f"Selected country {country} is not available")
        return None

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        pre_elements = soup.find_all('pre')

        if not pre_elements:
            print(f"No data found for {country}")
            return None

        if country == "Germany":
            raw_data = pre_elements[1].get_text()
        else:
            raw_data = pre_elements[0].get_text()

        # Process the data based on country format
        filtered_data = []
        filtered_data.append("Date,Location,Opponent,Score,League")
        matches_found = 0

        for line in raw_data.splitlines():
            try:
                if country == "France":
                    char = '-'
                    date_range = (5, 15)
                    location_range = (17, 32)
                    opponent_range = (32, 51)
                    score_range = (51, 55)
                    league_start = 55
                elif country == "Germany":
                    char = '/'
                    date_range = (6, 16)
                    location_range = (17, 37)
                    opponent_range = (37, 54)
                    score_range = (54, 59)
                    league_start = 59
                elif country == "Turkey":
                    char = '.'
                    date_range = (6, 16)
                    location_range = (17, 32)
                    opponent_range = (32, 64)
                    score_range = (64, 67)
                    league_start = 67
                elif country == "Spain":
                    char = '/'
                    date_range = (4, 14)
                    location_range = (16, 29)
                    opponent_range = (29, 52)
                    score_range = (52, 57)
                    league_start = 57
                elif country == "England":
                    char = '-'
                    date_range = (6, 16)
                    location_range = (17, 33)
                    opponent_range = (33, 52)
                    score_range = (52, 56)
                    league_start = 56
                elif country == "Belgium":
                    char = '-'
                    date_range = (6, 15)
                    location_range = (17, 32)
                    opponent_range = (32, 51)
                    score_range = (51, 54)
                    league_start = 59
                else:
                    continue

                index = line.find(char)
                if index > 0:
                    year_str = line[index+4:index+8]
                    try:
                        year = int(year_str)
                        if year >= 2000:
                            # Extract and clean data
                            date = line[date_range[0]:date_range[1]].strip()
                            location = line[location_range[0]:location_range[1]].strip()
                            if country == "Germany" and ',' in location:
                                location = location.split(',')[0].strip()
                            opponent = line[opponent_range[0]:opponent_range[1]].strip()
                            score = line[score_range[0]:score_range[1]].strip()
                            league = line[league_start:].strip() or "Friendly"
                            
                            # Clean the data
                            location = ' '.join(location.split()).replace(',', ' ').strip()
                            opponent = ' '.join(opponent.split()).replace(',', ' ').strip()
                            # Standardize different types of dashes in score
                            score = score.replace('–', '-').replace('—', '-').strip()
                            score = ''.join(c for c in score if c.isdigit() or c == '-')
                            league = ' '.join(league.split()).replace(',', ' ').strip()
                            
                            # Validate score format
                            if score and '-' in score and score.count('-') == 1:
                                try:
                                    home, away = map(int, score.split('-'))
                                    if all([date, location, opponent]):
                                        filtered_data.append(f"{date},{location},{opponent},{score},{league}")
                                        matches_found += 1
                                except ValueError:
                                    continue
                    except ValueError:
                        continue
            except Exception as e:
                print(f"Error processing line for {country}: {str(e)}")
                continue

        print(f"Found {matches_found} matches for {country}")
        return "\n".join(filtered_data) if matches_found > 0 else None

    except requests.RequestException as e:
        print(f"An error occurred while fetching data for {country}: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred for {country}: {e}")
        return None
