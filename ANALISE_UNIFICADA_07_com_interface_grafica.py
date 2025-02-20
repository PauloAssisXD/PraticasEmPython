import xlrd
import PySimpleGUI as sg

# Analise de resultados de loterias locais
# Objetivo: encontrar possível padrão nos resultados
# Projeto de 2020

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
    pergunta = sorteioTela
    #pergunta = int(input("Até quantos jogos você quer analisar? (ZERO para todos) :"))
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


class TelaPython:
	def __init__(self):
		sg.change_look_and_feel('DarkTeal6')
		# layout
		layout = [
			[sg.Text('', size=(30, 0))],
			[sg.Text('----- ANÁLISE UNIFICADA 6.0.0 ----', size=(30, 0))],
			[sg.Text('', size=(30, 0))],
			[sg.Text('O propósito desse programa é definir a ausência de 2 a 10 grupos:', size=(30, 0))],
			[sg.Text('', size=(30, 0))],
			[sg.Text('Qual a quantidade de GRUPOS:')],
			[sg.Input(size=(5, 0), key='qtdGrupos')],
			[sg.Text('', size=(30, 0))],
			[sg.Text('Qual UNIVERSO:')],
			#[sg.Radio('Sim', 'cartoes', key='aceitaCartao'), sg.Radio('Nao', 'cartoes', key='naoAceitaCartao')],
			[sg.Radio('LOTEP', 'universoEscolhido',key='lotep'), sg.Radio('SONHOS','universoEscolhido', key='sonhos')],
			[sg.Text('', size=(30, 0))],
			[sg.Text('Até que sorteio? Valor maior que 100!')],
			[sg.Input(size=(10, 0), key='nroSorteio')],
			[sg.Text('', size=(30, 0))],
			[sg.Button('Analisar')]
			#[sg.Output(size=(30,10))]

		]


		# Janela
		self.janela = sg.Window("Análise Unificada").layout(layout)
		# Extrair os dados da tela


	def Iniciar(self):
		#print(self.values)
		#while True:
		self.button, self.values = self.janela.Read()

		v_grupos = self.values['qtdGrupos']
		v_lotep = self.values['lotep']
		v_sonhos = self.values['sonhos']
		v_sorteio = self.values['nroSorteio']

		if(v_lotep):
			v_universo = 'lotep'
		else:
			v_universo = 'sonhos'
		#print(f'GRUPOS: {v_grupos}')
		#print(f'UNIVERSO: {v_universo}')
		#print(f'SORTEIO: {v_sorteio}')


tela = TelaPython()
tela.Iniciar()


# Testando se a variável não está como uma string vazia
# Por padrão o número de grupos será 8 grupos
if (tela.values['qtdGrupos']) == '':
	qtdeGruposTela = 8
else:
	qtdeGruposTela = int(tela.values['qtdGrupos'])

if (tela.values['lotep']):
	universoTela = "p"
else:
	universoTela = "s"

# Testando se a variável não está como uma string vazia
if (tela.values['nroSorteio']) == '':
	sorteioTela =  0
else:
	sorteioTela =  int(tela.values['nroSorteio'])

# Acho que isso fecha a janela
tela.janela.close()
# Variaveis importantes


# qtdeGruposTela = padrão - 8
# universoTela = padrão - s
# sorteioTela = padrão - 0

# -----------------------------------------------------
# -----------------------------------------------------
# -----------------------------------------------------

grupoDeQuanto = qtdeGruposTela

print("\n\n")

escolhaDoUniverso = universoTela

book = xlrd.open_workbook("diamante.xls")


if (escolhaDoUniverso=='s') or (escolhaDoUniverso=='S'):
    nominho = "LOTERIA DOS SONHOS"
    novidade = book.sheet_by_name("SONHOS")


elif (escolhaDoUniverso=='p') or (escolhaDoUniverso=='P'):
    nominho = "LOTEP"
    novidade = book.sheet_by_name("LOTEP")

