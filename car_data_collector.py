



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
        self.stopThread = False
        self.urlsFetched = False

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
            


    """
    def scrape_listings(self):
        
        urls = [
                'https://www.arabam.com/ikinci-el/otomobil?view=Box&take=50',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=2',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=3',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=4',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=5',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=6',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=7',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=8',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=9',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=10',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=11',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=12',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=13',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=14',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=15',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=16',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=17',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=18',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=19',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=20',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=21',   
            ]

        # Function to scrape a single URL
        def scrape_single_url(url_batch):
            driver = self.setup_driver()
            if not driver:
                print("Failed to initialize driver")
                return []

            final_car_urls = []
            car_urls = []

            for url in url_batch:
                print(f"Scraping URL: {url}")
                try:
                    driver.get(url)
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located((By.CLASS_NAME, 'content-container'))
                    )
                    car_elements = WebDriverWait(driver, 20).until(
                        EC.presence_of_all_elements_located((By.CLASS_NAME, 'content-container'))
                    )
                    car_urls = [elem.get_attribute('href') for elem in car_elements]
                    car_urls = list(set(car_urls))  # Remove duplicates
                    print(f"Scraped {len(car_urls)} car URLs from {url}")
                except Exception as e:
                    print(f"Error scraping {url}: {e}")
                finally:
                    final_car_urls.extend(car_urls)  # Remove duplicates
            driver.quit()        
            return final_car_urls

        # Divide URLs into batches and process with ThreadPoolExecutor
        batch_size = 5
        url_batches = [urls[i:i + batch_size] for i in range(0, len(urls), batch_size)]
        print(f"Divided URLs into {len(url_batches)} batches")

        all_car_urls = []

        with ThreadPoolExecutor(max_workers=5) as executor:
            # Execute each batch in parallel
            futures = executor.map(scrape_single_url, url_batches) 

            # Gather results
            for future in futures:
                all_car_urls.extend(future)

        self.urls = list(set(all_car_urls))  # Remove duplicates from final list
        print(f"Total unique car URLs scraped: {len(self.urls)}")
"""   
    def scrape_listings(self):
        driver = self.setup_driver()
        driver.get(self.base_url)
        driver.maximize_window()
        
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
            ).click()
        except Exception as e:    
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
            ).click()

        urls = [
                'https://www.arabam.com/ikinci-el/otomobil?view=Box&take=50',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=2',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=3',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=4',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=5',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=6',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=7',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=8',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=9',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=10',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=11',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=12',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=13',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=14',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=15',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=16',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=17',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=18',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=19',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=20',
                'https://www.arabam.com/ikinci-el/otomobil?take=50&view=Box&page=21',   
            ]

        car_urls = []
        for page in range(1, 22):  # Iterate through 21 pages
            print(urls[page-1])
            if self.stopThread:
                break
            driver.get(urls[page-1])
            print(f"Scraping page {page}")
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'content-container')))

            try:
                # Re-fetch elements to avoid stale references
                car_elements = WebDriverWait(driver, 20).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'content-container'))
                )
                print(f"Found {len(car_elements)} car elements")
                # Create a fresh list of hrefs after ensuring elements are loaded
                car_urls.extend([elem.get_attribute('href') for elem in car_elements])
            except Exception as e:
                print("Stale element found, retrying...")
                # Retry locating the elements
                car_elements = WebDriverWait(driver, 20).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'content-container'))
                )

            try:
                for elem in car_elements:
                    link_element = elem.find_element(By.TAG_NAME, 'a')
                    car_urls.append(link_element.get_attribute('href'))
            except Exception as e:
                for elem in car_elements:
                    link_element = elem.find_element(By.TAG_NAME, 'a')
                    car_urls.append(link_element.get_attribute('href'))
            
                
            print(f"Found {len(car_urls)} car URLs\n")
            print(car_urls)
            car_urls = list(set(car_urls))  # Remove duplicates
            print(f"Found {len(car_urls)} car URLs\n")
            print(car_urls)                     
            

        driver.quit()
        car_urls.remove(None)
        self.urls = car_urls
        self.urlsFetched = True

    def scrape_car_details(self, urls_batch):
        driver = self.setup_driver()
        driver.maximize_window()
        car = None  
        cars = []
          
        for url in urls_batch:
            if self.stopThread:
                break
            driver.get(url)
            try:
                attributes = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="wrapper"]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[*]/div[2]'))
                )
                
                del attributes[0]  # Remove irrelevant elements
                del attributes[13]
                
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
                
                
                attributes = [attr for attr in attributes if attr.text != "Evet"]        
                    

                if 'lt' in attributes[13].text:
                    if 'lt' in attributes[14].text:
                        fuelConsumption = attributes[13].text
                        fuelTank = attributes[14].text
                        paintChange = attributes[15].text
                        if 'Takasa' in attributes[16].text or '-' in attributes[16].text:
                            fromWho = attributes[17].text
                        else:
                            fromWho = attributes[16].text    
                    else:
                        fuelTank = attributes[13].text 
                        fuelConsumption = "belirtilmemiş"
                        paintChange = attributes[14].text
                        if 'Takasa' in attributes[15].text or '-' in attributes[15].text:
                            fromWho = attributes[16].text     
                        else:
                            fromWho = attributes[15].text
                else:
                    fuelConsumption = "belirtilmemiş"
                    fuelTank = "belirtilmemiş"
                    paintChange = attributes[13].text  
                    if 'Takasa' in attributes[14].text or '-' in attributes[14].text:
                        fromWho = attributes[15].text  
                    else:
                        fromWho = attributes[14].text

                if not 'HP' in horsepower and not 'hp' in horsepower:
                    raise Exception("Horsepower not found")
                if 'İkinci El' in traction:
                    raise Exception("Traction not found")


                price = float(attributes[len(attributes)-1].text.replace(' TL', '').replace('.', '').replace(',', ''))

                # Create a Car object
                car = Car(brand, series, model, year, price, kilometer, fuel, gear, bodytype, horsepower, enginesize, colour, addate, traction, fuelConsumption, fuelTank, paintChange, fromWho)
                print(f"Scraped car: {car.brand}, {car.model}, {car.series}, {car.year}, {car.price}, {car.kilometer}, {car.fuel}, {car.gear}, {car.bodytype}, {car.horsepower}, {car.enginesize}, {car.colour}, {car.addate}, {car.traction}, {car.fuelConsumption}, {car.fuelTank}, {car.paintChange}, {car.fromWho}")
                
                cars.append(car)
                
                
            except Exception as e:
                print(f"Error scraping {url}: {e}")
                

        driver.quit()
        return cars  # Return None if scraping failed




    def run(self):
        if not self.urlsFetched:
            self.scrape_listings()
        print(f"Total car URLs fetched: {len(self.urls)}")

        # Divide the URLs into batches of 20
        batch_size = 10
        url_batches = [self.urls[i:i + batch_size] for i in range(0, len(self.urls), batch_size)]
        print(f"Divided URLs into {len(url_batches)} batches")

        with ThreadPoolExecutor(max_workers=5) as executor:
            # Map each batch of URLs to a thread
            results = executor.map(self.scrape_car_details, url_batches)

            # Iterate through each batch's results and add them to self.cars
            for batch_cars in results:
                self.cars.extend(batch_cars)  # Add the cars of the current batch to self.cars
                print(f"Batch completed! Cars scraped so far: {len(self.cars)}")
                
        if self.stopThread:
            print("Scraping stopped!")
            return   
        self.cars = list(set(self.cars))  # Remove duplicates
        print("Scraping completed!")
        print(f"Total cars successfully scraped: {len(self.cars)}")

    def scrapeInBackground(self):
        thread = threading.Thread(target=self.run)
        thread.start()
        return thread

#if __name__ == "__main__":
#    scraper = CarScraper()
#    scraper.scrapeInBackground().join()



