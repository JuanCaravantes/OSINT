import phonenumbers #vsc no detecta el paquete, pero existe. Ignorar los warnings
from phonenumbers import geocoder 
from phonenumbers import carrier
from phonenumbers import timezone 

class phone_info():

    def __init__(self, number, format = 'es') :
        self.number = number
        self.format = format
        try:
            self.phone = phonenumbers.parse(number)
        except:
            print("El número no puede tener caracteres especiales o letras")
            exit()
        

    def phone_region(self):
        phone_region = geocoder.description_for_number(self.phone, self.format)  
        return "The region's number is: " + str(phone_region)
    
    def phone_provider(self):
        provider = carrier.name_for_number(self.phone, self.format)
        return "The intenert provider of the number is: "+ str(provider)
    
    def phone_format(self):
        return str(self.phone)

    def phone_timezone(self):
        tz = timezone.time_zones_for_number(self.phone)
        return "The timezone's number is: "+ str(tz)

    def phone_validation(self):
        isValid =  phonenumbers.is_valid_number(self.phone) 
        isPossible = phonenumbers.is_possible_number(self.phone)
        info = ""
        if(isValid):
            info += "The number is valid"
        else:
            info += "The number isn't valid"
        if(isPossible):
            info += "\nThe number could exits"
        else:
            info += "\nThe number can't exits"

        return info

    def phone_comparation(self, scam_list):
        scam_phones = phonenumbers.PhoneNumberMatcher(scam_list, "IN")  
        for self.number in scam_phones:  
            return self.number 
    