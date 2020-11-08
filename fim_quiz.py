# FIM DO QUIZ
import quest1
import quest2

def fim_quiz():
    loop_fim = 1
    while loop_fim == 1:
        print('=' *51)
        print('[1]- Para ver os dados do Cliente')
        print('[2]- Para ver os dados do Criador')
        finalizer = str(input('Digite aqui: '))
        if finalizer == '1':
            pass
        elif finalizer == '2':
            confirmar_senha = str(input('Digite a senha Mestre*: '))
            if confirmar_senha == 'grandemestre123':
                print('=' *51)
                print('Dados Questão 1:')
                print(f'Data inicial: {quest1.iniciou_dia_quest1}/{quest1.iniciou_mes_quest1}/{quest1.iniciou_ano_quest1}')
                print(f'Hora inicial: {quest1.iniciou_hora_quest1}:{quest1.iniciou_minuto_quest1}:{quest1.iniciou_segundo_quest1}')
                print()
                print(f'Data final: {quest1.fim_dia_quest_1}/{quest1.fim_mes_quest_1}/{quest1.fim_ano_quest_1}')
                print(f'Hora final: {quest1.fim_hora_quest_1}:{quest1.fim_minuto_quest_1}:{quest1.fim_segundo_quest_1}')
                print()
                print(f'Resposta da Questão: {quest1.res1}')
                print(f'Resposta própria: {quest1.pessoal_quest1}')
                print()
                print(f'Comandos inválidos: {quest1.comando_invalido_quest1}')
                print('=' *51)
                exit()
            else:
                print('Senha inválida!')
                loop_fim = 1