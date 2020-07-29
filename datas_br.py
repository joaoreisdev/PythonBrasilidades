from datetime import datetime

#Classe responsável por devolver datas de forma amigável para usuários brasileiros
class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano=[
            'janeiro', 'fevereiro', 'março',
            'abril', 'maio', 'junho', 'julho',
            'agosto','setembro', 'outubro', 
            'novembro', 'dezembro'
        ]
        mes_cadastro = self.momento_cadastro.month 
        #O -1 é para ajustar o mês, pois a lista começa em zero
        return meses_do_ano[mes_cadastro - 1]

    def dia_semana(self):
        dias_da_semana = [
            'segunda', 'terça', 'quarta',
            'quinta', 'sexta', 'sabado', 'domingo'
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dias_da_semana[dia_semana]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime('%d/%m/%Y %H:%M')
        return data_formatada

    def tempo_cadastro(self):
        #Está retornando 0 pois não está armazenando em nenhum banco o momento cadastrada
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro