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
            return mostrar_info(self,response)
        except:
            print("Algo falló")

def mostrar_info(self, response):
    self.response = response

    info = []

    info.append("Información del correo: " + str(self.response.json().get("email")))
    info.append("Formato correcto: " + str(self.response.json().get("is_valid_format").get("value")))
    info.append("Correo gratuito: " + str(self.response.json().get("is_free_email").get("value")))
    info.append("Correo destinado a un fin especifico (team@, support@, etc): " + str(self.response.json().get("is_role_email").get("value")))
    info.append("Protocolo SMTP: " + str(self.response.json().get("is_smtp_valid").get("value")))
    info.append("Servidor MX: " + str(self.response.json().get("is_mx_found").get("value")))
    info.append("¿Es seguro la entrega de este correo?: " + str(self.response.json().get("deliverability")))
    info.append("Fiabilidad del correo:" +  str(self.response.json().get("quality_score"))+"\\1")

    return info
