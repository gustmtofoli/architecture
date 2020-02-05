from models.User import User
from mocks import DebitMock as debitMock

def mockedUserInfos():
        user = User()

        user.setName("Gustavo")
        user.setCpf("22544050047")
        user.setAddress("Rua de Maringá")
        user.setDebtList(debitMock.mockedDebitListSerialized())

        return user