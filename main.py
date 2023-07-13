#Geralmente utilizada quando se deseja trabalhar com caminhos no windows
#Deseja-se evitar escrever caminhos hard coded, um dos fatores que levam a usar esse modulo

from pathlib import Path

CAMINHO_PROJETO = Path()
#Como achar o caminho relativo:
print(CAMINHO_PROJETO)
#Como achar o caminho absoluto
print(CAMINHO_PROJETO.absolute())

#Para pegar o caminho desse arquivo:
CAMINHO_ARQUIVO = Path(__file__)
print(CAMINHO_ARQUIVO)
print(CAMINHO_ARQUIVO.parent.parent.parent) #Faz o arquivo retornar uma posição anterior

NOVO_CAMINHO = CAMINHO_ARQUIVO.parent / 'novo_caminho'
print(NOVO_CAMINHO)

print(Path.home()) #Retorna a home do SO
print(Path.home() / 'Desktop') 

GERAR_ARQUIVO = CAMINHO_ARQUIVO.parent / 'teste.txt'
GERAR_ARQUIVO.touch() #Criar o arquivo no PC

# GERAR_ARQUIVO.unlink() Para apagar o arquivo

GERAR_ARQUIVO.write_text('Olá mundo', encoding='utf-8')#Escrever no arquivo

print(GERAR_ARQUIVO.read_text(encoding='utf-8')) #Ler o que está no arquivo

#Note que o metódo de cima gera um arquvio sem o append mode, ou seja toda vez que o código roda ele é sobrescrito, entretanto podemos mudar para adicionar o append mode:

NOVO_ARQUIVO = CAMINHO_ARQUIVO.parent/ 'TextWithAppendMode.txt'
with NOVO_ARQUIVO.open('a+', encoding='utf-8') as file:
    file.write('Uma linha\n')
    file.write('Olha a linha não foi sobrescita!\n')

print(NOVO_ARQUIVO.read_text(encoding='utf-8'))

CAMINHO_PASTA = CAMINHO_ARQUIVO.parent / 'Criando um diretório'
CAMINHO_PASTA.mkdir(exist_ok=True) #Sem esse existe_ok = True, só seria possivel rodar o códgio uma única vez, pois o diretorio ja iria existir e o programa não sobrescreve a pasta

SUBPASTA = CAMINHO_PASTA / 'Subpasta'
SUBPASTA.mkdir(exist_ok=True)

OUTRO_ARQUIVO = SUBPASTA / 'arquivoTextoDoSubDiretório.txt'
OUTRO_ARQUIVO.touch()
OUTRO_ARQUIVO.write_text('Eae')

MAIS_ARQUIVO = SUBPASTA.parent / 'arquivoTextoDoDiretorio.txt'
MAIS_ARQUIVO.touch()
MAIS_ARQUIVO.write_text('Eae')

#Como criar varios arquivos de uma vez:
FILES = SUBPASTA / 'files'
FILES.mkdir(exist_ok=True)

for i in range(10):
    file = FILES / f'FILE_{i}.txt'
    file.touch()

    #Escrevendo em varios arquivos de uma só vez
    if file.exists():
        file.unlink()
    else:
        file.touch()
    
    with file.open('+a', encoding='utf-8') as text_file:
        text_file.write('Olá Mundo!! \n')
        text_file.write(f'File_{i}.txt')


#Função recursiva para apagar pastas e arquivos

def rmtree(root: Path, remove_root = True ):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR: ', file)
            rmtree(file)
            file.rmdir()
        else:
            print('FILE: ', file )
            file.unlink()

rmtree(CAMINHO_PASTA)
CAMINHO_PASTA.rmdir()