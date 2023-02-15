#sistema_arquivos.py

#funções básicas:
#os.path.basename() = retorna final do caminho do arquivo
#os.path.dirname() = retorna o nome do caminhio sem o final
#os.path.exists() = arquivo existe? retorns True ou False
#os.path.getsize() = retorna o tamanho do arquivo em bytes
#glob.glob() = retorna uma lista com nomes que atendam o critério passado como parâmetro

import os.path
import glob

#lista todos os arquivos.py
def listar():
    nomes = glob.glob('*.py')
    for arq in nomes:
        print(arq, os.path.getsize(arq))

if (__name__ == '__main__'):
    listar()
