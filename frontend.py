# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Work location: Fatec de Ferraz de Vasconcelos
# Developer: Kaik Mendes e Luis Guilherme S Sousa
# Date: 05/2023
# Project: ALP 004
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


import tkinter as tk
import ttkbootstrap as ttk
import backend as df
import os
from datetime import date


def tela_cadastro():
    cadastro = ttk.Toplevel()  # popup de cadastro
    cadastro.title("Cadastro - Anoriat")  # titulo da tela
    label = ttk.Label(cadastro, text="Cadastrar uma nova conta")
    label.grid(columnspan=2, row=0,pady=20,padx=20)
    cadastro.geometry('250x250')
    aviso = ttk.StringVar()
    aviso_label = ttk.Label(master=cadastro, textvariable=aviso)
    aviso_label.grid(columnspan=2, row=4,padx=20)

    usuario = ttk.Label(cadastro, text='Usuário')
    usuario.grid(column=0, row=1,padx=20)
    # onde o usuário digitará o username
    cadastrar_usuario = ttk.Entry(cadastro, width=20)
    cadastrar_usuario.grid(column=1, row=1,padx=20)

    email = ttk.Label(cadastro, text="Email")
    email.grid(column=0, row=2,padx=20)
    # onde o usuário digitará o email
    cadastrar_email = ttk.Entry(cadastro, width=20)
    cadastrar_email.grid(column=1, row=2,padx=20)

    senha = ttk.Label(cadastro, text='Senha')
    senha.grid(column=0, row=3,padx=20)
    # onde o usuario digitará a senha
    cadastrar_senha = ttk.Entry(cadastro, show="*", width=20)
    cadastrar_senha.grid(column=1, row=3,padx=20)

    def cadastrar():
        fc_cadastrar = df.cadastrar(cadastrar_usuario.get(),
                                    cadastrar_email.get(),
                                    cadastrar_senha.get())
        if fc_cadastrar == "campos vazios":
            aviso.set("por favor preencha todos os campos")
        elif fc_cadastrar == "usuário inválido":
            aviso.set("usuário inválido")
        elif fc_cadastrar == "Usuário já existe":
            aviso.set("Usuário já existe")
        elif fc_cadastrar == "E-mail já cadastrado":
            aviso.set("E-mail já cadastrado")
        elif fc_cadastrar == "email inválido":
            aviso.set("email inválido")
        elif fc_cadastrar == 'senha inválida':
            aviso.set("Senha deve conter mais que 8 caracteres")
        elif fc_cadastrar == "cadastro sucesso":
            aviso.set("Cadastro realizado com sucesso")

    # chama funcao de cadastro
    botao = ttk.Button(cadastro, text="Cadastrar", command=cadastrar)
    botao.grid(columnspan=2, row=5,pady=20,padx=20)


# Teste editar
# so pra testar, inutil


def editando():
    editar = ttk.Toplevel()
    editar.title('TESTE')
    editar.geometry('270x200')
    label = ttk.Label(editar, text='edite seu cadastro')
    label.grid(columnspan=2, row=0)

    usuario = ttk.Label(editar, text='Usuário cadastrado')
    usuario.grid(column=0, row=1)
    Usuario = ttk.Entry(editar, width=20)  # username do cadastro atual
    Usuario.grid(column=1, row=1)

    email = ttk.Label(editar, text="Email cadastrado")
    email.grid(column=0, row=2)
    Email = ttk.Entry(editar, width=20)  # email do cadastro atual
    Email.grid(column=1, row=2)

    senha = ttk.Label(editar, text='Senha atual')
    senha.grid(column=0, row=3)
    Senha = ttk.Entry(editar, width=20, show="*")  # senha do cadastro atual
    Senha.grid(column=1, row=3)

    novo_usuario = ttk.Label(editar, text='Novo usuário')
    novo_usuario.grid(column=0, row=4)
    novousuario = ttk.Entry(editar, width=20)  # input de novo username
    novousuario.grid(column=1, row=4)

    novo_email = ttk.Label(editar, text="Novo Email")
    novo_email.grid(column=0, row=5)
    novoemail = ttk.Entry(editar, width=20)  # input de novo email
    novoemail.grid(column=1, row=5)

    nova_senha = ttk.Label(editar, text='Nova senha')
    nova_senha.grid(column=0, row=6)
    novasenha = ttk.Entry(editar, width=20, show="*")  # input de nova senha
    novasenha.grid(column=1, row=6)

    # confirma as alterações, chamando funcao de editar cadastro
    botao_confirmar = ttk.Button(editar, text='confirmar',
                                 command=lambda: df.editar_cadastro
                                 (Usuario, Email, Senha, novousuario,
                                  novoemail, novasenha))
    botao_confirmar.grid(columnspan=2, row=7)


