import xlrd

def ajeitandoQnumero(a):
    print()
    #Travado aqui
    if ((a>=0) and (a<=65)):
        return a
    else:
        print("Valor inválido! Foi setado para 30.")
        return 30

def ajeitaNomeNumero(b):
    b = int(b)
    #Travado aqui
    if ((b>=1) and (b<=65)):
        return str(b)
    else:
        return "30"

def faixaDeAnalise(lista):
    pergunta = int(input("Até quantos jogos você quer analisar? (ZERO para todos) :"))
    saindo = []

    if pergunta == 0:
        return lista

    elif pergunta>=len(lista[0]):
        print("Valor inválido, mas tudo bem.")
        print("A lista foi passada completa")
        return lista

    elif pergunta>100:
        for i in lista:
            saindo.append(i[:pergunta])
        return saindo

    else:
        print("Valor inválido, mas tudo bem.")
        print("A lista foi passada completa")
        return lista

def pulos(numero):
    for i in range(0, numero, 1):
        print("\n")

def imprimirComTabulacao(lista):
    saida = ""

    for i in lista:
        saida = ""
        for j in i:
            if (j<10):
                saida = saida+"0"+str(j)+"\t"
            else:
                saida = saida+str(j)+"\t"
        print(saida)

def escreverComTabulacao(lista):
    saida = ""

    listaDeSaida = []
    for i in lista:
        saida = ""
        for j in i:
            if (j<10):
                saida = saida+"0"+str(j)+"\t"
            else:
                saida = saida+str(j)+"\t"
        saida = saida+"\n"
        listaDeSaida.append(saida)

    return listaDeSaida

def escreverComTabulacaoDezena(lista):
    saida = ""

    listaDeSaida = []
    for i in lista:
        saida = ""
        for j in i:
            if (j<10):
                saida = saida+"_0"+str(j)+"\t"
            else:
                saida = saida+"_"+str(j)+"\t"
        saida = saida+"\n"
        listaDeSaida.append(saida)

    return listaDeSaida


# Imprimir a lista completa "0001" com tabulação
def imprimirlistaCompleta(lista):
    saida = ""
    for i in lista:
        saida = ""
        for j in i:
            if (j<10):
                saida = saida+"000"+str(j)+"\t"
            elif (j<100):
                saida = saida+"00"+str(j)+"\t"
            elif (j<1000):
                saida = saida+"0"+str(j)+"\t"
            else:
                saida = saida+str(j)+"\t"
        print(saida)

def contagemNumero(entrada, numero):
    saida = 0
    for i in entrada:
        saida = saida + i.count(numero)
    return saida


def clonar(lista):
	tamanho = len(lista)
	nova = []
	for iz in range (0, tamanho, 1):
		nova.append(lista[iz])
	return nova

def limpadorDePulos(entrada):
    nova = []

    for a in entrada:
        novidade = a.split()
        nova.append(novidade)

    return nova

def analisaPresencaAusencia(dezenaHori, listaGrupo30):
    # Criar e preencher uma lista com 10 listas vazias
    ausenciaPresenca = []
    for i in range(0, 10, 1):
        ausenciaPresenca.append([])

    for i in range(0, len(dezenaHori), 1):
        for j in dezenaHori[i]:
            # Se lista da vez está vazia
            if (len(ausenciaPresenca[i]) == 0):
                if j in listaGrupo30:
                    ausenciaPresenca[i].append(0)
                else:
                    ausenciaPresenca[i].append(1)
            else:
                if j in listaGrupo30:
                    ausenciaPresenca[i].append(0)
                else:
                    ausenciaPresenca[i].append((ausenciaPresenca[i][len(ausenciaPresenca[i]) - 1]) + 1)

    return ausenciaPresenca



#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

print("---- ANÁLISE UNIFICADA versão 0.0.3 ----")
print("\n Objetivo do programa: \nEstabelecer ausências de grupos de 4 números")
print("\n Analisar se a situação de determinado conjunto de (2 A 10) grupos se enquadra em algum filtro \n\n")

grupoDeQuanto = int(input("\n VOCÊ QUER A AUSÊNCIA DE QUANTOS GRUPOS (2 A 10)?: "))

print("\n\n")

escolhaDoUniverso = str(input("\n DIGITE:\n s para LOTERIA DOS SONHOS\n p para LOTEP\n"))

