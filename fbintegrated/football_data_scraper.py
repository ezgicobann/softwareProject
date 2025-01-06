import requests
import pandas as pd
import re
from datetime import datetime 
from bs4 import BeautifulSoup
import logging
import time

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_match_data(country):
    logger.info(f"Fetching data for {country}")
    url_mapping = {
        "England": "https://www.rsssf.org/tablese/eng-intres.html",  # Removed #c anchor
        "Spain": "https://www.rsssf.org/tabless/span-intres.html",
        "Turkey": "https://www.rsssf.org/tablest/turk-intres.html",
        "France": "https://www.rsssf.org/tablesf/fran-intres.html",
        "Germany": "https://www.rsssf.org/tablesd/duit-intres.html",
        "Italy": "https://www.rsssf.org/tablesi/ital-intres.html"
    }

    url = url_mapping.get(country)
    if not url:
        logger.error(f"Invalid country selected: {country}")
        raise ValueError(f"Selected country '{country}' is not available")

    # Add headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Try up to 3 times with increasing delays
    max_retries = 3
    for attempt in range(max_retries):
        try:
            logger.info(f"Requesting URL: {url} (Attempt {attempt + 1}/{max_retries})")
            response = requests.get(url, headers=headers, timeout=30)  # Increased timeout
            response.raise_for_status()
            
            # Check if we got HTML content
            if 'text/html' not in response.headers.get('content-type', '').lower():
                raise ValueError("Response is not HTML content")
            
            soup = BeautifulSoup(response.text, 'html.parser')
            pre_elements = soup.find_all('pre')

            if not pre_elements:
                logger.error(f"No pre elements found for {country}")
                raise ValueError(f"No data found for {country}")

            pre_text = pre_elements[1].get_text() if country == "Germany" else pre_elements[0].get_text()
            
            if not pre_text.strip():
                raise ValueError("Retrieved data is empty")
                
            filtered_data = []
            
            logger.info(f"Processing data for {country}")
            # Process data based on country format
            if country == "Italy":
                filtered_data = []
                lines = pre_text.splitlines()
                current_year = None
                in_results_section = False
                
                # Debug: Print first few lines to see structure
                logger.info("First 10 lines of data:")
                for i, line in enumerate(lines[:10]):
                    logger.info(f"Line {i}: {line}")
                
                for i, line in enumerate(lines):
                    # Look for year markers first (standalone years)
                    if re.match(r'^\s*2\d{3}\s*$', line):
                        current_year = int(line.strip())
                        logger.info(f"Found year: {current_year}")
                        continue
                    
                    # Skip empty or header lines
                    if not line.strip() or all(c.isupper() for c in line.strip()):
                        continue
                    
                    # If we have a year, look for match data
                    if current_year and current_year >= 2000:
                        # Look for date patterns at the start of lines
                        date_match = re.match(r'^\s*(\d{1,2})[-./](\d{1,2})', line)
                        if date_match:
                            day, month = map(int, date_match.groups())
                            # Validate date
                            if 1 <= day <= 31 and 1 <= month <= 12:
                                # Check if line contains score pattern
                                if re.search(r'\d[-:]\d', line):
                                    filtered_data.append(f"{day:02d}-{month:02d}-{current_year} {line.strip()}")
                                    logger.info(f"Found match: {day:02d}-{month:02d}-{current_year} {line.strip()}")
                
                # If still no data, try alternative approach
                if not filtered_data:
                    logger.info("Trying alternative approach...")
                    current_year = None
                    for line in lines:
                        # Look for year headers
                        year_match = re.search(r'\b(20\d{2})\b', line)
                        if year_match and len(line.strip()) < 15:  # Year lines are usually short
                            current_year = int(year_match.group(1))
                            continue
                        
                        if current_year and current_year >= 2000:
                            # Look for lines with both date and score
                            if re.search(r'\d{1,2}[-./]\d{1,2}.*?\d[-:]\d', line):
                                filtered_data.append(f"{line.strip()}")
                                logger.info(f"Alternative match found: {line.strip()}")
                
                logger.info(f"Total matches found for Italy: {len(filtered_data)}")
            else:
                # Process other countries
                char_map = {
                    "France": '-',
                    "Germany": '/',
                    "Turkey": '.',
                    "Spain": '/',
                    "England": '-'
                }
                char = char_map.get(country, '-')
                
                for line in pre_text.splitlines():
                    index = line.find(char)
                    if index > 0:
                        try:
                            year_str = line[index+4:index+8]
                            year = int(year_str)
                            if year >= 2000:
                                filtered_data.append(line[index-2:index+80])
                        except (ValueError, IndexError):
                            continue

            if not filtered_data:
                logger.error(f"No matches found for {country}")
                raise ValueError(f"No matches found for {country}")

            logger.info(f"Processing {len(filtered_data)} matches for {country}")
            # Process filtered data into structured format
            matches = []
            for line in filtered_data:
                try:
                    # Extract date with multiple format support
                    date = None
                    
                    # For Italy, handle the special date format
                    if country == "Italy":
                        # First try to find a full date
                        date_match = re.search(r'(\d{1,2})[-./](\d{1,2})[-./](\d{4})', line)
                        if not date_match:
                            # Try to find DD-MM format at the start of the line
                            date_match = re.match(r'^\s*(\d{1,2})[-./](\d{1,2})', line)
                            if date_match:
                                day, month = map(int, date_match.groups())
                                # Find year in the rest of the line
                                year_match = re.search(r'\b(20\d{2})\b', line)
                                if year_match:
                                    year = int(year_match.group(1))
                                else:
                                    continue
                            else:
                                continue
                        else:
                            day, month, year = map(int, date_match.groups())
                    else:
                        # Handle other countries (existing code)
                        date_match = re.search(r'(\d{1,2})[-./](\d{1,2})[-./](\d{4})', line)
                        if date_match:
                            day, month, year = map(int, date_match.groups())
                            if month > 12:  # Swap if month > 12
                                day, month = month, day
                        else:
                            continue
                    
                    # Validate date components
                    if not (1 <= month <= 12 and 1 <= day <= 31 and 2000 <= year <= 2024):
                        continue
                        
                    date = f"{day:02d}-{month:02d}-{year}"

                    # Extract score with more patterns
                    score = "N/A"
                    score_patterns = [
                        r'(\d+)[-:](\d+)',  # Standard format
                        r'(\d+)\s*[-:]\s*(\d+)',  # Format with spaces
                        r'(\d+)/(\d+)',  # Alternative format
                    ]
                    
                    for pattern in score_patterns:
                        score_match = re.search(pattern, line)
                        if score_match:
                            score = f"{score_match.group(1)}-{score_match.group(2)}"
                            break

                    # Extract location and opponent
                    location = "Home"
                    if any(marker in line.lower() for marker in ["away", "(a)", "@", "at "]):
                        location = "Away"
                    
                    # Extract opponent and competition
                    opponent = "Unknown"
                    competition = "International Match"
                    
                    if "World Cup" in line:
                        competition = "World Cup"
                    elif "Euro" in line or "European" in line:
                        competition = "European Championship"
                    elif "Friend" in line:
                        competition = "Friendly"
                    
                    # Common country names in international football
                    countries = {
                        'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Argentina', 'Armenia', 'Australia', 
                        'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Belarus', 'Belgium', 'Benin', 'Bolivia', 
                        'Bosnia', 'Brazil', 'Bulgaria', 'Burkina Faso', 'Cameroon', 'Canada', 'Chile', 'China', 
                        'Colombia', 'Congo', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 
                        'Ecuador', 'Egypt', 'England', 'Estonia', 'Ethiopia', 'Faroe Islands', 'Finland', 'France', 
                        'Georgia', 'Germany', 'Ghana', 'Greece', 'Guatemala', 'Guinea', 'Honduras', 'Hungary', 
                        'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 
                        'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kosovo', 'Kuwait', 'Latvia', 'Lebanon', 'Libya', 
                        'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Malaysia', 'Mali', 'Malta', 'Mexico', 
                        'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Netherlands', 'New Zealand', 
                        'Nigeria', 'North Korea', 'Northern Ireland', 'Norway', 'Oman', 'Pakistan', 'Palestine', 
                        'Panama', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 
                        'Russia', 'San Marino', 'Saudi Arabia', 'Scotland', 'Senegal', 'Serbia', 'Singapore', 
                        'Slovakia', 'Slovenia', 'South Africa', 'South Korea', 'Spain', 'Sweden', 'Switzerland', 
                        'Syria', 'Taiwan', 'Tanzania', 'Thailand', 'Tunisia', 'Turkey', 'Ukraine', 'United Arab Emirates', 
                        'United States', 'Uruguay', 'USA', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Wales', 'Yemen', 
                        'Yugoslavia', 'Zambia', 'Zimbabwe'
                    }
                    
                    # First try to find exact country names
                    for possible_opponent in countries:
                        if possible_opponent in line and possible_opponent != country:
                            opponent = possible_opponent
                            break
                    
                    # If still unknown, try to find partial matches with word boundaries
                    if opponent == "Unknown":
                        for possible_opponent in countries:
                            pattern = r'\b' + re.escape(possible_opponent) + r'\b'
                            if re.search(pattern, line, re.IGNORECASE) and possible_opponent.lower() != country.lower():
                                opponent = possible_opponent
                                break

                    matches.append({
                        "Match Number": len(matches) + 1,
                        "Date": date,
                        "Location": location,
                        "Opponent": opponent,
                        "Score": score,
                        "Competition": competition
                    })
                except Exception as e:
                    logger.error(f"Error processing line: {line}")
                    logger.error(f"Error: {str(e)}")
                    continue

            if not matches:
                logger.error(f"No valid matches found for {country}")
                raise ValueError(f"No valid matches could be processed for {country}")

            # Create DataFrame and save to CSV
            df = pd.DataFrame(matches)
            csv_file = f"{country}_matches_standardized.csv"
            df.to_csv(csv_file, index=False)
            logger.info(f"Successfully saved {len(matches)} matches to {csv_file}")
            return True

        except requests.RequestException as e:
            logger.error(f"Network error on attempt {attempt + 1}: {str(e)}")
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 2  # Exponential backoff
                logger.info(f"Waiting {wait_time} seconds before retrying...")
                time.sleep(wait_time)
                continue
            raise Exception(f"Failed to fetch data after {max_retries} attempts: {str(e)}")
        except Exception as e:
            logger.error(f"Unexpected error on attempt {attempt + 1}: {str(e)}")
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 2
                logger.info(f"Waiting {wait_time} seconds before retrying...")
                time.sleep(wait_time)
                continue
            raise

if __name__ == "__main__":
    # Test the function
    try:
        country = "England"
        success = get_match_data(country)
        print(f"Data retrieval {'successful' if success else 'failed'} for {country}")
    except Exception as e:
        print(f"Error: {str(e)}")
