usuarios = []
animais = []
produtos = []
comentarios = []

lucros = []
gastos = []

caracteres = ['!', '@', '#', '$', '%', '&']

while True:

    print('\n==============================')
    print('      SISTEMA RURAL')
    print('==============================')

    print('[1] Cadastrar usuário')
    print('[2] Fazer login')
    print('[0] Encerrar')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':

        nome = input('Digite o nome: ').lower().strip()

        existe = False

        for u in usuarios:

            if u[0] == nome:
                existe = True

        if existe == True:

            print('Usuário já existe.')

        else:

            while True:

                senha = input('Digite a senha: ')

                if len(senha) < 8:

                    print('Senha muito curta.')

                else:

                    especial = False

                    for c in senha:

                        if c in caracteres:
                            especial = True

                    if especial == False:

                        print('Senha precisa ter caractere especial.')

                    else:
                        break

            while True:

                tipo = input('Tipo de usuário (adm/cliente): ').lower()

                if tipo == 'adm' or tipo == 'cliente':
                    break

                else:
                    print('Tipo inválido.')

            usuarios.append([nome, senha, tipo])

            print('Cadastro realizado com sucesso.')

    elif opcao == '2':

        nome = input('Nome: ').lower().strip()
        senha = input('Senha: ')

        login = False
        tipo_usuario = ''

        for u in usuarios:

            if u[0] == nome and u[1] == senha:

                login = True
                tipo_usuario = u[2]

        if login == False:

            print('Login incorreto.')

        else:

            print('Login realizado.')

            while login == True and tipo_usuario == 'adm':

                print('\n========== MENU ADM ==========')

                print('[1] Adicionar animal')
                print('[2] Listar animais')
                print('[3] Adicionar produto')
                print('[4] Ver produtos')
                print('[5] Estatísticas')
                print('[6] Ver comentários')
                print('[0] Logout')

                escolha = input('Escolha: ')

                if escolha == '1':

                    tipo = input('Tipo do animal: ')
                    codigo = int(input('ID: '))
                    status = input('Status: ')

                    animais.append([tipo, codigo, status])

                    print('Animal cadastrado.')

                elif escolha == '2':

                    if len(animais) == 0:

                        print('Nenhum animal cadastrado.')

                    else:

                        for a in animais:

                            print(f'Tipo: {a[0]}')
                            print(f'ID: {a[1]}')
                            print(f'Status: {a[2]}')
                            print('----------------')

                elif escolha == '3':

                    nome_produto = input('Nome do produto: ').upper()

                    quantidade = int(input('Quantidade: '))

                    valor = float(input('Valor: '))

                    produtos.append([nome_produto, quantidade, valor])

                    gastos.append(valor * quantidade)

                    print('Produto adicionado.')

                elif escolha == '4':

                    if len(produtos) == 0:

                        print('Nenhum produto cadastrado.')

                    else:

                        for p in produtos:

                            print(f'Produto: {p[0]}')
                            print(f'Quantidade: {p[1]}')
                            print(f'Valor: R$ {p[2]}')
                            print('----------------')

                elif escolha == '5':

                    total_lucro = 0
                    total_gasto = 0

                    for l in lucros:
                        total_lucro += l

                    for g in gastos:
                        total_gasto += g

                    resultado = total_lucro - total_gasto

                    print(f'Lucros: R$ {total_lucro}')
                    print(f'Gastos: R$ {total_gasto}')
                    print(f'Resultado final: R$ {resultado}')

                elif escolha == '6':

                    if len(comentarios) == 0:

                        print('Nenhum comentário.')

                    else:

                        for c in comentarios:

                            print(c)

                elif escolha == '0':

                    login = False

                    print('Logout realizado.')

                else:

                    print('Opção inválida.')

            while login == True and tipo_usuario == 'cliente':

                print('\n======= MENU CLIENTE =======')

                print('[1] Ver produtos')
                print('[2] Comprar produto')
                print('[3] Fazer reclamação')
                print('[0] Logout')

                escolha = input('Escolha: ')

                if escolha == '1':

                    if len(produtos) == 0:

                        print('Nenhum produto disponível.')

                    else:

                        for p in produtos:

                            print(f'Produto: {p[0]}')
                            print(f'Quantidade: {p[1]}')
                            print(f'Valor: R$ {p[2]}')
                            print('----------------')

                elif escolha == '2':

                    if len(produtos) == 0:

                        print('Sem produtos.')

                    else:

                        contador = 1

                        for p in produtos:

                            print(f'{contador} - {p[0]}')

                            contador += 1

                        compra = int(input('Escolha o produto: '))

                        quantidade = int(input('Quantidade: '))

                        produto = produtos[compra - 1]

                        if quantidade > produto[1]:

                            print('Quantidade indisponível.')

                        else:

                            total = quantidade * produto[2]

                            produto[1] -= quantidade

                            lucros.append(total)

                            print(f'Compra realizada.')
                            print(f'Total: R$ {total}')

                elif escolha == '3':

                    texto = input('Digite sua reclamação: ')

                    comentarios.append(texto)

                    print('Comentário enviado.')

                elif escolha == '0':

                    login = False

                    print('Logout realizado.')

                else:

                    print('Opção inválida.')

    elif opcao == '0':

        print('Sistema encerrado.')
        break

    else:

        print('Opção inválida.')
