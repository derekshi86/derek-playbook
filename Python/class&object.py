class Phone:
    def __init__(self,os,number,is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof
    def add(self, number1,number2):
        return number1 + number2
    
    def is_ios(self):
        if self.os == "ios":
            return True
        else:
            return False

phone1 = Phone("IOS", 123 , True)
print(phone1.is_ios())
print(phone1.is_waterproof)
print(phone1.add(5, 6))