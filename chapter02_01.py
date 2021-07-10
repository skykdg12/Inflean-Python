# 객체 지향 프로그래밍(oop) -> 코드 재사용, 코드 중복 방지, 유지보수, 대형프로젝트

# 일반적인 코딩

# 차량1
car_company_1 = 'Ferrar1'
car_detail_1 = [
    {'color': 'White'},
    {'horsepower':400},
    {'price':8000}
]

# 차량2
car_company_2 = 'Bmw'
car_detail_2 = [
    {'color': 'Black'},
    {'horsepower':270},
    {'price':5000}
]

# 차량3
car_company_3 = 'Audi'
car_detail_3 = [
    {'color': 'Silver'},
    {'horsepower':300},
    {'price':6000}
]

# 리스트 구조
# 관리하기 불편
# 인덱스 접근 시 실수 가능성, 삭제 불편 > 리스트는 인덱스를 알아야 하기 때문
car_company_list = ['Ferrari', 'Bmw', 'Audi']
car_detail_list = [
    {'color': 'White', 'horsepower':400, 'price':8000},
    {'color': 'Black','horsepower':270,'price':5000},
    {'color': 'Silver','horsepower':300,'price':6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()


# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리

car_dict = [
    {'car_company': 'Ferrari', 'car_detail': {'color': 'White', 'horsepower':400, 'price':8000}},
    {'car_company': 'Bmw', 'car_detail': {'color': 'Black','horsepower':270,'price':5000}},
    {'car_company': 'Audi', 'car_detail': {'color': 'Silver','horsepower':300,'price':6000}}
]


del car_dict[1]
print(car_dict)

print()
print()

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용 

class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self): # 개발 상태 확인
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

car1 = Car('Ferrari', {'color': 'White', 'horsepower':400, 'price':8000})
car2 = Car('Bmw', {'color': 'Black','horsepower':270,'price':5000})
car3 = Car('Audi', {'color': 'Silver','horsepower':300,'price':6000})

print(car1)
print(car2)
print(car3)

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

print()
print()

# 리스트 선언
car_list=[]

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

print()
print()

# 반복(__str__)
for x in car_list:
    print(x)