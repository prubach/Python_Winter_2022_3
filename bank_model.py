from sqlalchemy import Column, Integer, String, Float

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(80), nullable=True)
    lastname = Column(String(80), nullable=False)
    email = Column(String(150), nullable=False)


    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def __repr__(self):
        return f'Customer[{self.id}, {self.firstname}, {self.lastname}, {self.email}]'


class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Float, default=0)

    def __init__(self, customer):
        self.customer = customer
        self.balance = 0

    def deposit(self, amount):
        #TODO implement
        if type(amount) != int or amount < 0:
            raise InvalidAmountException(f'Amount is invalid {amount}')
        self.balance += amount

    def charge(self, amount):
        #TODO implement
        if type(amount) != int or amount < 0:
            raise InvalidAmountException(f'Amount is invalid {amount}')
        self.balance -= amount


    def __repr__(self):
        return f'Account[{self.id}, {self.customer.lastname}, {self.balance}]'


class Bank(Base):
    __tablename__ = 'bank'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __init__(self, name):
        self.name = name
        self.customer_list = []
        self.account_list = []

    def create_customer(self, firstname, lastname):
        c = Customer(firstname, lastname)
        self.customer_list.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self.account_list.append(a)
        return a

    def transfer(self, from_account_id, to_account_id, amount):
        #TODO
        pass

    def find_account(self, account_id):
        #TODO
        pass

    def __repr__(self):
        return f'Bank[{self.customer_list}; {self.account_list}]'


class BankException(Exception):
    pass


class InsufficientFundsException(BankException):
    pass


class InvalidAmountException(BankException):
    pass

bank = Bank()

c = bank.create_customer('John', 'Brown')
print(c)
a = bank.create_account(c)
a2 = bank.create_account(c)
print(a)

c2 = bank.create_customer('Anne', 'Smith')
a3 = bank.create_account(c2)
print(bank)
print('--------')
try:
    #a = None
    #raise ValueError('aafafa')
    #a.deposit(330)
    a3.deposit(100)
    #a3.deposit(-50)
except BankException as ie:
    print(f'Something went wrong {ie}')
#except (InvalidAmountException, InsufficientFundsException) as ie:
#    print(f'Something went wrong {ie}')
except Exception as e:
    print(f'Exception was thrown: {e}')
else:
    print('Run it when no exception occured')
finally:
    print('This was run at the end')


# if a3.deposit(100):
#     print('deposit succeeded')
# else:
#     print('deposit failed')
# print(bank)
# if a3.deposit(-50):
#     print('deposit succeeded')
# else:
#     print('deposit failed')
print('before transfer')
print(bank)
bank.transfer(1003, 1002, 140)
print('after transfer')
print(bank)
