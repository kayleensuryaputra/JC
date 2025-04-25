
#(a)(i)
class Device:
    def __init__(self,device_name,brand,battery_life,price):
        self.device_name = device_name
        self.brand = brand
        self.battery_life = battery_life
        self.price = price
    
    def get_device_name(self):
        return self.device_name
    
    def get_brand(self):
        return self.brand
    
    def get_battery_life(self):
        return self.battery_life
    
    def get_price(self):
        return self.price
    
    def print_details(self, device_name, brand, battery_life, price):
        print(f"Device Name: {device_name}, Brand: {brand}, Battery Life: {battery_life}, Price: {price}")

#(a)(ii)
class Phone:
    