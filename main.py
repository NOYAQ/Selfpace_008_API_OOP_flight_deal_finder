"""
Keep asking destination city and budget to the user until the user press q.
The cities and budgets that are entered stores in a csv file.
The codes compares the budget and found flight price, if the found flight is
equal to budget or cheaper  in the next 30 days. if yes, sends a sms with flight details.
*******************************************************************************
Notes: Some of airport names refer to country instead of city in the 
'data_iata_code_list.csv' ex: Stansted airport in England region not in London
A revision is required for the region names in the 'data_iata_code_list.csv'
*******************************************************************************
"""
from search_flight import SearchFlight
from notification import Notification
from found_flight import FoundFlight
from data import Data
import pandas
import datetime
FLY_FROM = "LGW"
CITY_FROM = "London Gatwick"
def send_message(found_flight: FoundFlight ):
    """
    Get flight object and passes the detail of flight to notification object which sends SMS
    """
    new_message_text = f"""
    Outbound: {found_flight.date_from}, Inbound: {found_flight.date_to}
    From: {found_flight.city_from}({found_flight.fly_from}) 
    To: {found_flight.city_to}({found_flight.fly_to})
    Price £: {found_flight.price_to}
    """
    new_message = Notification()
    new_message.send_sms(new_message_text)
    
while True:
    """
    Keep asking cities and budget of them, then send the city and budget to 'Data' object 
    which responsibles to manage get iata code,city name and budget, stores in a csv file
    also checks the entered cities have a airport and changes the budgets, if entered more then one.
    """
    city_selection = input("Please enter a city name to add the travel list or\nPress 'q' for quit and search the flights in the travel list!\n")
    if city_selection.lower() == "q":
        break
    price_to = input("Please enter your budget:\n")
    while not price_to.isnumeric():
        print("You haven't entered a valid price, try again! Ex: 20, 100")
        price_to = input("Please enter your budget:\n")
    new_destination = Data(city_selection, int(price_to))
    
date_from = datetime.date.today() # today which is the saerching date starts
date_to = date_from + datetime.timedelta(days = 30) # 30 days later which is the searching date ends

# Reading cities and budgets from the travel list
city_to_dframe = pandas.read_csv("travel_destination_list.csv", names=["fly_to", "city_to", "price_to"])    
city_to_list =city_to_dframe.to_dict(orient="records")

for item in city_to_list:
    """
    getting every city's flighies in the travel list between the dates, if finds any cheaper flight
    then sends found fligth to send_message function.
    """
    new_search = SearchFlight()
    found_flight = new_search.search_flight(FLY_FROM, item["fly_to"], date_from, date_to)    
    try:
        if (found_flight.price_to) <= item["price_to"]:
            send_message(found_flight)         
    except:
        pass






    