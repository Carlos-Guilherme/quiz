import time
import informacoes
import welcome_to_quiz
import quest1
import quest2
import fim_quiz


loop = 'voltar ao inicio'
while loop == 'voltar ao inicio':
    print('=' *51)
    print('\033[0;34m                 Main Quiz 0.0                \033[0m')
    print('=' *51)
    print()
    time.sleep(2)
    print('[1]- Informações sobre o quiz')
    print('[2]- Começar Agora!')
    print()
    primeira_pergunta = str(input('Digite aqui: '))
    if primeira_pergunta == '1': #informações do quiz
        time.sleep(1)
        informacoes.info()
    elif primeira_pergunta == '2': #começar agora!
        time.sleep(1)
        welcome_to_quiz.welcome_to_quiz()
        quest1.quest1()
        quest2.quest2()
        fim_quiz.fim_quiz()
    else:
        print('Comando Inválido!')
        loop = 'voltar ao inicio'