def tela_pedidos():

    def ver_pedidos():

        # Chama função de para visualizar os produtos
        # Existentes no banco de dados

        texto = df.ver_pedidos()
        for i in dados.get_children():
            dados.delete(i)
        texto.reverse()
        for linha in texto:
            id, idprod, quantd, idcliente, valor, situacao, data, desc = linha
            valor = f'R$ {valor}'
            texto_formatado = (id,idprod,idcliente,valor,situacao,data)
            dados.insert(parent = '', index = 0, values = texto_formatado)
        return texto

    def add_pedido():

        # Onde o usuário preencherá os dados para adicionar um pedido
        # Chama a função de adicionar um pedido

        adicionar = ttk.Toplevel()
        adicionar.title('Adicionar pedido')
        adicionar.geometry('405x260')

        adicionar_label = ttk.Label(adicionar, text='Adicionar um pedido')
        adicionar_label.pack(pady=10)

        frame_geral = ttk.Frame(adicionar)
        frame_geral.pack(padx=20)
        frame_labels = ttk.Frame(frame_geral)
        frame_labels.pack(side = 'left', fill='y',ipadx=10)
        frame_entrys = ttk.Frame(frame_geral)
        frame_entrys.pack(side = 'right')

        produto_var= tk.StringVar()
        quantd_var= tk.StringVar()
        cliente_var= tk.StringVar()
        valor_var= tk.StringVar(value='0.0')
        situacao_var = tk.StringVar()

        produto_label = ttk.Label(frame_labels, text='Produto')
        produto_label.pack(pady=5,anchor='w')
        quantidade_label = ttk.Label(frame_labels, text='Quantidade')
        quantidade_label.pack(pady=10,anchor='w')
        cliente_label = ttk.Label(frame_labels, text='Cliente')
        cliente_label.pack(pady=5,anchor='w')
        valor_label = ttk.Label(frame_labels, text='Valor Total R$')
        valor_label.pack(pady=10,anchor='w')
        situacao_label = ttk.Label(frame_labels, text= 'Situação atual')
        situacao_label.pack(pady=5,anchor='w')
        
        def checar_produto(evento):
            global quantidade
            global valor_produto
            global produto_selecionado
            global categoria
            global id_produto
            global nome_produto
            produto_selecionado = produto_var.get().split(': ')[1].split(', ')
            for i in range(len(lista_produtos)):
                if produto_selecionado[0] == lista_produtos[i][0]:
                    quantidade = int(lista_produtos[i][2])
                    valor_produto = float(lista_produtos[i][4])
                    categoria = lista_produtos[i][3]
                    nome_produto = lista_produtos[i][1]
                    id_produto = lista_produtos[i][0]
                    quantd_var.set(str(quantidade))
            quantd_var.trace('w', lambda *args: quant.configure(from_=0, to=quantidade))
        
        def checar_cliente(evento):
            global cliente_selecionado
            global cliente_id
            global cliente_nome
            global cliente_cpfnj
            global telefone

            cliente_selecionado = cliente_var.get().split(': ')[1].split(', ')
            for i in range(len(lista_clientes)):
                if cliente_selecionado[0] == lista_clientes[i][3]:
                    cliente_id = lista_clientes[i][0]
                    cliente_nome = f'{lista_clientes[i][1]} {lista_clientes[i][2]}'
                    cliente_cpfnj = lista_clientes[i][3]
                    telefone = lista_clientes[i][4]
        
        produto = ttk.Combobox(frame_entrys, width=34, textvariable=produto_var)
        produto.pack(anchor='e',)
        produto.bind('<<ComboboxSelected>>', checar_produto)
        quant = ttk.Spinbox(frame_entrys, width=33, from_= 0, to = 0, textvariable=quantd_var)
        quant.pack(pady=5,anchor='e')
        cliente = ttk.Combobox(frame_entrys, width=34, textvariable=cliente_var)
        cliente.pack(anchor='e')
        cliente.bind('<<ComboboxSelected>>', checar_cliente)
        valor = ttk.Entry(frame_entrys, width=36, textvariable=valor_var, state='disabled')
        valor.pack(pady=5,anchor='e')
        situacao = ttk.Entry(frame_entrys, width = 36, textvariable=situacao_var)
        situacao.pack(anchor='e')

        lista_produtos = df.ver_produtos('Todas')
        produtos = []
        for i in lista_produtos:
            id, nome, quantd, categ, valor, desc = i
            produtos.append('ID: '+id + ', '+'Nome: '+nome)
        produto['value'] = produtos

        lista_clientes = df.ver_clientes()
        clientes = []
        for i in lista_clientes:
            id, nome, sobrenome, cpfnj, tel = i
            if len(cpfnj) < 14:
                cpfnjText = 'CPF'
            else:
                cpfnjText = 'CNPJ'
            clientes.append(nome + ' ' + sobrenome +  ', '+f'{cpfnjText}: ' +cpfnj )
        cliente['value'] = clientes

        def calcular_valor(*args):
            try:
                if int(quantd_var.get()) > quantidade:
                    quantd_var.set(str(quantidade))
                valor_var.set(f'{int(quantd_var.get()) * valor_produto}')
            except (ValueError,NameError):
                valor_var.set(0.0)
        quantd_var.trace('w', calcular_valor )
        def confirmar():
            global quantidade
            global cliente_cpfnj
            global telefone
            try:
                int(quantd_var.get())
                float(valor_var.get())
            except ValueError:
                adicionar_label.configure(text='Valores inválidos')
            else:
                if produto_var.get() == "" or cliente_var.get() == "" or situacao_var.get() == "":
                    adicionar_label.configure(text='Os campos não podem estar em branco')
                else:
                    quantd = quantd_var.get()
                    if quantd == '0':
                        adicionar_label.configure(text='Estoque insuficiente')
                        return
                    if quantd[0] == '0':
                        quantd = quantd.replace('0', '', 1)
                    pedido = []
                    data = date.today().strftime("%d/%m/%Y")
                    if len(cliente_cpfnj) == 11:
                        cliente_cpfnj = f'{cliente_cpfnj[0:3]}.{cliente_cpfnj[3:6]}.{cliente_cpfnj[6:9]}-{cliente_cpfnj[9:]}'
                    else:
                        cliente_cpfnj = f'{cliente_cpfnj[:2]}.{cliente_cpfnj[2:5]}.{cliente_cpfnj[5:8]}/{cliente_cpfnj[8:12]}-{cliente_cpfnj[12:]}'
                    if len(telefone) == 11:
                        telefone = f'({telefone[0:2]}) {telefone[2:7]}-{telefone[7:]}'
                    else:
                        telefone = f'({telefone[0:2]}) {telefone[2:6]}-{telefone[6:]}'
                    descricao = (f'ID do produto: {id_produto}ǵNome do produto: {nome_produto}ǵQuantidade: {quantd}ǵCategoria do produto: {categoria}ǵ'
                                 f'Nome do cliente: {cliente_nome}ǵCPF/CNPJ: {cliente_cpfnj}ǵTelefone: {telefone}ǵ'
                                 f'Valor total: R$ {valor_var.get()}')
                    pedido.append((produto_selecionado[0],quantd,cliente_id,valor_var.get(), situacao_var.get(),data,descricao))
                    add = df.add_pedidos(pedido)
                    if add == 'cadastrado':
                        quantidade = quantidade - int(quantd)
                        if int(quantd_var.get()) > quantidade:
                            quant.set(quantidade)
                        for i in range(len(lista_produtos)):
                            if produto_selecionado[0] == lista_produtos[i][0]:
                                produto_alterar = []
                                produto_alterar.append(lista_produtos[i])
                                produto_alterar[0][2] = int(lista_produtos[i][2])-int(quantd)
                                df.alterar_produtos(produto_alterar)
                        ver_pedidos()
        botao_confirmar = ttk.Button(adicionar, text='confirmar', command=confirmar)
        botao_confirmar.pack(pady=10)

    def detalhes():
        detalhes = tk.Toplevel()
        detalhes.geometry('500x325')
        
        detalhes_label = ttk.Label(detalhes, text='Informações detalhadas')
        detalhes_label.pack(pady=10)

        pedido = ttk.Treeview(detalhes, columns=('ID','IDPROD','IDCLIENTE',
                                                'VALOR','SITUACAO','DATA'),
                                                show = 'headings',
                                                height = 1)
        colunas = [('ID', 'ID', 30),
            ('IDPROD', 'ID Produtos', 78),
            ('IDCLIENTE', 'ID Cliente', 70),
            ('VALOR', 'Valor', 85),
            ('SITUACAO', 'Situação', 130),
            ('DATA', 'Data', 69)]
        for column_name, heading_text, width in colunas:
            if column_name == 'VALOR':
                pedido.column(column_name, anchor='w',width=width)
            else:
                pedido.column(column_name, anchor='center',width=width)
            pedido.heading(column_name, text=heading_text)
        pedido.pack(expand='yes')
        descricao_label = ttk.Label(detalhes, text='Descrição do pedido')
        descricao_label.pack(pady=10)
        descricao = tk.Text(detalhes, height=10, width=65)
        descricao.pack()
        
        lista = df.ver_pedidos()
        
        for i in range(len(lista)):
            if pedidos_selecionados[0][0] == int(lista[i][0]):
                texto = f'{lista[i][0]},{lista[i][1]},{lista[i][3]},R$ {lista[i][4]:^15},{lista[i][5]},{lista[i][6]}'
                texto_formatado = (texto.split(','))
                pedido.insert(parent = '', index = 0, values = texto_formatado)
                
                descricao.insert(1.0, lista[i][7].replace('ǵ','\n'))
                descricao.configure(state='disabled')
                break
        botao_fechar = ttk.Button(detalhes, text='Fechar', command=lambda: detalhes.destroy())
        botao_fechar.pack(pady=10)
    
    def pedido_selecionado(*args):
        if len(dados.selection()) == 0:
            botao_detalhes.pack_forget()
            return
        if botao_detalhes.winfo_viewable() == 1:
            botao_detalhes.pack_forget()
        if len(dados.selection()) == 1:
            botao_detalhes.pack(before=botao_relatorio,pady=2)
        global pedidos_selecionados
        pedidos_selecionados = []
        for i in dados.selection():
            pedidos_selecionados.append(dados.item(i)['values'])
        def apagar(event):
            df.deletar_pedido(pedidos_selecionados)
            for i in dados.selection():
                dados.delete(i)
        dados.bind('<KeyPress-Delete>', apagar)

        def verificar_evento(event):
            widget = event.widget
            if isinstance(widget,(ttk.Button,ttk.Treeview)):
                return
            for item in dados.selection():
                dados.selection_remove(item)
            botao_detalhes.pack_forget()
        pedidos.bind('<Button-1>', verificar_evento)

    def cancelar():

        # Abre tela de confirmação
        # Para cancelar os pedidos selecionados
        delete = ttk.Toplevel()
        delete.title('Confirmar deleção')
        delete.geometry('500x260')

        aviso = ttk.StringVar(value = 'Os seguintes pedidos serão cancelados')
        aviso_label = ttk.Label(delete, textvariable=aviso)
        aviso_label.pack(pady=10)

        dados.bind('<<TreeviewSelect>>', lambda event: (pedido_selecionado(), checar()))

        pedidos = ttk.Treeview(delete, columns=('ID','IDPROD','IDCLIENTE',
                                                'VALOR','SITUACAO','DATA'),
                                                show = 'headings',
                                                height = 10)
        colunas = [('ID', 'ID', 30),
            ('IDPROD', 'ID Produtos', 80),
            ('IDCLIENTE', 'ID Cliente', 70),
            ('VALOR', 'Valor', 100),
            ('SITUACAO', 'Situação', 130),
            ('DATA', 'Data', 80)]
        for column_name, heading_text, width in colunas:
            if column_name == 'VALOR':
                pedidos.column(column_name, anchor='w', width=width)
            else:
                pedidos.column(column_name, anchor='center', width=width)
            pedidos.heading(column_name, text=heading_text)
        pedidos.pack()
        def checar():
            try:
                for i in pedidos.get_children():
                    pedidos.delete(i)
                pedidos_selecionados.reverse()
                if len(pedidos_selecionados) > 0:
                    for i in pedidos_selecionados:
                        id, idprod, idcliente, valor, situacao, data = i
                        texto_formatado = (id,idprod,idcliente,valor,situacao,data)
                        pedidos.insert(parent = '', index = 0, values = texto_formatado)
                        aviso.set('Os seguintes pedidos serão cancelados')
                else:
                    aviso.set('Nenhum pedido selecionado')
            except NameError:
                aviso.set('Nenhum pedido selecionado')
        def excluir_pedido(pedido):
            resultado = df.deletar_pedido(pedido)
            if resultado == "deletado":
                for i in pedidos.get_children():
                    pedidos.delete(i)
                ver_pedidos()
                pedidos_selecionados.clear()
                dados.selection_clear()

        botao_confirmar = ttk.Button(delete, text='confirmar',
                                    command=lambda: excluir_pedido(pedidos_selecionados))
        botao_confirmar.pack(pady=10)
        def fechar():
            dados.bind('<<TreeviewSelect>>', pedido_selecionado)
            delete.destroy()
        delete.protocol("WM_DELETE_WINDOW", fechar)
        checar()

    def alterar_pedido():

        # Abre tela para alterar pedidos
        # Chama função de alterar pedidos
        
        adicionar = ttk.Toplevel()
        adicionar.title('Adicionar pedido')
        adicionar.geometry('405x290')

        adicionar_label = ttk.Label(adicionar, text='Adicionar um pedido')
        adicionar_label.pack(pady=10)

        frame_geral = ttk.Frame(adicionar)
        frame_geral.pack(padx=20)
        frame_labels = ttk.Frame(frame_geral)
        frame_labels.pack(side = 'left', fill='y',ipadx=10)
        frame_entrys = ttk.Frame(frame_geral)
        frame_entrys.pack(side = 'right')

        idpedido_var= tk.StringVar()
        produto_var= tk.StringVar()
        quantd_var= tk.StringVar()
        cliente_var= tk.StringVar()
        valor_var= tk.StringVar(value='0.0')
        situacao_var = tk.StringVar()

        idpedido_label = ttk.Label(frame_labels, text='ID do Pedido')
        idpedido_label.pack(pady=10,anchor='w')
        produto_label = ttk.Label(frame_labels, text='Produto')
        produto_label.pack(pady=5,anchor='w')
        quantidade_label = ttk.Label(frame_labels, text='Quantidade')
        quantidade_label.pack(pady=10,anchor='w')
        cliente_label = ttk.Label(frame_labels, text='Cliente')
        cliente_label.pack(pady=5,anchor='w')
        valor_label = ttk.Label(frame_labels, text='Valor Total R$')
        valor_label.pack(pady=10,anchor='w')
        situacao_label = ttk.Label(frame_labels, text= 'Situação atual')
        situacao_label.pack(pady=5,anchor='w')
        
        def checar_produto(*args):
            global quantidade
            global valor_produto
            global produto_selecionado
            global categoria
            global id_produto
            global nome_produto
            produto_selecionado = produto_var.get().split(': ')[1].split(', ')
            for i in range(len(lista_produtos)):
                if produto_selecionado[0] == lista_produtos[i][0]:
                    quantidade = int(lista_produtos[i][2])
                    valor_produto = float(lista_produtos[i][4])
                    categoria = lista_produtos[i][3]
                    nome_produto = lista_produtos[i][1]
                    id_produto = lista_produtos[i][0]
            calcular_valor()

        def checar_cliente(*args):
            global cliente_selecionado
            global cliente_id
            global cliente_nome
            global cliente_cpfnj
            global telefone

            cliente_selecionado = cliente_var.get()
            cliente_selecionado = cliente_selecionado.split(': ')
            for i in range(len(lista_clientes)):
                if cliente_selecionado[0] == lista_clientes[i][0]:
                    cliente_id=lista_clientes[i][0]
                    cliente_nome = f'{lista_clientes[i][1]} {lista_clientes[i][2]}'
                    cliente_cpfnj = lista_clientes[i][3]
                    telefone = lista_clientes[i][4]
                    cliente_var.set(f'{lista_clientes[i][1]} {lista_clientes[i][2]}')
                if len(cliente_selecionado) > 1:
                    if cliente_selecionado[1] == lista_clientes[i][3]:
                        cliente_id=lista_clientes[i][0]
                        cliente_nome = f'{lista_clientes[i][1]} {lista_clientes[i][2]}'
                        cliente_cpfnj = lista_clientes[i][3]
                        telefone = lista_clientes[i][4]

        idpedido = ttk.Entry(frame_entrys, width=36, textvariable=idpedido_var)
        idpedido.pack(pady=5,anchor='e')
        produto = ttk.Combobox(frame_entrys, width=34, textvariable=produto_var)
        produto.pack(anchor='e')
        produto.bind('<<ComboboxSelected>>', checar_produto)
        quant = ttk.Spinbox(frame_entrys, width=33, from_= 0, to = 0, textvariable=quantd_var)
        quant.pack(pady=5,anchor='e')
        cliente = ttk.Combobox(frame_entrys, width=34, textvariable=cliente_var)
        cliente.pack(anchor='e')
        cliente.bind('<<ComboboxSelected>>', checar_cliente)
        valor = ttk.Entry(frame_entrys, width=36, textvariable=valor_var, state='disabled')
        valor.pack(pady=5,anchor='e')
        situacao = ttk.Entry(frame_entrys, width = 36, textvariable=situacao_var)
        situacao.pack(anchor='e')

        lista_produtos = df.ver_produtos('Todas')
        produtos = []
        quantidade_produto=[]
        for i in lista_produtos:
            id, nome, quantd, categ, valor, desc = i
            produtos.append('ID: '+id + ', '+'Nome: '+nome)
            quantidade_produto.append((id,quantd))
        produto['value'] = produtos

        lista_clientes = df.ver_clientes()
        clientes = []
        for i in lista_clientes:
            id, nome, sobrenome, cpfnj, tel = i
            if len(cpfnj) < 14:
                cpfnjText = 'CPF'
            else:
                cpfnjText = 'CNPJ'
            clientes.append(nome + ' ' + sobrenome +  ', '+f'{cpfnjText}: ' +cpfnj )
        cliente['value'] = clientes
        
        def checar_id(*args):
            global quantidade
            global produto_pedido
            global quantidade_pedido
            pedidos = ver_pedidos()
            encontrado = False
            for i in range(len(pedidos)):
                if idpedido_var.get() == pedidos[i][0]:
                    for x in produto['value']:
                        s = x.split(',')
                        if f'ID: {pedidos[i][1]}' == s[0]:
                            produto_var.set(x)
                            break
                    cliente_var.set(f'{pedidos[i][3]}')
                    checar_cliente()
                    for x in cliente['value']:
                        s = x.split(',')
                        if cliente_var.get() == s[0]:
                            cliente_var.set(x)
                            break
                    situacao_var.set(pedidos[i][5])
                    checar_produto()
                    quantd_var.set(pedidos[i][2])
                    quantidade = quantidade + int(quantd_var.get())
                    quantidade_pedido = pedidos[i][2]
                    quantd_var.trace('w',lambda *args: quant.configure(from_=0, to=quantidade))
                    produto_pedido = produto_selecionado[0]
                    encontrado = True
                    break
            if not encontrado:
                produto_var.set('Não encontrado')
                quantd_var.set(0)
                cliente_var.set('Não encontrado')
                valor_var.set('0.0')

        def calcular_valor(*args):
            global quantidade
            try:
                if int(quantd_var.get()) < 0:
                    quantd_var.set('0')
                if int(quantd_var.get()) > int(quantidade) :
                        quantd_var.set(str(quantidade))
                valor_var.set(f'{int(quantd_var.get())*valor_produto}')
            except Exception as e:
                if len(quantd_var.get()) < 1:
                    valor_var.set(0.0)

        idpedido_var.trace('w', checar_id )
        quantd_var.trace('w', calcular_valor)
        produto_var.trace('w', calcular_valor)

        def confirmar():
            global quantidade
            global produto_pedido
            global quantidade_pedido
            global cliente_cpfnj
            global telefone
            try:
                int(quantd_var.get())
                float(valor_var.get())
            except ValueError:
                adicionar_label.configure(text='Valores inválidos')
            else:
                if produto_var.get() == "" or cliente_var.get() == "" or situacao_var.get() == "":
                    adicionar_label.configure(text='Os campos não podem estar em branco')
                else:
                    quantd = quantd_var.get()
                    if quantd == '0' or int(quantidade-int(quantd)) < 0:
                        adicionar_label.configure(text='Estoque insuficiente')
                        return
                    if quantd[0] == '0':
                        quantd = quantd.replace('0', '', 1)
                    pedido = []
                    data = date.today().strftime("%d/%m/%Y")
                    if len(cliente_cpfnj) == 11:
                        cliente_cpfnj = f'{cliente_cpfnj[0:3]}.{cliente_cpfnj[3:6]}.{cliente_cpfnj[6:9]}-{cliente_cpfnj[9:]}'
                    else:
                        cliente_cpfnj = f'{cliente_cpfnj[:2]}.{cliente_cpfnj[2:5]}.{cliente_cpfnj[5:8]}/{cliente_cpfnj[8:12]}-{cliente_cpfnj[12:]}'
                    if len(telefone) == 11:
                        telefone = f'({telefone[0:2]}) {telefone[2:7]}-{telefone[7:]}'
                    else:
                        telefone = f'({telefone[0:2]}) {telefone[2:6]}-{telefone[6:]}'
                    descricao = (f'ID do produto: {id_produto}ǵNome do produto: {nome_produto}ǵQuantidade: {quantd}ǵCategoria do produto: {categoria}ǵ'
                                 f'Nome do cliente: {cliente_nome}ǵCPF/CNPJ: {cliente_cpfnj}ǵTelefone: {telefone}ǵ'
                                 f'Valor total: R$ {valor_var.get()}')
                    pedido.append((idpedido_var.get(),produto_selecionado[0],quantd_var.get(),cliente_id,valor_var.get(), situacao_var.get(),data,descricao))
                    alterar = df.alterar_pedidos(pedido)
                    if alterar == 'alterado':
                        for i in range(len(lista_produtos)):
                            if produto_selecionado[0] != produto_pedido and produto_pedido == lista_produtos[i][0]:
                                produto_alterar_estoque = []
                                produto_alterar_estoque.append(lista_produtos[i])
                                produto_alterar_estoque[0][0] = produto_pedido
                                produto_alterar_estoque[0][2] = int(quantidade)
                                df.alterar_produtos(produto_alterar_estoque)
                            elif produto_selecionado[0] == lista_produtos[i][0]:
                                produto_alterar_estoque = []
                                produto_alterar_estoque.append(lista_produtos[i])
                                produto_alterar_estoque[0][2] = int(quantidade-int(quantd))
                                df.alterar_produtos(produto_alterar_estoque)
                        ver_pedidos()
        
        botao_confirmar = ttk.Button(adicionar, text='confirmar', command=confirmar)
        botao_confirmar.pack(pady=10)

    def pesquisar(event):
        if pesquisa_var.get() == 'Pesquisar um pedido':
            pesquisa_var.set('')
        pesquisa.bind('<KeyRelease>', pesquisar)
        for i in dados.get_children():
            dados.delete(i)
        parametro = pesquisa_var.get().lower()
        texto = df.ver_pedidos()
        texto.reverse()
        for i in range(len(texto)):
            for x in range(1,7):
                if texto[i][x].lower().__contains__(parametro):
                    text= f'{texto[i][0]},{texto[i][1]},{texto[i][3]},R$ {texto[i][4]},{texto[i][5]},{texto[i][6]},{texto[i][7]}'
                    texto_formatado = (text.split(','))
                    dados.insert(parent = '', index = 0, values = texto_formatado)
                    break
    
    
    pedidos = ttk.Toplevel()  # tela de pedidos
    pedidos.title("Pedidos - Anoriat")  # título da tela
    pedidos.geometry('700x550')
    pedidos.geometry(f"+{x-200}+{y-150}")

    botoes_telas_frame = ttk.Frame(pedidos)
    botoes_telas_frame.pack(pady=10)

    #visualizar_frame = ttk.Frame(produtos)
    #visualizar_frame.pack()

    frame_funcoes = ttk.Frame(pedidos)
    frame_funcoes.pack()
    frame_botoes_funcoes = ttk.Frame(frame_funcoes)
    frame_botoes_funcoes.pack(pady=28,padx=20,side='right',fill='y')

    pesquisa_var = tk.StringVar(value='Pesquisar um pedido')
    pesquisa = tk.Entry(frame_funcoes, textvariable=pesquisa_var, width= 40)
    pesquisa.pack()
    pesquisa.bind('<Button-1>', pesquisar)


    # Listagem pedidos
    dados = ttk.Treeview(frame_funcoes, columns=('ID','IDPROD','IDCLIENTE',
                                            'VALOR','SITUACAO','DATA'),
                                            show = 'headings',
                                            height = 30)
    colunas = [('ID', 'ID', 30),
        ('IDPROD', 'ID Produtos', 80),
        ('IDCLIENTE', 'ID Cliente', 70),
        ('VALOR', 'Valor', 100),
        ('SITUACAO', 'Situação', 150),
        ('DATA', 'Data', 80)]
    for column_name, heading_text, width in colunas:
        if column_name == 'VALOR':
            dados.column(column_name, anchor='w', width=width)
        else:
            dados.column(column_name, anchor='center', width=width)
        dados.heading(column_name, text=heading_text)
    dados.pack(side='left',pady=10)
    dados.bind('<<TreeviewSelect>>', pedido_selecionado )

    ver_pedidos()

    def fechar(tela):
        if tela == 'home':
            home.deiconify()
            pedidos.destroy()
        elif tela == 'clientes':
            tela_clientes()
            pedidos.destroy()
        elif tela == 'produtos':
            tela_produtos()
            pedidos.destroy()
        elif tela == 'rendimentos':
            tela_rendimentos()
            pedidos.destroy()
        else:
            login.destroy()
    botao_home = ttk.Button(botoes_telas_frame, text = 'Início',
                            command = lambda: fechar('home'),width=12)
    botao_home.pack(side='left',padx=2)
    botao_clientes = ttk.Button(botoes_telas_frame, text = 'Clientes',
                                command = lambda: fechar('clientes'),width=12)
    botao_clientes.pack(side='left',padx=2)
    botao_produtos = ttk.Button(botoes_telas_frame, text='Produtos',
                                command=lambda: fechar('produtos'),width=12)
    botao_produtos.pack(side='left', padx=2)
    botao_rendimentos = ttk.Button(botoes_telas_frame, text='Rendimentos',
                                   command=lambda: fechar('rendimentos'), width=12)
    botao_rendimentos.pack(side='left', padx=2)

    botao_add = ttk.Button(frame_botoes_funcoes, text='Adicionar pedido(s)',
                           command=add_pedido,width=17)
    botao_add.pack(pady=2)
    
    botao_alterar = ttk.Button(frame_botoes_funcoes, text='Alterar pedido(s)',
                               command=alterar_pedido,width=17)
    botao_alterar.pack(pady=2)

    botao_cancelar = ttk.Button(frame_botoes_funcoes, text='Cancelar pedido(s)', command=cancelar,width=17)
    botao_cancelar.pack(pady=2)

    botao_detalhes = ttk.Button(frame_botoes_funcoes, text='Detalhes', command=detalhes,width=17)

    botao_relatorio = ttk.Button(frame_botoes_funcoes, text='Exportar relatório',
                                 command=df.relatorio_pedidos,width=17)
    botao_relatorio.pack(pady=2)
    pedidos.protocol("WM_DELETE_WINDOW", lambda: fechar(''))


