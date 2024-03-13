import pandas

iata_dframe = pandas.read_csv("data_iata_code_list.csv")
data_dict = iata_dframe.to_dict(orient="records")

class Data:
    def __init__(self, city_to: str, price_to: int) -> None:
      self.city_to = city_to.title()
      self.price_to = price_to
      self.fly_to = None
      self.has_airport = False  
      self.destination_has_airport()
      self.is_destination_in_travel_list()

    def destination_has_airport(self):
        """
        checks the city has any airports 
        """
        for item in data_dict:
            if item["region_name"] == self.city_to:
                self.has_airport = True
                break
        
    def is_destination_in_travel_list(self):
        """
        checks if the city is already in the travel list, if yes then just updates budget via
        'update_price_to' function. otherwise get iata code via "get_iata_code" func.
        """
        in_travel_list = False
        if not self.has_airport: 
            """
            If the city hasn't got any airport or 
            the user enters incorrect name return below message
            """ 
            print(f"The destination({self.city_to}) doesn't have any airports.\n{self.city_to} hasn't been added to the travel list.")
        else:
            try:
                destination_data = pandas.read_csv("travel_destination_list.csv", names=["fly_to", "city_to", "price_to"])
                for city in destination_data ["city_to"]:# checks the city is in travel list or not.
                    if city == self.city_to:
                        in_travel_list = True
                        self.update_price_to()
                        print(f"The destination({self.city_to}) has been added the travelling list.")
                        break
                if not in_travel_list: # If it is a new city, then get iata code of it.
                    self.get_iata_code() 
            except FileNotFoundError: # If the file is deleted, creates an empty csv file.
                with open("travel_destination_list.csv", mode= "w") as file:
                    pass
                print("Unable to access to the traveling list.")
                    
    def update_price_to(self):
        """
        Updating the budget price of city which is already in the travel list.
        """
        destination_dframe = pandas.read_csv("travel_destination_list.csv", names=["fly_to", "city_to", "price_to"])
        destination_dframe.loc[destination_dframe["city_to"] == self.city_to, "price_to"] = self.price_to
        destination_dframe.to_csv(f"travel_destination_list.csv", index=False, header= False,)
        
    def get_iata_code(self):
        """
        get iata codes for new city
        *******************************************************************************
        Notes: Some of airport names refer to country instead of city in the 
        'data_iata_code_list.csv' ex: Stansted airport in England region not in London
        A revision is required for the region names in the 'data_iata_code_list.csv'
        *******************************************************************************
        """
        for item in data_dict:
            if item["region_name"] == self.city_to:       
                new_entry = {"fly_to": [item["iata"]], "city_to": [self.city_to], "price_to": [self.price_to]}           
                travel_dframe = pandas.DataFrame(new_entry)
                try:
                    travel_dframe.to_csv(f"travel_destination_list.csv",mode="a", index=False, header= False,)
                except :
                    print("Unable to access to the traveling list.")
    


                        
                    
                


