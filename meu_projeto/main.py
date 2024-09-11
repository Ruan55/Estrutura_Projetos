import os
from models.pessoa import Pessoa
from models.enums.sexo import Sexo

os.system("cls || clear")

aluno = Pessoa("Ruan", 22, Sexo.MASCULINO)

print(aluno)