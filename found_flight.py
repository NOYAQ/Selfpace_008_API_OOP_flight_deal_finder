"""
search flight returns with all details to the object 
which will be used for notification message in the main.
"""
class FoundFlight:
    def __init__(self, fly_from, city_from, fly_to, city_to, 
                 date_from, date_to, price_to):
        self.fly_from = fly_from
        self.city_from = city_from
        self.fly_to = fly_to
        self.city_to = city_to
        self.date_from = date_from
        self.date_to = date_to
        self.price_to = price_to