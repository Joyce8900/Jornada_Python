class Pessoa:
    def __init__(self, nome, idade, cidade, genero):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.genero = genero
    def __repr__(self):
        return f"Pessoa: {self.nome}"




pessoas = {
    Pessoa ("João", 18, "Rio de Janeiro", "M"),
    Pessoa ("Maria", 30, "Manaus", "F"),
    Pessoa ("Joyce", 20, "Manaus", "F")
}
cidade = {pessoa.cidade for pessoa in pessoas}
print (cidade)
maiores_18 = {pessoa.idade for pessoa in pessoas if pessoa.idade > 18}
print(maiores_18)
sexo_M = {pessoa.genero for pessoa in pessoas if pessoa.genero.lower() == "M"}
print (sexo_M)
iniciadas_com_J = {pessoa for pessoa in pessoas if pessoa.nome[0] == "J"}
print(iniciadas_com_J)