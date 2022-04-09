from dns import resolver

class DNSDomain():      

    def comprobar_dominio(nombre):
        try:
            ans = resolver.resolve(nombre,"A")
            for i in ans.response.answer:
                print (i.to_text())
        except:
            print("El nombre de dominio "+nombre+ "no se encontro en el dominio A")
        try:
            ans = resolver.resolve(nombre,"MX")
            for i in ans.response.answer:
                print (i.to_text())
        except:
            print("El nombre de dominio "+nombre+ "no se encontro en el dominio MX")
          
        try:
            ans = resolver.resolve(nombre,"NS")
            for i in ans.response.answer:
                print (i.to_text())
        except:
            print("El nombre de dominio "+nombre+ "no se encontro en el dominio NS")

        try:
            ans = resolver.resolve(nombre,"CNAME")
            for i in ans.response.answer:
                print (i.to_text())
        except:
            print("El nombre de dominio "+nombre+ "no se encontro en el dominio CNAME")
