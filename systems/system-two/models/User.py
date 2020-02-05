class User:
    def __init__(self):
        self.age = 0
        self.cpf = ""
        self.assetsList = []
        self.address = ""
        self.debtList = []
        self.sourceOfIncome = []
    
    def getAge(self):
        return self.age
    
    def setAge(self, age):
        self.age = age
        
    def getCpf(self):
        return self.cpf
    
    def setCpf(self, cpf):
        self.cpf = cpf
    
    def getAssetsList(self):
        return self.assetsList

    def setAssetsList(self, assetsList):
        self.assetsList = assetsList

    def getAddress(self):
        return self.address
    
    def setAddress(self, address):
        self.address = address
        
    def getDebtList(self):
        return self.debtList
    
    def setDebtList(self, debtList):
        self.debtList = debtList
    
    def getSourceOfIncome(self):
        return self.sourceOfIncome
    
    def setSourceOfIncome(self, sourceOfIncome):
        self.sourceOfIncome = sourceOfIncome
    

