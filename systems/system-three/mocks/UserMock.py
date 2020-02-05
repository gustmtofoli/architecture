from models.User import User
from mocks import DebitMock as debitMock

def mockedUserInfos():
        user = User()

        user.setLastSearchCreditBureau({'creditBureau': 'credit bureau X','date': '12/09/2019 15:33:48'})
        user.setCpf("22544050047")
        user.setFinancialTransaction([{'establishment': 'Establishment 1', 'operation': '-', 'value': '98.29', 'date': '30/12/2019 10:22:57'}])
        user.setLastPurchaseWithCreditCard({'agency': '12334', 'account': '3443223', 'establishment': 'Establishment 1', 'date': '30/12/2019 10:22:57', 'value': '98.29', 'flag': 'visa'})
        
        return user