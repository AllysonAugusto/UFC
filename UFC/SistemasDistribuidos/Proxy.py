from UDPClient import UDPClient
import json


class Proxy:
    """
    Lida com as requisições com o cliente

    Colocar os objetos de requisição em JSON e depois chamar as funções no lado do UDPCLIENTE pra enviar 
    """
    def __init__(self, hostname, port):
        self.request_id = 0  # Inicializa o ID das requisições
        self.client = UDPClient(hostname, port)
        self.is_connected = False

    def conectar_servidor(self):
        try:
            response = self.client.receber_requisicao()
            if response:
                self.is_connected = True
                print("Conexão com o servidor estabelecida.")
            else:
                print("Erro ao conectar com o servidor.")
        except Exception as e:
            print(f"Erro ao tentar conectar: {e}")
            self.is_connected = False

    def iniciar(self): #
        self.conectar_servidor()
        if not self.is_connected:
            print("Não foi possível conectar ao servidor. O cliente não pode entrar no menu.")
            return

        while True:
            escolha = input("Escolha uma opção: ")
            if escolha == "1":
                self.verificar_ticket()
            elif escolha == "2":
                self.reservar_ticket()
            elif escolha == "3":
                self.atualizar_ticket()
            elif escolha == "4":
                self.cancelar_ticket()
            elif escolha == "5":
                self.consultar_reserva()
            elif escolha == "6":
                self.buscar_historico()
            elif escolha == "7":
                self.close()
                break
            else:
                print("Opção inválida. Tente novamente.")


    def doOperation(self, acao, params=None):
        # Incrementa o request_id a cada operação
        self.request_id += 1

        if params is not None:
            # Cria a mensagem de requisição
            message = {
                "messageType": 0,  # 0 = Requisição
                "requestId": self.request_id,
                "acao": acao,
                "arguments": params
            }
            # Serializa a mensagem em JSON
            return json.dumps(message)
        else:
            # Processa a resposta
            message = json.loads(acao)  # Desserializa a resposta em JSON

            if message["messageType"] == 1:  # 1 = Resposta
                arguments = message["arguments"]

                if isinstance(arguments, str):
                    try:
                        arguments_json = json.loads(arguments)
                    except json.JSONDecodeError as e:
                        print(f"Falha ao decodificar o JSON: {e}")
                        return None
                else:
                    arguments_json = arguments
                
                # Verifica se houve sucesso na operação
                response = {
                    "result": arguments_json,
                    "status": message.get("status", "sem status")
                }
                return response
            return None

    def verificar_ticket(self, ticket_id, cpf):
        requisicao = self.doOperation("consultar_reserva", {
            "ticket_id": ticket_id,
            "cpf": cpf
        })
        self.client.enviar_solicitacao(requisicao)
        resposta = self.client.receber_requisicao()
        return self.doOperation(resposta)

    def reservar_ticket(self, cpf, nome, data, hora, origem, destino, poltrona):
        requisicao = self.doOperation("reservar_ticket", {
            "cpf": cpf,
            "data": data,
            "hora": hora,
            "origem": origem,
            "destino": destino,
            "nome": nome,
            "poltrona": poltrona
        })
        self.client.enviar_solicitacao(requisicao)
        resposta = self.client.receber_requisicao()
        return self.doOperation(resposta)

    def atualizar_ticket(self, ticket_id, cpf, data, hora, origem, destino, nome, poltrona):
        requisicao = self.doOperation("atualizar_reserva", {
            "ticket_id": ticket_id,
            "cpf": cpf,
            "data": data,
            "hora": hora,
            "origem": origem,
            "destino": destino,
            "nome": nome,
            "poltrona": poltrona
        })
        self.client.enviar_solicitacao(requisicao)
        resposta = self.client.receber_requisicao()
        return self.doOperation(resposta)

    def cancelar_ticket(self, ticket_id):
        requisicao = self.doOperation("cancelar_ticket", {
            "ticket_id": ticket_id
        })
        self.client.enviar_solicitacao(requisicao)
        resposta = self.client.receber_requisicao()
        return self.doOperation(resposta)

    def consultar_reserva(self, cpf):
        requisicao = self.doOperation("consultar_reserva", {
            "cpf": cpf
        })
        self.client.enviar_solicitacao(requisicao)
        resposta = self.client.receber_requisicao()
        return self.doOperation(resposta)

    def buscar_historico(self):
        requisicao = self.doOperation("consultar_histórico")
        self.client.enviar_solicitacao(requisicao)
        resposta = self.client.receber_requisicao()
        return self.doOperation(resposta)

    def close(self):
        self.client.close()