def tela_rendimentos():

    def ver_tipos():
        tipos = df.ver_rendimentos('Todos')
        lista = []
        lista2 = []
        for item in tipos:
            idrendi, idped, tipos, valores, situa, datarend, detalhes = item
            if tipos not in lista:
                lista.append(tipos)
            if situa not in lista2:
                lista2.append(situa)

        lista.insert(0,"Todos")
        sel_tipo['value'] = lista
        return lista, lista2


    def ver_rendimentos(*args):

        # Chama função para visualizar os rendimentos   
        # Existentes no banco de dados
        texto = df.ver_rendimentos(tipo_var.get())
        for i in dados.get_children():
            dados.delete(i)
        texto.reverse()
        for linha in texto:
            id, idped, tipo, valor, situacao, data, detalhes = linha
            valor = f'R$ {valor}'
            texto_formatado = (id, idped, tipo, valor, situacao, data)
            dados.insert(parent = '', index = 0, values = texto_formatado)
        ver_tipos()
    

    def add_rendimento():
        

        adicionar = ttk.Toplevel()
        adicionar.title('Adicionar Rendimento')
        adicionar.geometry('300x320')

        adicionar_label = ttk.Label(adicionar, text = 'Adicionar um rendimento')
        adicionar_label.pack(pady = 10)

        frame_geral = ttk.Frame(adicionar)
        frame_geral.pack()
        frame_labels = ttk.Frame(frame_geral)
        frame_labels.pack(side = 'left', fill = 'y')
        frame_entrys = ttk.Frame(frame_geral)
        frame_entrys.pack(side = 'right', fill = 'y')

        idped_var = tk.StringVar()
        tipo_var = tk.StringVar(value = "Saida")
        valor_var = tk.StringVar(value='0.0')
        situacao_var = tk.StringVar()
        detalhes_var = tk.StringVar()

        
        tipo_label = ttk.Label(frame_labels, text = 'Tipo')
        tipo_label.pack(pady = 5, anchor = 'w')
        valor_label = ttk.Label(frame_labels, text = 'Valor Total R$')
        valor_label.pack(pady = 10, anchor = 'w')
        situacao_label = ttk.Label(frame_labels, text = 'Situação atual')
        situacao_label.pack(pady = 5, anchor = 'w')
        detalhes_label = ttk.Label(frame_labels, text = 'Detalhes')
        detalhes_label.pack(pady = 5, anchor = 'w')

        def butao_tipo():
            if tipo_var.get() == "Entrada":
                tipo_var.set("Saida")
            elif tipo_var.get() == "Saida":
                tipo_var.set("Entrada")       

        
        tipo = ttk.Checkbutton(frame_entrys, width=12, textvariable = tipo_var,
                                command= butao_tipo, bootstyle= 'round-toggle' )
        tipo.pack(anchor='e', ipady=5)

        valor = ttk.Entry(frame_entrys, width = 12, textvariable= valor_var)
        valor.pack(anchor='e', pady=2)

        situacao = ttk.Combobox(frame_entrys, width = 12, textvariable= situacao_var)
        situacao.pack(anchor='e', pady=2)

        listas = ver_tipos()
        lista1, lista2 = listas
        situacao['value'] = lista2


        detalhe = ttk.Text(frame_entrys, width = 22,
                           height=8)
        detalhe.pack(anchor='e', pady=2)

        def confirmar():
            try:
                float(valor_var.get())
            except:
                adicionar_label.configure(text='Valores inválidos')
            else:
                if valor_var.get() == "0.0" or situacao_var.get() == "":
                    adicionar_label.configure(text="Os campos obrigatórios não podem estar em branco")
                else:
                    idped = '-'
                    descricao = (detalhe.get(1.0, 'end').rstrip().replace('\n', 'æ'))
                    if len(descricao) == 1:
                        descricao = ''
                    data = date.today().strftime("%d/%m/%Y")
                    rendimento = []
                    rendimento.append((idped, tipo_var.get(), valor_var.get(), situacao_var.get(), data, descricao))
                    add = df.add_rendimentos(rendimento)
                    if add == "cadastrado":
                        ver_rendimentos("Todos")

        botao_confirmar = ttk.Button(adicionar, text='confirmar', command=confirmar)
        botao_confirmar.pack(pady=10)


    def detalhes_rend():
        detalhes = tk.Toplevel()
        detalhes.geometry('530x325')
        
        detalhes_label = ttk.Label(detalhes, text='Informações detalhadas')
        detalhes_label.pack(pady=10)

        rend = ttk.Treeview(detalhes, columns=('ID','IDPED','TIPO',
                                                 'VALOR','SIT','DATA'),
                                                 show = 'headings',
                                                 height=2)
        colunas = [('ID','ID', 30),
               ('IDPED', 'ID Pedido', 70),
               ('TIPO','Tipo', 50),
               ('VALOR','Valor', 100),
               ('SIT','Situação', 100),
               ('DATA','Data', 100)]
        for column_name, heading_text, width in colunas:
            if column_name == 'VALOR':
                rend.column(column_name, anchor='w', width=width)
            else:
                rend.column(column_name, anchor='center', width=width)
            rend.heading(column_name, text=heading_text)

        rend.pack()
        descricao_label = ttk.Label(detalhes, text='Descrição do Rendimento')
        descricao_label.pack(pady=10)
        descricao = tk.Text(detalhes, height=10, width=56)
        descricao.pack()
        
        lista = df.ver_rendimentos('Todos')
        for i in range(len(lista)):
            if rendimentos_selecionados[0][0] == int(lista[i][0]):
                texto = f'{lista[i][0]},{lista[i][1]},{lista[i][2]},R$ {lista[i][3]},{lista[i][4]},{lista[i][5]}'
                texto_formatado = (texto.split(','))
                rend.insert(parent = '', index = 0, values = texto_formatado)
                
                descricao.insert(1.0, lista[i][6].replace('ǵ','\n'))
                descricao.configure(state='disabled')
                break
            else:
                pass
        botao_fechar = ttk.Button(detalhes, text='Fechar', command=lambda: detalhes.destroy())
        botao_fechar.pack(pady=10)
          

    def alterar_rend():

        # Abre tela para alterar pedidos
        # Chama função de alterar pedidos
        
        checkbtn = tk.BooleanVar(value = False)

        adicionar = ttk.Toplevel()
        adicionar.title('Alterar Rendimento')
        adicionar.geometry('405x400')

        adicionar_label = ttk.Label(adicionar, text='Alterar um rendimento')
        adicionar_label.pack(pady=10)

        frame_geral = ttk.Frame(adicionar)
        frame_geral.pack(padx=20)
        frame_labels = ttk.Frame(frame_geral)
        frame_labels.pack(side = 'left', fill='y',ipadx=10)
        frame_entrys = ttk.Frame(frame_geral)
        frame_entrys.pack(side = 'right')

        idrend_var = tk.StringVar()
        idped_var = tk.StringVar()
        tipo_var = tk.StringVar(value = "Saida")
        valor_var = tk.StringVar(value='0.0')
        situacao_var = tk.StringVar()
        data_var = tk.StringVar()
        detalhes_var = tk.StringVar()

        idrend_label = ttk.Label(frame_labels, text = 'Id Rendimento')
        idrend_label.pack(pady = 5, anchor = 'w')
        idped_label = ttk.Label(frame_labels, text = 'Id Pedido')
        idped_label.pack(pady = 5, anchor = 'w')
        tipo_label = ttk.Label(frame_labels, text = 'Tipo')
        tipo_label.pack(pady = 5, anchor = 'w')
        valor_label = ttk.Label(frame_labels, text = 'Valor Total R$')
        valor_label.pack(pady = 10, anchor = 'w')
        situacao_label = ttk.Label(frame_labels, text = 'Situação atual')
        situacao_label.pack(pady = 5, anchor = 'w')
        detalhes_label = ttk.Label(frame_labels, text = 'Detalhes')
        detalhes_label.pack(pady = 5, anchor = 'w')

        def checar_id(event):
            rendimento = df.ver_rendimentos('Todos')
            encontrado = False
            for i in range(len(rendimento)):
                if idrend.get() == rendimento[i][0]:
                    idped_var.set(f'{rendimento[i][1]}')
                    tipo_var.set(f'{rendimento[i][2]}')
                    if tipo_var.get() == "Saida":
                        checkbtn.set(False)
                        tipo.configure(variable=checkbtn,text="Saida")
                    else:
                        checkbtn.set(True)
                        tipo.configure(variable=checkbtn,text="Entrada")
                    valor_var.set(f'{rendimento[i][3]}')
                    situacao_var.set(f'{rendimento[i][4]}')
                    data_var.set(f'{rendimento[i][5]}')
                    detalhe.delete('1.0','end')
                    detalhe.insert('end',rendimento[i][6].replace('æ','\n'))
                    encontrado = True
                    break

            if not encontrado:
                idped_var.set(f'Não encontrado')
                checkbtn.set(False)
                tipo.configure(variable=checkbtn,text="Saida")
                valor_var.set(f'0.0')
                situacao_var.set(f'Não encontrado')
                data_var.set(f'0000-00-00')
                detalhes_var.set(f'Não encontrado')

        def butao_tipo():
            if checkbtn.get() == False:
                tipo_var.set("Saida")
                tipo.configure(text="Saida")
            elif checkbtn.get() == True:
                tipo_var.set("Entrada")
                tipo.configure(text="Entrada")

        idrend = ttk.Entry(frame_entrys, width=36, textvariable=idrend_var)
        idrend.pack(pady=5,anchor='e')

        idrend.bind('<KeyRelease>', lambda event: checar_id(event))
        
        idpedido = ttk.Entry(frame_entrys, width=36, textvariable=idped_var)
        idpedido.pack(pady=5,anchor='e')

        
        tipo = ttk.Checkbutton(frame_entrys, width=12, text="Saida",
                               variable= checkbtn,
                                 command= butao_tipo, bootstyle= 'round-toggle' )
        tipo.pack(anchor='e', ipady=5)

        valor = ttk.Entry(frame_entrys, width = 12, textvariable= valor_var)
        valor.pack(anchor='e', pady=2)

        situacao = ttk.Combobox(frame_entrys, width = 12, textvariable= situacao_var)
        situacao.pack(anchor='e', pady=2)

        listas = ver_tipos()
        lista1, lista2 = listas
        situacao['value'] = lista2

        detalhe = ttk.Text(frame_entrys, width = 22,
                           height=8)
        detalhe.pack(anchor='e', pady=2)   


        def confirmar():
            try:
                float(valor_var.get())
            except:
                adicionar_label.configure(text='Valores inválidos')
            else:
                if valor_var.get() == "0.0" or situacao_var.get() == "":
                    adicionar_label.configure(text="Os campos obrigatórios não podem estar em branco")
                else:
                    descricao = (detalhe.get(1.0, 'end').rstrip().replace('\n', 'æ'))
                    rendimento = []
                    rendimento.append((idrend_var.get(),idped_var.get(),tipo_var.get(),valor_var.get(), situacao_var.get(),data_var.get(), descricao))
                    att = df.alterar_rend(rendimento)
                    if att == "Alterado":
                        ver_rendimentos("Todos")


        botao_confirmar = ttk.Button(adicionar, text='confirmar', command=confirmar)
        botao_confirmar.pack(pady=10)
                
    def deletar():

        # Abre tela de confirmação
        # Para cancelar os pedidos selecionados

        delete = ttk.Toplevel()
        delete.title('Confirmar deleção')
        delete.geometry('530x325')

        aviso = ttk.StringVar(value = 'Os seguintes rendimentos serão deletados')
        aviso_label = ttk.Label(delete, textvariable=aviso)
        aviso_label.pack(pady=10)

        dados.bind('<<TreeviewSelect>>', lambda event: (rendimento_selecionado(), checar()))

        rendimentos = ttk.Treeview(delete, columns=('ID','IDPED','TIPO',
                                                'VALOR','SIT','DATA'),
                                                show = 'headings',
                                                height = 10)
        colunas = [('ID','ID', 30),
               ('IDPED', 'ID Pedido', 70),
               ('TIPO','Tipo', 100),
               ('VALOR','Valor', 100),
               ('SIT','Situação', 100),
               ('DATA','Data', 80)]
        for column_name, heading_text, width in colunas:
            if column_name == 'VALOR':
                rendimentos.column(column_name, anchor='w', width=width)
            else:
                rendimentos.column(column_name, anchor='center', width=width)
            rendimentos.heading(column_name, text=heading_text)
        rendimentos.pack()

        def checar():
            try:
                for i in rendimentos.get_children():
                    rendimentos.delete(i)
                rendimentos_selecionados.reverse()
                if len(rendimentos_selecionados) > 0:
                    for i in rendimentos_selecionados:
                        id, idped, tipo, valor, situa, data = i
                        texto_formatado = (id, idped, tipo, valor, situa, data)
                        rendimentos.insert(parent='', index=0, values= texto_formatado)
                        aviso.set('Os seguintes rendimentos serão deletados')
                else:
                    aviso.set('Nenhum rendimento selecionado')
            except NameError:
                aviso.set('Nenhum rendimento selecionado')

        def excluir_rend(rendimento):
            resultado = df.deletar_rendimento(rendimento)
            if resultado == "deletado":
                for i in rendimentos.get_children():
                    rendimentos.delete(i)
                ver_rendimentos()
                rendimentos_selecionados.clear()
                dados.selection_clear()
            
        botao_confirmar = ttk.Button(delete, text='confirmar',
                                    command=lambda: excluir_rend(rendimentos_selecionados))
        botao_confirmar.pack(pady=10)

        def fechar():
            dados.bind('<<TreeviewSelect>>', rendimento_selecionado)
            delete.destroy()
        delete.protocol("WM_DELETE_WINDOW", fechar)
        checar()
    
    
    def rendimento_selecionado(*args):
        if len(dados.selection()) == 0:
            botao_detalhes.pack_forget()
            return
        if botao_detalhes.winfo_viewable() == 1:
            botao_detalhes.pack_forget()
        if len(dados.selection()) == 1:
            botao_detalhes.pack(before=botao_relatorio,pady=2)
        global rendimentos_selecionados
        rendimentos_selecionados = []
        for i in dados.selection():
            rendimentos_selecionados.append(dados.item(i)['values'])
        def apagar(event):
            df.deletar_rendimentos(rendimentos_selecionados)
            for i in dados.selection():
                dados.delete(i)
        dados.bind('<KeyPress-Delete>', apagar)

        def verificar_evento(event):
            widget = event.widget
            if isinstance(widget,(ttk.Button,ttk.Treeview)):
                return
            for item in dados.selection():
                dados.selection_remove(item)
            botao_detalhes.pack_forget()
        rendimentos.bind('<Button-1>', verificar_evento)


    rendimentos = ttk.Toplevel() # Tela de Rendimentos
    rendimentos.title("Rendimentos - Anoriat") # Título da tela
    rendimentos.geometry('780x550')

    botoes_telas_frame = ttk.Frame(rendimentos)
    botoes_telas_frame.pack(pady = 10)

    #frame_funcoes = ttk.Frame(rendimentos)
    frame_funcoes = ttk.Frame(rendimentos)
    frame_funcoes.pack()
    frame_botoes_funcoes = ttk.Frame(frame_funcoes)
    frame_botoes_funcoes.pack(side='right', fill='y', padx=3)

    pesquisa_var = tk.StringVar(value='Pesquisar um rendimento')
    pesquisa = tk.Entry(frame_funcoes, textvariable=pesquisa_var, width=40)
    pesquisa.pack()
    pesquisa.bind('<Button-1>', ver_rendimentos)

    tipo_var = tk.StringVar(value='Selecione um Tipo')
    sel_tipo = ttk.Combobox(frame_botoes_funcoes, textvariable=tipo_var, width=23)
    sel_tipo.pack(side = 'top', pady=2)
    sel_tipo.bind('<<ComboboxSelected>>', ver_rendimentos)

    


    # Listagem Rendimentos

    dados = ttk.Treeview(frame_funcoes, columns=('ID','IDPED','TIPO',
                                                 'VALOR','SIT','DATA',
                                                 'DESC'),
                                                 show = 'headings',
                                                 height=30)
    colunas = [('ID','ID', 30),
               ('IDPED', 'ID Pedido', 70),
               ('TIPO','Tipo', 100),
               ('VALOR','Valor', 100),
               ('SIT','Situação', 100),
               ('DATA','Data', 80)]
    for column_name, heading_text, width in colunas:
        dados.column(column_name, anchor='center', width=width)
        dados.heading(column_name, text=heading_text)
    dados.pack(side='left', pady=10)
    dados.bind('<<TreeviewSelect>>', rendimento_selecionado)

    ver_rendimentos()

    def fechar(tela):
        if tela == 'home':
            home.deiconify()
            rendimentos.destroy()
        elif tela == 'clientes':
            tela_clientes()
            rendimentos.destroy()
        elif tela == 'produtos':
            tela_produtos()
            rendimentos.destroy()
        else:
            if isinstance(home, ttk.Toplevel):
                login.destroy()
            else:
                home.destroy()
     

    botao_home = ttk.Button(botoes_telas_frame, text = 'Início',
                            command = lambda: fechar('home'), width=15)
    botao_home.pack(side='left',padx=2)
    botao_clientes = ttk.Button(botoes_telas_frame, text = 'Clientes',
                            command = lambda: fechar('clientes'), width=15)
    botao_clientes.pack(side='left',padx=2)
    botao_produtos = ttk.Button(botoes_telas_frame, text='Produtos',
                                 command=lambda: fechar('produtos'), width=15)
    botao_produtos.pack(side='left', padx=2)

    
    botao_add = ttk.Button(frame_botoes_funcoes, text='Adicionar rendimento(s)',
                           command= add_rendimento,width=23)
    botao_add.pack(pady=2)
    
    botao_alterar = ttk.Button(frame_botoes_funcoes, text='Alterar rendimento(s)',
                               command= alterar_rend,width=23)
    botao_alterar.pack(pady=2)

    botao_deletar = ttk.Button(frame_botoes_funcoes, text='Deletar rendimento(s)',
                                command=deletar,width=23)
    botao_deletar.pack(pady=2)

    botao_detalhes = ttk.Button(frame_botoes_funcoes, text='Detalhes',
                                 command=detalhes_rend,width=23)

    botao_relatorio = ttk.Button(frame_botoes_funcoes, text='Exportar relatório',
                                 command=df.relatorio_rend,width=23)
    botao_relatorio.pack(pady=2)

    rendimentos.protocol("WM_DELETE_WINDOW", lambda: fechar(''))


