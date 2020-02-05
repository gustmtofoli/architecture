from models.User import User
from mocks import DebitMock as debitMock

def mockedUserInfos():
        user = User()

        user.setAge("25")
        user.setCpf("22544050047")
        user.setAssetsList([{'name': 'asset 1', 'value': '15322.98'}, {'name': 'asset 2', 'value': '20049.03'}])
        user.setAddress("Rua de Maringá")
        user.setDebtList(debitMock.mockedDebitListSerialized())
        user.setSourceOfIncome([{'sourceName': 'source 1'}])

        return user