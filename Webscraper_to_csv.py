import pandas as pd 
from Guitar_Scraper import *
import csv

class Instrument_to_CSV:
    def __init__(self, Instrument):
        self.name = Instrument.name
        self.price_list= Instrument.guitar_price_list   #wrong - need omni list for all classes: Guitar, Drums, Bass, etc but HOW
        self.model_list = Instrument.guitar_model_list
        self.manufacturer_list = Instrument.guitar_manufacturer_list
        self.instrument_dict = {}


    def list_to_csv(self):
        self.instrument_dict = {"Brand ": self.manufacturer_list,
                                "Model ": self.model_list,
                                "Price ": self.price_list                                
                                }

   
        self.instrument_df = pd.DataFrame(self.instrument_dict)
        

    
        self.instrument_df.to_csv(self.name + "_Table.csv", encoding='utf-8')
        
        



    def __str__(self):
        return str(self.instrument_df)




Guitars= Instrument_to_CSV(guitar)
Basses = Instrument_to_CSV(bass)
print("Copying to CSV...")
Guitars.list_to_csv()
Basses.list_to_csv()

