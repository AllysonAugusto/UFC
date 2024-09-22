import json 
from Proxy import Proxy 


class Mensagem:
    def __init__(self, json_obj=None):
        if json_obj:
            self.messageType = json_obj.get("tipoMensagem", None) 
            self.id_metodo = json_obj.get("methodId", None)        
            self.argumento = json_obj.get("argument", {})   
        else:
            print("Erro: JSON não foi definido")

    def para_json(self):
        return json.dumps({
            "tipoMensagem": self.messageType,
            "methodId": self.id_metodo,
            "argumentos": self.argumento,
        })

    def para_objeto(json_string):
        json_obj = json.loads(json_string)
        return Mensagem(json_obj)

json_data = '{"tipoMensagem": 1, "methodId": "metodo1", "argumentos": {"arg1": "valor1"}'

#Json -> objeto
mensagem = Mensagem.para_objeto(json_data)


print(mensagem.messageType) 
print(mensagem.id_metodo)     
print(mensagem.argumento)     

# objeto -> json
print(mensagem.para_json())