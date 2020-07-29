from validate_docbr import CPF, CNPJ

#Documento is a factory, uma classe que retorna outras classes de acordo com algum atributo
class Documento:
    
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos está incorreta")

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validate_cpf = CPF()
        return validate_cpf.validate(documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        cnpj = CNPJ()
        return cnpj.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

