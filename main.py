from acesso_cep import BuscaEndereco

cep = input("Digite seu CEP: ")
#exemplo de cep = "01001000"

objeto_cep = BuscaEndereco(cep)
a = objeto_cep.acessa_via_cep()

cep, logradouro, complemento, bairro, localidade, uf, ddd, ibge, gia, siafi = objeto_cep.acessa_via_cep()
print(f'CEP: {cep}\nLogradouro: {logradouro}\nComplemento: {complemento}\nBairro: {bairro}\nLocalidade: {localidade}\nUF: {uf}\nDDD: {ddd}\nIBGE: {ibge}\nGIA: {gia}\nSIAFI: {siafi}')