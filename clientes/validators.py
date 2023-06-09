import re 
from validate_docbr import CPF

def cpf_valido(cpf):
    cpf_valido = CPF()
    return cpf_valido.validate(cpf)
    

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(rg):
    return len(rg) == 9

def numero_valido(numero):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero)
    return resposta
