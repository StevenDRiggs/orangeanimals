import orangeanimals
from orangeanimals import *
from datetime import datetime

num_tests = 67

rec1 = Membership(priority=25, date_of_rec=datetime(2019, 2, 11), account_name='Amazon Prime', amount=6.74, is_regular=True, frequency='1M')
rec2 = FastFood(priority=25, date_of_rec=datetime(2019, 2, 11), account_name='Fast Food', amount=28.68, description='Burger King')
rec3 = Vaping(priority=25, date_of_rec=datetime(2019, 2, 11), account_name='Vaping', amount=37.98, description='I Got U Vape')
rec4 = Groceries(date_of_rec=datetime(2019, 2, 11), account_name='Groceries', amount=46.22, description='Whole Foods')
rec5 = MiscFood(date_of_rec=datetime(2019, 2, 11), account_name='Deep Rock Water', amount=58.17, is_regular=True, frequency='1M')
rec6 = Vaping(priority=25, date_of_rec=datetime(2019, 2, 11), account_name='Vaping', amount=130.20, description='I Got U Vape')
rec7 = CableTV(priority=25, date_of_rec=datetime(2019, 2, 11), account_name='Comcast Xfinity', amount=192.03, is_regular=True, frequency='1M')
rec8 = Groceries(date_of_rec=datetime(2019, 2, 11), account_name='Groceries', amount=278.89, description='Costco')
rec9 = Utilities(date_of_rec=datetime(2019, 2, 11), account_name='Xcel Energy', amount=149.00, is_regular=True, frequency='1M')
rec10 = MiscFood(priority=25, date_of_rec=datetime(2019, 2, 13), account_name='Groceries', amount=39.06, description='Rocky Mountain Liquor')
rec11 = MiscFee(priority=25, date_of_rec=datetime(2019, 2, 14), account_name='Taxes', amount=15.90, description='On-Line Taxes olt.com')
rec12 = HygieneSupplies(priority=25, date_of_rec=datetime(2019, 2, 14), account_name='Feminine Hygiene', amount=63.97, description='Target')
rec13 = HygieneSupplies(priority=25, date_of_rec=datetime(2019, 2, 19), account_name='Feminine Hygiene', amount=15.62, description='Target')
rec14 = FastFood(priority=25, date_of_rec=datetime(2019, 2, 19), account_name='Fast Food', amount=19.66, description='A&W')
rec15 = Groceries(date_of_rec=datetime(2019, 2, 19), account_name='Groceries', amount=31.13, description='Barnes & Noble (tea)')
rec16 = Groceries(date_of_rec=datetime(2019, 2, 19), account_name='Groceries', amount=36.27, description='Whole Foods')
rec17 = VehiclePurchase(date_of_rec=datetime(2019, 2, 19), account_name='Car Loan', amount=98.43, is_regular=True, frequency='1M2', description='USAA')
rec18 = DepositFromCheque(cheque_author='Dad & Mom', date_of_rec=datetime(2019, 2, 21), account_name='MiscIncome', amount=50.00)
rec19 = TaxReturn(date_of_rec=datetime(2019, 2, 21), account_name='MiscIncome', amount=346.00, description='State return')
rec20 = TaxReturn(date_of_rec=datetime(2019, 2, 21), account_name='MiscIncome', amount=2180.00, description='Federal return')
rec21 = BeautySupplies(priority=25, date_of_rec=datetime(2019, 2, 21), account_name='Beauty Supplies', amount=56.48)
rec22 = Groceries(date_of_rec=datetime(2019, 2, 21), account_name='Groceries', amount=178.65)
rec23 = Wage(date_of_rec=datetime(2019, 2, 22), account_name='Covidien (Medtronic)', amount=1528.84, is_regular=True, frequency='2W')
rec24 = Vaping(priority=25, date_of_rec=datetime(2019, 2, 22), account_name='Vaping', amount=162.75)
rec25 = Event(priority=25, date_of_rec=datetime(2019, 2, 22), account_name='ComiCon', amount=183.20, description='AXS.com')
rec26 = Television(priority=25, date_of_rec=datetime(2019, 2, 25), account_name='Crunchyroll', amount=6.95, is_regular=True, frequency='1M')
rec27 = Groceries(date_of_rec=datetime(2019, 2, 25), account_name='Groceries', amount=18.67, description='Whole Foods')
rec28 = Groceries(date_of_rec=datetime(2019, 2, 25), account_name='Groceries', amount=29.86, description='Wal-Mart')
rec29 = Hair(priority=25, date_of_rec=datetime(2019, 2, 25), account_name='QVC', amount=33.28, description='payment 5/6')
rec30 = Hair(priority=25, date_of_rec=datetime(2019, 2, 25), account_name='QVC', amount=35.01, description='payment 5/6')
rec31 = VehicleFuel(date_of_rec=datetime(2019, 2, 25), account_name='Gas', amount=37.83, description='Shell (Boulder)')
rec32 = Groceries(date_of_rec=datetime(2019, 2, 25), account_name='Groceries', amount=45.32, description='Whole Foods')
rec33 = HealthFitness(priority=25, date_of_rec=datetime(2019, 2, 25), account_name='Keto', amount=49.50, description='Amazon')
rec34 = HealthFitness(priority=25, date_of_rec=datetime(2019, 2, 25), account_name='Vitamins & Supplements', amount=64.88, description='GNC')
rec35 = PetFood(priority=25, date_of_rec=datetime(2019, 2, 25), account_name='Pet Food', amount=121.09, description='Willow Run Feed Store')
rec36 = PetSupply(priority=25, date_of_rec=datetime(2019, 2, 26), account_name='Pet Toys and Supplies', amount=30.32, description='PetSmart')
rec37 = HealthFitness(priority=25, date_of_rec=datetime(2019, 2, 26), account_name='Keto', amount=56.99, description='Amazon')
rec38 = HealthFitness(priority=25, date_of_rec=datetime(2019, 2, 27), account_name='Keto', amount=4.94, description='Amazon')
rec39 = Membership(priority=25, date_of_rec=datetime(2019, 2, 27), account_name='Dropbox', amount=9.99, is_regular=True, frequency='1M')
rec40 = VideoGame(priority=25, date_of_rec=datetime(2019, 2, 27), account_name='The Sims', amount=19.99, description='Strangerville')
rec41 = Disability(date_of_rec=datetime(2019, 2, 28), account_name='VACP', amount=1215.86, is_regular=True, frequency='1M')
rec42 = ReapportionOut(target='Savings', priority=25, date_of_rec=datetime(2019, 2, 28), account_name='MiscOutput', amount=1000.00)
rec43 = VehiclePurchase(date_of_rec=datetime(2019, 3, 1), account_name='Car Loan', amount=98.43, is_regular=True, frequency='1M2')
rec44 = MiscInput(date_of_rec=datetime(2019, 3, 4), account_name='MiscInput', amount=0.05, description='PayPal VerifyBank')
rec45 = MiscInput(date_of_rec=datetime(2019, 3, 4), account_name='MiscInput', amount=0.11, description='PayPal VerifyBank')
rec46 = Movie(priority=25, date_of_rec=datetime(2019, 3, 4), account_name='Movies', amount=5.99, description='Roku/Unknown')
rec47 = VideoGame(priority=25, date_of_rec=datetime(2019, 3, 4), account_name='Black Desert Online', amount=20.16, description='PayPal')
rec48 = VideoGame(priority=25, date_of_rec=datetime(2019, 3, 4), account_name='Black Desert Online', amount=30.24, description='PayPal')
rec49 = HealthFitness(priority=25, date_of_rec=datetime(2019, 3, 4), account_name='Keto', amount=33.65, description='Amazon')
rec50 = VideoGame(priority=25, date_of_rec=datetime(2019, 3, 4), account_name='Black Desert Online', amount=100.80, description='PayPal')
rec51 = VideoGame(priority=25, date_of_rec=datetime(2019, 3, 4), account_name='Black Desert Online', amount=100.80, description='PayPal')
rec52 = CellularPhone(priority=25, date_of_rec=datetime(2019, 3, 4), account_name='Sprint', amount=139.92, is_regular=True, frequency='1M')
rec53 = MiscInput(date_of_rec=datetime(2019, 3, 4), account_name='MiscInput', amount=0.16, description='PayPal VerifyBank')
rec54 = MiscOutput(priority=25, date_of_rec=datetime(2019, 3, 4), account_name='Costco Card', amount=201.61, is_regular=True, frequency='1M')
rec55 = HousingRent(date_of_rec=datetime(2019, 3, 4), account_name='Rent', amount=1918.13)
rec56 = Groceries(date_of_rec=datetime(2019, 3, 5), account_name='Groceries', amount=14.33)
rec57 = HealthFitness(priority=25, date_of_rec=datetime(2019, 3, 5), account_name='Keto', amount=97.31, description='GNC')
rec58 = LifeInsurance(priority=25, date_of_rec=datetime(2019, 3, 5), account_name='Life Insurance', amount=30.00, is_regular=True, frequency='1M')
rec59 = RentersInsurance(priority=25, date_of_rec=datetime(2019, 3, 5), account_name="Renter's Insurance", amount=184.47, is_regular=True, frequency='1M')
rec60 = Television(priority=25, date_of_rec=datetime(2019, 3, 7), account_name='Hulu', amount=11.99, is_regular=True, frequency='1M')
rec61 = Wage(date_of_rec=datetime(2019, 3, 8), account_name='Covidien (Medtronic)', amount=1514.57, is_regular=True, frequency='2W')
rec62 = Groceries(date_of_rec=datetime(2019, 3, 8), account_name='Groceries', amount=13.67, description='Sprouts Farmers Market')
rec63 = Groceries(date_of_rec=datetime(2019, 3, 8), account_name='Groceries', amount=44.21, description='Whole Foods')
rec64 = Groceries(date_of_rec=datetime(2019, 3, 8), account_name='Groceries', amount=55.53, description='Natural Grocers')
rec65 = Groceries(date_of_rec=datetime(2019, 3, 8), account_name='Groceries', amount=250.73, description='Costco')
rec66 = VideoGame(priority=25, date_of_rec=datetime(2019, 3, 8), account_name='Black Desert Online', amount=100.00, description='PayPal (Kakao Games Europe)')
rec67 = VideoGame(priority=25, date_of_rec=datetime(2019, 3, 8), account_name='Black Desert Online', amount=100.00, description='PayPal (Kakao Games Europe)')

if __name__ == '__main__':
    engine = create_engine('sqlite:///test.db', echo=True)
    Session = sessionmaker(engine)
    session = Session()
    Base.metadata.create_all(engine)

    for i in range(1, num_tests+1):
        exec(f'session.add(rec{i})')

    session.commit()
    names = set()

    for item in session:
        names.add(type(item).__name__)

    for name in names:
        print(name)
        q = eval(f'{name}.read()')
        for rec in q:
            print(rec.date_of_rec, rec.amount)
