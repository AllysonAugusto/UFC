import json 

class Mensagem:
    def __init__(self, json_obj=None):
        if json_obj:
            self.messageType = json_obj.get("tipoMensagem", None)
            self.id_metodo = json_obj.get("methodId", None)
            self.argumento = json_obj.get("argumentos", {})
        else:
            print("Erro: JSON não foi definido")

    def para_json(self):
        return json.dumps({
            "tipoMensagem": self.messageType,
            "methodId": self.id_metodo,
            "argumentos": self.argumento,
        })

    @staticmethod
    def para_objeto(json_string):
        json_obj = json.loads(json_string)
        return Mensagem(json_obj)

# JSON corrigido
json_data = '{"tipoMensagem": 1, "methodId": "metodo1", "argumentos": {"arg1": "valor1"}}'

# Json -> objeto
mensagem = Mensagem.para_objeto(json_data)

# Acessando os atributos do objeto
print(mensagem.messageType)  # Saída: 1
print(mensagem.id_metodo)    # Saída: metodo1
print(mensagem.argumento)    # Saída: {'arg1': 'valor1'}

# objeto -> json
print(mensagem.para_json())  # Converte de volta para JSON
