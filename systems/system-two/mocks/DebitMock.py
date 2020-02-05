from models.Debit import Debit
import json

def mockedDebit_1():
    debit = Debit()
    
    debit.setEstablishmentName("Establishment 1")
    debit.setCnpj("23745463000188")
    debit.setDebtValue(950.45)
    debit.setDaysOfDebit(63)
    debit.setExtractId("123456789")
    
    return debit

def mockedDebit_2():
    debit = Debit()
    
    debit.setEstablishmentName("Establishment 2")
    debit.setCnpj("30172927000170")
    debit.setDebtValue(1387.20)
    debit.setDaysOfDebit(112)
    debit.setExtractId("13243546576879")
    
    return debit

def mockedDebitList():
    return [mockedDebit_1(), mockedDebit_2()]

def mockedDebitListSerialized():
    return [json.dumps(mockedDebit_1().__dict__), json.dumps(mockedDebit_2().__dict__)]