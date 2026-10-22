from z2_classes.Library import Library
from z2_classes.Employee import Employee
from z2_classes.Book import Book
from z2_classes.Student import Student
from z2_classes.Order import Order

library1 = Library('Katowice', 'Lipowa 23', '30-320',
                   '8.00-16.00', '725982475')
library2 = Library('Warszawa', 'Akacjowa 12', '41-103',
                   '13.00-18.00', '666666666')

book1 = Book('Leonardo da Vinci', library1, '2019-05-15',
             'Walter', 'Isaacson', 800)
book2 = Book('W pustyni i w puszczy', library1, '2025-09-24',
             'Henryk', 'Sienkiewicz', 432)
book3 = Book('Wiedźmin', library1, '1986-12-01',
             'Andrzej', 'Sapkowski', 320)
book4 = Book('Lalka', library2, '2026-09-09',
             'Bolesław', 'Prus', 864)
book5 = Book('Kubuś Puchatek', library2, '2022-01-26',
             'Alan', 'Milne', 144)

employee1 = Employee('Jan', 'Kowalski', '2020-02-01', '1985-04-12',
                     'Katowice', 'Polna 5', '40-001', '500111222')
employee2 = Employee('Anna', 'Nowak', '2019-06-15', '1990-08-23',
                     'Warszawa', 'Lesna 10', '00-101', '500222333')
employee3 = Employee('Piotr', 'Wisniewski', '2022-09-01', '1995-12-03',
                     'Katowice', 'Szkolna 8', '40-002', '500333444')

student1 = Student('Maria', 'Zielinska', 'Katowice',
                   'Kwiatowa 4', '40-003', '600111222')
student2 = Student('Tobiasz', 'Mruk', 'Warszawa',
                   'Długa 7', '00-102', '600222333')
student3 = Student('Katarzyna', 'Kaminska', 'Katowice',
                   'Mickiewicza 9', '40-004', '600333444')

order1 = Order(employee1, student1, [book1, book2], '2026-10-15')
order2 = Order(employee2, student2, [book3, book4, book5], '2026-10-16')

print(order1)
print(order2)
