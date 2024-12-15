# import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import requests
import os

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless=new")  # Use the latest headless mode for Chrome
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 2)  # Add explicit wait

def search_and_download(search_item, max_images_to_download):

    def scroll_to_end(wd:webdriver):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    # Construct the URL for Google Images
    url = f"https://www.google.com/search?hl=en&tbm=isch&q={search_item}"

    driver.get(url)

    # Allow time for the page to load
    time.sleep(2)

    # Find image thumbnails
    thumbnails = driver.find_elements(By.XPATH, "//img[@class='YQ4gaf']")


    while len(thumbnails) < max_images_to_download:
        scroll_to_end(driver)

    # Click on the thumbnails
    downloaded_images = 0

    for i in range(0, len(thumbnails)):
        if downloaded_images >= max_images_to_download:
            break
        try:
            thumbnails[i].click()
            time.sleep(2)  # Wait for the image to load

            # Find the image element on the page
            image_element = driver.find_element(By.XPATH, "//img[@class='sFlh5c FyHeAf iPVvYb']")
            image_url = image_element.get_attribute("src")
            #print(image_url)

            # Download the image
            if image_url.startswith('http'):
                response = requests.get(image_url)
                if response.status_code == 200:
                    # Create a directory to save images
                    if not os.path.exists(f"downloaded_images/{search_item}"):
                        os.makedirs(f"downloaded_images/{search_item}")

                    # Save the image
                    with open(f"downloaded_images/{search_item}/{search_item}_{downloaded_images + 1}.jpg", 'wb') as f:
                        f.write(response.content)
                    downloaded_images += 1


            # Go back to the search results
            driver.back()
            time.sleep(2)  # Wait for the search results to load
            # Re-find thumbnails after going back
            thumbnails = driver.find_elements(By.XPATH, "//img[@class='YQ4gaf']")
            #print(f"Sucess try {count}")

        except Exception as e:
            print(f"An error occurred: {e}")

    # Close the WebDriver
    driver.quit()

search_and_download("cats",10)