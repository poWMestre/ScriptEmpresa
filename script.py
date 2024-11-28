import time
import xml.etree.ElementTree as ET
import re

DIRETORIO_PRINCIPAL = 'C:\\DigiSat\\SuiteG6\\Servidor' 

DIRETORIO_PEGAR_ARQUIVO_CNPJ = DIRETORIO_PRINCIPAL+'\\info.dat'
def pegarCNPJ(diretorio_cnpj):
    
    tree = ET.parse(diretorio_cnpj)
    root = tree.getroot()
    cnpj = ""

    for procurar_cnpj in root.findall('Matriz'):
        cnpj = procurar_cnpj.find('Cnpj')
        cnpj = cnpj.text
        break
        
    return cnpj

coletar_cnpj = pegarCNPJ(DIRETORIO_PEGAR_ARQUIVO_CNPJ)

#CNPJ é devolvido com './-' aqui ele retira e deixa só em números
def transformarCNPJ(cnpj_coletado):
    temp = re.split("[./-]",cnpj_coletado)
    cnpj = ""
    for elementos in temp:
        cnpj = cnpj+elementos

    return cnpj

cnpj = transformarCNPJ(coletar_cnpj)

def pastaDoMesNFE():
    ano = time.strftime("%Y", time.localtime())
    mes = time.strftime("%m", time.localtime())
    if mes == "01":
        mes = "12"
        #transformo em inteiro para fazer a subtração depois volto para string
        ano = str(int(ano)-1)
    diretorio = ano+mes
    return diretorio

pasta_do_mes = pastaDoMesNFE()

DIRETORIO_PARA_NFE = DIRETORIO_PRINCIPAL+f'DFe\\{cnpj}\\Enviado\\NFe\\{pasta_do_mes}'
print(DIRETORIO_PARA_NFE)
    