def tela_produtos():

    def categorias():
        categoria = df.ver_produtos('Todas')
        lista = []
        for item in categoria:
            indice, nome, quant, categ, valor, desc = item
            if categ not in lista:
                lista.append(categ)

        lista.insert(0,'Todas')
        sel_categ['values'] = lista
        return lista

    def ver_produtos(*args):

        # Chama função de para visualizar os produtos
        # Existentes no banco de dados

        texto = df.ver_produtos(categoria_var.get())
        for i in dados.get_children():
            dados.delete(i)
        texto.reverse()
        for linha in texto:
            id, nome, quantd, categ, valor, desc = linha
            valor = f'R$ {valor}'
            texto_formatado = (id,nome,quantd,categ,valor)
            dados.insert(parent = '', index = 0, values = texto_formatado)
        categorias()

    def substituir_virgulas(valor):
        valor_novo = valor.replace(',', '.')
        return valor_novo

    def add_produto():

        # Onde o usuário preencherá os dados para adicionar um produto
        # Chama a função de adicionar um produto

        adicionar = ttk.Toplevel()
        adicionar.title('adicionar produto')
        adicionar.geometry('320x380')

        adicionar_label = ttk.Label(adicionar, text='Adicionar um produto')
        adicionar_label.pack(pady=10)

        frame_geral = ttk.Frame(adicionar)
        frame_geral.pack(padx=20)
        frame_labels = ttk.Frame(frame_geral)
        frame_labels.pack(side = 'left', fill='y',ipadx=10)
        frame_entrys = ttk.Frame(frame_geral)
        frame_entrys.pack(side = 'right')

        nome_var= tk.StringVar()
        quantd_var= tk.StringVar()
        categ_var= tk.StringVar()
        valor_var= tk.StringVar(value='0.0')
        valor_var.trace_add('write', lambda *args: valor_var.set(substituir_virgulas(valor_var.get())))

        nome_label = ttk.Label(frame_labels, text='Nome')
        nome_label.pack(pady=5,anchor='w')
        quant_label = ttk.Label(frame_labels, text='Quantidade')
        quant_label.pack(pady=10,anchor='w')
        categoria_label = ttk.Label(frame_labels, text='Categoria')
        categoria_label.pack(pady=5,anchor='w')
        valor_label = ttk.Label(frame_labels, text='Valor R$')
        valor_label.pack(pady=10,anchor='w')
        desc_label = ttk.Label(frame_labels, text= 'Descrição\n(Opicional)')
        desc_label.pack(pady=5,anchor='w')

        nome = ttk.Entry(frame_entrys, width=20, textvariable=nome_var)
        nome.pack(anchor='e')
        quant = ttk.Spinbox(frame_entrys, width=17, from_= 1, to = 9999, textvariable=quantd_var)
        quant.pack(pady=5,anchor='e')
        categoria = ttk.Combobox(frame_entrys, width=18, textvariable=categ_var)
        lista = categorias()
        if lista is not None:
            lista.remove(lista[0])
            categoria['value'] = lista
        categoria.pack(anchor='e')
        valor = ttk.Entry(frame_entrys, width=20, textvariable=valor_var)
        valor.pack(pady=5,anchor='e')
        desc = ttk.Text(frame_entrys, width = 20, height=10)
        desc.pack(anchor='e')

        def confirmar():
            try:
                int(quantd_var.get())
                float(valor_var.get())
            except:
                adicionar_label.configure(text='Valores inválidos')
            else:
                if nome_var.get() == "" or categ_var.get() == "":
                    adicionar_label.configure(text='Os campos obrigatórios não podem estar em branco')
                else:
                    quantidade = quantd_var.get()
                    if quantidade[0] == '0':
                        quantidade = quantidade.replace('0', '', 1)
                    produto = []
                    descricao = (desc.get(1.0, 'end').rstrip().replace('\n', 'ǵ'))
                    if len(descricao) == 1:
                        descricao = ''
                    produto.append((nome_var.get(),quantidade,categ_var.get(),valor_var.get(), descricao))
                    add = df.add_produtos(produto)
                    if add == 'cadastrado':
                        adicionar_label.configure(text='Produto cadastrado com sucesso')
                        ver_produtos()
        botao_confirmar = ttk.Button(adicionar, text='confirmar', command=confirmar)
        botao_confirmar.pack(pady=10)

    def detalhes():
        detalhes = tk.Toplevel()
        detalhes.geometry('470x325')
        detalhes.title('Produto - Informações detalhadas')
        
        detalhes_label = ttk.Label(detalhes, text='Informações detalhadas')
        detalhes_label.pack(pady=10)

        produto = ttk.Treeview(detalhes, columns=('ID','Nome','Quantidade',
                                            'Categoria','Valor'),
                                            show = 'headings',
                                            height = 1)
        colunas = [('ID', 'ID', 30),
            ('Nome', 'Nome', 150),
            ('Quantidade', 'Quantidade', 80),
            ('Categoria', 'Categoria', 100),
            ('Valor', 'Valor', 100)]
        for column_name, heading_text, width in colunas:
            if column_name == 'VALOR':
                produto.column(column_name, anchor='w', width=width)
            else:
                produto.column(column_name, anchor='center', width=width)
            produto.heading(column_name, text=heading_text)

        produto.pack()
        descricao_label = ttk.Label(detalhes, text='Descrição do produto')
        descricao_label.pack(pady=10)
        descricao = tk.Text(detalhes, height=10, width=64)
        descricao.pack()
        
        lista = df.ver_produtos('Todas')
        
        for i in range(len(lista)):
            if produtos_selecionados[0][0] == int(lista[i][0]):
                texto = f'{lista[i][0]},{lista[i][1]},{lista[i][2]},{lista[i][3]},R$ {lista[i][4]}'
                texto_formatado = (texto.split(','))
                produto.insert(parent = '', index = 0, values = texto_formatado)
                
                descricao.insert(1.0, lista[i][5].replace('ǵ','\n'))
                descricao.configure(state='disabled')
                break
        botao_fechar = ttk.Button(detalhes, text='Fechar', command=lambda: detalhes.destroy())
        botao_fechar.pack(pady=10)
    
    def produto_selecionado(*args):
        if len(dados.selection()) == 0:
            botao_detalhes.pack_forget()
            return
        if botao_detalhes.winfo_viewable() == 1:
            botao_detalhes.pack_forget()
        if len(dados.selection()) == 1:
            botao_detalhes.pack(before=botao_relatorio,pady=2)
        global produtos_selecionados
        produtos_selecionados = []
        for i in dados.selection():
            produtos_selecionados.append(dados.item(i)['values'])
        def apagar(event):
            df.deletar_produto(produtos_selecionados)
            for i in dados.selection():
                dados.delete(i)
        dados.bind('<KeyPress-Delete>', apagar)

        def verificar_evento(event):
            widget = event.widget
            if isinstance(widget,(ttk.Button,ttk.Treeview)):
                return
            for item in dados.selection():
                dados.selection_remove(item)
            botao_detalhes.pack_forget()
        produtos.bind('<Button-1>', verificar_evento)

    def deletar():

        # Abre tela de confirmação
        # Para deletar os produtos selecionados
        apagar = True
        delete = ttk.Toplevel()
        delete.title('Confirmar deleção')
        delete.geometry('470x260')

        aviso = ttk.StringVar(value = 'Os seguintes produtos serão deletados')
        aviso_label = ttk.Label(delete, textvariable=aviso)
        aviso_label.pack(pady=10)

        dados.bind('<<TreeviewSelect>>', lambda event: (produto_selecionado(), checar()))

        produtos = ttk.Treeview(delete, columns=('ID','Nome','Quantidade','Categoria','Valor'), show = 'headings', height = 10)
        colunas = [('ID', 'ID', 30),
            ('Nome', 'Nome', 150),
            ('Quantidade', 'Quantidade', 80),
            ('Categoria', 'Categoria', 100),
            ('Valor', 'Valor', 100)]
        for column_name, heading_text, width in colunas:
            if column_name == 'VALOR':
                produtos.column(column_name, anchor='w', width=width)
            else:
                produtos.column(column_name, anchor='center', width=width)
            produtos.heading(column_name, text=heading_text)
        produtos.pack()
        def checar():
            try:
                for i in produtos.get_children():
                    produtos.delete(i)
                produtos_selecionados.reverse()
                if len(produtos_selecionados) > 0:
                    for i in produtos_selecionados:
                        id, nome, quantd, categ, valor = i
                        texto_formatado = (id,nome,quantd,categ,valor)
                        produtos.insert(parent = '', index = 0, values = texto_formatado)
                        aviso.set('Os seguintes produtos serão deletados')
                else:
                    aviso.set('Nenhum produto selecionado')
            except NameError:
                aviso.set('Nenhum produto selecionado')
        def excluir_produto(produto):
            resultado = df.deletar_produto(produto)
            if resultado == "deletado":
                for i in produtos.get_children():
                    produtos.delete(i)
                ver_produtos()
                produtos_selecionados.clear()
                dados.selection_clear()

        botao_confirmar = ttk.Button(delete, text='confirmar',
                                    command=lambda: excluir_produto(produtos_selecionados))
        botao_confirmar.pack(pady=10)
        def fechar():
            dados.bind('<<TreeviewSelect>>', produto_selecionado)
            delete.destroy()
        delete.protocol("WM_DELETE_WINDOW", fechar)
        checar()

    def alterar_produto():

        # Abre tela para alterar produtos
        # Chama função de alterar produtos

        alterar = ttk.Toplevel()
        alterar.title('alterar produto')
        alterar.geometry('320x430')

        alterar_label = ttk.Label(alterar, text='Alterar um produto')
        alterar_label.pack(pady=10)

        frame_geral = ttk.Frame(alterar)
        frame_geral.pack(padx=20)
        frame_labels = ttk.Frame(frame_geral)
        frame_labels.pack(side = 'left', fill='y',ipadx=10)
        frame_entrys = ttk.Frame(frame_geral)
        frame_entrys.pack(side = 'right')

        id_var = tk.StringVar()
        id_label = tk.Label(frame_labels, text='ID do produto')
        id_label.pack(pady=10,anchor='w')
        id_entry = ttk.Entry(frame_entrys, width=20, textvariable=id_var)
        id_entry.pack(pady=5,anchor='e')
        
        id_entry.bind('<KeyRelease>', lambda event: checar_id(event))

        nome_var= tk.StringVar()
        quantd_var= tk.IntVar()
        categ_var= tk.StringVar()
        valor_var= tk.StringVar(value='0.0')
        valor_var.trace_add('write', lambda *args: valor_var.set(substituir_virgulas(valor_var.get())))

        def checar_id(event):
            alterar_label.configure(text='Alterar um produto')
            produtos = df.ver_produtos('Todas')
            
            encontrado = False
            for i in range(len(produtos)):
                if id_var.get() == produtos[i][0]:
                    nome_var.set(f'{produtos[i][1]}')
                    quantd_var.set(produtos[i][2])
                    categ_var.set(f'{produtos[i][3]}')
                    valor_var.set(produtos[i][4])
                    desc.delete('1.0', 'end')
                    desc.insert('end', produtos[i][5].replace('ǵ','\n'))
                    encontrado = True
                    break
            
            if not encontrado:
                nome_var.set('Não encontrado')
                quantd_var.set(0)
                categ_var.set('Não encontrado')
                valor_var.set('0.0')

        nome_label = ttk.Label(frame_labels, text='Nome')
        nome_label.pack(pady=5,anchor='w')
        quant_label = ttk.Label(frame_labels, text='Quantidade')
        quant_label.pack(pady=10,anchor='w')
        categoria_label = ttk.Label(frame_labels, text='Categoria')
        categoria_label.pack(pady=5,anchor='w')
        valor_label = ttk.Label(frame_labels, text='Valor R$')
        valor_label.pack(pady=10,anchor='w')
        desc_label = ttk.Label(frame_labels, text= 'Descrição\n(Opicional)')
        desc_label.pack(pady=5,anchor='w')

        nome = ttk.Entry(frame_entrys, width=20, textvariable=nome_var)
        nome.pack(anchor='e')
        quant = ttk.Spinbox(frame_entrys, width=17, from_= 1, to = 9999, textvariable=quantd_var)
        quant.pack(pady=5,anchor='e')
        categoria = ttk.Combobox(frame_entrys, width=18, textvariable=categ_var)
        lista = categorias()
        if lista is not None:
            lista.remove(lista[0])
            categoria['value'] = lista
        categoria.pack(anchor='e')
        valor = ttk.Entry(frame_entrys, width=20, textvariable=valor_var)
        valor.pack(pady=5,anchor='e')
        desc = ttk.Text(frame_entrys, width = 20, height=10)
        desc.pack(anchor='e')

        def confirmar():
            try:
                quantd_var.get()
                float(valor_var.get())
            except:
                alterar_label.configure(text='Valores inválidos')
            else:
                descricao = (desc.get(1.0, 'end').replace('\n','ǵ'))
                if len(descricao) == 1:
                    descricao = ''
                produto = []
                produto.append((id_var.get(),nome_var.get(),quantd_var.get(),categ_var.get(),valor_var.get(),descricao))
                s = df.alterar_produtos(produto)
                if s == 'alterado':
                    alterar_label.configure(text='Alterado')
                    ver_produtos()
        
        botao_confirmar = ttk.Button(alterar, text='confirmar',
                                     command=confirmar)
        botao_confirmar.pack(pady=15)

    def pesquisar(event):
        if pesquisa_var.get() == 'Pesquisar um produto':
            pesquisa_var.set('')
        pesquisa.bind('<KeyRelease>', pesquisar)
        for i in dados.get_children():
            dados.delete(i)
        categorias()
        parametro = pesquisa_var.get().lower()
        texto = df.ver_produtos('Todas')
        texto.reverse()
        for i in range(len(texto)):
            for x in range(1,6):
                if texto[i][x].lower().__contains__(parametro):
                    text= f'{texto[i][0]},{texto[i][1]},{texto[i][2]},{texto[i][3]},R$ {texto[i][4]}'
                    texto_formatado = (text.split(','))
                    dados.insert(parent = '', index = 0, values = texto_formatado)
                    break
    
    
    produtos = ttk.Toplevel()  # tela de produtos
    produtos.title("Produtos - Anoriat")  # título da tela
    produtos.geometry('700x550')
    produtos.geometry(f"+{x-200}+{y-150}")

    botoes_telas_frame = ttk.Frame(produtos)
    botoes_telas_frame.pack(pady=10)

    #visualizar_frame = ttk.Frame(produtos)
    #visualizar_frame.pack()

    frame_funcoes = ttk.Frame(produtos)
    frame_funcoes.pack()
    frame_botoes_funcoes = ttk.Frame(frame_funcoes)
    frame_botoes_funcoes.pack(side='right',fill='y')

    pesquisa_var = tk.StringVar(value='Pesquisar um produto')
    pesquisa = tk.Entry(frame_funcoes, textvariable=pesquisa_var, width= 40)
    pesquisa.pack()
    pesquisa.bind('<Button-1>', pesquisar)

    def expandir_categorias(event):
        sel_categ.event_generate('<Down>')
        sel_categ.bind('<<ComboboxSelected>>', ver_produtos)
    categoria_var = tk.StringVar(value = 'Selecione uma categoria')
    sel_categ = ttk.Combobox(frame_botoes_funcoes, textvariable=categoria_var, width=23)
    sel_categ.pack(side = 'top')
    sel_categ.bind('<Button-1>', expandir_categorias)
    # Listagem produtos
    dados = ttk.Treeview(frame_funcoes, columns=('ID','Nome','Quantidade',
                                            'Categoria','Valor'),
                                            show = 'headings',
                                            height = 30)
    colunas = [('ID', 'ID', 30),
        ('Nome', 'Nome', 150),
        ('Quantidade', 'Quantidade', 80),
        ('Categoria', 'Categoria', 100),
        ('Valor', 'Valor', 100)]
    for column_name, heading_text, width in colunas:
        if column_name == 'VALOR':
            dados.column(column_name, anchor='w', width=width)
        else:
            dados.column(column_name, anchor='center', width=width)
        dados.heading(column_name, text=heading_text)
    dados.pack(side='left',pady=10)
    dados.bind('<<TreeviewSelect>>', produto_selecionado )

    ver_produtos()

    def fechar(tela):
        if tela == 'home':
            home.deiconify()
            produtos.destroy()
        elif tela == 'clientes':
            tela_clientes()
            produtos.destroy()
        elif tela == 'pedidos':
            tela_pedidos()
            produtos.destroy()
        elif tela == 'rendimentos':
            tela_rendimentos()
            produtos.destroy()
        else:
            login.destroy()

    botao_home = ttk.Button(botoes_telas_frame, text = 'Início',
                            command = lambda: fechar('home'),width=12)
    botao_home.pack(side='left', padx=2)
    botao_clientes = ttk.Button(botoes_telas_frame, text = 'Clientes',
                            command = lambda: fechar('clientes'),width=12)
    botao_clientes.pack(side='left', padx=2)
    botao_pedidos = ttk.Button(botoes_telas_frame,text='Pedidos',
                               command=lambda: fechar('pedidos'),width=12)
    botao_pedidos.pack(side='left', padx=2)
    botao_rendimentos = ttk.Button(botoes_telas_frame, text='Rendimentos',
                                   command=lambda: fechar('rendimentos'), width=12)
    botao_rendimentos.pack(side='left', padx=2)
    botao_add = ttk.Button(frame_botoes_funcoes, text='Adicionar produto(s)',
                           command=add_produto,width=17)
    botao_add.pack(pady=2)
    
    botao_alterar = ttk.Button(frame_botoes_funcoes, text='Alterar produto(s)',
                               command=alterar_produto,width=17)
    botao_alterar.pack(pady=2)

    botao_deletar = ttk.Button(frame_botoes_funcoes, text='Deletar produto(s)', command=deletar,width=17)
    botao_deletar.pack(pady=2)

    botao_detalhes = ttk.Button(frame_botoes_funcoes, text='Detalhes', command=detalhes,width=17)

    botao_relatorio = ttk.Button(frame_botoes_funcoes, text='Exportar relatório',
                                 command=df.relatorio_produtos,width=17)
    botao_relatorio.pack(pady=2)
    produtos.protocol("WM_DELETE_WINDOW", lambda: fechar(''))


