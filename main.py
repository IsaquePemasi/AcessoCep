from acesso_cep import BuscaEndereco

cep = "01001000"
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)
a = objeto_cep.acessa_via_cep()
print(type(a))
print(dir(a))

bairro, localidade, uf = objeto_cep.acessa_via_cep()
print(bairro, localidade, uf)