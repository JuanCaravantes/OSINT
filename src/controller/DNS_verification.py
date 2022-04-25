from dns import resolver

class DNSDomain():      

    def comprobar_dominio(nombre):

        info = []

        try:
            ans = resolver.resolve(nombre,"A")
            sacar_names(ans,info)
        except:
            info.append("El nombre de dominio "+nombre+ " no se encontro en el dominio A")
        try:
            ans = resolver.resolve(nombre,"MX")
            sacar_names(ans,info)
        except:
            info.append("El nombre de dominio "+nombre+ " no se encontro en el dominio MX")
          
        try:
            ans = resolver.resolve(nombre,"NS")
            sacar_names(ans,info)
        except:
            info.append("El nombre de dominio "+nombre+ " no se encontro en el dominio NS")

        try:
            ans = resolver.resolve(nombre,"CNAME")
            sacar_names(ans,info)
        except:
            info.append("El nombre de dominio "+nombre+ " no se encontro en el dominio CNAME")

        return info

def sacar_names(answer,buffer):
    for i in answer.response.answer:
        text = i.to_text()
        names = text.split("\n")
        for _ in names:
            buffer.append(_)
