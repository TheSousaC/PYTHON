##Dicionários

persons = {
    "id": 1,
    "nome": "Gabriel",
    "idade": 18,
    "sexo": "Masculino"
}
print(persons)
##Caso eu queira adicionar algum dado ou informação:
# persons["Profissao"] = "De férias"
# del persons["idade"]
#
# filme = {
#     "titulo": "Zootopia 2",
#     "ano": "2025",
#     "diretor": "Jared Bush e Byron Howard"
# }

# print(filme.values())  ##Mostrará os dados. Ex.: Zootopia 2, 2025, Jared Bush e Byron Howard
#
# print(filme.keys())  ##Mostrará as chaves. Ex.: titulo, ano, diretor
#
# print(filme.items())  ##Mostrará tanto os keys como os valores. Ex.: titulo: Zootopia 2, ano: 2025, diretores: Jared Bush e Byron Howard

# ##Podemos usar em um for:
# for keys, values in filme.items():
#     print(f"{keys}: {values}")
##            key    value      key  value   key      value
##Resposta: titulo: Zootopia 2, ano: 2025, diretores: Jared Bush e Byron Howard


##Dicionarios dentro de lista

filmes = [
    {
        "id": 1,
        "titulo": "Zootopia 2",
        "ano": 2025,
        "diretor": " Jared Bush e Byron Howard"
    },
    {
        "id": 2,
        "titulo": "Truque de Mestre",
        "ano": 2013,
        "diretor": "Louis Leterrier"
    },
    {
        "id": 3,
        "titulo": "Truqe de Mestre 2",
        "ano": 2016,
        "diretor":  "Jon M. Chu e Ruben Fleischer"
    },
    {
        "id": 4,
        "titulo": "Truque de Mestre 3",
        "ano": 2025,
        "diretor": " Jared Bush e Byron Howard"
    }
]
# print(filmes[0]["titulo"]) ## Zootopia 2
# print(filmes[1]["id"]) ## É o id 2
# print(filmes[2]["diretor"]) ## Diretor do truque de mestre 2:  Jon M. Chu e Ruben Fleischer

print(filmes)
