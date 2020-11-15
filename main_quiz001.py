import time
import all_quests


loop = 'voltar ao inicio'
while loop == 'voltar ao inicio':  # Ponto de restauração
    print('=' *51)
    print('\033[0;34m                 Main Quiz 0.2                \033[0m')
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
        print('7-')
        print('')
        print('=' *51)
        print('Criador: Carlos Emanoel')
        print('Data de início: 07/11/2020   sáb.')
        print('=' *51)
    elif primeira_pergunta == '2': #começar agora!
        time.sleep(1)
        print()
        print('                   Bem - Vind@')
        time.sleep(1)
        print('                        Ao                         ')
        time.sleep(1)
        print('                       QUIZ                        ')
        time.sleep(2)
        all_quests.quests()
    else: # Caso o comando não seja nenhum dos citados acima
        print('Comando Inválido!')
        loop = 'voltar ao inicio'
        