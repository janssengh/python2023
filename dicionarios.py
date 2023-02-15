#dicionarios.py

#Um dicionário é formado pelo par {"chave": valor}

#dicionários são indexados pela chave
tel = {'joao': '(42) 98888-3344', 'maria': '(42)99999-7788'}

print(tel['joao'])
print(tel['maria'])

#altera o número do telefone
tel['joao'] = '(11)99999-9999'
print(tel['joao'])

#podemos criar dicionário a partir de uma lista;
#exemplo
lista_contatos = [('joao', '1234-5678'),
                  ('Pedro', '9999-9999'),
                  ('Ana', '8765-4321'),
                  ('Mariana', '8877-7788')
                  ]

#cria um dicionário a partir de uma lista
contatos = dict(lista_contatos)
print('Dicionário contatos:\n', contatos)
print('Telefone da Ana = ', contatos['Ana'])

if 'Zacarias' in contatos:
    print('Telefone da Zacarias = ',contatos['Zacarias'])
else:
    print('Não tem o telefone do Zacarias')

#mostra todas as chaves do dicionário
print(contatos.keys())

#mostra todos os valores do dicionário
print(contatos.values())

#adicionando um contato
contatos['Luiz'] = '5544-5544'
print('Telefone do Luiz =', contatos['Luiz'])

#adicionando um contato
contatos['Luiz Souza'] = '5544-5544'
print('Telefone do Luiz =', contatos['Luiz'])

#Removendo um contato do dicionário
del contatos['Luiz']
print(contatos.keys())








        
    






  
