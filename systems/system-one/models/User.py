class User:
    def __init__(self):
        self.name = ""
        self.cpf = ""
        self.address = ""
        self.debtList = []
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
        
    def getCpf(self):
        return self.cpf
    
    def setCpf(self, cpf):
        self.cpf = cpf

    def getAddress(self):
        return self.address
    
    def setAddress(self, address):
        self.address = address
    
    def getDebtList(self):
        return self.debtList

    def setDebtList(self, debtList):
        self.debtList = debtList
