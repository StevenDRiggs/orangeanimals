from sys import argv
from os import remove
from datetime import datetime, date

from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database = 'mysql+mysqlconnector://{}:{}@localhost:3306'

if len(argv) == 1:  # test mode
    with open('test.db', 'w') as db:
        pass

    engine = create_engine('sqlite:///test.db')
    Base = declarative_base(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    from oa_classes import Record, DepositFromCheque, Bonus, CreditCard, HousingRepair

    t = 'before tests'
    try:
        # cls.create() test

        t = 'DepositFromCheque.create()'
        DepositFromCheque.create(bank_name='Test Federal', bank_routing_num='123456789', cheque_author='Amazon', cheque_num=12345, date_of_rec=datetime(2019, 1, 1), account_name='DFC Test', account_num='5', amount=15000.00, is_regular=True, frequency='1M', regular_end_date=datetime(2099, 12, 31), description='Test for Deposit From Cheque', target='DFC Test')

        t = 'Bonus.create()'
        Bonus.create(account_name='Bonus Test', amount=100.00)

        t = 'CreditCard.create()'
        CreditCard.create(interest_rate=25.00, priority=25, sub_priority=5, date_of_rec=datetime(2019, 3, 3), account_name='Credit Card Test', account_num='7', amount=12.00, is_regular=True, frequency='1M', regular_end_date=datetime(2099, 10, 29), description='Test for Credit Card', target='Credit Card Test')

        t = 'HousingRepair.create()'
        HousingRepair.create(priority=17, account_name='Housing Repair Test', amount=25.00)

        session.close()
        engine.dispose()

        del Base
        del session
        del Session
        del engine

        # connect with new session test

        engine = create_engine('sqlite:///test.db', echo=True)
        Base = declarative_base(bind=engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # cls.read() test

        t = 'Record.read()'
        q = Record.read()
        if q:
            t += 'q.count() == 4'
            assert q.count() == 4
        else:
            print(f'Test failed: Zero records found at {t}')
            quit()
        
        t = 'DepositFromCheque.read()'
        q = DepositFromCheque.read()
        if q:
            t += ': q.count() == 1'
            assert q.count() == 1
            t += ': values mismatch'
            assert (q[0].rec_id, q[0].bank_name, q[0].bank_routing_num, q[0].cheque_author, q[0].cheque_num, q[0].date_of_rec, q[0].date_entered, q[0].account_name, q[0].account_num, q[0].amount, q[0].is_regular, q[0].frequency, q[0].regular_end_date, q[0].description, q[0].target) == (1, 'Test Federal', '123456789', 'Amazon', 12345, date(2019, 1, 1), date.today(), 'DFC Test', '5', 15000.00, True, '1M', date(2099, 12, 31), 'Test for Deposit From Cheque', 'DFC Test')
        else:
            print(f'Test failed: Zero records found at {t}')
            quit()

        t = 'Bonus.read()'
        q = Bonus.read()
        if q:
            t += ': q.count() == 1'
            assert q.count() == 1
            t += ': values mismatch'
            assert (q[0].rec_id, q[0].date_of_rec, q[0].date_entered, q[0].account_name, q[0].account_num, q[0].amount, q[0].is_regular, q[0].frequency, q[0].regular_end_date, q[0].description, q[0].target) == (2, None, date.today(), 'Bonus Test', None, 100.00, False, None, None, None, None)
        else:
            print(f'Test failed: Zero records found at {t}')
            quit()

        t = 'CreditCard.read()'
        q = CreditCard.read()
        if q:
            t += ': q.count() == 1'
            assert q.count() == 1
            t += ': values mismatch'
            assert (q[0].rec_id, q[0].interest_rate, q[0].priority, q[0].sub_priority, q[0].date_of_rec, q[0].date_entered, q[0].account_name, q[0].account_num, q[0].amount, q[0].is_regular, q[0].frequency, q[0].regular_end_date, q[0].description, q[0].target) == (3, 25.00, 25, 5, date(2019, 3, 3), date.today(), 'Credit Card Test', '7', 12.00, True, '1M', date(2099, 10, 29), 'Test for Credit Card', 'Credit Card Test')
        else:
            print(f'Test failed: Zero records found at {t}')
            quit()

        t = 'HousingRepair.read()'
        q = HousingRepair.read()
        if q:
            t += ': q.count() == 1'
            assert q.count() == 1
            t += ': values mismatch'
            assert (q[0].rec_id, q[0].priority, q[0].sub_priority, q[0].date_of_rec, q[0].date_entered, q[0].account_name, q[0].account_num, q[0].amount, q[0].is_regular, q[0].frequency, q[0].regular_end_date, q[0].description, q[0].target) == (4, 2, None, None, date.today(), 'Housing Repair Test', None, 25.00, False, None, None, None, None)
        else:
            print(f'Test failed: Zero records found at {t}')
            quit()

        # cls.update() test

        t = 'DepositFromCheque.update()'
        DepositFromCheque.update(rec_num=1, cheque_author='Google', amount=25000.0)
        q = DepositFromCheque.read()
        assert (q[0].cheque_author, q[0].amount) == ('Google', 25000.0)

        t = 'Bonus.update()'
        Bonus.update(rec_num=2, date_of_rec=date(2019, 6, 16), is_regular=True, frequency='6M')
        q = Bonus.read()
        assert (q[0].date_of_rec, q[0].is_regular, q[0].frequency) == (date(2019, 6, 16), True, '6M')

        t = 'CreditCard.update()'
        CreditCard.update(rec_num=3, interest_rate=15.00)
        q = CreditCard.read()
        assert q[0].interest_rate == 15.00

        t = 'HousingRepair.update()'
        HousingRepair.update(rec_num=4, amount=2500.0, description='Backhoe rescue')
        q = HousingRepair.read()
        assert (q[0].amount, q[0].description) == (2500.00, 'Backhoe rescue')

        t = 'verify number of records has not changed'
        q = Record.read()
        assert q.count() == 4

        # cls.delete() test

        t = 'DepositFromCheque.delete() test'
        DepositFromCheque.delete(rec_num=1)
        assert not DepositFromCheque.read()

        t = 'Bonus.delete() test'
        Bonus.delete(rec_num=2)
        assert not Bonus.read()

        t = 'CreditCard.delete() test'
        CreditCard.delete(rec_num=3)
        assert not CreditCard.read()

        t = 'HousingRepair.delete() test'
        HousingRepair.delete(rec_num=4)
        assert not HousingRepair.read()

    except AssertionError:
        print(f'\n\n\nTest failed on:\n{t}\n\n\n')
        quit()
    
    
    print('All tests passed.')
    quit()


elif len(argv) == 2:
    user = argv[1]
    password = ''

else:  # len(argv) > 2
    user, password = argv[1:]


engine = create_engine(database.format(user))
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

import oa_classes as oac
