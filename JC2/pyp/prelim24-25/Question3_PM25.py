
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

#(b)
def ReadDeviceData():
    try:
        DeviceArr = [] #of type Device
        file = open("Devices.txt",'r')
        line = file.readline().strip()
        while line != "":
            value = line.split(',')

            if value[0] == "Phone":
                phone = Phone(value[0],value[1],value[2],value[3],value[4])
                DeviceArr.append(phone)

            if value[0] == "Laptop":
                laptop = Laptop(value[0],value[1],value[2],value[3],value[4])
                DeviceArr.append(laptop)
            
            if value[0] == "Tablet":
                laptop = Laptop(value[0],value[1],value[2],value[3],value[4])
                DeviceArr.append(laptop)
            
            line = file.readline().strip()
        file.close()
        return DeviceArr #dont bracket return
                
    except:
        print("File not found")

#(c)
def PrintDevices(DeviceArr):
    for element in DeviceArr: #element is element of arrray, not index
        element.print_details()

#(d)(i)
Result = ReadDeviceData()

