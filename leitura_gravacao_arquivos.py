#leitura_gravacao_arquivos.py
#arquivo texto:
#gravação = 'w' = write
#leitura = 'r' = read
#anexar = 'a' = append

frutas = ['banana', 'laranja', 'uva']

#cria uma função para gravar a lista de frutas
def gravar():
    #cria um arquivo para gravar (write)
    arquivo = open('frutas.txt', 'w')

    for f in frutas:
        arquivo.write(f + '\n')

    #fecha o arquivo
    arquivo.close()
    print('Gravou os dados')


#faz a leitura do arquivo frutas.txt
def ler():
    #abre arquivo somente para leitura
    arquivo = open('frutas.txt', 'r')  #read
    #le cada linha do arquivo e imprime
    for x in arquivo:
        print(x, end='')

    #fecha o arquivo
    arquivo.close()

#anexa novas frutas no final do arquivo
def anexar():
    arquivo = open('frutas.txt', 'a')  #append
    arquivo.write('kiwi' + '\n')
    arquivo.write('melancia' + '\n')
    arquivo.close()
    print('Anexou mais frutas')
    

if (__name__== '__main__'):
    gravar()
    anexar()
    ler()
  
