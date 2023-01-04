from funcoes21 import ListaTipoFicheiro,Menu1,LerFicheiroTXT,constroiNomeApelido,constroiNumero,escreveFicheirosCSV,perguntaSair,FicheiroRES_CSV,opcaoMenu1,perguntaSair

userSair = False
while not userSair:
    Menu1()
    opcao1 = opcaoMenu1()
    if opcao1 == 1:
        LerFicheiroTXT()
        escreveFicheirosCSV()
        FicheiroRES_CSV()
               
    else:
        userSair = perguntaSair()