import sys
import codecs
from time import sleep
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

from concurrent.futures import ThreadPoolExecutor
import os
import threading
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from fake_useragent import UserAgent



class Car():
    def __init__(self, brand, series, model, year, price, kilometer, fuel, gear, bodytype, horsepower, enginesize, colour, addate, traction, fuelConsumption, fuelTank, paintChange, fromWho):
        self.brand = brand
        self.series = series
        self.model = model
        self.year = year
        self.price = price
        self.kilometer = kilometer
        self.fuel = fuel
        self.gear = gear
        self.bodytype = bodytype
        self.horsepower = horsepower
        self.enginesize = enginesize
        self.colour = colour
        self.addate = addate
        self.traction = traction
        self.fuelConsumption = fuelConsumption
        self.fuelTank = fuelTank
        self.paintChange = paintChange
        self.fromWho = fromWho
        

class CarScraper:
    def __init__(self):
        self.base_url = 'https://www.arabam.com/ikinci-el/otomobil?view=Box'
        self.cars = []
        self.urls = []
        self.is_paused = False
        self.scraping_thread = None
        self.current_page = 1
        self.max_pages = 21

    def pause(self):
        self.is_paused = True
        print(f"Scraping paused at page {self.current_page}")

    def resume(self):
        self.is_paused = False
        print(f"Scraping resumed from page {self.current_page}")

    def setup_driver(self):
        driver_lock = threading.Lock()
        user_agent = UserAgent()
        options = uc.ChromeOptions()
        #options.add_argument(f"user-agent={user_agent.random}")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-features=IsolateOrigins,site-per-process")
        options.add_argument("--useAutomationExtension=false")
        options.add_argument('--blink-settings=imagesEnabled=false') 
        options.page_load_strategy = 'eager'
        options.add_argument("--headless=new")  # Enable headless mode
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        chromedriver_path = './chromedriver.exe'
        with driver_lock:
            try:
                return uc.Chrome(options=options, version_main=131, driver_executable_path=chromedriver_path)
            except Exception as e:
                print(f"Error setting up driver: {e}")
                return None
            
   
    def scrape_listings(self):
        if self.is_paused:
            return
        
        if self.current_page > self.max_pages:
            print("All pages scraped, starting over")
            self.current_page = 1
            return

        driver = self.setup_driver()
        driver.get(self.base_url)
        driver.maximize_window()
        
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
            ).click()
        except Exception as e:    
            try:
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
                ).click()
            except:
                pass  # Cookie banner might not appear

        url = f'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page={self.current_page}'
        print(f"Scraping page {self.current_page}: {url}")
        
        car_urls = []
        try:
            driver.get(url)
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'content-container')))

            try:
                car_elements = WebDriverWait(driver, 20).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'content-container'))
                )
                print(f"Found {len(car_elements)} car elements on page {self.current_page}")
                car_urls.extend([elem.get_attribute('href') for elem in car_elements])
            except Exception as e:
                print("Stale element found, retrying...")
                car_elements = WebDriverWait(driver, 20).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'content-container'))
                )

            try:
                for elem in car_elements:
                    link_element = elem.find_element(By.TAG_NAME, 'a')
                    car_urls.append(link_element.get_attribute('href'))
            except Exception as e:
                print(f"Error getting URLs from page {self.current_page}: {str(e)}")
            
            car_urls = list(set(car_urls))  # Remove duplicates
            if None in car_urls:
                car_urls.remove(None)
                
            print(f"Found {len(car_urls)} unique car URLs on page {self.current_page}")
            
        except Exception as e:
            print(f"Error in page {self.current_page}: {str(e)}")
        finally:
            driver.quit()

        self.urls = car_urls
        self.current_page += 1

    def scrape_car_details(self, urls_batch):
        if self.is_paused:
            return []
        # Add a delay to avoid getting blocked
        driver = self.setup_driver()
        driver.maximize_window()
        
        car = None  # Initialize the car variable to ensure it's always defined
        
        cars = []
          
        

        for url in urls_batch:
            driver.get(url)
            
            try:
                attributes = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="wrapper"]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[*]/div[2]'))
                )
                # Parse the attributes into car data
                
                del attributes[0]  # Remove irrelevant elements
                
                del attributes[13]
                
                
                
                #attributes.append(driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div'))  # Add price
                attributes.append(
                    WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div'))
                )
                )
                
                
                # Extract the car details
                addate = attributes[0].text
                brand = attributes[1].text
                series = attributes[2].text
                model = attributes[3].text
                year = int(attributes[4].text)
                kilometer = int(attributes[5].text.replace('.', '').replace(' km', ''))
                gear = attributes[6].text
                fuel = attributes[7].text
                bodytype = attributes[8].text
                colour = attributes[9].text
                enginesize = attributes[10].text
                horsepower = attributes[11].text
                traction = attributes[12].text

                if 'lt' in attributes[13].text:
                    if 'lt' in attributes[14].text:
                        fuelConsumption = attributes[13].text
                        fuelTank = attributes[14].text
                        paintChange = attributes[15].text
                        if 'Takasa' in attributes[16].text:
                            fromWho = attributes[17].text
                        else:
                            fromWho = attributes[16].text    
                    else:
                        fuelTank = attributes[13].text 
                        fuelConsumption = "belirtilmemiş"
                        paintChange = attributes[14].text
                        if 'Takasa' in attributes[15].text:
                            fromWho = attributes[16].text     
                        else:
                            fromWho = attributes[15].text
                else:
                    fuelConsumption = "belirtilmemiş"
                    fuelTank = "belirtilmemiş"
                    paintChange = attributes[13].text  
                    if 'Takasa' in attributes[14].text:
                        fromWho = attributes[15].text  
                    else:
                        fromWho = attributes[14].text

                price = float(attributes[len(attributes)-1].text.replace(' TL', '').replace('.', '').replace(',', ''))

                # Create a Car object
                # Normalize fromWho value
                if fromWho and fromWho.strip():
                    if "Galeriden" in fromWho or "galeri" in fromWho.lower():
                        fromWho = "Galeriden"
                    elif "Sahibinden" in fromWho or "sahibi" in fromWho.lower():
                        fromWho = "Sahibinden"
                    else:
                        fromWho = "belirtilmemiş"
                else:
                    fromWho = "belirtilmemiş"

                car = Car(brand, series, model, year, price, kilometer, fuel, gear, bodytype, horsepower, enginesize, colour, addate, traction, fuelConsumption, fuelTank, paintChange, fromWho)
                print(f"Scraped car: {car.brand}, {car.model}, {car.series}, {car.year}, {car.price}, {car.kilometer}, {car.fuel}, {car.gear}, {car.bodytype}, {car.horsepower}, {car.enginesize}, {car.colour}, {car.addate}, {car.traction}, {car.fuelConsumption}, {car.fuelTank}, {car.paintChange}, {car.fromWho}")
                cars.append(car)
                
            except Exception as e:
                print(f"Error scraping {url}: {str(e)}")
                
                
                
        
        driver.quit()
        return cars  # Return None if scraping failed


    def run(self):
        while True:
            if len(self.cars) > 1000:
                break

            if self.is_paused:
                sleep(1)
                continue
                
            try:
                self.scrape_listings()
                if not self.urls:  # If no URLs were found
                    sleep(60)
                    continue

                print(f"Processing {len(self.urls)} car URLs from page {self.current_page-1}")

                batch_size = 10
                url_batches = [self.urls[i:i + batch_size] for i in range(0, len(self.urls), batch_size)]
                print(f"Divided URLs into {len(url_batches)} batches")

                with ThreadPoolExecutor(max_workers=5) as executor:
                    futures = []
                    for batch in url_batches:
                        if not self.is_paused:
                            future = executor.submit(self.scrape_car_details, batch)
                            futures.append(future)

                    for future in futures:
                        if not self.is_paused:
                            try:
                                batch_cars = future.result()
                                if batch_cars:
                                    self.cars.extend(batch_cars)
                                    print(f"Batch completed! Cars scraped so far: {len(self.cars)}")
                            except Exception as e:
                                print(f"Error processing batch: {e}")

                print(f"Page {self.current_page-1} completed!")
                print(f"Total cars successfully scraped: {len(self.cars)}")
                
                if self.is_paused:
                    sleep(1)
                else:
                    sleep(10)  # Short delay between pages
                    
            except Exception as e:
                print(f"Error in scraping cycle: {e}")
                sleep(60)  # Wait 1 minute before retrying

    def scrapeInBackground(self):
        self.is_paused = False
        if self.scraping_thread and self.scraping_thread.is_alive():
            self.resume()
        else:
            self.scraping_thread = threading.Thread(target=self.run)
            self.scraping_thread.daemon = True
            self.scraping_thread.start()
        return self.scraping_thread

#if __name__ == "__main__":
#    scraper = CarScraper()
#    scraper.scrapeInBackground().join()



