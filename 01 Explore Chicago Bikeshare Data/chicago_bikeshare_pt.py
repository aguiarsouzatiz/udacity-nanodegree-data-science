# coding: utf-8

# Começando com os imports
import csv
from zipfile import ZipFile
import matplotlib.pyplot as plt
from pprint import pprint
from statistics import mean, median

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("./dataset/chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Funções de apoio
# Imprime divisão para separar pergunta e resposta
def divider(): return print('='*50)

data_list_header = data_list[0]

def find_column_index_of(column_name):
    """
    Procura o index de por nome dentre as colunas do cabeçalho.
    Argumentos:
        column_name: nome do cabeçalho.
    Retorna:
        O index da coluna correspondente ao nome.
    """
    return data_list_header.index(column_name)

def convert_to_int(data_strings):
    """
    Converte strings em integers.
    Argumentos:
        data_strings: lista com números como strings.
    Retorna:
        Uma lista de valores em integer para cada string.
    """
    return [int(string_value) for string_value in data_strings]

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

# DONE TAREFA 1.1: Por For Loop
divider()
for index in range(0,20):
    print(data_list[index])
divider()

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# DONE TAREFA 1.2: Por List Comprehension
sample_first_20 = [line for line in data_list[:20]]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
gender_index = find_column_index_of('Gender')
sample_gender_first_20 = [line[gender_index] for line in sample_first_20]

divider()
pprint(sample_gender_first_20)
divider()

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data_list, index):
    """
    Cria uma lista a partir do index de uma determinada coluna.
    Argumentos:
        data_list: coleção de dados.
        index: posição da coluna do data_list
    Retorna:
        Uma lista da coluna indicada.
    """
    return [data[index] for data in data_list]

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
divider()
print(column_to_list(data_list, -2)[:20])
divider()

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
gender_index = find_column_index_of('Gender')
gender = column_to_list(data_list, gender_index)
male = gender.count('Male')
female = gender.count('Female')

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
divider()
print("Masculinos: ", male, "\nFemininos: ", female)
divider()

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
    Conta a quantidade de cada gênero na coleção de dados.
    Argumentos:
        data_list: coleção de dados.
    Retorna:
        Uma lista com a quantidade do gênero masculino e feminino.
        Ignora os valores vazios.
    """
    gender_index = find_column_index_of('Gender')
    gender = column_to_list(data_list, gender_index)

    return [gender.count('Male'), gender.count('Female')]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
divider()
print('[ Male | Female ]')
print(count_gender(data_list))
divider()
# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
genders_label = ["Masculino", "Feminino"]
def group_genders_by(numbers, labels):
    """
    Associa as informações duas listas de numbers e labels.
    Argumentos:
        numbers: lista com quantidade dos gêneros.
        label: lista nomes dos gêneros em string.
    Retorna:
        Um dicionário com cada label associada a seu valor.
    """
    return dict(zip(numbers, labels))

def most_popular_gender(data_list):
    """
    Informa qual gênero possui maior quantidade.
    Argumentos:
        data_list: coleção de dados.
    Retorna:
        Após comparar se há dois máximos iguais, uma string para 3 casos:
        Empata, masculino ou feminino em maior quantidade.
    """
    genders_number = count_gender(data_list)
    genders = group_genders_by(genders_number, genders_label)
    popular = max(genders_number)
    has_equals_max_values = genders_number.count(popular) > 1

    return 'Igual' if has_equals_max_values else genders[popular]


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
divider()
print("Gráfico sobre gênero")
divider()
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

reduce_to_unique_values = lambda column_list: set(column_list)

# Retorna uma nova lista de valores
get_unique = lambda values: [value for value in values]

def get_quantity_of(values, column_list):
    """
    Calcula quantidade de cada valor na coluna.
    Argumentos:
        values: coleção de dados únicos.
        column_list: coleção de dados com todos os valores.
    Retorna:
        Uma lista com a quantidade de cada valor
    """
    return [column_list.count(value) for value in values]

def group_values_of(data_list, index):
    """
    Combina valores únicos e a quantidade deles.
    Argumentos:
        data_list: coleção de dados.
        index: posição da coluna na coleção de dados.
    Retorna:
        Um dicionário com 2 chaves com valores únicos e de quantidade de cada um dos valores
    """
    data_without_headers = data_list[1:]
    column_list = column_to_list(data_without_headers, index)
    values = reduce_to_unique_values(column_list)
    return {
        'values': get_unique(values),
        'quantity': get_quantity_of(values, column_list)
    }

labels = {
 'Start Time': 'Tempo inicial',
 'End Time': 'Tempo final',
 'Trip Duration': 'Duração da viagem',
 'Start Station': 'Estação inicial',
 'End Station': 'Estação final',
 'User Type': 'Tipo de usuário',
 'Gender': 'Gênero',
 'Birth Year': 'Data de nascimento'
}

get_label_of = lambda column, labels: labels[column]

def generate_chart_of(column_data, column_name):
    """
    Cria um gráfico a partir dos dados.
    Argumentos:
        column_data: coleção de dados com valores únicos e a quantidade deles.
        column_name: referência para exibição da label.
    Retorna:
        Um dicionário com 2 chaves com valores únicos e de quantidade de cada um dos valores
    """
    values = column_data['values']
    quantity = column_data['quantity']
    y_pos = list(range(len(values)))
    label = get_label_of(column_name, labels)
    plt.bar(y_pos, quantity)
    plt.ylabel('Quantidade')
    plt.xlabel(f'{label}')
    plt.xticks(y_pos, values)
    plt.title(f'Quantidade por {label.lower()}')
    plt.show(block=True)

def draw_chart_by(data_list, column_name):
    """
    Fornece os dados principais para executar a criação do gráfico.
    Argumentos:
        data_list: coleção de dados.
        column_name: referência para procura do index da coluna e construção do gráfico.
    """
    index = find_column_index_of(column_name)
    column_data = group_values_of(data_list, index)
    generate_chart_of(column_data, column_name)

divider()
print("Gráfico sobre tipo de usuário")
divider()
draw_chart_by(data_list, 'User Type')
input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "A condição é falsa porque na coluna de Gênero há valores vazios. Estes são contabilizados no cálculo da quantidade de valores o que causa a diferença."
divider()
print("resposta:", answer)
divider()

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().

trip_duration_list = column_to_list(data_list, 2)

# SOLUÇÃO TAREFA 9.1 max - Por function
# def get_max_from(values):
#     final = values[0]
#     for value in values:
#         if value > final:
#             final = value
#     return final

# SOLUÇÃO TAREFA 9.2 max - Por reduce
# to_get_max = lambda previous, current: previous if previous > current else current
# reduce(to_get_max, trips_values)

# SOLUÇÃO TAREFA 9.3 max - Por sorted
trip_duration_integers = convert_to_int(trip_duration_list[1:])
min_trip = sorted(trip_duration_integers)[0]
max_trip = sorted(trip_duration_integers)[-1]
mean_trip = mean(trip_duration_integers)
median_trip = median(trip_duration_integers)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
divider()
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", median_trip, "Mediana: ", mean_trip)
divider()

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()

start_stations_index = find_column_index_of('Start Station')
start_stations_list = column_to_list(data_list, start_stations_index)
start_stations = set(start_stations_list)

print("\nTAREFA 10: Imprimindo as start stations:")
divider()
pprint(start_stations)
divider()


# Corrige variável com nome trocado. O correto seria 'start_stations' de acordo com enunciado
user_types = start_stations
# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

# input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
    #   """
    #   Função de exemplo com anotações.
    #   Argumentos:
    #       param1: O primeiro parâmetro.
    #       param2: O segundo parâmetro.
    #   Retorna:
    #       Uma lista de valores x.

    #   """

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
answer = str(input("Você vai encarar o desafio? (yes ou no): "))

def count_items(column_list):
    list_without_headers = column_list[1:]
    values = reduce_to_unique_values(list_without_headers)
    item_types = get_unique(values)
    count_items = get_quantity_of(values, column_list)
    return item_types, count_items

while not answer.lower() == "yes" and not answer.lower() == "no":
    answer = str(input("Putz, não entendi. Tente de novo com (yes or no): "))

def farewell_message():
    divider()
    print("Terminamos por aqui. Hasta la vista baby!")

def execute_challenge_task():
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------
    divider()
    farewell_message()
# TODO fix lower answer
execute_challenge_task() if answer == "yes" else farewell_message()