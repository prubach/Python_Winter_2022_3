from bank_model import init_db, Bank, DBSession, Customer

db = DBSession.db_session()

def initialize():
    init_db()
    my_bank = Bank('Python Bank')
    db.add(my_bank)
    db.commit()



def add_data():
    bank = db.query(Bank).filter(Bank.id == 1).first()
    c = bank.create_customer('John', 'Brown', 'john@brown')
    db.add(c)
    print(c)
    a = bank.create_account(c)
    db.add(a)
    a2 = bank.create_account(c)
    db.add(a2)
    print(a)
    c2 = bank.create_customer('Anne', 'Smith', 'anne@smith')
    db.add(c2)
    a3 = bank.create_account(c2)
    db.add(a3)
    print(bank)
    db.commit()

def perform_operations():
    custs = db.query(Customer).filter(Customer.lastname.like('Br%')).all()
    for c in custs:
        print(c)
        for a in c.accounts:
            print(a)
            a.deposit(1000)
            db.merge(a)
        print(c.accounts)
    db.commit()


if __name__ == '__main__':
    #initialize()
    #add_data()
    perform_operations()

#
# bank = Bank()
#
# c = bank.create_customer('John', 'Brown')
# print(c)
# a = bank.create_account(c)
# a2 = bank.create_account(c)
# print(a)
#
# c2 = bank.create_customer('Anne', 'Smith')
# a3 = bank.create_account(c2)
# print(bank)
# print('--------')
# try:
#     #a = None
#     #raise ValueError('aafafa')
#     #a.deposit(330)
#     a3.deposit(100)
#     #a3.deposit(-50)
# except BankException as ie:
#     print(f'Something went wrong {ie}')
# #except (InvalidAmountException, InsufficientFundsException) as ie:
# #    print(f'Something went wrong {ie}')
# except Exception as e:
#     print(f'Exception was thrown: {e}')
# else:
#     print('Run it when no exception occured')
# finally:
#     print('This was run at the end')
#
#
# # if a3.deposit(100):
# #     print('deposit succeeded')
# # else:
# #     print('deposit failed')
# # print(bank)
# # if a3.deposit(-50):
# #     print('deposit succeeded')
# # else:
# #     print('deposit failed')
# print('before transfer')
# print(bank)
# bank.transfer(1003, 1002, 140)
# print('after transfer')
# print(bank)
