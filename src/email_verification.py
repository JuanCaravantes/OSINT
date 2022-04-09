from dotenv import load_dotenv
from os import getenv
import requests

class email_info():
    def __init__(self):
        load_dotenv()
        self.key = getenv('EMAIL_KEY')
        self.url = "https://emailvalidation.abstractapi.com/v1/?api_key="

    def email_verification(self, email):
        try:
            self.email = "&email="+email
            response = requests.get(self.url+self.key+self.email)
            mostrar_info(self,response)
        except:
            print("Algo falló")

def mostrar_info(self, response):
    self.response = response
    print("Información del correo: " + str(self.response.json().get("email")))
    print("\nFormato correcto: " + str(self.response.json().get("is_valid_format").get("value")))
    print("\nCorreo gratuito: " + str(self.response.json().get("is_free_email").get("value")))
    print("\nCorreo destinado a un fin especifico (team@, support@, etc): " + str(self.response.json().get("is_role_email").get("value")))
    print("\nProtocolo SMTP: " + str(self.response.json().get("is_smtp_valid").get("value")))
    print("\nServidor MX: " + str(self.response.json().get("is_mx_found").get("value")))
    print("\n¿Es seguro la entrega de este correo? (Delivarable: sí, undelivarable: no, Risky: arriesgado, unknown: desconocido): " + str(self.response.json().get("deliverability")))
    print("\n\nFiabilidad del correo:" +  str(self.response.json().get("quality_score"))+"\\1")

if __name__ == '__main__':
    email_info().email_verification("juan.caravantes.algaba@gmail.com")