else:
    nominho = "LOTERIA DOS SONHOS"
    novidade = book.sheet_by_name("SONHOS")

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
    escritaDefinitiva = open("V07 "+str(grupoDeQuanto)+"_GRUPOS_"+nominho+"--SORTEIO---"+atualmente+"_PISCA"+plim1Palavra+".txt","w")
else:
    escritaDefinitiva = open("V07 "+str(grupoDeQuanto)+"_GRUPOS_"+nominho+"--SORTEIO---"+atualmente +plim1Palavra+".txt", "w")
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

listaSuprassumo = []

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
    listaSuprassumo.append(oqueResta)
    escritaDefinitiva.write("MELHORES GRUPOS: " + str(oqueResta)+"\n\n\n")

escritaDefinitiva.close()


#print("-------------------------------")
#print(listaG[0])
#buscandoMaximo = []
#print("Para um conjunto de "+str(grupoDeQuanto)+" grupos")
#for i in listaG:
#    buscandoMaximo.append(max(i))
#print("O máximo foi: "+str(max(buscandoMaximo)))


# tela com resultados finais

universoMostrar = nominho
gruposMostrar = grupoDeQuanto
sorteioMostrar = len(alista[0])

tituloDoResumoDaAnalise = universoMostrar + " - " + str(gruposMostrar) + " GRUPOS | ATÉ O SORTEIO " + str(sorteioMostrar)

m_ausenciasrar = listaGuardadora[0]

m_gruposAusentesrar = listaDeGRUPOFUTURO[0]
m_gruposPioresrar = listaDeGRUPOFUTURO2[0]
m_gruposMelhoresrar = listaSuprassumo

# Linhas que mostram aumentos e permutações

linhasMostrar = []
coresMostrar = []

for m in range(0, 10, 1):
    linhaAmostrada = []
    corAmostrada = []
    for y in range(9, -1, -1):
        if (listaGuardadora[y][m])>(listaGuardadora[y+1][m]):
            linhaAmostrada.append("aumento")
        else:
            linhaAmostrada.append("permuta")

    for bino in linhaAmostrada:
        if bino=="aumento":
            adicionarAquiMesmo = "red"
            corAmostrada.append(adicionarAquiMesmo)
        elif bino=="permuta":
            adicionarAquiMesmo = "green"
            corAmostrada.append(adicionarAquiMesmo)
    linhasMostrar.append(linhaAmostrada)
    coresMostrar.append(corAmostrada)

#--------------------------------



sg.theme('GreenTan')

#Text('This is some text', font='Courier 12', text_color='blue', background_color='green')

