from funcoes import listaTipoFicheiroTXT ,listaTipoFicheiroCSV, Menu1, LerFicheiroTXT, constroiNomeApelido,constroiNumero, escreveFicheirosCSV, perguntaSair,FicheiroRES_CSV

Menu1()

op = int(input(' Opção -> '))
while op not in {0,1,2}:
     op = int(input(' Opção -> '))

if op == 1:
    LerFicheiroTXT()
    escreveFicheirosCSV()
    FicheiroRES_CSV()


if op == 0:
    perguntaSair()