def tela_clientes():
    
    def ver_clientes():
        texto = df.ver_clientes()
        for i in dados.get_children():
            dados.delete(i)
        texto.reverse()
        for linha in texto:
            id, nome, sobrenome, cpfnj, telefone = linha
            if len(cpfnj) == 11:
                cpfnj = f'{cpfnj[0:3]}.{cpfnj[3:6]}.{cpfnj[6:9]}-{cpfnj[9:]}'
            else:
                cpfnj = f'{cpfnj[:2]}.{cpfnj[2:5]}.{cpfnj[5:8]}/{cpfnj[8:12]}-{cpfnj[12:]}'
            if len(telefone) == 11:
                telefone = f'({telefone[0:2]}) {telefone[2:7]}-{telefone[7:]}'
            else:
                telefone = f'({telefone[0:2]}) {telefone[2:6]}-{telefone[6:]}'

            texto_formatado = (id, nome, sobrenome, cpfnj, telefone)
            dados.insert(parent = '', index = 0, values = texto_formatado)
            

    def cliente_selecionado(*args):
        global clientes_selecionados
        clientes_selecionados = []
        for i in dados.selection():
            clientes_selecionados.append(dados.item(i)['values'])
        def apagar(event):
            df.deletar_cliente(clientes_selecionados)
            for i in dados.selection():
                dados.delete(i)
        dados.bind('<KeyPress-Delete>', apagar)


    def formatar_documento(documento,telefone):
            if '.' in documento:
                documento = documento.replace('.', '')
            if '-' in documento:
                documento = documento.replace('-', '')
            if '/' in documento:
                documento = documento.replace('/', '')

            if '(' in telefone:
                telefone = telefone.replace('(', '')
            if ')' in telefone:
                telefone = telefone.replace(')', '')
            if '-' in telefone:
                telefone = telefone.replace('-', '')

            telefone = telefone.rstrip()
            documento = documento.rstrip()

            return documento, telefone


    def add_cliente():
        adicionar = ttk.Toplevel()
        adicionar.title('Adicionar Cliente')
        adicionar.geometry('320x230')

        label = ttk.Label(master = adicionar, text = 'Adicionar um cliente')
        label.pack(pady = 10)

        frame_geral = ttk.Frame(adicionar)
        frame_geral.pack(padx=20)

        labels_frame = ttk.Frame(frame_geral)
        labels_frame.pack(side='left',fill='y',ipadx=10)

        entry_frames  = ttk.Frame(frame_geral)
        entry_frames.pack(side='right',fill='y')

        nome_label = ttk.Label(labels_frame, text = 'Nome')
        nome_label.pack(pady=8,anchor='w')
        sobrenome_label = ttk.Label(labels_frame, text = 'Sobrenome')
        sobrenome_label.pack(pady=4,anchor='w')
        cpfnj_label = ttk.Label(labels_frame, text = 'CPF/CNPJ')
        cpfnj_label.pack(pady=8,anchor='w')
        tel_label = ttk.Label(labels_frame, text = 'Telefone/Celular')
        tel_label.pack(pady=5,anchor='w')

        nome_var = tk.StringVar()
        sobrenome_var = tk.StringVar()
        cpfnj_var = tk.StringVar()
        tel_var = tk.StringVar()

        nome = ttk.Entry(entry_frames, width = 20, textvariable = nome_var)
        nome.pack(pady=3,anchor='e')
        sobrenome = ttk.Entry(entry_frames, width = 20, textvariable = sobrenome_var)
        sobrenome.pack(anchor='e')
        cpfnj = ttk.Entry(entry_frames, width = 20, textvariable = cpfnj_var)
        cpfnj.pack(pady=3,anchor='e')
        tel = ttk.Entry(entry_frames, width = 20, textvariable = tel_var)
        tel.pack(anchor='e')
                
        def confirmar():
            try:
                resultado = formatar_documento(cpfnj_var.get(), tel_var.get())
                if resultado is None:
                    return
            except:
                label.configure(text='Documento ou telefone inválido')
            else:
                documento, telefone = resultado
                if not documento.isdigit() or not telefone.isdigit():
                    label.configure(text='Documento ou telefone inválido')
                else:
                    if len(documento) != 11 and len(documento) != 14:
                        label.configure(text='Documento inválido')
                        return
                    elif len(telefone) != 9 and len(telefone) != 8 and len(telefone) != 11 and len(telefone) != 10:
                        label.configure(text='Número de telefone inválido')
                        return
                    else:
                        telefones = df.verificar_telefone(telefone)
                        if telefones == 'DDD':
                            label.configure(text='Celular deve conter o DDD')
                            return
                        elif telefones == 'invalidoT':
                            label.configure(text='Telefone Inválido')
                            return
                        elif telefones == 'invalidoC':
                            label.configure(text='Celular Inválido')
                            return
                    if len(documento) == 11:
                        if not df.verificar_documento(documento):
                            label.configure(text='CPF inválido')
                            return
                            
                    if len(documento) == 14:
                        if not df.verificar_documento(documento):
                            label.configure(text='CNPJ inválido')
                            return
                            
                nome_ = nome_var.get()
                sobrenome_ = sobrenome_var.get()
                if nome_ == '' or sobrenome_ == '':
                    label.configure(text='Os campos obrigatórios devem ser preenchidos')
                else:
                    cliente = []
                    cliente.append((nome_,sobrenome_,documento,telefone))
                    add = df.add_clientes(cliente)
                    if add == 'ja existente':
                        if len(documento) == 11:
                            label.configure(text='CPF já cadastrado')
                        else:
                            label.configure(text='CNPJ já cadastrado')
                        return
                    elif add == 'cadastrado':
                        label.configure(text='Cliente cadastrado com sucesso')
                        ver_clientes()
        botao_confirmar = ttk.Button(adicionar, text='confirmar', command=confirmar)
        botao_confirmar.pack(pady=15)


    def deletar():
        
        # Abre tela de confirmação
        # Para deletar os produtos selecionados

        delete = ttk.Toplevel()
        delete.title('Confirmar deleção')
        delete.geometry('480x270')

        aviso = ttk.StringVar(value = 'Os seguintes clientes serão apagados')
        aviso_label = ttk.Label(delete, textvariable=aviso)
        aviso_label.pack(pady=10)

        dados.bind('<<TreeviewSelect>>', lambda event: (cliente_selecionado(), checar()))
        cliente = ttk.Treeview(delete, columns = ('ID', 'Nome', 'Sobrenome',
                                               'CPF/CNPJ', 'Telefone/Celular'),
                                               show = 'headings',
                                               height = 10)
        colunas = [('ID', 'ID', 30),
        ('Nome', 'Nome', 100),
        ('Sobrenome', 'Sobrenome', 100),
        ('CPF/CNPJ', 'CPF/CNPJ', 130),
        ('Telefone/Celular', 'Telefone/Celular', 110)]
        for column_name, heading_text, width in colunas:
            cliente.column(column_name, anchor='center', width=width)
            cliente.heading(column_name, text=heading_text)
        cliente.pack()

        def checar():
            try:
                for i in cliente.get_children():
                    cliente.delete(i)
                clientes_selecionados.reverse()
                if len(clientes_selecionados) > 0:
                    for i in clientes_selecionados:
                        id, nome, sobren, cpfnj, tel = i
                        texto_formatado = (id,nome,sobren,cpfnj,tel)
                        cliente.insert(parent = '', index = 0, values = texto_formatado)
                        aviso.set('Os seguintes clientes serão apagados')
                else:
                    aviso.set('Nenhum cliente selecionado')
            except NameError:
                aviso.set('Nenhum cliente selecionado')
        checar()

        def excluir_cliente(clientes):

            # Chama função de exclusão
            resultado = df.deletar_cliente(clientes)
            if resultado == "deletado":
                for i in cliente.get_children():
                    cliente.delete(i)
                aviso.set("Clientes apagados com sucesso")
                ver_clientes()

        botao_confirmar = ttk.Button(delete, text='confirmar',
                                    command=lambda: excluir_cliente(clientes_selecionados))
        botao_confirmar.pack(pady=10)
        def fechar():
            dados.bind('<<TreeviewSelect>>', cliente_selecionado)
            delete.destroy()
        delete.protocol("WM_DELETE_WINDOW", fechar)


    def alterar_cliente():
        alterar = ttk.Toplevel()
        alterar.title('alterar cliente')
        alterar.geometry('320x280')

        label = ttk.Label(alterar, text='Alterar cadastro de um cliente')
        label.pack(pady=10)

        frame_geral = ttk.Frame(alterar)
        frame_geral.pack(padx=20)

        labels_frame = ttk.Frame(frame_geral)
        labels_frame.pack(side='left',fill='y',ipadx=10)

        entry_frames  = ttk.Frame(frame_geral)
        entry_frames.pack(side='right',fill='y')

        cpfid_var = tk.StringVar()
        cpfid_label = tk.Label(labels_frame, text='CPF/CNPJ\nou\nID do cliente')
        cpfid_label.pack(pady=5,anchor='w')
        cpfid_entry = ttk.Entry(entry_frames, width=20, textvariable=cpfid_var)
        cpfid_entry.pack(pady=14,anchor='e')
        cpfid_entry.bind('<KeyRelease>', lambda event: checar_id(event))

        nome_var = tk.StringVar()
        sobrenome_var = tk.StringVar()
        cpfnj_var = tk.StringVar()
        tel_var = tk.StringVar()

        def checar_id(event):
            label.configure(text='Alterar um cliente')
            clientes = df.ver_clientes()
            encontrado = False
            for i in range(len(clientes)):
                if cpfid_var.get() == clientes[i][0] or cpfid_var.get() == clientes[i][3]:
                    nome_var.set(f'{clientes[i][1]}')
                    sobrenome_var.set(clientes[i][2])
                    documento = clientes[i][3]
                    if len(documento) == 11:
                        documento = f'{documento[0:3]}.{documento[3:6]}.{documento[6:9]}-{documento[9:]}'
                    else:
                        documento = f'{documento[:2]}.{documento[2:5]}.{documento[5:8]}/{documento[8:12]}-{documento[12:]}'
                    
                    cpfnj_var.set(documento)
                    telefone = clientes[i][4]
                    if len(telefone) == 11:
                        telefone = f'({telefone[0:2]}) {telefone[2:7]}-{telefone[7:]}'
                    else:
                        telefone = f'({telefone[0:2]}) {telefone[2:6]}-{telefone[6:]}'
                    tel_var.set(telefone)
                    encontrado = True
                    break
            
            if not encontrado:
                nome_var.set('Não encontrado')
                sobrenome_var.set('Não encontrado')
                cpfnj_var.set('Não encontrado')
                tel_var.set('Não encontrado')

        nome_label = ttk.Label(labels_frame, text='Nome')
        nome_label.pack(pady=7,anchor='w')
        sobrenome_label = ttk.Label(labels_frame, text='Sobrenome')
        sobrenome_label.pack(pady=7,anchor='w')
        cpfnj_label = ttk.Label(labels_frame, text='CPF/CNPJ')
        cpfnj_label.pack(pady=7,anchor='w')
        tel_label = ttk.Label(labels_frame, text='Telefone')
        tel_label.pack(pady=5,anchor='w')

        nome = ttk.Entry(entry_frames, width=20, textvariable=nome_var)
        nome.pack(pady=3,anchor='e')
        sobrenome = ttk.Entry(entry_frames, width=20, textvariable=sobrenome_var)
        sobrenome.pack(anchor='e')
        cpfnj = ttk.Entry(entry_frames, width=20, textvariable=cpfnj_var)
        cpfnj.pack(pady=3,anchor='e')
        tel = ttk.Entry(entry_frames, width=20, textvariable=tel_var)
        tel.pack(anchor='e')

        def confirmar():
            try:
                resultado = formatar_documento(cpfnj_var.get(), tel_var.get())
                if resultado is None:
                        return
            except:
                label.configure(text='Documento ou telefone inválido')
            else:
                documento, telefone = resultado
                if not documento.isdigit() or not telefone.isdigit():
                    label.configure(text='Documento ou telefone inválido')
                else:
                    if len(documento) != 11 and len(documento) != 14:
                        label.configure(text='Documento inválido')
                        return
                    elif len(telefone) != 9 and len(telefone) != 8 and len(telefone) != 11:
                        label.configure(text='Número de telefone inválido')
                        return
                    else:
                        telefones = df.verificar_telefone(telefone)
                        if telefones == 'DDD':
                            label.configure(text='Celular deve conter o DDD')
                            return
                        elif telefones == 'invalidoT':
                            label.configure(text='Telefone Inválido')
                            return
                        elif telefones == 'invalidoC':
                            label.configure(text='Celular Inválido')
                            return
                    if len(documento) == 11:
                        if not df.verificar_documento(documento):
                            label.configure(text='CPF inválido')
                            return
                            
                    if len(documento) == 14:
                        if not df.verificar_documento(documento):
                            label.configure(text='CNPJ inválido')
                            return
                            
                    
                nome_ = nome_var.get()
                sobrenome_ = sobrenome_var.get()
                if nome_ == '' or sobrenome_ == '':
                    label.configure(text='Os campos obrigatórios devem ser preenchidos')
                else:
                    cliente = []
                    cliente.append((cpfid_var.get(),nome_,sobrenome_,documento,telefone))
                    alterar = df.alterar_clientes(cliente)
                    if alterar == 'ja existente':
                        if len(documento) == 11:
                            label.configure(text='CPF já cadastrado')
                        else:
                            label.configure(text='CNPJ já cadastrado')
                        return
                    elif alterar == 'alterado':
                        label.configure(text='Cliente alterado com sucesso')
                        ver_clientes()
        botao_confirmar = ttk.Button(alterar, text='confirmar',
                                     command=confirmar)
        botao_confirmar.pack(pady=15)


    def pesquisar(event):
        if pesquisa_var.get() == 'Pesquisar um cliente':
            pesquisa_var.set('')
        pesquisa.bind('<KeyRelease>', pesquisar)
        for i in dados.get_children():
            dados.delete(i)
        parametro = pesquisa_var.get().lower()
        texto = df.ver_clientes()
        texto.reverse()
        for i in range(len(texto)):
            for x in range(1,5):
                if texto[i][x].lower().__contains__(parametro):
                    text= f'{texto[i][0]},{texto[i][1]},{texto[i][2]},{texto[i][3]},{texto[i][4]}'
                    texto_formatado = (text.split(','))
                    dados.insert(parent = '', index = 0, values = texto_formatado)
                    break
    
    clientes = ttk.Toplevel() # tela de clientes
    clientes.title("Clientes - Anoriat") # título da tela
    clientes.geometry('700x550')
    clientes.geometry(f"+{x-200}+{y-150}")

    botoes_telas_frame = ttk.Frame(clientes)
    botoes_telas_frame.pack(pady=10)

    frame_funcoes = ttk.Frame(clientes)
    frame_funcoes.pack()
    botoes_telas_funcoes = ttk.Frame(frame_funcoes)
    botoes_telas_funcoes.pack(pady=28,padx=20,side='right',fill='y') 

    pesquisa_var = tk.StringVar(value='Pesquisar um cliente')
    pesquisa = tk.Entry(frame_funcoes, textvariable=pesquisa_var, width= 40)
    pesquisa.pack()
    pesquisa.bind('<Button-1>', pesquisar)

    # Listagem de Clientes
    dados = ttk.Treeview(frame_funcoes, columns = ('ID', 'Nome', 'Sobrenome',
                                               'CPF/CNPJ', 'Telefone/Celular'),
                                               show = 'headings',
                                               height = 40)
    colunas = [('ID', 'ID', 30),
        ('Nome', 'Nome', 100),
        ('Sobrenome', 'Sobrenome', 100),
        ('CPF/CNPJ', 'CPF/CNPJ', 130),
        ('Telefone/Celular', 'Telefone/Celular', 110)]
    for column_name, heading_text, width in colunas:
        dados.column(column_name, anchor='center', width=width)
        dados.heading(column_name, text=heading_text)
    dados.pack(side='left', pady=10)
    dados.bind('<<TreeviewSelect>>', cliente_selecionado)
    ver_clientes()

    botao_add = ttk.Button(botoes_telas_funcoes, text = 'Adicionar Cliente(s)',
                           command=add_cliente, width=20)
    
    botao_add.pack(side='top',pady=2)

    botao_deletar = ttk.Button(botoes_telas_funcoes, text = 'Deletar Cliente(s)',
                               command=deletar, width=20)
    botao_deletar.pack(pady=2)

    botao_alterar = ttk.Button(botoes_telas_funcoes, text='Alterar Cliente(s)',
                               command=alterar_cliente, width=20)
    botao_alterar.pack(pady=2)

    botao_relatorio = ttk.Button(botoes_telas_funcoes, text = 'Exportar Relatório',
                                 command=df.relatorio_clientes, width=20)
    botao_relatorio.pack(pady=2)

    def fechar(tela):
        if tela == 'home':
            home.deiconify()
            clientes.destroy()
        elif tela == 'produtos':
            tela_produtos()
            clientes.destroy()
        elif tela == 'pedidos':
            tela_pedidos()
            clientes.destroy()
        elif tela == 'rendimentos':
            tela_rendimentos()
            clientes.destroy()
        else:
            login.destroy()

    botao_home = ttk.Button(botoes_telas_frame, text = 'Início',
                            command = lambda: fechar('home'),
                            width=12)
    botao_home.pack(side='left', padx=2)
    botao_pedidos = ttk.Button(botoes_telas_frame, text='Pedidos',
                               command=lambda: fechar('pedidos'), width=12)
    botao_pedidos.pack(side='left', padx=2)
    botao_produtos = ttk.Button(botoes_telas_frame, text = 'Produtos',
                            command = lambda: fechar('produtos'),
                            width=12)
    botao_produtos.pack(side='left', padx=2)
    botao_rendimentos = ttk.Button(botoes_telas_frame, text='Rendimentos',
                                   command=lambda: fechar('rendimentos'), width=12)
    botao_rendimentos.pack(side='left', padx=2)
    clientes.protocol("WM_DELETE_WINDOW", lambda: fechar(''))


