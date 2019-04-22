from sqlalchemy import create_engine, ForeignKey, Column, Integer, Date, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, with_polymorphic
from datetime import datetime, date
import __main__


if __name__ == '__main__':
    database = 'sqlite:///test.db'
    engine = create_engine(database, echo=True)
    Base = declarative_base(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

else:
    database = __main__.database
    engine = __main__.engine
    Base = __main__.Base
    Session = __main__.Session
    session = __main__.session


# ==============================================================
# ==============================================================

class Record(Base):
    __tablename__ = 'Record'

    rec_id = Column(Integer, primary_key=True)  # auto generated
    date_of_rec = Column(Date)  # date transaction occurred
    date_entered = Column(Date, nullable=False, default=datetime.today())
    account_name = Column(String(40), nullable=False)
    account_num = Column(String(40))
    amount = Column(Float, nullable=False)
    is_regular = Column(Boolean, nullable=False, default=False)  # will this transaction regularly occur?
    frequency = Column(String(10))  # if is_regular, how often?
    regular_end_date = Column(Date)  # if is_regular, until when? (or NULL for N/A or indefinite)
    description = Column(String(255))
    target = Column(String(40))  # also from_account, to_account, company
    class_ = Column('type', String(40))
    
    # meta = Column(String(255))  # used for internal processing, not (usually) seen by user

    __mapper_args__ = {
        'polymorphic_on': class_,
        }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_ = self.__class__.__name__

    def __repr__(self):
        return f'instance of {self.__class__}:({self.__dict__})'

    @classmethod
    def create(cls, **kwargs):
        try:
            rec = cls(**kwargs)
            session.add(rec)
            session.commit()
        except:
            session.rollback()
            raise

    @classmethod
    def read(cls, type_=None):
        try:
            if type_:
                q = session.query(cls).filter(Record.class_==type_)
            else:
                type_ = cls.__name__
                q = session.query(cls)
            if q.count() > 0:
                return q
            else:
                parent = cls.__bases__[0]
                if parent is not Base:
                    return parent.read(type_)
                else:
                    raise KeyError('No records found.')

        except KeyError as e:
            print(e)
            print('Please try again.')
            session.rollback()
            return False
                
        except:
            session.rollback()
            raise

    @classmethod
    def update(cls, *, rec_num, **kwargs):
        try:
            q = cls.read().filter(Record.rec_id==rec_num)
            if q:
                rec = q[0]
                for k, v in kwargs.items():
                    if isinstance(v, str):
                        v_ = '"' + v + '"'
                    elif isinstance(v, date) or isinstance(v, datetime):
                        v_ = f'date({v.year}, {v.month}, {v.day})'
                    else:
                        v_ = str(v)
                    exec(f'rec.{k} = {v_}')
                session.commit()
            else:
                raise KeyError('No record found.')

        except:
            session.rollback()
            raise

    @classmethod
    def delete(cls, *, rec_num):
        try:
            q = cls.read().filter(Record.rec_id==rec_num)
            if q:
                rec = q[0]
                session.delete(rec)
                del rec
                session.commit()
            else:
                raise KeyError('No record found')

        except:
            session.rollback()
            raise

# ==============================================================
# ==============================================================

# ______________________________________________________________
class Input(Record):
    pass

class DepositFromCash(Input):
    pass

class DepositFromCheque(Input):
    __tablename__ = 'DepositFromCheque'
    rec_id = Column(ForeignKey(Input.rec_id), primary_key=True)
    bank_name = Column(String(40))
    bank_routing_num = Column(String(40))
    cheque_author = Column(String(40))  # required for DepositFromCheque
    cheque_num = Column(Integer)  # required for WithdrawToCheque

    @classmethod
    def create(cls, **kwargs):
        try:
            if kwargs['cheque_author']:
                super().create(**kwargs)
        except KeyError:
            session.rollback()
            raise KeyError('Deposit from Cheque requires cheque author.')

class ForeignIn(Input):
    pass

class MiscInput(Input):
    pass

class PrivateSale(Input):
    pass

class ReapportionIn(Input):

    @classmethod
    def create(cls, **kwargs):
        try:
            if kwargs['target']:
                super().create(**kwargs)
        except KeyError:
            session.rollback()
            raise KeyError('Reapportioning funds requires two accounts.')

    
# --------------------------------------------------------------
class SpecialtyPay(Input):
    pass

class Annuity(SpecialtyPay):
    pass

class BusinessReimbursement(SpecialtyPay):
    pass

class Disability(SpecialtyPay):
    pass

class InvestmentDividend(SpecialtyPay):
    pass

class RetirementIn(SpecialtyPay):
    pass

class TaxReturn(SpecialtyPay):
    pass

class TrustFundIn(SpecialtyPay):
    pass
# --------------------------------------------------------------

class TransferFromBusiness(Input):
    pass

# --------------------------------------------------------------
class Wage(Input):
    pass

class Bonus(Wage):
    pass
# --------------------------------------------------------------

# ______________________________________________________________
# ______________________________________________________________


class Output(Record):
    __tablename__ = 'Output'
    rec_id = Column(ForeignKey(Record.rec_id), primary_key=True)
    priority = Column(Integer)  # required for Output types
    sub_priority = Column(Integer)

    @classmethod
    def create(cls, **kwargs):
        try:
            if kwargs['priority']:
                super().create(**kwargs)
        except KeyError:
            session.rollback()
            raise KeyError('Output types must have a priority assigned.')

class Alimony(Output):
    pass

class ChildSupport(Output):
    pass

# --------------------------------------------------------------
class Debt(Output):
    __tablename__ = 'Debt'
    rec_id = Column(ForeignKey(Output.rec_id), primary_key=True)
    interest_rate = Column(Float)  # required for Debt types

    @classmethod
    def create(cls, **kwargs):
        try:
            if kwargs['interest_rate']:
                super().create(**kwargs)
        except KeyError:
            session.rollback()
            raise KeyError('Debt types require an interest rate.')

class CreditCard(Debt):
    pass

class Loan(Debt):
    pass

class MiscDebt(Debt):
    pass
# --------------------------------------------------------------

# --------------------------------------------------------------
class Dental(Output):
    pass

class DentalEquipment(Dental):
    pass

class DentalMedicine(Dental):
    pass

class DentalProcedure(Dental):
    pass

class DentalVisit(Dental):
    pass
# --------------------------------------------------------------

# --------------------------------------------------------------
class Expenditure(Output):
    pass

# --------------------------------------------------------------
class Bill(Expenditure):
    pass

# --------------------------------------------------------------
class FourWalls(Bill):
    pass

class Clothing(FourWalls):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.priority = 4

# --------------------------------------------------------------
class Food(FourWalls):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.priority = 1

class FastFood(Food):
    pass

class Groceries(Food):
    pass

class MiscFood(Food):
    pass

class Restaraunt(Food):
    pass
# --------------------------------------------------------------

# --------------------------------------------------------------
class Shelter(FourWalls):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.priority = 2

# --------------------------------------------------------------
class HomePurchase(Shelter):
    pass

class Mortgage(HomePurchase):
    pass
# --------------------------------------------------------------

# --------------------------------------------------------------
class HousingExpense(Shelter):
    pass

class HOAFee(HousingExpense):
    pass

class HomeSecurity(HousingExpense):
    pass

class HousingFee(HousingExpense):
    pass

class HousingRepair(HousingExpense):
    pass

class LawnCare(HousingExpense):
    pass

class Utilities(HousingExpense):
    pass
# --------------------------------------------------------------

class HousingRent(Shelter):
    pass

class MiscShelter(Shelter):
    pass
# --------------------------------------------------------------

# --------------------------------------------------------------
class Transportation(FourWalls):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.priority = 3

class MiscTransportation(Transportation):
    pass

class PublicTransit(Transportation):
    pass

# --------------------------------------------------------------
class VehicleExpense(Transportation):
    pass

class VehicleFuel(VehicleExpense):
    pass

class VehicleRepair(VehicleExpense):
    pass
# --------------------------------------------------------------

class VehicleLease(Transportation):
    pass

class VehiclePurchase(Transportation):
    pass

class VehicleRental(Transportation):
    pass
# --------------------------------------------------------------

class Internet(Bill):
    pass

class Membership(Bill):
    pass

# --------------------------------------------------------------
class PhoneService(Bill):
    pass

class CellularPhone(PhoneService):
    pass

class LandLine(PhoneService):
    pass

class SatellitePhone(PhoneService):
    pass
# --------------------------------------------------------------

# --------------------------------------------------------------
class Television(Bill):
    pass

class CableTV(Television):
    pass

class SatelliteTV(Television):
    pass
# --------------------------------------------------------------
# --------------------------------------------------------------

class BusinessExpense(Expenditure):
    pass

# --------------------------------------------------------------
class Education(Expenditure):
    pass

# --------------------------------------------------------------
class PrimaryEducation(Education):
    pass

class ParkingPermit(PrimaryEducation):
    pass

class PrivateTuition(PrimaryEducation):
    pass

class SchoolFee(PrimaryEducation):
    pass

class SchoolSupplies(PrimaryEducation):
    pass
# --------------------------------------------------------------

# --------------------------------------------------------------
class SecondaryEducation(Education):
    pass

class CollegeSupplies(SecondaryEducation):
    pass

class ParkingFee(SecondaryEducation):
    pass

class RoomAndBoard(SecondaryEducation):
    pass

class Tuition(SecondaryEducation):
    pass
# --------------------------------------------------------------

# --------------------------------------------------------------
class HealthFitness(Expenditure):
    pass

class BeautySupplies(Expenditure):
    pass

class Hair(HealthFitness):
    pass

class HygieneSupplies(Expenditure):
    pass

class Spa(HealthFitness):
    pass

class WorkoutGear(HealthFitness):
    pass
# --------------------------------------------------------------

# --------------------------------------------------------------
class Holiday(Expenditure):
    pass

class HolidayFood(Holiday):
    pass

class HolidayGift(Holiday):
    pass

class HolidayTravel(Holiday):
    pass
# --------------------------------------------------------------

# --------------------------------------------------------------
class Insurance(Expenditure):
    pass

class EarthquakeInsurance(Insurance):
    pass

class FireInsurance(Insurance):
    pass

class FloodInsurance(Insurance):
    pass

class HealthInsurance(Insurance):
    pass

class LifeInsurance(Insurance):
    pass

class MiscInsurance(Insurance):
    pass

class MortgageInsurance(Insurance):
    pass

class RentersInsurance(Insurance):
    pass

class VehicleInsurance(Insurance):
    pass

class VisionInsurance(Insurance):
    pass
# --------------------------------------------------------------

# --------------------------------------------------------------
class LifeEvent(Expenditure):
    pass

class Dating(LifeEvent):
    pass

class Divorce(LifeEvent):
    pass

class Engagement(LifeEvent):
    pass

class Funeral(LifeEvent):
    pass

class Wedding(LifeEvent):
    pass
# --------------------------------------------------------------

class PersonalDevelopment(Expenditure):
    pass

# --------------------------------------------------------------
class Pet(Expenditure):
    pass

class PetFood(Pet):
    pass

class PetMedicine(Pet):
    pass

class PetPurchase(Pet):
    pass

class PetSupply(Pet):
    pass

class Veterinarian(Pet):
    pass
# --------------------------------------------------------------

# --------------------------------------------------------------
class NonBilledEntertainment(Expenditure):
    pass

class Activity(NonBilledEntertainment):
    pass

class Concert(NonBilledEntertainment):
    pass

class Event(NonBilledEntertainment):
    pass

class Gambling(NonBilledEntertainment):
    pass

class Hobby(NonBilledEntertainment):
    pass

class MiscNonBilledEntertainment(NonBilledEntertainment):
    pass

class Movie(NonBilledEntertainment):
    pass

class VideoGame(NonBilledEntertainment):
    pass
# --------------------------------------------------------------

# --------------------------------------------------------------
class Technology(Expenditure):
    pass

class TechMaintenance(Technology):
    pass

class TechPurchase(Technology):
    pass

class TechRepair(Technology):
    pass

class TechReplacement(Technology):
    pass

class TechUpgrade(Technology):
    pass
# --------------------------------------------------------------

# --------------------------------------------------------------
class Travel(Expenditure):
    pass

class BusinessTravel(Travel):
    pass

class Vacation(Travel):
    pass
# --------------------------------------------------------------

# --------------------------------------------------------------
class Vice(Expenditure):
    pass

class Marijuana(Vice):
    pass

class Smoking(Vice):
    pass

class Vaping(Vice):
    pass
# --------------------------------------------------------------

# --------------------------------------------------------------
class Fee(Output):
    pass

class BankingFee(Fee):
    pass

class BusinessFee(Fee):
    pass

class CourtFee(Fee):
    pass

# --------------------------------------------------------------
class LegalFee(Fee):
    pass

class ParkingTicket(LegalFee):
    pass

class TrafficTicket(LegalFee):
    pass
# --------------------------------------------------------------

class MiscFee(Fee):
    pass

class PassportFee(Fee):
    pass

class VisaFee(Fee):
    pass
# --------------------------------------------------------------

class Fine(Output):
    pass

class ForeignOut(Output):
    pass

# --------------------------------------------------------------
class Investment(Output):
    pass

class Stocks(Investment):
    pass
# --------------------------------------------------------------

# --------------------------------------------------------------
class Medical(Output):
    pass

class Hearing(Medical):
    pass

class Hospital(Medical):
    pass

class MedicalProcedure(Medical):
    pass

class MedicalVisit(Medical):
    pass

class Medicine(Medical):
    pass

class SpecialtyMedical(Medical):
    pass

class Vision(Medical):
    pass
# --------------------------------------------------------------

class MiscOutput(Output):
    pass

class ReapportionOut(Output):

    @classmethod
    def create(cls, **kwargs):
        try:
            if kwargs['target']:
                super().create(**kwargs)
        except KeyError:
            session.rollback()
            raise KeyError('Reapportioning funds requires two accounts.')

class RetirementOut(Output):
    pass

class TaxPayment(Output):
    pass

class Tithe(Output):
    pass

class TransferToBusiness(Output):
    pass

class TrustFundOut(Output):
    pass

class WageGarnishment(Output):
    pass

class WithdrawalToCash(Output):
    pass

class WithdrawalToCheque(Output):
    __tablename__ = 'WithdrawToCheque'
    rec_id = Column(ForeignKey(Output.rec_id), primary_key=True)
    bank_name = Column(String(40))
    bank_routing_num = Column(String(40))
    cheque_author = Column(String(40))  # required for DepositFromCheque
    cheque_num = Column(Integer)  # required for WithdrawToCheque

    @classmethod
    def create(cls, **kwargs):
        try:
            if kwargs['cheque_num']:
                super().create(**kwargs)
        except KeyError:
            session.rollback()
            raise KeyError('Withdrawal to Cheque requires a cheque number.')

# ==============================================================
# ==============================================================


Base.metadata.create_all(engine)
