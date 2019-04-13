from sys import argv

from sqlalchemy import create_engine, ForeignKey, Column, Integer, Date
from sqlalchemy import String, Float, Boolean
from sqlalchemy.orm import sessionmaker, with_polymorphic
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

if len(argv) == 1:  # test mode
    with open('test.db', 'w'):
        pass

    test_engine = create_engine('sqlite:///test.db', echo=True)
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

        rec_id = Column(ForeignKey(Test.rec_id))
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

        rec_id = Column(ForeignKey(Test.rec_id))
        c_data = Column(Integer, autoincrement=True)

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

    q = session.query(Test)
    for q_ in q:
        print(q_)

    q_a = session.query(SubTestA)
    for q_a_ in q_a:
        print(q_a_)

    q_b = session.query(SubTestB)
    for q_b_ in q_b:
        print(q_b_)

    q_c = session.query(SubTestC)
    for q_c_ in q_c:
        print(q_c_)