def tela_home():
    global home
    home = ttk.Toplevel()  # tela de inicio do programa, apos o login
    home.title("Início - Anoriat")  # título da tela
    home.geometry('400x250')
    home.geometry(f"+{x}+{y}")

    label = ttk.Label(home, text='Início do programa anoriat')
    label.pack()
    label1 = ttk.Label(home, text='Aqui você pode ver as credenciais cadastradas e editar seu conteudo')
    label1.pack()
    def trocar_tema():
        if login.style.theme.type == 'dark':
            login.style.theme_use("cosmo")
            botao_tema.configure(text='Claro')
            df.trocar_tema('dark')
        else:
            login.style.theme_use("darkly")
            botao_tema.configure(text='Escuro')
            df.trocar_tema('light')
    def botao_produtos():
        home.withdraw()
        tela_produtos()
    def botao_clientes():
        home.withdraw()
        tela_clientes()
    def botao_pedidos():
        home.withdraw()
        tela_pedidos()
    def botao_rendi():
        home.withdraw()
        tela_rendimentos()
    def botao_deslogar():
        home.destroy()
        deslogar = df.deslogar()
        if deslogar:
            login.deiconify()
    # abre tela de produtos
    botao_cliente = ttk.Button(home, text='Clientes', command=botao_clientes, width=12)
    botao_cliente.pack(pady=2)
    botao_pedido = ttk.Button(home, text= 'Pedidos', command=botao_pedidos, width=12)
    botao_pedido.pack(pady=2)
    botao_produto = ttk.Button(home, text="Produtos", command=botao_produtos, width=12)
    botao_produto.pack(pady=2)
    botao_rend = ttk.Button(home, text= 'Rendimentos', command=botao_rendi, width=12)
    botao_rend.pack(pady=2)
    botao_sair = ttk.Button(home,text='Deslogar',command=botao_deslogar,width=12,bootstyle="danger-outline")
    botao_sair.pack(pady=2)
    botao_tema = ttk.Checkbutton(home, text= 'Escuro', command = trocar_tema, width=12, bootstyle='round-toggle')
    botao_tema.pack(pady=15, anchor='se')
    def fechar():
        login.destroy()
    home.protocol("WM_DELETE_WINDOW", fechar)
       

