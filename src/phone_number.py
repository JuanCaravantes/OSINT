import phonenumbers #vsc no detecta el paquete, pero existe. Ignorar los warnings
from phonenumbers import geocoder 
from phonenumbers import carrier
from phonenumbers import timezone 

class phone_information():

    def __init__(self, number, format = 'es') :
        self.number = number
        self.format = format
        try:
            self.phone = phonenumbers.parse(number)
        except:
            print("\nEl número no puede tener caracteres especiales o letras")
            exit()
        

    def phone_region(self):
            phone_region = geocoder.description_for_number(self.phone, self.format)  
            print("\nThe region's number is: " + phone_region)
    
    def phone_provider(self):
        provider = carrier.name_for_number(self.phone, self.format)
        print("\n The intenert provider of the number is: "+ provider)
    
    def phone_format(self):
        print(self.phone)

    def phone_timezone(self):
        tz = timezone.time_zones_for_number(self.phone)
        print("\n The timezone's number is: "+ tz)

    def phone_validation(self):
        isValid =  phonenumbers.is_valid_number(self.phone) 
        isPossible = phonenumbers.is_possible_number(self.phone)
        
        if(isValid):
            print("\n The number is valid")
        else:
            print("\n The number isn't valid")
        if(isPossible):
            print("\n The number could exits")
        else:
            print("\n The number can't exits")

    def phone_comparation(self, scam_list):
        scam_phones = phonenumbers.PhoneNumberMatcher(scam_list, "IN")  
        for self.number in scam_phones:  
            print(self.number)   
  
if __name__ == '__main__':
    phone_information("+1222222222").phone_validation()
    