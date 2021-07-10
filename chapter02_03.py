# 객체 지향 프로그래밍(oop) -> 코드 재사용, 코드 중복 방지, 유지보수, 대형프로젝트


class Car():
    """
    Car class
    Author : Kim
    Date:2021.05.31
    Description : Class, Static, Instance Method
    """

    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self): # 개발 상태 확인
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)
    
    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    # Instance Method
    def get_price(self):
        return 'Before Car Price -> company :{}, price : {}'.format(self._company, self._details.get('price'))

    # Instance Method
    def get_price_culc(self):
        return 'After Car Price -> company :{}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise) 

    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 Or More')
            return
        cls.price_per_raise = per
        print('Succeed! price increased')

    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'Ok! This car is {}'.format(inst._company)
        return 'Sorry This car is not Bmw'


# self 의미 
car1 = Car('Ferrari', {'color': 'White', 'horsepower':400, 'price':8000})
car2 = Car('Bmw', {'color': 'Black','horsepower':270,'price':5000})

# 전체정보
car1.detail_info()

# 가격정보(직접 접근)
print(car1._details.get('price'))
print(car2._details['price'])

# 가격정보(인상 전)
print(car1.get_price())

# 가격 인상(클래스 메소드 미사용)
Car.price_per_raise = 1.4

# 가격정보(인상 후)
print(car1.get_price_culc())

# 가격 인상(클래스 메소드 사용)
Car.raise_price(1.6)
print(car1.get_price_culc())

# 인스턴스 호출(스테이틱)
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))

#클래스로 호출(스테이틱)
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))