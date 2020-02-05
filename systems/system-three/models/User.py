class User:
    def __init__(self):
        self.lastSearchCreditBureau = {}
        self.cpf = ""
        self.financialTransaction = []
        self.lastPurchaseWithCreditCard = {}
    
    def getLastSearchCreditBureau(self):
        return self.lastSearchCreditBureau
    
    def setLastSearchCreditBureau(self, lastSearchCreditBureau):
        self.lastSearchCreditBureau = lastSearchCreditBureau
        
    def getCpf(self):
        return self.cpf
    
    def setCpf(self, cpf):
        self.cpf = cpf
    
    def getFinancialTransaction(self):
        return self.financialTransaction

    def setFinancialTransaction(self, financialTransaction):
        self.financialTransaction = financialTransaction

    def getLastPurchaseWithCreditCard(self):
        return self.lastPurchaseWithCreditCard
    
    def setLastPurchaseWithCreditCard(self, lastPurchaseWithCreditCard):
        self.lastPurchaseWithCreditCard = lastPurchaseWithCreditCard
        