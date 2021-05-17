# Web Scraping using Selenium with Python!

Author: Praveen Kumar Anwla

Date: 2020-08-30

[Original](https://bit.ly/3hqjNrQ)



## Introduction

+ Data Science
  + Machine learning: requiring a large volume of data to build a robust & reliable machine learning model for such business problems
  + Data mining or gathering data
    + primitive step in the data science life cycle
    + business requirements: gathering data from sources like SAP servers, logs, Databases, APIs, online repositories, or web

## What is Web Scraping?

+ Overview of Web Scrapping
  + a.k.a. “Crawling” or “Spidering”
  + the technique to gather data automatically from an online source usually from a website
  + an easy way to get a large volume of data in a relatively short time frame, it adds stress to the server where the source is hosted
  + a large volume of data such as text and images in a relatively short time
    + many website not allowing scrping at all
    + disrupting the primary function of the online source

## How Web Scraping is useful?

+ Popular tools for web scraping
  + BeautifulSoup
  + Scrappy
  + Selenium

## What is Selenium

+ Selenium
  + an open-source web-based automation tool
  + primarily used for testing in the industry
  + also used for web scraping

+ Selenium Setup & methods
  + Installation:
    + Install selenium using `pip`: `pip install selenium`
    + Install selenium using `conda`: `conda install -c conda-forge selenium`
  + Download Chrome Driver:
    + directly download [chrome driver](https://chromedriver.chromium.org/downloads)
    + directly using the line of code: `driver = webdriver.Chrome(ChromeDriverManager().install())`
  + [documentation](https://selenium-python.readthedocs.io/)
  + [methods to find elements](https://selenium-python.readthedocs.io/locating-elements.html) in a Web-page (these methods will return a list):
    + `find_elements_by_name`
    + `find_elements_by_xpath`
    + `find_elements_by_link_text`
    + `find_elements_by_partial_link_text`
    + `find_elements_by_tag_name`
    + `find_elements_by_class_name`
    + `find_elements_by_css_selector`

## Implementation of Image Web Scrapping using Selenium Python

+ Procedure to implement image web scraping
  + Step1: – Import libraries

    ```python
    import os
    import selenium
    from selenium import webdriver
    import time
    from PIL import Image
    import io
    import requests
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.common.exceptions import ElementClickInterceptedException
    ```

  + Step 2: – Install Driver

    ```python
    #Install Driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    ```

  + Step 3: –  Specify search URL

    ```python
    #Specify Search URL 
    search_url=“https://www.google.com/..." 

    driver.get(search_url.format(q='Car'))
    ```

  + Step 4: –  Scroll to the end of the page

    ```python
    #Scroll to the end of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)#sleep_between_interactions
    ```

  + Step 5: –  Locate the images to be scraped from the page

    ```python
    #Locate the images to be scraped from the current page 
    imgResults = driver.find_elements_by_xpath("//img[contains(@class,'Q4LuWd')]")
    totalResults=len(imgResults)
    ```

  + Step 6: – Extract the corresponding link of each Image
    + iterate through each thumbnail and then click it
    + making browser sleep for 2 seconds
    + finding the unique HTML tag correpsonding to that image to locate it on page
    + more than one result for a particular image
    + iterating through each result for that image, extracting `src` attribute and checking `https` link

    ```python
    #Click on each Image to extract its corresponding link to download

    img_urls = set()
    for i in  range(0,len(imgResults)):
        img=imgResults[i]
        try:
            img.click()
            time.sleep(2)
            actual_images = driver.find_elements_by_css_selector('img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'https' in actual_image.get_attribute('src'):
                    img_urls.add(actual_image.get_attribute('src'))
        except ElementClickInterceptedException or ElementNotInteractableException as err:
            print(err)
    ```

  + Step 7: – Download & save each image in the Destination directory

    ```python
    os.chdir('C:/Qurantine/Blog/WebScrapping/Dataset1')
    baseDir=os.getcwd()
    for i, url in enumerate(img_urls):
        file_name = f"{i:150}.jpg"    
        try:
            image_content = requests.get(url).content

    except Exception as e:
            print(f"ERROR - COULD NOT DOWNLOAD {url} - {e}")

    try:
            image_file = io.BytesIO(image_content)
            image = Image.open(image_file).convert('RGB')
            
            file_path = os.path.join(baseDir, file_name)
            
            with open(file_path, 'wb') as f:
                image.save(f, "JPEG", quality=85)
            print(f"SAVED - {url} - AT: {file_path}")
        except Exception as e:
            print(f"ERROR - COULD NOT SAVE {url} - {e}")
    ```

## Headless Chrome browser

+ Headless Chrome browser
  + not running browser in background
  + helpful deploying a solution in production

  ```python
  #Headless chrome browser
  from selenium import webdriver 
  opts = webdriver.ChromeOptions()
  opts.headless =True
  driver =webdriver.Chrome(ChromeDriverManager().install())
  ```

## Putting it all together

+ Python code links
  + [Original source code](https://github.com/Praveen76/Web-Scraping-using-Selenium-Python)
  + [Local demo notebook - version 1](src/Web-Scraping-Selenium/Image_Web-Scraping_Part1.ipynb)
  + [Local demo notebook - version 2](src/Web-Scraping-Selenium/Image_Web-Scraping_Part2.ipynb)
  + [Local demo code](src/Web-Scraping-Selenium/image_Web-Scraping.py)


