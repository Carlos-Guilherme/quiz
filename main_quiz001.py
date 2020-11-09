import time

loop = 'voltar ao inicio'
while loop == 'voltar ao inicio':  # Ponto de restauração
    print('=' *51)
    print('\033[0;34m                 Main Quiz 0.1                \033[0m')
    print('=' *51)
    print()
    time.sleep(2)
    print('[1]- Informações sobre o quiz')
    print('[2]- Começar Agora!')
    print()
    primeira_pergunta = str(input('Digite aqui: '))
    if primeira_pergunta == '1': #informações do quiz
        time.sleep(1)
        print('=' *51)
        print('                   IFORMAÇÕES                     ')
        print('')
        print('1- Você deverá responder as questões com o número\ncorrespondente dela!')
        print('2- Cada questão é conometrada!')
        print('3- Você poderá acabar o quiz a qualquer momento!\nbasta digitar "fim" em qualquer questão!')
        print('4- Você terá acesso aos dados do cliente (dados de\nhierarquia menor) quando terminar!')
        print('5- Cada questão tem uma pontuação, você poderá ter\nacesso á elas no final do quiz!')
        print('6- A pontuação não indica o seu nível de inteligên\ncia!')
        print('')
        print('=' *51)
        print('Criador: Carlos Emanoel')
        print('Data de início: 07/11/2020   sáb.')
        print('=' *51)
    elif primeira_pergunta == '2': #começar agora!
        time.sleep(1)
        print()
        print('=-=-=-=-=-=-=-=- Seja Bem - Vind@! =-=-=-=-=-=-=-=-')
        time.sleep(1)
        print('=-=-=-=-=-=-=-=-=-=-=-= AO =-=-=-=-=-=-=-=-=-=-=-=-')
        time.sleep(1)
        print('=-==-=-=-=-=-=-=-=-=-= QUIZ =-=-=-=-=-=-=-=-=-=-=-=')
        time.sleep(2)
        comando_invalido_quest1 = 0
        loop_quest1 = 1
        while loop_quest1 == 1:
            iniciou_contagem_quest1 = time.localtime()
            iniciou_ano_quest1 = iniciou_contagem_quest1.tm_year
            iniciou_mes_quest1 = iniciou_contagem_quest1.tm_mon
            iniciou_dia_quest1 = iniciou_contagem_quest1.tm_mday
            iniciou_hora_quest1 = iniciou_contagem_quest1.tm_hour
            iniciou_minuto_quest1 = iniciou_contagem_quest1.tm_min
            iniciou_segundo_quest1 = iniciou_contagem_quest1.tm_sec
            print()
            print('                     QUESTÃO 1!')
            print()
            pontuacao_quest1 = 0
            print(f'Pontuação atual: {pontuacao_quest1}')
            print('Em uma situação de risco de vida escolha:')
            print('[1]- Lutar para sobreviver como o risco de morrer\nantes do que o esperado')
            print('[2]- Deixar que a morte venha e não fazer nada')
            print('[3]- Pedir ajuda')
            print('[4]- Outro')
            res1 = str(input('Digite aqui: '))
            pessoal_quest1 = 'vazio'
            fim_contagem_quest1 =  time.localtime()
            fim_ano_quest_1 = fim_contagem_quest1.tm_year
            fim_mes_quest_1 = fim_contagem_quest1.tm_mon
            fim_dia_quest_1 = fim_contagem_quest1.tm_mday
            fim_hora_quest_1 = fim_contagem_quest1.tm_hour
            fim_minuto_quest_1 = fim_contagem_quest1.tm_min
            fim_segundo_quest_1 = fim_contagem_quest1.tm_sec
            if res1 == '1':
                pontuacao_quest1 += 10
            elif res1 == '2':
                pontuacao_quest1 += 1
            elif res1 == '3':
                pontuacao_quest1 += 100
            elif res1 == '4':
                pessoal_quest1 = 'vazio'
                pessoal_quest1 = str(input('Qual? '))
            elif res1 == 'fim':
                loop_fim = 1
            else:
                print('Comando inválido!')
                comando_invalido_quest1 += 1
            time.sleep(1)
            break
        loop_quest2 = 1
        while loop_quest2 == 1:
            comando_invalido_quest2 = 0
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
            pontuacao_quest2 = 0
            pontuacao_quest2 += pontuacao_quest1
            print(f'Pontuação atual: {pontuacao_quest2}')
            print('Escolha o melhor animal de estimação:')
            print('[1]- Gat@(s)')
            print('[2]- Cachorr@(s)')
            print('[3]- Pássaros')
            print('[4]- Outro')
            res2 = str(input('Digite aqui: '))
            pessoal_quest2 = 'vazio'
            fim_contagem_quest2 =  time.localtime()
            fim_ano_quest_2 = fim_contagem_quest2.tm_year
            fim_mes_quest_2 = fim_contagem_quest2.tm_mon
            fim_dia_quest_2 = fim_contagem_quest2.tm_mday
            fim_hora_quest_2 = fim_contagem_quest2.tm_hour
            fim_minuto_quest_2 = fim_contagem_quest2.tm_min
            fim_segundo_quest_2 = fim_contagem_quest2.tm_sec
            if res2 == '1':
                pontuacao_quest2 += 100
            elif res2 == '2':
                pontuacao_quest2 += 10
            elif res2 == '3':
                pontuacao_quest2 += 1
            elif res2 == '4':
                pessoal_quest2 = str(input('Qual? '))
            elif res2 == 'fim':
                loop_fim = 1
            else:
                print('Comando inválido!')
                comando_invalido_quest2 += 1
                loop_quest2 = 1
            time.sleep(1)
            break
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
                    print()
                    print(f'Data inicial: {iniciou_dia_quest1}/{iniciou_mes_quest1}/{iniciou_ano_quest1}')
                    print(f'Hora inicial: {iniciou_hora_quest1}:{iniciou_minuto_quest1}:{iniciou_segundo_quest1}')
                    print()
                    print(f'Data final: {fim_dia_quest_1}/{fim_mes_quest_1}/{fim_ano_quest_1}')
                    print(f'Hora final: {fim_hora_quest_1}:{fim_minuto_quest_1}:{fim_segundo_quest_1}')
                    print()
                    print(f'Resposta da Questão: {res1}')
                    print(f'Potuação da Questão: {pontuacao_quest1}')
                    print(f'Resposta própria: {pessoal_quest1}') 
                    print()
                    print(f'Comandos inválidos: {comando_invalido_quest1}')
                    print('=' *51)
                    exit()
                else:
                    print('Senha inválida!')
                    loop_fim = 1 
            else:
                print('Comando inválido!')
                loop_fim = 1
    else: # Caso o comando não seja nenhum dos citados acima
        print('Comando Inválido!')
        loop = 'voltar ao inicio'