import datetime


# 當一個person建構時，就同時計算年紀
# 並且在透過instance method age()查詢年紀時，若查詢時間與上次計算年記時間超過一天才重新計算年紀
class Person:
    def __init__(self, name, surname, birthdate):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.today = datetime.date.today()
        self._age = self.today.year - self.birthdate.year

    def age(self):
        if self.today < datetime.date.today():
            self.today = datetime.date.today()
            self._age = self.today.year - self.birthdate.year
        return self._age

    @property
    def fullname(self):
        return self.name + ' ' + self.surname


person = Person('Jane', 'Doe', datetime.date(1992, 3, 12))

print(person.age())
print(person.fullname)
