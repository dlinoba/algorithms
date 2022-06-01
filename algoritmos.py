from datetime import date
import datetime


def split_words(texto):
    palavra = ''
    lista = []
    lista_completa = []
    valores = []
    tamanho = len(texto)
    cont = 0
    for i in texto:
        cont +=1
        if i != ' ':
            palavra += i
        if i == ' ' or cont == tamanho:
            lista.append(palavra)
            palavra = ''    
    for palavra in lista:
        if palavra not in valores:
            valores.append(palavra)
    for p in valores:
        lista_completa.append([p,lista.count(p)])
    return lista_completa


def interseccao_data(periodo1_dt_ini,
                    periodo1_dt_fim,
                    periodo2_dt_ini,
                    periodo2_dt_fim):
    periodo1_lista_datas = []
    periodo2_lista_datas = []

    periodo1_dataini = datetime.datetime.strptime(periodo1_dt_ini, '%d/%m/%Y').date()
    periodo1_datafim = datetime.datetime.strptime(periodo1_dt_fim, '%d/%m/%Y').date()
    periodo1_dataini = date.fromordinal(periodo1_dataini.toordinal()-1)
    periodo1_dif = periodo1_datafim - periodo1_dataini
    periodo1_dias = periodo1_dif.days

    while periodo1_dias > 0:
        periodo1_data_atualizada = date.fromordinal(periodo1_dataini.toordinal()+periodo1_dias)
        periodo1_dias -= 1
        periodo1_lista_datas.append(str(periodo1_data_atualizada))

        periodo2_dataini = datetime.datetime.strptime(periodo2_dt_ini, '%d/%m/%Y').date()
        periodo2_datafim = datetime.datetime.strptime(periodo2_dt_fim, '%d/%m/%Y').date()
        periodo2_dataini = date.fromordinal(periodo2_dataini.toordinal()-1)
        periodo2_dif = periodo2_datafim - periodo2_dataini
        periodo2_dias = periodo2_dif.days
    
    while periodo2_dias > 0:
        periodo2_data_atualizada = date.fromordinal(periodo2_dataini.toordinal()+periodo2_dias)
        periodo2_dias -= 1
        periodo2_lista_datas.append(str(periodo2_data_atualizada))

    resultado = list(set(periodo1_lista_datas) & set(periodo2_lista_datas))
    if len(resultado) == 0:
        return False
    else:
        return True

texto = split_words('C# Python Java Python Node Node Python')
#verificar quantas vezes a palavra aparece no texto
print('Verificando as Palavras do Texto e Quantidades')
for i in texto:
    print(i)

print('-'*20)
#setando datas
periodo1_data_inicial = '26/02/2022'
periodo1_data_final = '02/03/2022'
periodo2_data_inicial = '01/03/2022'
periodo2_data_final = '10/03/2022'

interseccao = interseccao_data(periodo1_data_inicial,periodo1_data_final,periodo2_data_inicial,periodo2_data_final)
#Verificando se há intersecção das datas
print('Há intersecção entre as datas ?: ')
print(interseccao)