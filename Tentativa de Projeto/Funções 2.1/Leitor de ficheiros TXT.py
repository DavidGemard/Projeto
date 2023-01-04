# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 14:32:50 2023

@author: david
"""

def ListaTipoFicheiro(tipo):
    from os import listdir
     
    txt = 'Lista de Ficheiros : ' + tipo.upper()
    print(txt)
    print('-' * len(txt)) 
    
    for fileId in listdir():
        if fileId.endswith(tipo):
            print(fileId)
            
def LerFicheiroTXT():
    from os.path import isfile
    global dados
    dados = dict()

    ListaTipoFicheiro('.txt')
    nomeFile = ""
    while not isfile(nomeFile):
        nomeFile = input('Nome do Ficheiro: ')
    
    Perg = '--> Pergunta: <--'
    ResA = 'Resposta: ...... A'
    ResB = 'Resposta: ...... B'
    ResC = 'Resposta: ...... C'
    ResD = 'Resposta: ...... D'
    Resp_Possiveis = [ResA, ResB, ResC, ResD]

    with open(nomeFile, 'r') as fileId:
        for linha in fileId:
            linha = linha.strip()

            if linha != ResA and linha != ResB and linha != ResC and linha != ResD and linha != Perg:
                NPerg = linha
                TxtPerg = fileId.readline().strip()
                OpCerta = fileId.readline().strip()
                Opcoes = []
                linha = fileId.readline().strip()
                while linha in Resp_Possiveis:
                    Opcoes.append(linha)
                    linha = fileId.readline().strip()
                dados[NPerg] = [NPerg, TxtPerg, OpCerta, Opcoes]
    
    return dados
           