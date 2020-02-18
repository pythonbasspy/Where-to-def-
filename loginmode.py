# -*- coding: utf-8 -*-
while True:
    user = raw_input('Insira seu login: ')
    password = raw_input('Insira sua senha: ')

    if user == 'admin' and password == '00101':
        print 'Bem-vindo %s' % user + ' .Podemos dar inicio?'
        answer = raw_input('sim ou não? ')
        if answer == 'sim':
            print 'Para começar informe o valor da seguinte conta: '
            resposta = raw_input('5 + 2: ')
            if resposta == '7':
                print 'Correto. Tudo pronto para começar a integração.'
                break
            else:
                print 'Pense um pouco e tente novamente.'



        if answer == 'não':
            print 'Mas porquê não %s?' % user + '. Precisamos começar.'
            replica = raw_input('Podemos?')
            if replica == 'não':
                print 'Tudo bem. Usuário deslogado.'
                break

    if user == 'admin' and password != '00101':
        print 'Senha incorreta. Tente novamente.'

    if user != 'admin' and password == '00101':
        print 'Usuário incorreto. Tente novamente.'
    if user!= 'admin' and password != '00101':
        print 'Login incorreto.'
