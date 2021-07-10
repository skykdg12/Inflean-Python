# chapter03_01
# special method(magic method)
# 파이썬 핵심 -> 시퀀스(sezuence), 반복(iterator), 함수(functions), class
# 클래스안에 정의할 수 있는 특별한(built in) 메소드

# 기본형
print(int)

# 모든 속성 및 메소드 출력
print(dir(int))

n = 10

print(n + 100)
print(n.__add__(100))
#print(n.__doc__)
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))

print()
print()


# 클래스 예제1
class fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'fruit class info : {}, {}'.format(self._name, self._price)

    def __add__(self, x):
        print('called >> __add__')
        return self._price + x._price

    def __sub__(self, x):
        print('called >> __sub__')
        return self._price - x._price

    def __le__(self, x):
        print('called >> __le__')
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self, x):
        print('called >> __ge__')
        if self._price >= x._price:
            return True
        else:
            return False


# 인스턴스 생성
s1 = fruit('orange', 7500)
s2 = fruit('banana', 3000)

print(s1 + s2)

# 일반적인 계산
# print(s1._price + s2._price)

# 매직메소드
print(s1 >= s2)
print(s1 <= s2)
print(s1 - s2)
print(s2 - s1)
print(s1)
print(s2)
