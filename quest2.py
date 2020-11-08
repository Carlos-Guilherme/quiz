import time
import welcome_to_quiz
import fim_quiz

def quest2():
    comando_invalido_quest2 = 0
    loop_quest2 = 1
    while loop_quest2 == 1:
        iniciou_contagem_quest2 = time.localtime()
        iniciou_ano_quest2 = iniciou_contagem_quest2.tm_year
        iniciou_mes_quest2 = iniciou_contagem_quest2.tm_mon
        iniciou_dia_quest2 = iniciou_contagem_quest2.tm_mday
        iniciou_hora_quest2 = iniciou_contagem_quest2.tm_hour
        iniciou_minuto_quest2 = iniciou_contagem_quest2.tm_min
        iniciou_segundo_quest2 = iniciou_contagem_quest2.tm_sec
        print()
        print('                     QUESTÃO 2!')
        print()
        print(f'Pontuação atual: {welcome_to_quiz.pontuacao}')
        print('Escolha o melhor animal de estimação:')
        print('[1]- Gat@(s)')
        print('[2]- Cachorr@(s)')
        print('[3]- Pássaros')
        print('[4]- Outro')
        res2 = str(input('Digite aqui: '))
        fim_contagem_quest2 =  time.localtime()
        fim_ano_quest_2 = fim_contagem_quest2.tm_year
        fim_mes_quest_2 = fim_contagem_quest2.tm_mon
        fim_dia_quest_2 = fim_contagem_quest2.tm_mday
        fim_hora_quest_2 = fim_contagem_quest2.tm_hour
        fim_minuto_quest_2 = fim_contagem_quest2.tm_min
        fim_segundo_quest_2 = fim_contagem_quest2.tm_sec
        if res2 == '1':
            welcome_to_quiz.pontuacao += 100
        elif res2 == '2':
            welcome_to_quiz.pontuacao += 10
        elif res2 == '3':
            welcome_to_quiz.pontuacao += 1
        elif res2 == '4':
            pessoal_quest2 = ''
            pessoal_quest2 = str(input('Qual? '))
        elif res2 == 'fim':
            fim_quiz.fim_quiz()
        else:
            print('Comando inválido!')
            comando_invalido_quest2 += 1
            loop_quest2 = 1
        time.sleep(1)
        break   