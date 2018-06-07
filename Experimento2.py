import math
def trata_leituta(linha, vet):
    if(linha.find("\n")>-1):
        linha=linha.split("\n")
        vet.append(float(linha[0]))
    else:
        vet.append(float(linha))
def Valor_Medio(vet):
    media=0
    for i in vet:
        media=media+i
    media=media/len(vet)
    return(media)
def Desvio_Padrao(vet, media):
    Somatorio_De_Diferencas=0
    for valor in vet:
        Somatorio_De_Diferencas+=((valor- media)**2)
    Desvio=math.sqrt(Somatorio_De_Diferencas/len(vet))
    return Desvio
def Casas_Decimais_Do_Erro(erro):
    str_erro=str(erro)
    casas=0
    str_erro=str_erro.split(".")
    for numero in str_erro[1]:
        casas+=1
        if numero!="0":
            return  casas
    return casas
print("Bem-Vindo ao progrma de Física Expiremental experimento (2).")
print("Este programa é opensource.\nSinta-se a vontade para olhar seu codigo fonte e até mesmo modificá-lo")
print("O objetivo desse programa é obeter a velocidade inicial da bola ao deixar a calha a partir da equação:")
print("          ______________")
print("         /   g*x²")
print("V0 = \\  /  _______  ")
print("      \\/     2*y    ")
print("E a incerteza de V0, σ dada pela formula:")
print("          ___________________________")
print("         /  dV0            dV0       ")
print("σV0= \\  / ______  *σx  + ______ *σy ")
print("      \\/    dx             dy       ")
g=980
nome_arq = input("Digite o nome do arquivo contendo os X's obtidos  \nsendo x a distância obtida: ")
arq_x= open(nome_arq,"r")
xvet = []
for distancia in arq_x:
    if(distancia.find(" ")>-1):
        distancia=distancia.split(" ")
        print(distancia)
        for num in distancia:
            trata_leituta(num,xvet)
    else:
        trata_leituta(distancia,xvet)
arq_x.close()
y=float(input("digite y sendo Y a altura:" ))
x=0
x=Valor_Medio(xvet)
v0= math.sqrt((g/(2*y))*(x**2))
v0=v0/100
errY=float(input("Digite o erro da altura em cm: ")) #0.1
errY=errY**2
errY=round(errY,2)
errX=Desvio_Padrao(xvet,x)
errX=errX**2
errX=round(errX,2)
dx=(math.sqrt(g)/(2*y))
dy=(-x/(2*g))*math.sqrt(g/2*y)
errV0=math.sqrt((dx*errX)+(dy*errY))
errV0=errV0/100
arredonda =Casas_Decimais_Do_Erro(errV0)
errV0=round(errV0,arredonda)
v0=round(v0,arredonda)
print("V0 = "+str(v0)+"m/s +/- "+str(errV0))

