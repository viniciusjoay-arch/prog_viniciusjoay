"""Lista A - Python, listas, busca e custo.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Os exercicios do Bloco 3 devolvem DOIS valores: o resultado e a contagem.
"""

# ---------- Bloco 1: listas e percurso ----------

def conta_negativos(lista):
    contador=0
    for n in lista  if(lista[n]<0):
        contador = contador + 1
    return contador


def media(lista):
   resultado=0
   for n in lista:
        resultado> resultador + n
        resultado=resultado / len(lista)

    return resultado
    


def sem_o_maior(lista):
        if not lista:
        return []

        maior = max(lista)
        nova = []
        ja_tirou = False

        for n in lista:
            if n == maior and not ja_tirou:
                ja_tirou = True
            else:
                nova.append(n)
        return nova
    


def acumulada(lista):
    resultado = []
    soma = 0

        for numero in lista:
            soma += numero
                resultado.append(soma)

        return resultado


def achata(lista_de_listas):
    resultado = []

    for sublista in lista_de_listas:
        for elemento in sublista:
            resultado.append(elemento)

    return resultado


# ---------- Bloco 2: busca ----------

def busca_ultima(lista, alvo):
    ultima = -1

    for i in range(len(lista)):
        if lista[i] == alvo:
            ultima = i

    return ultima


def conta_ocorrencias(lista, alvo):
    contador = 0
    for elemento in lista:
        if elemento == alvo:
            contador += 1  
    return contador

    


def primeiro_maior_que(lista, limite):
    """Posicao do primeiro elemento maior que limite, ou -1."""
    for i in range(len(lista)):
        if lista[i] > limite:
            return i
    return -1


def busca_binaria_primeira(lista, alvo):
    """(Desafio) Lista JA ORDENADA, o alvo pode repetir.
    Devolve a PRIMEIRA posicao do alvo, ou -1. Sem percorrer tudo."""
    inicio = 0
    fim = len(lista) - 1
    resultado = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            resultado = meio
            fim = meio - 1
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return resultado


# ---------- Bloco 3: custo ----------

def soma_pares_contando(lista):
    """(soma_dos_pares, operacoes). Conte 1 por elemento examinado."""
    soma_dos_pares = 0
    operacoes = 0

    for i in range(len(lista)):
        operacoes += 1

        if lista[i] % 2 == 0:
            soma_dos_pares += lista[i]

    return soma_dos_pares, operacoes


def maior_contando(lista):
    """(maior, comparacoes). Lista nao vazia.
    Conte 1 comparacao por elemento a partir do segundo."""
    maior = lista[0]
    comparacoes = 0

    for i in range(1, len(lista)):
        comparacoes += 1

        if lista[i] > maior:
            maior = lista[i]

    return maior, comparacoes


def tem_soma_contando(lista, alvo):
    """(True/False, comparacoes). Existem dois elementos que somam alvo?
    Conte 1 por par comparado. Pare assim que achar."""
    comparacoes = 0

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            comparacoes += 1

            if lista[i] + lista[j] == alvo:
                return True, comparacoes

    return False, comparacoes


def ordenada_contando(lista):
    """(Desafio) (True/False, comparacoes). A lista esta em ordem crescente?
    Conte 1 por par de vizinhos comparado. Pare no primeiro fora de ordem."""
    comparacoes = 0

    for i in range(len(lista) - 1):
        comparacoes += 1

        if lista[i] > lista[i + 1]:
            return False, comparacoes

    return True, comparacoes


# ---------- Bloco 4: padroes ----------

def inverte_no_lugar(lista):
    """Inverte a PROPRIA lista recebida. NAO cria lista nova e NAO devolve nada."""
    inicio = 0
    fim = len(lista) - 1

    while inicio < fim:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
        inicio += 1
        fim -= 1


def eh_palindromo(lista):
    """True se a lista e igual lida de tras para frente."""
    inicio = 0
    fim = len(lista) - 1

    while inicio < fim:
        if lista[inicio] != lista[fim]:
            return False

        inicio += 1
        fim -= 1

    return True


def par_que_soma(lista, alvo):
    """Lista JA ORDENADA. Devolve (i, j) das posicoes cujos valores somam alvo,
    ou (-1, -1). Sem laco dentro de laco."""
    inicio = 0
    fim = len(lista) - 1

    while inicio < fim:
        soma = lista[inicio] + lista[fim]

        if soma == alvo:
            return inicio, fim
        elif soma < alvo:
            inicio += 1
        else:
            fim -= 1

    return -1, -1


def soma_maxima_janela(lista, k):
    """Maior soma de k elementos seguidos.
    soma_maxima_janela([1, 2, 3, 4], 2) -> 7"""
    soma = sum(lista[:k])
    maior = soma

    for i in range(k, len(lista)):
        soma = soma - lista[i - k] + lista[i]

        if soma > maior:
            maior = soma

    return maior


def parenteses_balanceados(texto):
    """(Desafio) True se os ( ) e [ ] do texto abrem e fecham na ordem certa."""
    pilha = []

    for caractere in texto:
        if caractere == '(' or caractere == '[':
            pilha.append(caractere)

        elif caractere == ')':
            if len(pilha) == 0 or pilha[-1] != '(':
                return False
            pilha.pop()

        elif caractere == ']':
            if len(pilha) == 0 or pilha[-1] != '[':
                return False
            pilha.pop()

    return len(pilha) == 0