layoutFinal = [  [sg.Text(tituloDoResumoDaAnalise, size=(55,0),font='Arial 14',background_color='yellow')],
            #[sg.Text('Texto para testes', size=(30, 0),text_color='white',background_color='green',font='Arial 14')],
            [sg.Text('', size=(65, 0)),sg.Text('HISTÓRICO DOS 10 ÚLTIMOS SORTEIOS', size=(48, 0),background_color='white')],
            [sg.Text('PRÊMIOS', size=(8, 0),font='Arial 10',justification='center',background_color='white'),sg.Text('Tempo de Ausência', size=(8, 0),font='Arial 10',justification='center',background_color='white'),sg.Text(str(gruposMostrar)+' grupos ausentes', size=(15, 0), justification='center',background_color='white'),sg.Text('3 piores', size=(12, 0),justification='center',background_color='white'),sg.Text('melhores', size=(12, 0),justification='center',background_color='white'),sg.Text('', size=(8, 0)),sg.Text(str(sorteioMostrar-9), size=(6, 0)),sg.Text(str(sorteioMostrar-8), size=(6, 0)),sg.Text(str(sorteioMostrar-7), size=(6, 0)),sg.Text(str(sorteioMostrar-6), size=(6, 0)),sg.Text(str(sorteioMostrar-5), size=(6, 0)),sg.Text(str(sorteioMostrar-4), size=(6, 0)),sg.Text(str(sorteioMostrar-3), size=(6, 0)),sg.Text(str(sorteioMostrar-2), size=(6, 0)),sg.Text(str(sorteioMostrar-1), size=(6, 0)), sg.Text(str(sorteioMostrar), size=(6, 0))],
            [sg.Text('1º prêmio', size=(8, 0),font='Arial 10'),sg.Text(str(m_ausenciasrar[0]), size=(8, 0),justification='center'),sg.Text(str(m_gruposAusentesrar[0]), size=(15, 0),font='Verdana 10'),sg.Text(str(m_gruposPioresrar[0]), size=(12, 0),text_color='white',background_color='red',font='Verdana 10',justification='center'),sg.Text(m_gruposMelhoresrar[0], size=(12, 0),text_color='black',background_color='light green',font='Verdana 10',justification='center'),sg.Text('1º prêmio', size=(8, 0),font='Arial 10'),sg.Text(linhasMostrar[0][0],size=(6,0),font='Arial 10',background_color=coresMostrar[0][0]),sg.Text(linhasMostrar[0][1],size=(6,0),font='Arial 10',background_color=coresMostrar[0][1]),sg.Text(linhasMostrar[0][2],size=(6,0),font='Arial 10',background_color=coresMostrar[0][2]),sg.Text(linhasMostrar[0][3],size=(6,0),font='Arial 10',background_color=coresMostrar[0][3]),sg.Text(linhasMostrar[0][4],size=(6,0),font='Arial 10',background_color=coresMostrar[0][4]),sg.Text(linhasMostrar[0][5],size=(6,0),font='Arial 10',background_color=coresMostrar[0][5]),sg.Text(linhasMostrar[0][6],size=(6,0),font='Arial 10',background_color=coresMostrar[0][6]),sg.Text(linhasMostrar[0][7],size=(6,0),font='Arial 10',background_color=coresMostrar[0][7]),sg.Text(linhasMostrar[0][8],size=(6,0),font='Arial 10',background_color=coresMostrar[0][8]),sg.Text(linhasMostrar[0][9],size=(6,0),font='Arial 10',background_color=coresMostrar[0][9])],

            [sg.Text('2º prêmio', size=(8, 0),font='Arial 10'),sg.Text(str(m_ausenciasrar[1]), size=(8, 0),justification='center'),sg.Text(str(m_gruposAusentesrar[1]), size=(15, 0),font='Verdana 10'),sg.Text(str(m_gruposPioresrar[1]), size=(12, 0),text_color='white',background_color='red',font='Verdana 10',justification='center'),sg.Text(m_gruposMelhoresrar[1], size=(12, 0),text_color='black',background_color='light green',font='Verdana 10',justification='center'),sg.Text('2º prêmio', size=(8, 0),font='Arial 10'),sg.Text(linhasMostrar[1][0],size=(6,0),font='Arial 10',background_color=coresMostrar[1][0]),sg.Text(linhasMostrar[1][1],size=(6,0),font='Arial 10',background_color=coresMostrar[1][1]),sg.Text(linhasMostrar[1][2],size=(6,0),font='Arial 10',background_color=coresMostrar[1][2]),sg.Text(linhasMostrar[1][3],size=(6,0),font='Arial 10',background_color=coresMostrar[1][3]),sg.Text(linhasMostrar[1][4],size=(6,0),font='Arial 10',background_color=coresMostrar[1][4]),sg.Text(linhasMostrar[1][5],size=(6,0),font='Arial 10',background_color=coresMostrar[1][5]),sg.Text(linhasMostrar[1][6],size=(6,0),font='Arial 10',background_color=coresMostrar[1][6]),sg.Text(linhasMostrar[1][7],size=(6,0),font='Arial 10',background_color=coresMostrar[1][7]),sg.Text(linhasMostrar[1][8],size=(6,0),font='Arial 10',background_color=coresMostrar[1][8]),sg.Text(linhasMostrar[1][9],size=(6,0),font='Arial 10',background_color=coresMostrar[1][9])],
            [sg.Text('3º prêmio', size=(8, 0),font='Arial 10'),sg.Text(str(m_ausenciasrar[2]), size=(8, 0),justification='center'),sg.Text(str(m_gruposAusentesrar[2]), size=(15, 0),font='Verdana 10'),sg.Text(str(m_gruposPioresrar[2]), size=(12, 0),text_color='white',background_color='red',font='Verdana 10',justification='center'),sg.Text(m_gruposMelhoresrar[2], size=(12, 0),text_color='black',background_color='light green',font='Verdana 10',justification='center'),sg.Text('3º prêmio', size=(8, 0),font='Arial 10'),sg.Text(linhasMostrar[2][0],size=(6,0),font='Arial 10',background_color=coresMostrar[2][0]),sg.Text(linhasMostrar[2][1],size=(6,0),font='Arial 10',background_color=coresMostrar[2][1]),sg.Text(linhasMostrar[2][2],size=(6,0),font='Arial 10',background_color=coresMostrar[2][2]),sg.Text(linhasMostrar[2][3],size=(6,0),font='Arial 10',background_color=coresMostrar[2][3]),sg.Text(linhasMostrar[2][4],size=(6,0),font='Arial 10',background_color=coresMostrar[2][4]),sg.Text(linhasMostrar[2][5],size=(6,0),font='Arial 10',background_color=coresMostrar[2][5]),sg.Text(linhasMostrar[2][6],size=(6,0),font='Arial 10',background_color=coresMostrar[2][6]),sg.Text(linhasMostrar[2][7],size=(6,0),font='Arial 10',background_color=coresMostrar[2][7]),sg.Text(linhasMostrar[2][8],size=(6,0),font='Arial 10',background_color=coresMostrar[2][8]),sg.Text(linhasMostrar[2][9],size=(6,0),font='Arial 10',background_color=coresMostrar[2][9])],
            [sg.Text('4º prêmio', size=(8, 0),font='Arial 10'),sg.Text(str(m_ausenciasrar[3]), size=(8, 0),justification='center'),sg.Text(str(m_gruposAusentesrar[3]), size=(15, 0),font='Verdana 10'),sg.Text(str(m_gruposPioresrar[3]), size=(12, 0),text_color='white',background_color='red',font='Verdana 10',justification='center'),sg.Text(m_gruposMelhoresrar[3], size=(12, 0),text_color='black',background_color='light green',font='Verdana 10',justification='center'),sg.Text('4º prêmio', size=(8, 0),font='Arial 10'),sg.Text(linhasMostrar[3][0],size=(6,0),font='Arial 10',background_color=coresMostrar[3][0]),sg.Text(linhasMostrar[3][1],size=(6,0),font='Arial 10',background_color=coresMostrar[3][1]),sg.Text(linhasMostrar[3][2],size=(6,0),font='Arial 10',background_color=coresMostrar[3][2]),sg.Text(linhasMostrar[3][3],size=(6,0),font='Arial 10',background_color=coresMostrar[3][3]),sg.Text(linhasMostrar[3][4],size=(6,0),font='Arial 10',background_color=coresMostrar[3][4]),sg.Text(linhasMostrar[3][5],size=(6,0),font='Arial 10',background_color=coresMostrar[3][5]),sg.Text(linhasMostrar[3][6],size=(6,0),font='Arial 10',background_color=coresMostrar[3][6]),sg.Text(linhasMostrar[3][7],size=(6,0),font='Arial 10',background_color=coresMostrar[3][7]),sg.Text(linhasMostrar[3][8],size=(6,0),font='Arial 10',background_color=coresMostrar[3][8]),sg.Text(linhasMostrar[3][9],size=(6,0),font='Arial 10',background_color=coresMostrar[3][9])],
            [sg.Text('5º prêmio', size=(8, 0),font='Arial 10'),sg.Text(str(m_ausenciasrar[4]), size=(8, 0),justification='center'),sg.Text(str(m_gruposAusentesrar[4]), size=(15, 0),font='Verdana 10'),sg.Text(str(m_gruposPioresrar[4]), size=(12, 0),text_color='white',background_color='red',font='Verdana 10',justification='center'),sg.Text(m_gruposMelhoresrar[4], size=(12, 0),text_color='black',background_color='light green',font='Verdana 10',justification='center'),sg.Text('5º prêmio', size=(8, 0),font='Arial 10'),sg.Text(linhasMostrar[4][0],size=(6,0),font='Arial 10',background_color=coresMostrar[4][0]),sg.Text(linhasMostrar[4][1],size=(6,0),font='Arial 10',background_color=coresMostrar[4][1]),sg.Text(linhasMostrar[4][2],size=(6,0),font='Arial 10',background_color=coresMostrar[4][2]),sg.Text(linhasMostrar[4][3],size=(6,0),font='Arial 10',background_color=coresMostrar[4][3]),sg.Text(linhasMostrar[4][4],size=(6,0),font='Arial 10',background_color=coresMostrar[4][4]),sg.Text(linhasMostrar[4][5],size=(6,0),font='Arial 10',background_color=coresMostrar[4][5]),sg.Text(linhasMostrar[4][6],size=(6,0),font='Arial 10',background_color=coresMostrar[4][6]),sg.Text(linhasMostrar[4][7],size=(6,0),font='Arial 10',background_color=coresMostrar[4][7]),sg.Text(linhasMostrar[4][8],size=(6,0),font='Arial 10',background_color=coresMostrar[4][8]),sg.Text(linhasMostrar[4][9],size=(6,0),font='Arial 10',background_color=coresMostrar[4][9])],
            [sg.Text('6º prêmio', size=(8, 0),font='Arial 10'),sg.Text(str(m_ausenciasrar[5]), size=(8, 0),justification='center'),sg.Text(str(m_gruposAusentesrar[5]), size=(15, 0),font='Verdana 10'),sg.Text(str(m_gruposPioresrar[5]), size=(12, 0),text_color='white',background_color='red',font='Verdana 10',justification='center'),sg.Text(m_gruposMelhoresrar[5], size=(12, 0),text_color='black',background_color='light green',font='Verdana 10',justification='center'),sg.Text('6º prêmio', size=(8, 0),font='Arial 10'),sg.Text(linhasMostrar[5][0],size=(6,0),font='Arial 10',background_color=coresMostrar[5][0]),sg.Text(linhasMostrar[5][1],size=(6,0),font='Arial 10',background_color=coresMostrar[5][1]),sg.Text(linhasMostrar[5][2],size=(6,0),font='Arial 10',background_color=coresMostrar[5][2]),sg.Text(linhasMostrar[5][3],size=(6,0),font='Arial 10',background_color=coresMostrar[5][3]),sg.Text(linhasMostrar[5][4],size=(6,0),font='Arial 10',background_color=coresMostrar[5][4]),sg.Text(linhasMostrar[5][5],size=(6,0),font='Arial 10',background_color=coresMostrar[5][5]),sg.Text(linhasMostrar[5][6],size=(6,0),font='Arial 10',background_color=coresMostrar[5][6]),sg.Text(linhasMostrar[5][7],size=(6,0),font='Arial 10',background_color=coresMostrar[5][7]),sg.Text(linhasMostrar[5][8],size=(6,0),font='Arial 10',background_color=coresMostrar[5][8]),sg.Text(linhasMostrar[5][9],size=(6,0),font='Arial 10',background_color=coresMostrar[5][9])],
            [sg.Text('7º prêmio', size=(8, 0),font='Arial 10'),sg.Text(str(m_ausenciasrar[6]), size=(8, 0),justification='center'),sg.Text(str(m_gruposAusentesrar[6]), size=(15, 0),font='Verdana 10'),sg.Text(str(m_gruposPioresrar[6]), size=(12, 0),text_color='white',background_color='red',font='Verdana 10',justification='center'),sg.Text(m_gruposMelhoresrar[6], size=(12, 0),text_color='black',background_color='light green',font='Verdana 10',justification='center'),sg.Text('7º prêmio', size=(8, 0),font='Arial 10'),sg.Text(linhasMostrar[6][0],size=(6,0),font='Arial 10',background_color=coresMostrar[6][0]),sg.Text(linhasMostrar[6][1],size=(6,0),font='Arial 10',background_color=coresMostrar[6][1]),sg.Text(linhasMostrar[6][2],size=(6,0),font='Arial 10',background_color=coresMostrar[6][2]),sg.Text(linhasMostrar[6][3],size=(6,0),font='Arial 10',background_color=coresMostrar[6][3]),sg.Text(linhasMostrar[6][4],size=(6,0),font='Arial 10',background_color=coresMostrar[6][4]),sg.Text(linhasMostrar[6][5],size=(6,0),font='Arial 10',background_color=coresMostrar[6][5]),sg.Text(linhasMostrar[6][6],size=(6,0),font='Arial 10',background_color=coresMostrar[6][6]),sg.Text(linhasMostrar[6][7],size=(6,0),font='Arial 10',background_color=coresMostrar[6][7]),sg.Text(linhasMostrar[6][8],size=(6,0),font='Arial 10',background_color=coresMostrar[6][8]),sg.Text(linhasMostrar[6][9],size=(6,0),font='Arial 10',background_color=coresMostrar[6][9])],
            [sg.Text('8º prêmio', size=(8, 0),font='Arial 10'),sg.Text(str(m_ausenciasrar[7]), size=(8, 0),justification='center'),sg.Text(str(m_gruposAusentesrar[7]), size=(15, 0),font='Verdana 10'),sg.Text(str(m_gruposPioresrar[7]), size=(12, 0),text_color='white',background_color='red',font='Verdana 10',justification='center'),sg.Text(m_gruposMelhoresrar[7], size=(12, 0),text_color='black',background_color='light green',font='Verdana 10',justification='center'),sg.Text('8º prêmio', size=(8, 0),font='Arial 10'),sg.Text(linhasMostrar[7][0],size=(6,0),font='Arial 10',background_color=coresMostrar[7][0]),sg.Text(linhasMostrar[7][1],size=(6,0),font='Arial 10',background_color=coresMostrar[7][1]),sg.Text(linhasMostrar[7][2],size=(6,0),font='Arial 10',background_color=coresMostrar[7][2]),sg.Text(linhasMostrar[7][3],size=(6,0),font='Arial 10',background_color=coresMostrar[7][3]),sg.Text(linhasMostrar[7][4],size=(6,0),font='Arial 10',background_color=coresMostrar[7][4]),sg.Text(linhasMostrar[7][5],size=(6,0),font='Arial 10',background_color=coresMostrar[7][5]),sg.Text(linhasMostrar[7][6],size=(6,0),font='Arial 10',background_color=coresMostrar[7][6]),sg.Text(linhasMostrar[7][7],size=(6,0),font='Arial 10',background_color=coresMostrar[7][7]),sg.Text(linhasMostrar[7][8],size=(6,0),font='Arial 10',background_color=coresMostrar[7][8]),sg.Text(linhasMostrar[7][9],size=(6,0),font='Arial 10',background_color=coresMostrar[7][9])],
            [sg.Text('9º prêmio', size=(8, 0),font='Arial 10'),sg.Text(str(m_ausenciasrar[8]), size=(8, 0),justification='center'),sg.Text(str(m_gruposAusentesrar[8]), size=(15, 0),font='Verdana 10'),sg.Text(str(m_gruposPioresrar[8]), size=(12, 0),text_color='white',background_color='red',font='Verdana 10',justification='center'),sg.Text(m_gruposMelhoresrar[8], size=(12, 0),text_color='black',background_color='light green',font='Verdana 10',justification='center'),sg.Text('9º prêmio', size=(8, 0),font='Arial 10'),sg.Text(linhasMostrar[8][0],size=(6,0),font='Arial 10',background_color=coresMostrar[8][0]),sg.Text(linhasMostrar[8][1],size=(6,0),font='Arial 10',background_color=coresMostrar[8][1]),sg.Text(linhasMostrar[8][2],size=(6,0),font='Arial 10',background_color=coresMostrar[8][2]),sg.Text(linhasMostrar[8][3],size=(6,0),font='Arial 10',background_color=coresMostrar[8][3]),sg.Text(linhasMostrar[8][4],size=(6,0),font='Arial 10',background_color=coresMostrar[8][4]),sg.Text(linhasMostrar[8][5],size=(6,0),font='Arial 10',background_color=coresMostrar[8][5]),sg.Text(linhasMostrar[8][6],size=(6,0),font='Arial 10',background_color=coresMostrar[8][6]),sg.Text(linhasMostrar[8][7],size=(6,0),font='Arial 10',background_color=coresMostrar[8][7]),sg.Text(linhasMostrar[8][8],size=(6,0),font='Arial 10',background_color=coresMostrar[8][8]),sg.Text(linhasMostrar[8][9],size=(6,0),font='Arial 10',background_color=coresMostrar[8][9])],
            [sg.Text('10º prêmio', size=(8, 0),font='Arial 10'),sg.Text(str(m_ausenciasrar[9]), size=(8, 0),justification='center'),sg.Text(str(m_gruposAusentesrar[9]), size=(15, 0),font='Verdana 10'),sg.Text(str(m_gruposPioresrar[9]), size=(12, 0),text_color='white',background_color='red',font='Verdana 10',justification='center'),sg.Text(m_gruposMelhoresrar[9], size=(12, 0),text_color='black',background_color='light green',font='Verdana 10',justification='center'),sg.Text('10º prêmio', size=(8, 0),font='Arial 10'),sg.Text(linhasMostrar[9][0],size=(6,0),font='Arial 10',background_color=coresMostrar[9][0]),sg.Text(linhasMostrar[9][1],size=(6,0),font='Arial 10',background_color=coresMostrar[9][1]),sg.Text(linhasMostrar[9][2],size=(6,0),font='Arial 10',background_color=coresMostrar[9][2]),sg.Text(linhasMostrar[9][3],size=(6,0),font='Arial 10',background_color=coresMostrar[9][3]),sg.Text(linhasMostrar[9][4],size=(6,0),font='Arial 10',background_color=coresMostrar[9][4]),sg.Text(linhasMostrar[9][5],size=(6,0),font='Arial 10',background_color=coresMostrar[9][5]),sg.Text(linhasMostrar[9][6],size=(6,0),font='Arial 10',background_color=coresMostrar[9][6]),sg.Text(linhasMostrar[9][7],size=(6,0),font='Arial 10',background_color=coresMostrar[9][7]),sg.Text(linhasMostrar[9][8],size=(6,0),font='Arial 10',background_color=coresMostrar[9][8]),sg.Text(linhasMostrar[9][9],size=(6,0),font='Arial 10',background_color=coresMostrar[9][9])],
            [sg.Text('', size=(30, 0))],
            [sg.Text('Observações', size=(30, 0))],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
janelaFinal = sg.Window('Análise Unificada - versão 6.0.1 - Zimzalabim', layoutFinal)
# Event Loop to process "events" and get the "values" of the inputs

while True:
    event, values = janelaFinal.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    elif event == 'Ok':
        break
    print('You entered ', values[0])

janelaFinal.close()

