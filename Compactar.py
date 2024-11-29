from shutil import make_archive
import os

''' WARNING
Na parte de zipar tem que mudar o diretório onde é salvo a pasta .zip
    WARNING
'''

class empacotarArquivos():

    def verificarExistenciaDeArquivos(caminho_da_pasta):

        arquivos = os.listdir(caminho_da_pasta)
        if len(arquivos) > 0:
            return True
        return False
    
    def zipar(caminho_dos_arquivos, mes_da_pasta):

        nome_da_pasta = "NFE_"+mes_da_pasta
        make_archive(nome_da_pasta, 'zip', caminho_dos_arquivos)

    
