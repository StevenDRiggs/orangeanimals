from orangeanimals import *
from datetime import datetime

rec1 = Membership(priority=25, date_of_rec=datetime.date(2019, 2, 11), account_name='Amazon Prime', amount=6.74, is_regular=True, frequency='1M')
rec2 = FastFood(priority=25, date_of_rec=datetime.date(2019, 2, 11), account_name='Fast Food', amount=28.68, description='Burger King')
rec3 = Vaping(priority=25, date_of_rec=datetime.date(2019, 2, 11), account_name='Vaping', amount=37.98, description='I Got U Vape')
rec4 = Groceries(date_of_rec=datetime.date(2019, 2, 11), account_name='Groceries', amount=46.22, description='Whole Foods')
rec5 = MiscFood(date_of_rec=datetime.date(2019, 2, 11), account_name='Deep Rock Water', amount=58.17, is_regular=True, frequency='1M')
rec6 = Vaping(priority=25, date_of_rec=datetime.date(2019, 2, 11), account_name='Vaping', amount=130.20, description='I Got U Vape')
rec7 = CableTV(priority=25, date_of_rec=datetime.date(2019, 2, 11), account_name='Comcast Xfinity', amount=192.03, is_regular=True, frequency='1M')
rec8 = Groceries(date_of_rec=datetime.date(2019, 2, 11), account_name='Groceries', amount=278.89, description='Costco')
rec9 = Utilities(date_of_rec=datetime.date(2019, 2, 11), account_name='Xcel Energy', amount=149.00, is_regular=True, frequency='1M')
rec10 = MiscFood(priority=25, date_of_rec=datetime.date(2019, 2, 13), account_name='Groceries', amount=39.06, description='Rocky Mountain Liquor')
rec11 = MiscFee(priority=25, date_of_rec=datetime.date(2019, 2, 14), account_name='Taxes', amount=15.90, description='On-Line Taxes olt.com')
rec12 = HygieneSupplies(priority=25, date_of_rec=datetime.date(2019, 2, 14), account_name='Feminine Hygiene', amount=63.97)
rec13 = HygieneSupplies(priority=25, date_of_rec=datetime.date(2019, 2, 19), account_name='Feminine Hygiene', amount=15.62)

session.commit()