def tela_login(prioridade,tema):
    global login
    global x
    global y
    login = ttk.Window()  # tela de login
    login.eval('tk::PlaceWindow . center')
    login.style.theme_use(f"{tema}")
    login.title("Login - Anoriat")  # titulo da tela
    login.geometry('300x200')

    titulo = tk.Label(login,
                    text="Login - Anoriat",
                    font='Arial 12 bold',)
    titulo.pack(pady=20)

    entry_frame = tk.Frame(master = login)
    entry_frame.pack()

    login_frame = tk.Frame(master=entry_frame,)
    login_frame.pack(side = 'top')

    usuario_email = tk.Label(master=login_frame,
                            text="Usuario/Email ",
                            font='Arial 10')
    usuario_email.pack(side = 'left')
    # input de username
    login_var = tk.StringVar()
    login_usuario = ttk.Entry(master=login_frame,
                            width=20,textvariable=login_var)
    login_usuario.pack(side = 'right')

    senha_frame = tk.Frame(master=entry_frame)
    senha_frame.pack(side = 'bottom')

    senha_var = tk.StringVar()
    senha = tk.Label(master=senha_frame,
                    text='Senha ',
                    font='Arial 10')
    senha.pack(side='left', ipadx=22)
    login_senha = ttk.Entry(master=senha_frame,
                            width=20, show="*", textvariable=senha_var)  # input de senha
    login_senha.pack(side = 'right',padx=1)

    manter_logado_var=tk.BooleanVar()
    manter_logado_check = ttk.Checkbutton(master = login,
                                        text= 'Manter logado',
                                        variable=manter_logado_var,)
    manter_logado_check.pack()

    aviso = tk.StringVar()  # aviso caso erro
    aviso_label = tk.Label(login, textvariable=aviso)
    aviso_label.pack()

    def entrar():
        funcao = df.logando(login_usuario.get(), login_senha.get(), manter_logado_var.get())
        if funcao == "True":
            login_var.set("")
            senha_var.set("")
            manter_logado_var.set(False)
            aviso.set("")
            login.withdraw()
            tela_home()
        elif funcao == "senha incorreta":
            aviso.set("senha incorreta")
        elif "conta inexistente":
            aviso.set("conta inexistente")

    botao_frame = tk.Frame(master=login)
    botao_frame.pack()

    # chama a funcao para verificar login
    botao_entrar = ttk.Button(master=botao_frame, text='Entrar', command=entrar)
    botao_entrar.pack(side='left', padx=10)

    # chama tela de cadastro
    botao_cadastrar = ttk.Button(master=botao_frame, text='Cadastrar', command=tela_cadastro)
    botao_cadastrar.pack(side='right', padx=10)
    x = login.winfo_x()
    y = login.winfo_y()
    if prioridade != 1:
        login.withdraw()
        tela_home()

    login.mainloop()


if __name__ == '__main__':
    if not os.path.exists('login_config.txt') or os.stat('login_config.txt').st_size == 0:

        with open('login_config.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write('tema=darkly\nusername=\nemail=\nsenha=\n')
    elif not os.path.exists('credenciais_cadastradas.txt'):
        with open('credenciais_cadastradas.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write('')
    with open('login_config.txt', 'r', encoding='utf-8') as arquivo:
        manter = []
        for i in arquivo:
            manter.append(i.rstrip().split('='))
    with open('credenciais_cadastradas.txt', 'r', encoding='utf-8') as arquivo:
        verificar = []
        for i in arquivo:
            verificar.append(i.rstrip().split(','))

    for i in manter:
        parametro,conteudo=i
        if parametro == 'tema':
            tema = conteudo
        if parametro == 'username':
            username = conteudo
        elif parametro == 'email':
            e_mail = conteudo
        elif parametro == 'senha':
            passw = conteudo

    home = False
    for i in verificar:
        user,email,senha = i
        if (username == user
            and e_mail == email
            and passw == senha):
            home = True
            tela_login(0,tema)
    if not home:
        tela_login(1,tema)
