from sys import argv
from os import remove

from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database = 'sqlite:///oa_{}.db'

if len(argv) == 1:  # test mode
    with open('test.db', 'w'):
        pass

    test_engine = create_engine(f'sqlite:///test.db', echo=True)
    Base = declarative_base()
    Session = sessionmaker(bind=test_engine)
    session = Session()

    class Test(Base):
        __tablename__ = 'test'

        rec_id = Column(Integer, primary_key=True)
        data = Column(String)

        __mapper_args__ = {
                'polymorphic_on': data,
                'polymorphic_identity': 'Test (lvl 0)',
                }

    class SubTestA(Test):
        __tablename__ = 'subtest_a'

        rec_id = Column(ForeignKey(Test.rec_id), primary_key=True)
        a_data = Column(String, default='a_data')

        __mapper_args__ = {
                'polymorphic_identity': 'Sub Test A (lvl 1)',
                }

    class SubTestB(Test):
        __mapper_args__ = {
                'polymorphic_identity': 'Sub Test B (lvl 1)',
                }

    class SubTestC(SubTestB):
        __tablename__ = 'subtest_c'

        rec_id = Column(ForeignKey(Test.rec_id), primary_key=True)
        c_data = Column(Integer, default=15)

        __mapper_args__ = {
                'polymorphic_identity': 'Sub Test C (lvl 2)',
                }

    Base.metadata.create_all(bind=test_engine)

    session.add_all([
            Test(),
            Test(),
            SubTestA(),
            SubTestA(),
            SubTestB(),
            SubTestB(),
            SubTestC(),
            SubTestC(),
            ])

    session.commit()
    session.close()
    test_engine.dispose()

    del session
    del Session
    del test_engine

    test_engine = create_engine('sqlite:///test.db', echo=True)
    Session = sessionmaker(bind=test_engine)
    session = Session()

    try:
        q = session.query(Test)
        for q_ in q:
            assert (q_.data)

        q_a = session.query(SubTestA)
        for q_a_ in q_a:
            assert (q_a_.data)
            assert (q_a_.a_data == 'a_data')

        q_b = session.query(SubTestB)
        for q_b_ in q_b:
            assert (q_b_.data)

        q_c = session.query(SubTestC)
        for q_c_ in q_c:
            assert (q_c_.data)
            assert (isinstance(q_c_.c_data, int))

        print('All tests passed.')

    except AssertionError:
        print('Test failed.')

    session.close()
    remove('test.db')
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

import orangeanimals as oa


