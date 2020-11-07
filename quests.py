import time

def all_quests():
    iniciou_contagem = time.localtime()
    iniciou_ano_quest1 = iniciou_contagem.tm_year
    iniciou_mes_quest1 = iniciou_contagem.tm_mon
    iniciou_dia_quest1 = iniciou_contagem.tm_mday
    iniciou_hora_quest1 = iniciou_contagem.tm_hour
    iniciou_minuto_quest1 = iniciou_contagem.tm_min
    iniciou_segundo_quest1 = iniciou_contagem.tm_sec
    print('=' *51)
    print('                       QUIZ')
    print('                Seja Bem - Vind@!')
    print('=' *51)
    print()
    print('=' *51)
    print('                     QUESTÃO 1!')
    print()
    print('Escolha um')
    print('[1]- Gato')
    print('[2]- Cachorro')
    print('[2]- Cavalo')
    res1 = str(input('Digite aqui: '))
    fim_contagem =  time.localtime()
    fim_ano_quest_1 = fim_contagem.tm_year
    fim_mes_quest_1 = fim_contagem.tm_mon
    fim_dia_quest_1 = fim_contagem.tm_mday
    fim_hora_quest_1 = fim_contagem.tm_hour
    fim_minuto_quest_1 = fim_contagem.tm_min
    fim_segundo_quest_1 = fim_contagem.tm_sec
    print('=' *51)
    print('[1]- Para ver os dados do Cliente')
    print('[2]- Para ver os dados do Criador')
    finalizer = str(input('Digite aqui: '))
    if finalizer == '1':
        pass
    elif finalizer == '2':
        confirmar_senha = str(input('Digite a senha Mestre: '))
        if confirmar_senha == 'grandemestre123':
            print('=' *51)
            print('Dados Questão 1:')
            print(f'Data inicial: {iniciou_dia_quest1}/{iniciou_mes_quest1}/{iniciou_ano_quest1}')
            print(f'Hora inicial: {iniciou_hora_quest1}:{iniciou_minuto_quest1}:{iniciou_segundo_quest1}')
            print()
            print(f'Data final: {fim_dia_quest_1}/{fim_mes_quest_1}/{fim_ano_quest_1}')
            print(f'Hora final: {fim_hora_quest_1}:{fim_minuto_quest_1}:{fim_segundo_quest_1}')
            print(f'Resposta da Questão: {res1}')
            print('=' *51)




    


