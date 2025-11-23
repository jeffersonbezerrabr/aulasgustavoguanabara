# Curso Python #19 - Dicionários

# https://www.youtube.com/watch?v=ZWj8o692qGY&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=22&t=1s

# pessoas = {"nome": "Gustavo", "sexo": "M", "idade": 22}

# print(pessoas)
# print("="*30)
# print(pessoas["nome"])
# print("="*30)
# print(pessoas["idade"])
# print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")
# print("="*30)
# print(pessoas.keys())
# print("="*30)
# print(pessoas.values())
# print("="*30)
# print(pessoas.items())
# print("="*30)
# print()

# # for k in pessoas.keys():
# #     print(k)
    
# # for k, v in pessoas.items():
# #     print(f"{k} = {v}")
    
# # del pessoas["sexo"]

# pessoas["nome"] = "Leandro"
# pessoas["peso"] = 98.5

# for k, v in pessoas.items():
#     print(f"{k} = {v}")
    
# brasil = []
# estado1 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
# estado2 = {"uf": "São Paulo", "sigla": "SP"}
# brasil.append(estado1)
# brasil.append(estado2)

# print(brasil[0]["uf"])
# print(brasil[1]["sigla"])

estado = {}
brasil = []

for c in range(0, 3):
    estado["uf"] = str(input("Unidade Federativa: "))
    estado["sigla"] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}")
        
    