book = xlrd.open_workbook("diamante8GRUPOS.xlsx")

print("Você escolheu: ")

if (escolhaDoUniverso=='s') or (escolhaDoUniverso=='S'):
    nominho = "LOTERIA DOS SONHOS"
    novidade = book.sheet_by_name("SONHOS")
    print("--------------------------------------------------")
    print("----------------LOTERIA DOS SONHOS----------------")
    print("--------------------------------------------------\n\n")

elif (escolhaDoUniverso=='p') or (escolhaDoUniverso=='P'):
    nominho = "LOTEP"
    novidade = book.sheet_by_name("LOTEP")
    print("--------------------------------------------------")
    print("----------------------LOTEP-----------------------")
    print("--------------------------------------------------\n\n")
else:
    nominho = "LOTERIA DOS SONHOS"
    novidade = book.sheet_by_name("SONHOS")
    print("--------------------------------------------------")
    print("----------------LOTERIA DOS SONHOS----------------")
    print("--------------------------------------------------\n\n")

listaEscritaAgora = []

for i in range(2, 12, 1):
	algoTemporaria = []
	for j in range(1, novidade.ncols, 1):
		algoTemporaria.append(novidade.cell_value(rowx=i, colx=j))
	listaEscritaAgora.append(algoTemporaria)

if (nominho == "LOTERIA DOS SONHOS"):
    novoArquivo60 = open("resultados.txt","w")
elif (nominho == "LOTEP"):
    novoArquivo60 = open("resultadosLTP.txt", "w")

for i in listaEscritaAgora:
	novaLinhasAgora = ""
	for j in i:
		if (j!=''):
			novaLinhasAgora = novaLinhasAgora+str(int(j))+"\t"
	if(novaLinhasAgora != ""):
		novoArquivo60.write(novaLinhasAgora+"\n")
novoArquivo60.close()


if (nominho=="LOTERIA DOS SONHOS"):
    leitor = open("resultados.txt","r")
elif (nominho=="LOTEP"):
    leitor = open("resultadosLTP.txt","r")

leitor2 = limpadorDePulos(leitor)
leitor.close()

usarVariavel = clonar(leitor2)

#for i in usarVariavel:
#    print(i)


# Transformar essa lista de listas de strings em uma lista de listas de inteiros

listaGeralInt = []

for i in usarVariavel:
    novaListinhaQualquerCoisa = []
    for j in i:
        novaListinhaQualquerCoisa.append(int(j))
    listaGeralInt.append(novaListinhaQualquerCoisa)

alista = clonar(listaGeralInt)

# -----------------------------------------------
# Escolhendo a quantidade do grupo
# -----------------------------------------------

soTeste = clonar(alista)
olhando = len(soTeste[0])



# -----------------------------------------------
# Definir até quantos jogos deve ser analisado
# -----------------------------------------------

print("Escolha o valor maior que 100!")
alista = faixaDeAnalise(alista)
numeroTotalZig = len(alista[0])

numeroTotalMesmo = 0
for i in range(0, numeroTotalZig, 1):
    numeroTotalMesmo = numeroTotalMesmo + 1

if(olhando>len(alista[0])):
    atualmente = str(len(alista[0]))
else:
    atualmente = str(len(alista[0]))+"_atual"

#for i in listaGeralInt:
#    print(i)

# Tirar a centena e a milhar na horizontal e na vertical

milharCentenaVert = []
milharCentenaHori = []

