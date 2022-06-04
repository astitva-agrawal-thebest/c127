from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
starturl="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browese = webdriver.Chrome("C:/Users/Astitva/Downloads/chromedriver")
browese.get(starturl)
time.sleep(10)
def scrap():
    headers=["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    planet_data=[]
    for i in range(0,202):
        soup=BeautifulSoup(browese.page_source,"html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browese.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrap()