# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Work location: Fatec de Ferraz de Vasconcelos
# Developer: Kaik Mendes e Luis Guilherme S Sousa
# Date: 05/2023
# Project: ALP 004
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
import os # pra caminhos txt
import textwrap # pra relatorios

# Variaveis globais
bdprod: str = 'produtos.txt'
bdpedido: str = 'pedido.txt'
bdcliente: str = 'cliente.txt'
bdcadastro: str = "credenciais_cadastradas.txt"
bdlogin: str = 'login_config.txt'
bdpedidos_cancelados: str = 'pedidos_cancelados.txt'
bdrendimentos: str = "rendimentos.txt"
bdrendimentos_cancelados: str = 'rendimentos_cancelados.txt'


def logando(usuario, senha, manter) -> str:
    if not os.path.exists(bdcadastro):
        with open(bdcadastro, 'w', encoding='utf-8') as arquivo:
            arquivo.write('')
    verificar = []  # lista para verificar se o login está correto
    with open(bdcadastro, "r", encoding='utf-8') as logar:
        for i in logar:
            verificar.append(i.rstrip().split(','))

    for conta in verificar:
        user, email, passw = conta
        if usuario == "username" or usuario == "email":
            return "conta inexistente"
        elif (email == usuario or user == usuario) and passw != senha:
            return "senha incorreta"
        elif (user == usuario or email == usuario) and passw == senha:
            if manter == True:
                with open(bdlogin, 'r', encoding='utf-8') as arquivo:
                    linhas = arquivo.readlines()
                    itens = []
                    for i in linhas:
                        itens.append(i.rstrip().split('='))
                for i in range(len(itens)):
                    if itens[i][0] == 'username':
                        linhas[i] = f'username={user}\n'
                    elif itens[i][0] == 'email':
                        linhas[i] = f'email={email}\n'
                    elif itens[i][0] == 'senha':
                        linhas[i] = f'senha={senha}\n'
                with open(bdlogin, 'w', encoding='utf-8') as arquivo:
                    arquivo.writelines(linhas)
            return "True"
    else:
        return "conta inexistente"


def deslogar() -> bool:
    with open(bdlogin, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        itens = []
    for i in linhas:
            itens.append(i.rstrip().split('='))
    for i in range(len(itens)):
        if itens[i][0] == 'username':
            linhas[i] = f'username=\n'
        elif itens[i][0] == 'email':
            linhas[i] = f'email=\n'
        elif itens[i][0] == 'senha':
            linhas[i] = f'senha=\n'
    with open(bdlogin, 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(linhas)
        
    return True


def cadastrar(usuario, email, senha) -> str:
    if not os.path.exists(bdcadastro):
        with open(bdcadastro, 'w', encoding='utf-8') as arquivo:
            arquivo.write('')
    verificacao = []  # verificacao para validar o cadastro
    with open(bdcadastro, "r", encoding='utf-8') as verificar:
        for i in verificar:
            verificacao.append(i.rstrip().split(','))

    for conta in verificacao:
        user, email_cadastrado, passw = conta
        if "username" == usuario:
            return "usuário inválido"
        elif user == usuario:
            return "Usuário já existe"
        elif email_cadastrado == email:
            return "E-mail já cadastrado"
    if usuario == "" or email == "" or senha == "":
        return "campos vazios"
    elif "@" not in email:
        return "email inválido"
    elif len(senha) < 8:
        return 'senha inválida' 
    else:
        with open(bdcadastro, "a", encoding='utf-8') as cadastro:
            cadastro.writelines(f'{usuario},{email},{senha}\n')
            return "cadastro sucesso"


def trocar_tema(modo):
    with open(bdlogin, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    itens = []
    for i in linhas:
            itens.append(i.rstrip().split('='))
    if modo == 'dark':
        for i in range(len(itens)):
            if itens[i][0] == 'tema':
                linhas[i] = f'tema=cosmo\n'
    else:
        for i in range(len(itens)):
            if itens[i][0] == 'tema':
                linhas[i] = f'tema=darkly\n'
    with open(bdlogin, 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(linhas)


def criar_bdcadastro():
    with open(bdcadastro, 'w') as arquivo:
        arquivo.write('')

# TESTE funcao de editar cadastro, inutil por enquanto


def editar_cadastro(UserAtual, EmailAtual, SenhaAtual,
                    NovoUser, NovoEmail, NovaSenha):
    verify = []
    with open(bdcadastro, "r", encoding='utf-8') as verificar:
        linhas = verificar.readlines()
        for i in linhas:
            verify.append(i.rstrip().split(','))

    # pega os inputs de confirmacao de cadastro atual e novo cadastro
    user = UserAtual.get()
    email = EmailAtual.get()
    senha = SenhaAtual.get()
    novouser = NovoUser.get()
    novoemail = NovoEmail.get()
    novasenha = NovaSenha.get()

    # verifica se as informações atuais batem para a edição
    sss = len(verify)
    for linha in range(sss):
        if (user == verify[linha][0]
            and email == verify[linha][1]
            and senha == verify[linha][2]):
            if linha < len(linhas):
                linhas[linha] = f'{novouser},{novoemail},{novasenha}\n'
                with open(bdcadastro, "w", encoding='utf-8') as editar:
                    editar.writelines(linhas)
                print('atualizado com sucesso')
                break
    else:
        print('ble')

# editar dados na tela home


def editar_dados(dados):
    L1 = []
    L1.append(dados.rstrip().split(' '))
    # transforma os espaços em virgula
    novo_texto = ' '.join(','.join(linha) for linha in L1)
    if novo_texto == '':
        print('calmo ai ce vai apagar tudo')
        # nao permite que o usuario apague todos os dados
        # evita que ele apague tudo sem querer
        # necessita de pelo menos uma linha escrita

    else:
        novo_texto += '\n'  # adiciona uma quebra de linha ao novo texto
        with open('credenciais_cadastradas.txt', 'w', encoding='utf-8') as editar:
            editar.writelines(novo_texto)

# funcao de consultar os dados atuais


def ver_dados(dados) -> None:
    L1 = []
    with open(bdcadastro, 'r', encoding='utf-8') as db:
        for i in db:
            L1.append(i.rstrip().split(','))
    for i in L1:
        nome, sobrenome, valor = i
        # formata os dados na interface
        dados.insert('end', f'{nome} {sobrenome} {valor}' + '\n')
    dados.update()

# seção PRODUTOS {


def criar_bdprod() -> None:
    with open(bdprod, 'w', encoding='utf-8') as arquivo:

        id: str = "ID:"
        nome: str = "NOME:"
        quantidade: str = "QUANTIDADE:"
        categoria: str = "CATEGORIA:"
        preco: str = "PREÇO:"
        desc: str = "DESCRIÇÃO:"

        linha1: str = f'{id}|{nome}|{quantidade}|{categoria}|{preco}|{desc}'

        arquivo.write(f'{linha1}\n')


def ver_produtos(categoria) -> list:
    if not os.path.exists(bdprod) or os.stat(bdprod).st_size == 0:
        criar_bdprod()

    category=[]
    with open ('produtos.txt', 'r', encoding='utf-8') as arquivo:
        for i in arquivo:
            category.append(i.rstrip().split('|'))
        category.remove(category[0])
    lista = []
    if categoria == 'Selecione uma categoria':
        return category
    elif categoria == 'Todas':
        return category
    else: 
        for item in range(len(category)):
            if categoria == category[item][3]:
                lista.append(category[item])
        return lista


def add_produtos(produto) -> str:
    if not os.path.exists(bdprod) or os.stat(bdprod).st_size == 0:
        criar_bdprod()

    with open(bdprod, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        id = []
        for i in linhas:
            id.append(i.rstrip().split('|'))
        if len(linhas) == 1:
            idprod = len(linhas)
        else:
            idprod = id[-1][0]
            idprod = (int(idprod))+1

    with open(bdprod, 'a', encoding='utf-8') as arquivo:
        for i in produto:
            nome, quantidade, categoria, valor, desc = i
            arquivo.writelines(f'{idprod}|{nome}|{quantidade}|{categoria}|{valor}|{desc}\n')
        return "cadastrado"


def deletar_produto(var) -> str:  # (list(var) = Ids dos produtos)
    if not os.path.exists(bdprod) or os.stat(bdprod).st_size == 0:
        return "não encontrado"

    else:
        produtos = []
        with open(bdprod, 'r', encoding='utf-8') as arquivo:
            linha = arquivo.readlines()
            for i in linha:
                produtos.append(i.rstrip().split('|'))
            produtos.remove(produtos[0])
        for i in range(len(produtos)):
            for x in range(len(var)):
                if var[x][0] == int(produtos[i][0]):
                    linha[i+1] = ''
                    with open(bdprod, "w", encoding='utf-8') as arquivo:
                        arquivo.writelines(linha)
        return "deletado"


def alterar_produtos(produto) -> str:
    if not os.path.exists(bdprod) or os.stat(bdprod).st_size == 0:
        criar_bdprod()
    produtos = []
    with open(bdprod, 'r', encoding='utf-8') as arquivo:
        linha = arquivo.readlines()
        for i in linha:
            produtos.append(i.rstrip().split('|'))
        produtos.remove(produtos[0])
    for i in range(len(produtos)):
        if int(produto[0][0]) == int(produtos[i][0]):
            linha[i+1] = (f'{produto[0][0]}|{produto[0][1]}|{produto[0][2]}|{produto[0][3]}|{produto[0][4]}|{produto[0][5]}\n')
            with open(bdprod, "w", encoding='utf-8') as arquivo:
                arquivo.writelines(linha)
    return 'alterado'


def relatorio_produtos() -> str:
    if not os.path.exists(bdprod) or os.stat(bdprod).st_size == 0:
        criar_bdprod()

    pasta_documentos = os.path.join(os.path.expanduser('~'), 'Documents')
    if not os.path.exists(pasta_documentos):
        pasta_documentos = os.path.join(os.path.expanduser('~'), 'Documentos')
        

    caminho_relatorio = os.path.join(pasta_documentos, 'relatorio_produtos.txt')
    with open(caminho_relatorio, 'w', encoding='utf-8') as arquivo:
            arquivo.write("")

    texto_vazio = ''
    divisores = '+'+'—'*10+'+'+'—'*20+'+'+'—'*25+'+'+'—'*20+'+'+'—'*19+'+'+'—'*20+'+'
    lista_relatorio = []
    with open(bdprod, 'r', encoding='utf-8') as arquivo:
        for i in arquivo:
            lista_relatorio.append(i.rstrip().split('|'))
    for i in lista_relatorio:
        id, nome, quantidade, categoria, valor, descricao = i
        if id == 'ID:':
            texto_formatado = (divisores,
                f'\n|{id:^10}|{nome:^20}|{quantidade:^25}|{categoria:^20}|{valor:^19}|{descricao:^20}|\n',
                divisores)
        else:
            descricao_formatada = descricao.split('ǵ')
            if len(descricao_formatada) > 1:
                while descricao_formatada[-1] == '':
                    descricao_formatada.remove(descricao_formatada[-1])
            descricao_formatada = [textwrap.wrap(descricao, width=20) for descricao in descricao_formatada]
            texto_formatado = (f'\n|{id:^10}|{nome:^20}|{quantidade:^20} un. |{categoria:^20}| R$ {valor:^15}|')
            if len(descricao_formatada) > 1:
                for linha in descricao_formatada:
                    for i in range(len(linha)):
                        if linha == descricao_formatada[-1]: # Verifica se é a última linha
                            texto_formatado += f'{linha[i]:^20}|\n' + divisores
                        else:
                            texto_formatado +=(f'{linha[i]:^20}|\n'
                                        f'|{texto_vazio:^10}|{texto_vazio:^20}|'
                                        f'{texto_vazio:^25}|{texto_vazio:^20}|{texto_vazio:^19}|')
            else:
                if descricao_formatada[0] == []:
                    descricao_formatada = ' '
                for linha in descricao_formatada:
                    for i in range(len(linha)):
                        if linha[i] == descricao_formatada[-1]:
                            texto_formatado +=f'{linha[i]:^20}|\n'+divisores
                        else:
                            texto_formatado +=(f'{linha[i]:^20}|\n'
                                        f'|{texto_vazio:^10}|{texto_vazio:^20}|'
                                        f'{texto_vazio:^25}|{texto_vazio:^20}|{texto_vazio:^19}|')
        with open(caminho_relatorio, 'a', encoding='utf-8') as arquivo:
            arquivo.writelines(texto_formatado)
    return "salvo"
# Fim da seção PRODUTOS }


# { Seção CLIENTES 


def criar_bdcliente() -> None:
    with open(bdcliente, 'w', encoding='utf-8') as arquivo:

        id: str = "ID:"
        nome: str = "NOME:"
        sobrenome: str = "SOBRENOME:"
        cpfnj: str = "CPF/CNPJ:"
        tel: str = "TELEFONE/CELULAR:"

        linha1: str = f'{id}|{nome}|{sobrenome}|{cpfnj}|{tel}'

        arquivo.write(f'{linha1}\n')


def ver_clientes() -> list:
    if not os.path.exists(bdcliente) or os.stat(bdcliente).st_size == 0:
        criar_bdcliente()

    lista=[]
    with open (bdcliente, 'r', encoding='utf-8') as arquivo:
        for i in arquivo:
            lista.append(i.rstrip().split('|'))
        lista.remove(lista[0])
    return lista


def add_clientes(cliente) -> str:
    if not os.path.exists(bdcliente) or os.stat(bdcliente).st_size == 0:
        criar_bdcliente()

    with open(bdcliente, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        id = []
        for i in linhas:
            id.append(i.rstrip().split('|'))
        if len(linhas) == 1:
            idcliente = len(linhas)
        else:
            idcliente = id[-1][0]
            idcliente = (int(idcliente))+1
    for i in id:
        id, nome, sobrenome, cpfnj, tel = i
        if str(cliente[0][2]) == cpfnj:
            return "ja existente"
    else:
        with open(bdcliente, 'a', encoding='utf-8') as arquivo:
            for i in cliente:
                nome, sobrenome, cpfnj, tel = i
                arquivo.writelines(f'{idcliente}|{nome}|{sobrenome}|{cpfnj}|{tel}\n')
            return "cadastrado"


def verificar_documento(documento) -> bool: #verificar se cpf ou cpnj é valido
    if len(documento) == 11:
        if len(set(documento)) == 1:
            return False
        soma_verificador_1: int = 0
        soma_verificador_2: int = 0
        cpf_9dig = [int(i) for i in documento[:9]]

        multiplicador = 10
        while multiplicador > 1:
            for i in cpf_9dig:
                soma_verificador_1 += (multiplicador * i)
                multiplicador -= 1

        resto1 = soma_verificador_1 % 11
        if resto1 < 2:
            verificador_1 = 0
        else:
            verificador_1 = 11 - resto1

        cpf_10dig = [int(i) for i in documento[:10]]

        multiplicador = 11
        while multiplicador > 1:
            for i in cpf_10dig:
                soma_verificador_2 += (multiplicador * i)
                multiplicador -= 1

        resto2 = soma_verificador_2 % 11
        if resto2 < 2:
            verificador_2 = 0
        else:
            verificador_2 = 11 - resto2
        if verificador_1 == int(documento[9]) and verificador_2 == int(documento[10]):
            return True
        else:
            return False
    elif len(documento) == 14:
        if len(set(documento)) == 1:
            return False
        soma_verificador_1: int = 0
        soma_verificador_2: int = 0
        multiplicador = [5,4,3,2,9,8,7,6,5,4,3,2]
        cnpj_12dig = [int(i) for i in documento[:12]]

        for i in multiplicador:
            for x in cnpj_12dig:
                soma_verificador_1 += (i * x)
                cnpj_12dig.remove(cnpj_12dig[0])
                break

        resto1 = soma_verificador_1 % 11
        if resto1 < 2:
            verificador_1 = 0
        else:
            verificador_1 = 11 - resto1

        multiplicador.insert(0,6)
        cnpj_13dig = [int(i) for i in documento[:13]]
        for i in multiplicador:
            for x in cnpj_13dig:
                soma_verificador_2 += (i * x)
                cnpj_13dig.remove(cnpj_13dig[0])
                break

        resto2 = soma_verificador_2 % 11
        if resto2 < 2:
            verificador_2 = 0
        else:
            verificador_2 = 11 - resto2

        if verificador_1 == int(documento[12]) and verificador_2 == int(documento[13]):
            return True
        else:
            return False
    else:
        return False


def verificar_telefone(telefone):
    if len(telefone) == 9 or len(telefone) == 8:
        return 'DDD'
    elif len(telefone) == 10:
        if str(telefone[2]) not in '2345':
            return 'invalidoT'
    elif len(telefone) == 11:
        if str(telefone[2]) not in '6789':
            return 'invalidoC'


def deletar_cliente(var) -> str:  # (list(var) = Ids dos clientes)
    if not os.path.exists(bdcliente) or os.stat(bdcliente).st_size == 0:
        return "não encontrado"

    else:
        clientes = []
        with open(bdcliente, 'r', encoding='utf-8') as arquivo:
            linha = arquivo.readlines()
            for i in linha:
                clientes.append(i.rstrip().split('|'))
            clientes.remove(clientes[0])
        for i in range(len(clientes)):
            for x in range(len(var)):
                if var[x][0] == int(clientes[i][0]):
                    linha[i+1] = ''
                    with open(bdcliente, "w", encoding='utf-8') as arquivo:
                        arquivo.writelines(linha)
        return "deletado"


def alterar_clientes(cliente) -> str:
    if not os.path.exists(bdcliente) or os.stat(bdcliente).st_size == 0:
        criar_bdcliente()
    clientes = []
    with open(bdcliente, 'r', encoding='utf-8') as arquivo:
        linha = arquivo.readlines()
        for i in linha:
            clientes.append(i.rstrip().split('|'))
        clientes.remove(clientes[0])
    for i in range(len(clientes)):
        if int(cliente[0][0]) == int(clientes[i][0]) or int(cliente[0][0]) == int(clientes[i][3]):
            linha[i+1] = (f'{clientes[i][0]}|{cliente[0][1]}|{cliente[0][2]}|{cliente[0][3]}|{cliente[0][4]}\n')
            for i in range(len(clientes)):
                if str(cliente[0][3]) in clientes[i]:
                    return "ja existente"
            else:
                with open(bdcliente, "w", encoding='utf-8') as arquivo:
                    arquivo.writelines(linha)
                return 'alterado'


def relatorio_clientes() -> str:
    if not os.path.exists(bdcliente) or os.stat(bdcliente).st_size == 0:
        criar_bdcliente()

    pasta_documentos = os.path.join(os.path.expanduser('~'), 'Documents')
    if not os.path.exists(pasta_documentos):
        pasta_documentos = os.path.join(os.path.expanduser('~'), 'Documentos')
        

    caminho_relatorio = os.path.join(pasta_documentos, 'relatorio_clientes.txt')
    with open(caminho_relatorio, 'w', encoding='utf-8') as arquivo:
            arquivo.write("")
    
    divisores = '+'+'—'*10+'+'+'—'*41+'+'+'—'*18+'+'+'—'*17+'+'
    lista_relatorio = []
    with open(bdcliente, 'r', encoding='utf-8') as arquivo:
        for i in arquivo:
            lista_relatorio.append(i.rstrip().split('|'))
    for i in lista_relatorio:
        id, nome, sobrenome, documento, tel= i

        if id == 'ID:':
            texto_formatado = (divisores,
                f'\n|{id:^10}|{"Nome e sobrenome":^41}|{documento:^18}|{tel:^17}|\n',
                divisores)
        else:
            if len(documento) == 11:
                documento = f'{documento[0:3]}.{documento[3:6]}.{documento[6:9]}-{documento[9:]}'
            else:
                documento = f'{documento[:2]}.{documento[2:5]}.{documento[5:8]}/{documento[8:12]}-{documento[12:]}'
            if len(tel) == 11:
                tel = f'({tel[0:2]}) {tel[2:7]}-{tel[7:]}'
            else:
                tel = f'({tel[0:2]}) {tel[2:6]}-{tel[6:]}'
            nome_completo = f'{nome} {sobrenome}'
            texto_formatado = (f'\n|{id:^10}|{nome_completo:^41}|{documento:^18}|{tel:^17}|\n'+divisores)
        with open(caminho_relatorio, 'a', encoding='utf-8') as arquivo:
            arquivo.writelines(texto_formatado)
    return "salvo"
# Fim da seção CLIENTES }


# { Seção PEDIDOS
def criar_bdpedido() -> None:
    with open(bdpedido, 'w', encoding='utf-8') as arquivo:

        id: str = 'ID:'
        idprod: str = 'IDPROD:'
        quantidade: str = 'QUANTIDADE:'
        idcliente: str = 'IDCLIENTE:'
        valor_total: str = 'VALOR:'
        situacao: str = 'SITUAÇÃO:'
        data: str = 'DATA:'
        detalhes: str = 'DETALHES:'
        
        linha1: str = f'{id}|{idprod}|{quantidade}|{idcliente}|{valor_total}|{situacao}|{data}|{detalhes}'

        arquivo.write(linha1+'\n')


def criar_bdpedido_cancelado():
    with open(bdpedidos_cancelados, 'w') as arquivo:
        arquivo.write('')


def ver_pedidos() -> list:
    if not os.path.exists(bdpedido) or os.stat(bdpedido).st_size == 0:
        criar_bdpedido()

    lista=[]
    with open (bdpedido, 'r', encoding='utf-8') as arquivo:
        for i in arquivo:
            lista.append(i.rstrip().split('|'))
        lista.remove(lista[0])
    return lista


def add_pedidos(pedido) -> str:
    if not os.path.exists(bdpedido) or os.stat(bdpedido).st_size == 0:
        criar_bdpedido()

    with open(bdpedido, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        id = []
        for i in linhas:
            id.append(i.rstrip().split('|'))
        if len(linhas) == 1:
            idpedido = len(linhas)
        else:
            idpedido = id[-1][0]
            idpedido = (int(idpedido))+1
    with open(bdpedidos_cancelados, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        id = []
        for i in linhas:
            id.append(i.rstrip().split('|'))
        for i in range(len(id)):
            if int(idpedido) == int(id[i][0]):
                idpedido = int(id[i][0]) + 1
    with open(bdpedido, 'a', encoding='utf-8') as arquivo:
        for i in pedido:
            idprod, quantd, idcliente, valor, situacao, data, desc = i
            arquivo.writelines(f'{idpedido}|{idprod}|{quantd}|{idcliente}|{valor}|{situacao}|{data}|{desc}\n')

    pedinrend()   
    return "cadastrado"


def deletar_pedido(var) -> str:  # (list(var) = Ids dos pedidos)
    if not os.path.exists(bdpedido) or os.stat(bdpedido).st_size == 0:
        return "não encontrado"
    elif not os.path.exists(bdpedidos_cancelados):
        with open(bdpedidos_cancelados, 'w') as arquivo:
            arquivo.write('')
    else:
        pedidos = []
        with open(bdpedido, 'r', encoding='utf-8') as arquivo:
            linha = arquivo.readlines()
            for i in linha:
                pedidos.append(i.rstrip().split('|'))
            pedidos.remove(pedidos[0])
        for i in range(len(pedidos)):
            for x in range(len(var)):
                if var[x][0] == int(pedidos[i][0]):
                    linha[i+1] = ''
                    with open(bdpedido, "w", encoding='utf-8') as arquivo:
                        arquivo.writelines(linha)
                    for y in range(len(pedidos[i])):
                            pedido_cancelado = (f'{pedidos[i][0]}|{pedidos[i][1]}|{pedidos[i][2]}'
                            f'|{pedidos[i][3]}|{pedidos[i][4]}|Cancelado|{pedidos[i][6]}|{pedidos[i][7]}\n')
                            id = pedidos[i][1]
                            quantidade = pedidos[i][2]
                            break
                    produto = ver_produtos('Todas')
                    for z in produto:
                        idprod,nome,quantd,categoria,valor,desc = z
                        if int(id) == int(idprod):
                            produto = []
                            produto.append((idprod,nome,int(quantd)+int(quantidade),categoria,valor,desc))
                            alterar_produtos(produto)
                    with open (bdpedidos_cancelados, 'a', encoding='utf-8') as cancelar:
                        cancelar.writelines(pedido_cancelado)
        pedinrend()
        return "deletado"
    

def alterar_pedidos(pedido) -> str:
    if not os.path.exists(bdpedido) or os.stat(bdpedido).st_size == 0:
        criar_bdpedido()
    pedidos = []
    with open(bdpedido, 'r', encoding='utf-8') as arquivo:
        linha = arquivo.readlines()
        for i in linha:
            pedidos.append(i.rstrip().split('|'))
        pedidos.remove(pedidos[0])
    for i in range(len(pedidos)):
        if int(pedidos[i][0]) == int(pedido[0][0]):
            linha[i+1] = (f'{pedido[0][0]}|{pedido[0][1]}'
                          f'|{pedido[0][2]}|{pedido[0][3]}'
                          f'|{pedido[0][4]}|{pedido[0][5]}'
                          f'|{pedido[0][6]}|{pedido[0][7]}\n')
            with open(bdpedido, "w", encoding='utf-8') as arquivo:
                arquivo.writelines(linha)
    pedinrend()
    return 'alterado'


def relatorio_pedidos() -> str:
    if not os.path.exists(bdpedido) or os.stat(bdpedido).st_size == 0:
        criar_bdpedido()

    pasta_documentos = os.path.join(os.path.expanduser('~'), 'Documents')
    if not os.path.exists(pasta_documentos):
        pasta_documentos = os.path.join(os.path.expanduser('~'), 'Documentos')

    caminho_relatorio = os.path.join(pasta_documentos, 'relatorio_pedidos.txt')
    with open(caminho_relatorio, 'w', encoding='utf-8') as arquivo:
            arquivo.write("")


    divisores = '+'+'—'*10+'+'+'—'*10+'+'+'—'*15+'+'+'—'*19+'+'+'—'*20+'+'+'—'*15+'+'+'—'*20+'+'
    lista_relatorio = []
    with open(bdpedido, 'r', encoding='utf-8') as arquivo:
        for i in arquivo:
            lista_relatorio.append(i.rstrip().split('|'))
    for i in lista_relatorio:
        id, idprod, quantd, idcliente, valor, situacao, data, detalhes = i
        if id == 'ID:':
            texto_formatado = (divisores,
                f'\n|{id:^10}|{idprod:^10}|{idcliente:^15}|{valor:^19}|{situacao:^20}|{data:^15}|{detalhes:^20}|\n',
                divisores)
        else:
            descricao_formatada = detalhes.split('ǵ')
            descricao_formatada = [textwrap.wrap(descricao, width=20) for descricao in descricao_formatada]
            texto_formatado = (f'\n|{id:^10}|{idprod:^10}|{idcliente:^15}| R$ {valor:^15}|{situacao:^20}|{data:^15}|')
            texto_vazio = ''
            for linha in descricao_formatada:
                for i in range(len(linha)):
                    if linha == descricao_formatada[-1] and linha[i] == linha [-1]:  # Verifica se é a última linha
                        texto_formatado += f'{linha[i]:^20}|\n' + divisores
                    else:
                        texto_formatado +=(f'{linha[i]:^20}|\n'
                                        f'|{texto_vazio:^10}|{texto_vazio:^10}|'
                                        f'{texto_vazio:^15}|{texto_vazio:^19}|'
                                        f'{texto_vazio:^20}|{texto_vazio:^15}|')
        with open(caminho_relatorio, 'a', encoding='utf-8') as arquivo:
            arquivo.writelines(texto_formatado)
    return "salvo"




# { Seção RENDIMENTOS
def criar_bdrendimentos() -> None:
    with open(bdrendimentos, 'w', encoding='utf-8') as arquivo:
        
        id: str = 'ID'
        idped: str = 'IDPED'
        tipo: str = 'TIPO'
        valor: str = 'VALOR'
        data: str = 'DATA'
        detalhes: str = 'DETALHES'
        situacao: str = 'SITUAÇÃO'

        linha1: str = f'{id}|{idped}|{tipo}|{valor}|{situacao}|{data}|{detalhes}'

        arquivo.write(f'{linha1}\n')


def ver_rendimentos(tipo) -> list:
    pedinrend()
    if not os.path.exists(bdrendimentos) or os.stat(bdrendimentos).st_size == 0:
        criar_bdrendimentos()
    
    lista=[]
    with open (bdrendimentos, 'r', encoding='utf-8') as arquivo:
        for i in arquivo:
            lista.append(i.rstrip().split('|'))
        lista.remove(lista[0])
    
    type = []
    if tipo == "Selecione um Tipo":
        return lista
    elif tipo == "Todos":
        return lista
    else:
        for item in range(len(lista)):
            if tipo == lista[item][2]:
                type.append(lista[item])
        return type


def add_rendimentos(rendimento) ->str:
    if not os.path.exists(bdrendimentos) or os.stat(bdrendimentos).st_size == 0:
        criar_bdrendimentos()
    
    with open (bdrendimentos, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        id = []
        for i in linhas:
            id.append(i.rstrip().split('|'))
        if len(linhas) == 1:
            idrendimento = len(linhas)
        else:
            idrendimento = id[-1][0]
            idrendimento = (int(idrendimento))+1
    with open (bdrendimentos, 'a', encoding='utf-8') as arquivo:
        for i in rendimento:
            idpedido, tipo, valor, situacao,data, detalhes = i
            arquivo.writelines(f'{idrendimento}|{idpedido}|{tipo}|{valor}|{situacao}|{data}|{detalhes}\n')
    return "cadastrado"


def alterar_rend(rendimento) -> str:
    if not os.path.exists(bdrendimentos) or os.stat(bdrendimentos).st_size == 0:
        criar_bdrendimentos()

    with open (bdrendimentos, 'r', encoding='utf-8') as arquivo:
        rendimentos = []
        linhas = arquivo.readlines()
        for i in linhas:
            rendimentos.append(i.rstrip().split('|'))
        rendimentos.remove(rendimentos[0])
    for i in range(len(rendimentos)):
        if int(rendimento[0][0]) == int(rendimentos[i][0]):
            linhas[i+1] = (f'{rendimento[0][0]}|{rendimento[0][1]}|{rendimento[0][2]}|{rendimento[0][3]}|{rendimento[0][4]}|{rendimento[0][5]}|{rendimento[0][6]}\n')
            with open (bdrendimentos, 'w', encoding='utf-8') as arquivo:
                arquivo.writelines(linhas)
    return 'Alterado'


def deletar_rendimento(var) -> str:
    if not os.path.exists(bdrendimentos) or os.stat(bdrendimentos).st_size == 0:
        criar_bdrendimentos()
    elif not os.path.exists(bdrendimentos_cancelados):
        with open (bdrendimentos_cancelados, 'w', encoding='utf-8') as arquivo:
            arquivo.write('')

    else:
        rendimento = []
        with open (bdrendimentos, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            for i in linhas:
                rendimento.append(i.rstrip().split('|'))
            rendimento.remove(rendimento[0])
        for i in range(len(rendimento)):
            for x in range(len(var)):
                if var[x][0] == int(rendimento[i][0]):
                    linhas[i+1] = ""
                    with open(bdrendimentos, "w", encoding='utf-8') as arquivo:
                        arquivo.writelines(linhas)
                    for x in range(len(rendimento[i])):
                        rendimento_cancelado = (f'{rendimento[i][0]}|{rendimento[i][1]}|{rendimento[i][2]}'
                            f'|{rendimento[i][3]}|{rendimento[i][4]}|{rendimento[i][5]}|{rendimento[i][6]}\n')
                        break
                    with open(bdrendimentos_cancelados, 'a', encoding='utf-8') as arquivo:
                        arquivo.writelines(rendimento_cancelado)
                    return "deletado"


def relatorio_rend() -> str:
    if not os.path.exists(bdrendimentos) or os.stat(bdrendimentos).st_size == 0:
        criar_bdrendimentos()

    pasta_documentos = os.path.join(os.path.expanduser('~'), 'Documents')
    if not os.path.exists(pasta_documentos):
        pasta_documentos = os.path.join(os.path.expanduser('~'), 'Documentos')

    caminho_relatorio = os.path.join(pasta_documentos, 'relatorio_rendimentos.txt')
    with open(caminho_relatorio, 'w', encoding='utf-8') as arquivo:
            arquivo.write("")

    divisores = '+'+'—'*10+'+'+'—'*10+'+'+'—'*10+'+'+'—'*19+'+'+'—'*20+'+'+'—'*15+'+'+'—'*20+'+'
    
    lista_relatorio = []
    with open (bdrendimentos, 'r', encoding='utf-8') as arquivo:
        for i in arquivo:
            lista_relatorio.append(i.rstrip().split('|'))
        for i in lista_relatorio:
            id, idped, tipo, valor, sit, data, detalhes= i
            if id == "ID":
                texto_formatado = (divisores,
                                   f'\n|{id:^10}|{idped:^10}|{tipo:^10}|{valor:^19}|{sit:^20}|{data:^15}|{detalhes:^20}|\n',
                                   divisores)
            else:
                descricao_formatada = detalhes.split('æ')
                descricao_formatada = [textwrap.wrap(descricao, width=20)for descricao in descricao_formatada]
                texto_formatado = (f'\n|{id:^10}|{idped:^10}|{tipo:^10}|{valor:^19}|{sit:^20}|{data:^15}|')
                texto_vazio = ''
                for linha in descricao_formatada:
                    for i in range(len(linha)):
                        if linha == descricao_formatada[-1] and linha[i] == linha [-1]:
                            texto_formatado += f'{linha[i]:^20}|\n' + divisores
                        else:
                            texto_formatado += (f'{linha[i]:^20}|\n'
                                                f'|{texto_vazio:^10}|{texto_vazio:^10}|'
                                                f'{texto_vazio:^10}|{texto_vazio:^19}|'
                                                f'{texto_vazio:^20}|{texto_vazio:^15}|')
            with open(caminho_relatorio, 'a', encoding='utf-8') as arquivo:
                arquivo.writelines(texto_formatado)                
        
    return "salvo"


def pedinrend() -> None:
    if not os.path.exists(bdrendimentos) or os.stat(bdrendimentos).st_size == 0:
        criar_bdrendimentos()
    elif not os.path.exists(bdpedidos_cancelados):
        criar_bdpedido_cancelado()
    elif not os.path.exists(bdpedido):
        criar_bdpedido

    pedidos = []
    with open (bdpedido, 'r', encoding='utf-8') as arquivo:
        linhaped = arquivo.readlines()
        for i in linhaped:
            pedidos.append(i.rstrip().split('|'))
        pedidos.remove(pedidos[0])
    for x in pedidos:
        id, idprod, quant, idcli, valor, situa, data, detalhe = x
        tipo = "Entrada"
        detalhes = f'Pedido realizado pelo cliente de ID: {idcli} no dia {data}'
        with open(bdrendimentos, 'r', encoding='utf-8') as arquivo:
            linharend = arquivo.readlines()
            rendimentos = []
            for i in linharend:
                rendimentos.append(i.rstrip().split('|'))
        if len(rendimentos) == 1:
            idrendimento = 1
        else:
            idrendimento = rendimentos[-1][0]
            idrendimento = (int(idrendimento))+1
        for i in range(len(rendimentos)):
            if rendimentos[i][1] == 'IDPED':
                pass
            elif str(id) == str(rendimentos[i][1]):
                idrendimento = rendimentos[i][0]
                with open(bdrendimentos, 'w', encoding='utf-8') as arquivo:
                    linharend[i] = f'{idrendimento}|{id}|{tipo}|{valor}|{situa}|{data}|{detalhes}\n'
                    arquivo.writelines(linharend)
                break
        else:
            with open(bdrendimentos, 'a', encoding='utf-8') as arquivo:
                    arquivo.writelines(f'{idrendimento}|{id}|{tipo}|{valor}|{situa}|{data}|{detalhes}\n')
    
    with open(bdpedidos_cancelados, 'r', encoding='utf-8') as arquivo:
        linha_cancelado = arquivo.readlines()
        cancelados = []
        for i in linha_cancelado:
            cancelados.append(i.rstrip().split('|'))
    if len(cancelados) > 0:
        for x in cancelados:
            id,idprod,quant,idcliente,valor,situacao,data,detalhe = x
            tipo = 'Saída'
            detalhes = f'Pedido cancelado pelo cliente de ID: {idcliente} no dia {data}'
            with open(bdrendimentos, 'r', encoding='utf-8') as arquivo:
                linharend = arquivo.readlines()
                rendimentos = []
                for i in linharend:
                    rendimentos.append(i.rstrip().split('|'))
            if len(rendimentos) == 1:
                idrendimento = 1
            else:
                idrendimento = rendimentos[-1][0]
                idrendimento = (int(idrendimento))+1
            for i in range(len(rendimentos)):
                if rendimentos[i][1] == 'IDPED':
                    pass
                elif str(id) == str(rendimentos[i][1]):
                    idrendimento = rendimentos[i][0]
                    with open(bdrendimentos, 'w', encoding='utf-8') as arquivo:
                        linharend[i] = f'{idrendimento}|{id}|{tipo}|-{valor}|{situacao}|{data}|{detalhes}\n'
                        arquivo.writelines(linharend)
                    break
            else:
                with open(bdrendimentos, 'a', encoding='utf-8') as arquivo:
                    arquivo.writelines(f'{idrendimento}|{id}|{tipo}|{valor}|{situacao}|{data}|{detalhes}\n')
# Fim da seção RENDIMENTOS}