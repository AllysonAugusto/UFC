from Proxy import Proxy
import json
from random import randint
from datetime import datetime
import pytz

def main():
    class Cliente:
        def __init__(self, hostname, porta):
            self.proxy = Proxy(hostname, porta)
            self.painel()

        def painel(self):
            while True:
                print("\nEscolha uma opção:")
                print("1. Reservar Ticket")
                print("2. Atualizar Reserva")
                print("3. Cancelar Reserva")
                print("4. Consultar Reserva")
                print("5. Consultar Histórico")
                print("6. Sair")

                try:
                    opcao = int(input("Opção: "))
                except ValueError:
                    print("ERRO: Digite apenas números.")
                    continue

                if opcao == 1:
                    self.reservar_ticket()
                elif opcao == 2:
                    self.atualizar_reserva()
                elif opcao == 3:
                    self.cancelar_reserva()
                elif opcao == 4:
                    self.consultar_reserva()
                elif opcao == 5:
                    self.consultar_historico()
                elif opcao == 6:
                    break
                else:
                    print("Opção inválida. Tente novamente.")

            self.proxy.close()

        def _tratar_execucao_metodo(self, metodo_proxy, *args):
            try:
                resposta = metodo_proxy(*args)
                print(f'Resposta recebida: {resposta}')
            except Exception as erro:
                print(f'Erro ao executar operação: {erro}')

        @staticmethod
        def _data():
            fuso_BR = pytz.timezone('Brazil/East')
            horario_BR = datetime.now(fuso_BR)
            return horario_BR

        def _validar_validade_passagem(self, data_passagem):
            try:
                data_passagem = datetime.strptime(data_passagem, '%Y-%m-%d')
                data_atual = self._data().date()
                if data_passagem.date() >= data_atual:
                    return True
                else:
                    print("Data da passagem deve ser para hoje ou para datas futuras.")
                    return False
            except ValueError:
                print("ERRO: Use apenas o formato YYYY-MM-DD.")
                return False

        def _validar_ticket(self, ticket_id):
            try:
                if self.proxy.verificar_ticket(ticket_id):
                    return True
                else:
                    print("Ticket não encontrado.")
                    return False
            except Exception as erro:
                print(f'Erro ao verificar ticket: {erro}')
                return False

        @staticmethod
        def _validar_cpf(cpf):
            while True:
                if cpf.isdigit() and len(cpf) == 11:
                    return True
                else:
                    print("ERRO ao digitar CPF. Só pode conter apenas números e ter 11 dígitos.")
                    cpf = input("CPF: ")

        @staticmethod
        def _validar_nome(nome):
            while True:
                if nome.strip().replace(" ", "").isalpha():
                    return True
                else:
                    print("Nome errado. Deve conter apenas letras e espaços.")
                    nome = input("Nome: ")

        @staticmethod
        def _validar_data(data):
            while True:
                try:
                    datetime.strptime(data, "%Y-%m-%d")
                    return True
                except ValueError:
                    print("Data inválida. Use o formato YYYY-MM-DD.")
                    data = input("Data (YYYY-MM-DD): ")

        @staticmethod
        def _validar_hora(hora):
            while True:
                try:
                    datetime.strptime(hora, "%H:%M")
                    return True
                except ValueError:
                    print("Hora inválida. Use o formato HH:MM.")
                    hora = input("Hora (HH:MM): ")

        @staticmethod
        def _validar_origem(origem):
            while True:
                if origem.strip():
                    return True
                else:
                    print("Origem não pode estar vazia.")
                    origem = input("Origem: ")

        @staticmethod
        def _validar_destino(destino):
            while True:
                if destino.strip():
                    return True
                else:
                    print("Destino não pode estar vazio.")
                    destino = input("Destino: ")

        @staticmethod
        def _validar_poltrona(poltrona, min_poltrona=1, max_poltrona=50):
            while True:
                if not str(poltrona).isdigit() or int(poltrona) <= 0:
                    print("Número de poltrona está errado. Coloque apenas número positivo.")
                    poltrona = input("Poltrona: ")
                    continue

                poltrona = int(poltrona)
                if min_poltrona <= poltrona <= max_poltrona:
                    return True
                
                print(f'O número da poltrona deve estar entre {min_poltrona} e {max_poltrona}.')
                poltrona = input("Poltrona: ")

        def reservar_ticket(self):
            cpf = input("CPF: ")
            if not self._validar_cpf(cpf):
                return

            nome = input("Nome: ")
            if not self._validar_nome(nome):
                return

            data = input("Data (YYYY-MM-DD): ")
            if not self._validar_data(data):
                return

            hora = input("Hora (HH:MM): ")
            if not self._validar_hora(hora):
                return

            origem = input("Origem: ")
            if not self._validar_origem(origem):
                return

            destino = input("Destino: ")
            if not self._validar_destino(destino):
                return

            poltrona = input("Poltrona: ")
            if not self._validar_poltrona(poltrona):
                return

            print("Reserva realizada com sucesso!")
            ticket_id = randint(1000, 9999)
            print(f"Reserva realizada. Seu ticket ID é {ticket_id}")
            self._tratar_execucao_metodo(self.proxy.reservar_ticket, ticket_id, nome, cpf, data, hora, origem, destino, int(poltrona))

        def atualizar_reserva(self):
            ticket_id = input("ID do Ticket: ")
            cpf = input("CPF: ")
            nome = input("Nome: ")
            data = input("Data (YYYY-MM-DD): ")
            hora = input("Hora (HH:MM): ")
            origem = input("Origem: ")
            destino = input("Destino: ")
            poltrona = input("Poltrona: ")

            ticket_id = randint(1000, 9999)
            self._tratar_execucao_metodo(self.proxy.atualizar_reserva, ticket_id, nome, cpf, data, hora, origem, destino, int(poltrona))


        def cancelar_reserva(self):
            ticket_id = input("ID do Ticket: ")
            if self._validar_ticket(ticket_id):
                print("Sua reserva foi cancelada.")
                self._tratar_execucao_metodo(self.proxy.cancelar_reserva, ticket_id)

        def consultar_reserva(self):
            cpf = input('CPF: ')
            self._tratar_execucao_metodo(self.proxy.consultar_reserva, cpf)

        def consultar_historico(self):
            cpf = input("Digite o seu CPF: ")
            if self._validar_cpf(cpf):
                self._tratar_execucao_metodo(self.proxy.buscar_historico, cpf)

                print("-=-=" * 20)
                print("Histórico de Viagens")
                if not self.historico:
                    print("Nenhuma viagem encontrada.")
                else:
                    for viagem in self.historico:
                        print(f"ID: {viagem.get('id')}, Data: {viagem.get('data')}, Hora: {viagem.get('hora')}, Origem: {viagem.get('origem')}, Destino: {viagem.get('destino')}, Poltrona: {viagem.get('poltrona')}")
            else:
                print("CPF errado. Não foi possível consultar o histórico.")

    cliente = Cliente('hostname', 8080)

if __name__ == '__main__':
    main()