for i in alista:
    novaListinhaQualquerCoisa =[]
    for j in i:
        novaListinhaQualquerCoisa.append(j//100)
    milharCentenaHori.append(novaListinhaQualquerCoisa)


for i in range (0, len(alista[0]), 1):
    novaListinhaQualquerCoisa = []
    for j in alista:
        novaListinhaQualquerCoisa.append(j[i]//100)
    milharCentenaVert.append(novaListinhaQualquerCoisa)


dezenaVert = []
dezenaHori = []

for i in alista:
    novaListinhaQualquerCoisa =[]
    for j in i:
        novaListinhaQualquerCoisa.append(j%100)
    dezenaHori.append(novaListinhaQualquerCoisa)

for i in range (0, len(alista[0]), 1):
    novaListinhaQualquerCoisa = []
    for j in alista:
        novaListinhaQualquerCoisa.append(j[i]%100)
    dezenaVert.append(novaListinhaQualquerCoisa)


# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
# -----Lista importantes: alista, milharCentenaVert, milharCentenaHori, dezenaVerti, dezenaHori ----------------
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------

# Criando os 25 grupos de dezenas

gruposDe4novo = []

contagemDeAjuda = 0
for rainOnMe in range (1,26,1):
    novaEntradaDeGrupo = []
    for z in range(1, 5, 1):
        novaEntradaDeGrupo.append(contagemDeAjuda+z)
    gruposDe4novo.append(novaEntradaDeGrupo)
    contagemDeAjuda = contagemDeAjuda + 4

gruposDe4novo[24][3] = 0

# Concluida a criacao dos 25 grupos de dezenas

# Nome dos animais
animal = ["Avestruz", "Aguia", "Burro", "Borboleta", "Cachorro", "Cabra", "Carneiro", "Camelo", "Cobra", "Coelho", "Cavalo", "Elefante", "Galo", "Gato", "Jacare", "Leao", "Macaco", "Porco", "Pavao", "Peru", "Touro", "Tigre", "Urso", "Veado", "Vaca"]

# Buscar o animal de cada premio

posicaoFinal = len(alista[0])-1


# Para ver como estao as dezenas em um determinado sorteio eu devo usar a lista Dezenas Vert

# Para analisar uma serie historica de um premio e necessario usa a lista Dezenas Hori



# Para analisar uma serie historica de um premio e necessario usa a lista Dezenas Hori

# Procurar por quanto tempo 17 grupos estão se repetindo

# Passo 1 - Traduzir para 25 numeros apenas

listaTraduzida25 = []
listaTraduzida25Reserva = []

for y in dezenaHori:
    parteDaTraducao = []
    for posicao in range(0, len(y), 1):
        for j in gruposDe4novo:
            if y[posicao] in j:
                parteDaTraducao.append(gruposDe4novo.index(j)+1)
                break
    listaTraduzida25.append(parteDaTraducao)
    parteTradu = clonar(parteDaTraducao)
    listaTraduzida25Reserva.append(parteTradu)


# Passo 2 - Fazer analise dessa lista traduzida para ver o que acontece
# Procurar os 17 grupos de que deram em seguida até aqui

listaGuardadora = []

listaDeGRUPOPASSADO = []
listaDeGRUPOFUTURO = []

cloneDaTradu25 = clonar(listaTraduzida25)



#for bolo in range(1666,100,-1):
for bolo in range(numeroTotalMesmo,100,-1):

    contadorPassado = []
    gruposPassado = []
    gruposFuturo = []

    for z in listaTraduzida25:
        parouNesseNumero = 0
        gruposJahEncontrados = []
        contagemDaViagem = 0
        for posicao in range (len(z)-1, -1, -1):
            if len(gruposJahEncontrados)==(25 - grupoDeQuanto):
                parouNesseNumero = posicao
                break
            if z[posicao] in gruposJahEncontrados:
                contagemDaViagem = contagemDaViagem + 1
            else:
                gruposJahEncontrados.append(z[posicao])
                contagemDaViagem = contagemDaViagem + 1
        gruposJahEncontrados.sort()
        gruposPassado.append(gruposJahEncontrados)
        gruposNaoSairam = []
        for i in range(1, 26, 1):
            if i not in gruposJahEncontrados:
                gruposNaoSairam.append(i)
        gruposFuturo.append(gruposNaoSairam)
        while(z[parouNesseNumero] in gruposJahEncontrados):
            contagemDaViagem = contagemDaViagem + 1
            parouNesseNumero = parouNesseNumero - 1
        contadorPassado.append(contagemDaViagem)
    listaGuardadora.append(contadorPassado)
    for nadica in range(0, 10, 1):
        del listaTraduzida25[nadica][-1]
    listaDeGRUPOFUTURO.append(gruposFuturo)
    listaDeGRUPOPASSADO.append(gruposPassado)


#for nota in listaGuardadora:
    #print(nota)

print("-----------------------")

# -------------------------------------------------------------------
# -------------------------------------------------------------------
# Criando a lista de 2 ausentes para excluir esses 2 grupos da lista maior de grupos:

listaTraduzinda25v02 = []

for y in dezenaHori:
    parteDaTraducao2 = []
    for posicao in range(0, len(y), 1):
        for j in gruposDe4novo:
            if y[posicao] in j:
                parteDaTraducao2.append(gruposDe4novo.index(j)+1)
                break
    listaTraduzinda25v02.append(parteDaTraducao2)

grupoDeQuanto2 = 3

listaGuardadora2 = []

listaDeGRUPOPASSADO2 = []
listaDeGRUPOFUTURO2 = []

cloneDaTradu252 = clonar(listaTraduzida25)



#for bolo in range(1666,100,-1):
for bolo2 in range(numeroTotalMesmo,100,-1):

    contadorPassado2 = []
    gruposPassado2 = []
    gruposFuturo2 = []

    for z2 in listaTraduzinda25v02:
        parouNesseNumero2 = 0
        gruposJahEncontrados2 = []
        contagemDaViagem2 = 0
        for posicao2 in range (len(z2)-1, -1, -1):
            if len(gruposJahEncontrados2)==(25 - grupoDeQuanto2):
                parouNesseNumero2 = posicao2
                break
            if z2[posicao2] in gruposJahEncontrados2:
                contagemDaViagem2 = contagemDaViagem2 + 1
            else:
                gruposJahEncontrados2.append(z2[posicao2])
                contagemDaViagem2 = contagemDaViagem2 + 1
        gruposJahEncontrados2.sort()
        gruposPassado2.append(gruposJahEncontrados2)
        gruposNaoSairam2 = []
        for i2 in range(1, 26, 1):
            if i2 not in gruposJahEncontrados2:
                gruposNaoSairam2.append(i2)
        gruposFuturo2.append(gruposNaoSairam2)
        while(z2[parouNesseNumero2] in gruposJahEncontrados2):
            contagemDaViagem2 = contagemDaViagem2 + 1
            parouNesseNumero2 = parouNesseNumero2 - 1
        contadorPassado2.append(contagemDaViagem2)
    listaGuardadora2.append(contadorPassado2)
    for nadica2 in range(0, 10, 1):
        del listaTraduzinda25v02[nadica2][-1]
    listaDeGRUPOFUTURO2.append(gruposFuturo2)
    listaDeGRUPOPASSADO2.append(gruposPassado2)



# -------------------------------------------------------------------
# -------------------------------------------------------------------



#for z in listaTraduzida25:
#    print(z)

# Usando a listaGuardadora definir quanta vezes o grupo de 8 saiu 1, 2 ou 3 jogos depois

# Exemplo: 20 aconteceu 230 vezes - POSITIVO (1) = 30 (2) = 26 (3) = 47

# Passo 1: Criar uma lista com números de 17 a 58

listaDosPossiveis = []

for z in range(17, 59, 1):
    listaDosPossiveis.append(z)

# Passo 2: Criar 3 listas para os 3 POSITIVOS, com tudo setado em 0
# Depois o programa faz as buscas para os positivos de cada número e atualiza o valor
# Para evitar problemas com o indice de cada lista eu usarei a função index
listaDosValoresPossiveis = []
listaPositiva01 = []
listaPositiva02 = []
listaPositiva03 = []
listaPositiva04 = []
listaPositiva05 = []

for i in range(17, 59, 1):
    listaDosValoresPossiveis.append(i)
    listaPositiva01.append(0)
    listaPositiva02.append(0)
    listaPositiva03.append(0)
    listaPositiva04.append(0)
    listaPositiva05.append(0)

# Passo 3: Contar quantas vezes cada ausência aconteceu

listaContagemDasAusencias = []

for w in range(17, 59, 1):
    contadorBemSimples10 = 0
    for nivelUm in listaGuardadora:
        for nivelDois in nivelUm:
            if nivelDois == w:
                contadorBemSimples10 = contadorBemSimples10 + 1
    listaContagemDasAusencias.append(contadorBemSimples10)

# Passo 4: Procurar os 3 níveis de POSITIVO
# É necessário observar que é preciso comerçar a partir do jogo 1663 ao invés do 1666
# Como a lista vai de 1 a 1566, ou melhor, índices de 0 a 1565
# A lista guardadora deve ser percorrida de 1562 a 0

#print(len(listaGuardadora))
#print(len(listaTraduzida25Reserva[9]))
#print(len(listaDeGRUPOPASSADO))
#print(listaGuardadora[0])

#Abreviando o nome da listaG

listaG = listaGuardadora

listaBuscaPiscaPisca = []
for posiBoa in range (0,10,1):
    sinalAlerta = 0
    #Aconteceu 5 aumentos seguidos
    if (listaG[0][posiBoa]) == ((listaG[5][posiBoa])+5):
        if(listaG[5][posiBoa]<=listaG[6][posiBoa]):
            if(listaG[6][posiBoa]==listaG[11][posiBoa]+5):
                sinalAlerta = 1
    listaBuscaPiscaPisca.append(sinalAlerta)

#print(listaBuscaPiscaPisca)

# IMPORTANTE

# A listaGuardadora tem 1**** listas com das uma delas tendo 10 números
# A posição 0 representa o sorteio mais recente


#Filtro PLIM
# A|A|A|A|P|A|A|A|P|A|A|P|A|A|A|A|P|A|P|A|A|P|A|A|A|P|P
# Apitar o filtro quando estiver nessa última permutação

filtroPlim1 = []
for i in range (0,10,1):
    parte1PLIM1 = 0
    parte2PLIM1 = 0
    buscarPlim1 = 0
    # O atual é uma permutação?
    if (listaG[0][i]) <= (listaG[1][i]):
        # O penúltimo é uma permutação?
        if (listaG[1][i]) <= (listaG[2][i]):
            #O antepenúltimo foi um aumento?
            if (listaG[2][i]) > (listaG[3][i]):
                parte1PLIM1 = parte1PLIM1 + 1
    # Momento de procurar as outras 6 permutações anteriores
    plimEnquanto1 = 0
    # Se algumas das permutações não for isolada a variável "conjuntaPlim1" vai ser setada para 1
    conjuntaPlim1 = 0
    #As buscas começam perguntando se a posição 3 é uma permutação
    posInPlim1 = 3
    while(plimEnquanto1<6):
        if (listaG[posInPlim1][i]) <= (listaG[posInPlim1+1][i]):
            #Permutação encontrada, logo é necessário incrementar a variável plimEnquanto1
            plimEnquanto1 = plimEnquanto1 + 1
            #Então é necessário saber se é uma permutação conjunta
            if (listaG[posInPlim1+1][i]) <= (listaG[posInPlim1+2][i]):
                #Caso seja conjunta o valor de conjuntaPlim1 é incrementado
                conjuntaPlim1 = conjuntaPlim1 + 1
        posInPlim1 = posInPlim1 + 1
    if (conjuntaPlim1==0):
        parte2PLIM1 = 1
    somaPartePlim1 = parte1PLIM1 + parte2PLIM1
    if somaPartePlim1 == 2:
        filtroPlim1.append(1)
    else:
        filtroPlim1.append(0)
    # No final a soma de parte1 + parte 2 deve ser igual a 2


# Conferir se algum plim foi encontrado
if 1 in filtroPlim1:
    plim1Palavra = "__PLIM"
else:
    plim1Palavra = "__"

# Filtro 1
# A|A|A|A|A|A|P|VOCE ESTA AQUI

filtro001 = []

for i in range (0, 10, 1):
    buscando = 0
    if (listaG[1][i]) <= ((listaG[2][i])):
        if(listaG[2][i]==listaG[7][i]+5):
            buscando = 1
    filtro001.append(buscando)

#----------------------------------------------------------

# Filtro 2
# A|A|A|A|A|A|A|P|VOCE ESTA AQUI

filtro002 = []

for i in range (0, 10, 1):
    buscando = 0
    if (listaG[1][i]) <= ((listaG[2][i])):
        if(listaG[2][i]==listaG[8][i]+6):
            buscando = 1
    filtro002.append(buscando)

#----------------------------------------------------------

# Filtro 3
# A|A|A|A|A|A|A|A|P|VOCE ESTA AQUI

filtro003 = []

for i in range (0, 10, 1):
    buscando = 0
    if (listaG[1][i]) <= ((listaG[2][i])):
        if(listaG[2][i]==listaG[9][i]+7):
            buscando = 1
    filtro003.append(buscando)

#----------------------------------------------------------

# Filtro 4
# A|A|A|A|A|A|A|A|A|P|VOCE ESTA AQUI
filtro004 = []

for i in range (0, 10, 1):
    buscando = 0
    if (listaG[1][i]) <= ((listaG[2][i])):
        if(listaG[2][i]==listaG[10][i]+8):
            buscando = 1
    filtro004.append(buscando)

# Escrevendo o arquivos
if( (1 in listaBuscaPiscaPisca) or (1 in filtro001) or (1 in filtro002) or (1 in filtro003) or (1 in filtro004)):
    escritaDefinitiva = open("V03 "+str(grupoDeQuanto)+"_GRUPOS_"+nominho+"--SORTEIO---"+atualmente+"_PISCA"+plim1Palavra+".txt","w")
else:
    escritaDefinitiva = open("V03 "+str(grupoDeQuanto)+"_GRUPOS_"+nominho+"--SORTEIO---"+atualmente +plim1Palavra+".txt", "w")
escritaDefinitiva.write("****************************************\n")
escritaDefinitiva.write("Comportamento dos 25 grupos no sorteio "+atualmente+"\n")
escritaDefinitiva.write("****************************************\n\n")


escritaDefinitiva.write("FILTROS:\n")

if 1 in filtroPlim1:
    encontradoPlim1 = ""
    for y in range(0,10,1):
        if filtroPlim1[y] == 1:
            encontradoPlim1 = encontradoPlim1 + str(y+1) + "  "
    escritaDefinitiva.write("Filtro PLIM 1 no(s) premio(s):  "+encontradoPlim1+"\n")


saidaFiltro000 = ""
for z in range(0,10,1):
    if(listaBuscaPiscaPisca[z]==1):
        saidaFiltro000 = saidaFiltro000+"   "+str(z+1)

if (1 in listaBuscaPiscaPisca):
    escritaDefinitiva.write("A|A|A|A|A|A|P|A|A|A|A|A|VOCE ESTA AQUI - nos premios:"+saidaFiltro000+"\n")


saidaFiltro001 = ""
for z in range(0,10,1):
    if(filtro001[z]==1):
        saidaFiltro001 = saidaFiltro001+"   "+str(z+1)

if (1 in filtro001):
    escritaDefinitiva.write("6 - A|A|A|A|A|A|P|VOCE ESTA AQUI - nos premios:"+saidaFiltro001+"\n")

saidaFiltro002 = ""
for z in range(0,10,1):
    if(filtro002[z]==1):
        saidaFiltro002 = saidaFiltro002+"   "+str(z+1)

if (1 in filtro002):
    escritaDefinitiva.write("7 - A|A|A|A|A|A|A|P|VOCE ESTA AQUI - nos premios:"+saidaFiltro002+"\n")

saidaFiltro003 = ""
for z in range(0,10,1):
    if(filtro003[z]==1):
        saidaFiltro003 = saidaFiltro003+"   "+str(z+1)

if (1 in filtro003):
    escritaDefinitiva.write("8 - A|A|A|A|A|A|A|A|P|VOCE ESTA AQUI - nos premios:"+saidaFiltro003+"\n")

saidaFiltro004 = ""
for z in range(0,10,1):
    if(filtro004[z]==1):
        saidaFiltro004 = saidaFiltro004+"   "+str(z+1)

if (1 in filtro004):
    escritaDefinitiva.write("9 - A|A|A|A|A|A|A|A|A|P|VOCE ESTA AQUI - nos premios:"+saidaFiltro004+"\n")

# Filtro 5
# A|A|A|A|A|A|A|A|A|A|P|VOCE ESTA AQUI
# Filtro 6
# A|A|A|A|A|A|A|A|A|A|A|P|VOCE ESTA AQUI
# Filtro 7
# A|A|A|A|A|A|A|A|A|A|A|A|P|VOCE ESTA AQUI
# Filtro 8
# A|A|A|A|A|A|A|A|A|A|A|A|A|P|VOCE ESTA AQUI
# Filtro 9
# A|A|A|A|A|A|A|A|A|A|A|A|A|A|P|VOCE ESTA AQUI

filtro005 = []
filtro006 = []
filtro007 = []
filtro008 = []
filtro009 = []

for i in range (0, 10, 1):
    buscando5 = 0
    if (listaG[1][i]) <= ((listaG[2][i])):
        if(listaG[2][i]==listaG[11][i]+9):
            buscando5 = 1
    filtro005.append(buscando5)

    buscando6 = 0
    if (listaG[1][i]) <= ((listaG[2][i])):
        if(listaG[2][i]==listaG[12][i]+10):
            buscando6 = 1
    filtro006.append(buscando6)

    buscando7 = 0
    if (listaG[1][i]) <= ((listaG[2][i])):
        if(listaG[2][i]==listaG[13][i]+11):
            buscando7 = 1
    filtro007.append(buscando7)

    buscando8 = 0
    if (listaG[1][i]) <= ((listaG[2][i])):
        if(listaG[2][i]==listaG[14][i]+12):
            buscando8 = 1
    filtro008.append(buscando8)

    buscando9 = 0
    if (listaG[1][i]) <= ((listaG[2][i])):
        if(listaG[2][i]==listaG[15][i]+13):
            buscando9 = 1
    filtro009.append(buscando9)

saidaFiltro005 = ""
saidaFiltro006 = ""
saidaFiltro007 = ""
saidaFiltro008 = ""
saidaFiltro009 = ""

for z in range(0,10,1):
    if(filtro005[z]==1):
        saidaFiltro005 = saidaFiltro005+"   "+str(z+1)
    if(filtro006[z]==1):
        saidaFiltro006 = saidaFiltro006+"   "+str(z+1)
    if(filtro007[z]==1):
        saidaFiltro007 = saidaFiltro007+"   "+str(z+1)
    if(filtro008[z]==1):
        saidaFiltro008 = saidaFiltro008+"   "+str(z+1)
    if(filtro009[z]==1):
        saidaFiltro009 = saidaFiltro009+"   "+str(z+1)

if (1 in filtro005):
    escritaDefinitiva.write("10 - A|A|A|A|A|A|A|A|A|A|P|VOCE ESTA AQUI - nos premios:"+saidaFiltro005+"\n")
if (1 in filtro006):
    escritaDefinitiva.write("11 - A|A|A|A|A|A|A|A|A|A|A|P|VOCE ESTA AQUI - nos premios:"+saidaFiltro006+"\n")
if (1 in filtro007):
    escritaDefinitiva.write("12 - A|A|A|A|A|A|A|A|A|A|A|A|P|VOCE ESTA AQUI - nos premios:"+saidaFiltro007+"\n")
if (1 in filtro008):
    escritaDefinitiva.write("13 - A|A|A|A|A|A|A|A|A|A|A|A|A|P|VOCE ESTA AQUI - nos premios:"+saidaFiltro008+"\n\n")
if (1 in filtro009):
    escritaDefinitiva.write("14 - A|A|A|A|A|A|A|A|A|A|A|A|A|A|P|VOCE ESTA AQUI - nos premios:"+saidaFiltro009+"\n\n")

for j in range (0, 10, 1):
    escritaDefinitiva.write("-------------------------------------------------------------\n")
    escritaDefinitiva.write("No "+str(j+1)+"º premio | \n")
    escritaDefinitiva.write("-----------------\n")
    escritaDefinitiva.write("Os " + str(25-grupoDeQuanto) +" que sairam: "+str(listaDeGRUPOPASSADO[0][j])+"\n\n")
    escritaDefinitiva.write("Faz "+str(listaGuardadora[0][j])+" jogos que so esses "+ str(25-grupoDeQuanto) + " saem\n\n")
    escritaDefinitiva.write("Os "+ str(grupoDeQuanto) +" restantes sao: "+str(listaDeGRUPOFUTURO[0][j])+"\n\n")
    # Indicando os 2 PIORES
    escritaDefinitiva.write("Os 3 PIORES GRUPOS sao: "+str(listaDeGRUPOFUTURO2[0][j])+"\n\n")
    #TIRANDO OS 2 PIORES PARA MOSTRAR
    oqueResta = []
    for d in listaDeGRUPOFUTURO[0][j]:
        if d not in listaDeGRUPOFUTURO2[0][j]:
            oqueResta.append(d)
    oqueResta.sort()
    escritaDefinitiva.write("MELHORES GRUPOS: " + str(oqueResta)+"\n\n\n")

escritaDefinitiva.close()


#print("-------------------------------")
#print(listaG[0])
#buscandoMaximo = []
#print("Para um conjunto de "+str(grupoDeQuanto)+" grupos")
#for i in listaG:
#    buscandoMaximo.append(max(i))
#print("O máximo foi: "+str(max(buscandoMaximo)))