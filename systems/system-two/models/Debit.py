class Debit:
    def __init__(self):
        self.establishmentName = ""
        self.cnpj = ""
        self.debtValue = 0
        self.daysOfDebit = 0
        self.extractId = ""
    
    def getEstablishmentName(self):
        return self.establishmentName

    def setEstablishmentName(self, establishmentName):
        self.establishmentName = establishmentName
    
    def getCnpj(self):
        return self.cnpj
    
    def setCnpj(self, cnpj):
        self.cnpj = cnpj
    
    def getDebtValue(self):
        return self.debtValue
    
    def setDebtValue(self, debtValue):
        self.debtValue = debtValue
    
    def getDaysOfDebit(self):
        return self.daysOfDebit
    
    def setDaysOfDebit(self, daysOfDebit):
        self.daysOfDebit = daysOfDebit
    
    def getExtractId(self):
        return self.extractId
    
    def setExtractId(self, extractId):
        self.extractId = extractId
         