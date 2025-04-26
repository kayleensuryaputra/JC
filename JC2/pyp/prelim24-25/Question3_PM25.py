
#(a)(i)
class Device:
    def __init__(self,device_name,brand,battery_life,price):
        self.__device_name = device_name
        self.__brand = brand
        self.__battery_life = battery_life
        self.__price = price
    
    def get_device_name(self):
        return self.__device_name
    
    def get_brand(self):
        return self.__brand
    
    def get_battery_life(self):
        return self.__battery_life
    
    def get_price(self):
        return self.__price
    
    def print_details(self):
        print(f"Device Name: {self.__device_name}")
        print(f"Brand: {self.__brand}")
        print(f"Battery Life: {self.__battery_life}")
        print(f"Price: {self.__price}")

#(a)(ii)
class Phone(Device):
    def __init__(self, device_name, brand, battery_life, price, storage):
        super().__init__(device_name, brand, battery_life, price)
        self.__storage = storage
    
    def get_storage(self):
        return self.__storage
    
    def print_details(self):
        print(f"Device Name: {self.__device_name}")
        print(f"Brand: {self.__brand}")
        print(f"Battery Life: {self.__battery_life}")
        print(f"Price: {self.__price}")
        print(f"Storage: {self.__storage}")

#(a)(iii)
class Laptop(Device):
    def __init__(self, device_name, brand, battery_life, price,ram):
        super().__init__(device_name, brand, battery_life, price)
        self.__ram = ram
    
    def get_ram(self):
        return self.__ram
    
    def print_details(self):
        print(f"Device Name: {self.__device_name}")
        print(f"Brand: {self.__brand}")
        print(f"Battery Life: {self.__battery_life}")
        print(f"Price: {self.__price}")
        print(f"RAM: {self.__ram}")

class Tablet(Device):
    def __init__(self, device_name, brand, battery_life, price,screen_size):
        super().__init__(device_name, brand, battery_life, price)
        self.__screen_size = screen_size #of type float

    def get_screen_size(self):
        return self.__screen_size 
    
    def print_details(self):
        print(f"Device Name: {self.__device_name}")
        print(f"Brand: {self.__brand}")
        print(f"Battery Life: {self.__battery_life}")
        print(f"Price: {self.__price}")
        print(f"Screen Size: {self.__screen_size}")

    