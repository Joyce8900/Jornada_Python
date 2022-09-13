import json


cadastros =[
  {
  "Nome": "Joyce",
  "idade": 20,
  "Profissões": ["Estagiario", "Dev. Python"]
},
{
  "Nome": "Anne",
  "Idade": 27,
  "Profissões": ["Estagiario", "Dev. Python"]
}

]
print (json.dumps(cadastros, ensure_ascii=False))


##ensure_ascii=False PERMITE OS ACENTOS