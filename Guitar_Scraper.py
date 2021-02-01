import requests
from bs4 import BeautifulSoup
import re

# Scraping thomann homepage for guitar information and storing it in a list
class crawler:
    
    def __init__(self, name):
        self.guitar_manufacturer_list = []
        self.guitar_model_list = []
        self.guitar_price_list = []
        self.name = name
        # guitar_html = requests.get(self.url).text
        # guitar_soup = BeautifulSoup(guitar_html, "html.parser")


    #Manufacturer from Website
    def fetch_data(self,url):
        self.url = url
        
        
        next_button = "start"
        while len(next_button)>1:
            
            try:
                guitar_html = requests.get(self.url).text
                guitar_soup = BeautifulSoup(guitar_html, "html.parser")
                next_button = guitar_soup.find("a",{"class": "button next"})["href"]
                
                        
                manufacturer_container = guitar_soup.findAll("span", {"class":"manufacturer"} )
                
                for i in range(len(manufacturer_container)):
                    try:
                        guitar_manufacturer_items = manufacturer_container[i]
                        guitar_manufacturer = guitar_manufacturer_items.text
                        self.guitar_manufacturer_list.append(guitar_manufacturer)
                        
                        
                
                    except AttributeError:
                        print("Wrong Div Container from HTML")
                


            #Model from Webside 
            
                guitar_html = requests.get(self.url).text
                guitar_soup = BeautifulSoup(guitar_html, "html.parser")
                guitar_model_container = guitar_soup.findAll("span", {"class":"model"})
                    
                for i in range(len(guitar_model_container)):
                    try:
                        guitar_model_item = guitar_model_container[i]
                        guitar_model = guitar_model_item.text
                        self.guitar_model_list.append(guitar_model)
                    except AttributeError:
                        print("Wrong Div Container from HTML")    
                

            #fetch price
                guitar_html = requests.get(self.url).text
                guitar_soup = BeautifulSoup(guitar_html, "html.parser")
                guitar_price_container = guitar_soup.findAll("span", {"class": "article-basketlink"})

                for i in range(len(guitar_price_container)):
                    try:
                        guitar_price_item = guitar_price_container[i]
                        guitar_price = guitar_price_item.text
                        price_reg = re.compile(r"\d+[.,]*\d+")
                        price = price_reg.search(guitar_price)
                        price = price.group()
                        price_e = str(price) +" €"
                        self.guitar_price_list.append(price_e)
                    except AttributeError:
                        print("Wrong Div")
            
                self.url = "https://www.thomann.de"+str(next_button)
                print(self.url)

                
            except :
                    next_button=""
                    print("Finish")


    def __str__(self):
            return "Preis: {} \n Hersteller: {} \n Model {}".format (self.guitar_price_list, self.guitar_manufacturer_list,self.guitar_model_list)


        
guitar = crawler("Guitars")
bass = crawler("Basses")

guitar.fetch_data("https://www.thomann.de/de/st-modelle.html?ls=100")
bass.fetch_data("https://www.thomann.de/de/4-saiter_j-baesse.html?ls=100")







