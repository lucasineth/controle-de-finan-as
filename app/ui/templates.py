from app.models.models import Bancos, Conta, Tipos, Historico
from app.services.finance_service import *
from datetime import datetime, date

class UI:
    def start(self):
        while True:
            print('''
            [1] -> Criar conta
            [2] -> Desativar conta
            [3] -> Transferir dinheiro
            [4] -> Movimentar dinheiro
            [5] -> Total contas
            [6] -> filtra historico
            [7] -> gráfico
                  ''')
            choice = int(input('Escolha uma opção: '))
            if choice == 1:
                self._criar_conta()
            elif choice == 2:
                self._desativar_conta()
            elif choice == 3:
                self._transferir_saldo()
            elif choice == 4:
                self._movimentar_dinheiro()
            elif choice == 5:
                self._total_contas()
            elif choice == 6:
                self._filtrar_movimentacoes()
            elif choice == 7:
                self._criar_grafico()
            else:
                break
    def _criar_conta(self):
        print('Digite o nome de algum dos bancos abaixo:')
        for banco in Bancos:
            print(f'---{banco.name}---')
        banco = input('Banco: ').strip().upper()
        if banco not in Bancos.__members__:
            print('Banco inválido! Use exatamente como mostrado acima.')
            return
        valor = float(input('Digite o valor em sua conta: '))
        conta = Conta(banco=Bancos[banco], valor=valor)
        criar_conta(conta)
    def _desativar_conta(self):
        print('Escolha a conta que deseja desativar (digite o ID ou o nome do banco):')
        contas = [i for i in listar_contas() if i.valor == 0]
        for i in contas:
            print(f'{i.id} -> {i.banco.name} -> R$ {i.valor}')
        entrada = input('ID ou banco: ').strip()
        id_conta = None
        # Tenta converter para int (ID)
        if entrada.isdigit():
            id_conta = int(entrada)
        else:
            # Tenta buscar pelo nome do banco
            entrada_upper = entrada.upper()
            for conta in contas:
                if conta.banco.name == entrada_upper:
                    id_conta = conta.id
                    break
        if id_conta is None:
            print('Conta não encontrada! Digite o ID ou o nome do banco exatamente como mostrado.')
            return
        try:
            desativar_conta(id_conta)
            print('Conta desativada com sucesso.')
        except ValueError:
            print('Essa conta ainda possui saldo, faça uma transferência')
    def _transferir_saldo(self):
        print('Escolha a conta retirar o dinheiro.')
        for i in listar_contas():
            print(f'{i.id} -> {i.banco.value} -> R$ {i.valor}')
        conta_retirar_id = int(input())
        print('Escolha a conta para enviar dinheiro.')
        for i in listar_contas():
            if i.id != conta_retirar_id:
                print(f'{i.id} -> {i.banco.value} -> R$ {i.valor}')
        conta_enviar_id = int(input())
        valor = float(input('Digite o valor para transferir: '))
        transferir_saldo(conta_retirar_id, conta_enviar_id, valor)
    def _movimentar_dinheiro(self):
        print('Escolha a conta.')
        for i in listar_contas():
            print(f'{i.id} -> {i.banco.value} -> R$ {i.valor}')
        conta_id = int(input())
        valor = float(input('Digite o valor movimentado: '))
        print('Selecione o tipo da movimentação')
        for tipo in Tipos:
            print(f'---{tipo.value}---')
        tipo_input = input('Tipo: ').strip().upper()
        # Aceita variações: entrada, Entrada, ENTRADA, etc
        tipo_map = {t.value.upper(): t for t in Tipos}
        if tipo_input not in tipo_map:
            print('Tipo inválido! Use ENTRADA ou SAIDA.')
            return
        historico = Historico(conta_id=conta_id, tipo=tipo_map[tipo_input], valor=valor, data=date.today())
        movimentar_dinheiro(historico)
    def _total_contas(self):
        print(f'R$ {total_contas()}')
    def _filtrar_movimentacoes(self):
        data_inicio = input('Digite a data de início: ')
        data_fim = input('Digite a data final: ')
        data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y').date()
        data_fim = datetime.strptime(data_fim, '%d/%m/%Y').date()
        for i in buscar_historicos_entre_datas(data_inicio, data_fim):
            print(f'{i.valor} - {i.tipo.value}')
    def _criar_grafico(self):
        criar_grafico_por_conta()

if __name__ == "__main__":
    UI().start()
