import time
import welcome_to_quiz

def quest2():
    loop_quest2 = 1
    while loop_quest2 == 1:
        iniciou_contagem_quest2 = time.localtime()
        iniciou_ano_quest2 = iniciou_contagem_quest2.tm_year
        iniciou_mes_quest2 = iniciou_contagem_quest2.tm_mon
        iniciou_dia_quest2 = iniciou_contagem_quest2.tm_mday
        iniciou_hora_quest2 = iniciou_contagem_quest2.tm_hour
        iniciou_minuto_quest2 = iniciou_contagem_quest2.tm_min
        iniciou_segundo_quest2 = iniciou_contagem_quest2.tm_sec
        print('=' *51)
        print('                     QUESTÃO 2!')
        print()
        comando_invalido_quest2 = 0
        print(f'Pontuação atual: {welcome_to_quiz.pontuacao}')
        print('Em uma situação de risco de vida escolha:')
        print('[1]- Lutar para sobreviver como o risco de morrer\nantes do que o esperado')
        print('[2]- Deixar que a morte venha e não fazer nada')
        print('[3]- Pedir ajuda')
        print('[4]- Outro')
        res2 = str(input('Digite aqui: '))
        fim_contagem_quest1 =  time.localtime()
        fim_ano_quest_1 = fim_contagem_quest1.tm_year
        fim_mes_quest_1 = fim_contagem_quest1.tm_mon
        fim_dia_quest_1 = fim_contagem_quest1.tm_mday
        fim_hora_quest_1 = fim_contagem_quest1.tm_hour
        fim_minuto_quest_1 = fim_contagem_quest1.tm_min
        fim_segundo_quest_1 = fim_contagem_quest1.tm_sec
        if res2 == '1':
            welcome_to_quiz.pontuacao += 10
        elif res2 == '2':
            welcome_to_quiz.pontuacao += 1
        elif res2 == '3':
            welcome_to_quiz.pontuacao += 100
        elif res2 == '4':
            pessoal_quest2 = str(input('Qual? '))
        else:
            print('Comando inválido!')
            comando_invalido_quest2 += 1
            loop_quest1 = 0
        time.sleep(1)
        loop_quest2 = 0    