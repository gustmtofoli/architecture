from validate_docbr import CPF

validatorCPF = CPF()

def isValidCpf(cpf):
    return validatorCPF.validate(cpf)