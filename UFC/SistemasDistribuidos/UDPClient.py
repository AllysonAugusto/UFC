import socket
import json
import Mensagem

class UDPClient:

    """
    Envia os dados para o server e recebe as respostas.Foi implementado tanto erro de rede (timeout) quanto socket
    __init__: inicializa o socket com porta e endereço
    enviar_solicitação: pegar o socket para enviar dados serelializados para o servidor
    receber_solicitação: recebe respostas do server
    """

    def __init__ (self, hostname, port, timeout = 5, max_retransmissao = 3):
        self.endereco_servidor = (hostname, port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.timeout = timeout
        self.max_retransmissao = max_retransmissao
        self.socket.settimeout(self.timeout)


    def enviar_solicitacao(self, requisicao):

        try:

            self.socket.sendto(requisicao.para_json().encode(), self.endereco_servidor)
            
            resposta_json = self.client.receber_requisicao()

            # retorna a mensagem (objeto)
            return Mensagem.para_objeto(resposta_json)

        except socket.error as erro:
            print(f"erro no envio da solicitacao: {erro}")

        except socket.timeout:
            print("erro por exceder o timeout")


    def receber_requisicao(self):

        """
        Recebendo dados do servidor e decodificando os dados recebidos de bytes para string
        Pega a string JSON para dicionario em py
        
        """

        tentativas = 0

        while tentativas <= self.max_retransmissao:
            try:
                dados_recebidos, endereco = self.socket.recvfrom(4096)
                resposta = json.loads(dados_recebidos.decode('utf-8'))
                return resposta
            
            except socket.timeout:
                print("Tempo da conexão foi esgotado ao esperar pela resposta")
                tentativas += 1
            except socket.error as erro:
                print("Erro ao receber a resposta: {erro}")
        
        print("Numero maximo de tentativas.Nao foi possivel estabelecer resposta com o servidor")
        print(f"Numero de tentativas: {tentativas}")


    def close(self):
        self.socket.close()


if __name__ == "__main__":
    client = UDPClient('localhost', 8448)

    mensagem = Mensagem({

    "tipoMensagem": 1,
    "methoId": "metodo1",
    "arguments": {"arg1": "valor1"}

    })

    resposta = client.enviar_solicitacao(mensagem)

    if resposta:
        print("Resposta recebida", resposta)