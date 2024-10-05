#Library management 
'''
class book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow_book(self):
        self.available = False
    
    def return_book(self):
        self.available = True

    def display_details(self):
        print(f"{self.title}, {self.author}, {self.available}")

class library():
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def show_books(self):
        for book in self.books:
            book.display_details()

    def borrow_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                book.borrow_book()
                return
        print("no book found")
'''
# Rental Car system 
'''
class car():
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.available = True
    
    def rent_car(self):
        if self.available == True:
            self.available = False
    
    def return_Car(self):
        self.available = True
    def display_details(self):
        status = "Available" if self.available else "Not Available"
        print(f"make {self.make}, model {self.model}, availability {status}")


class carRental():
    def __init__(self):
        self.cars =[]

    def add_car(self,car):
        self.cars.append(car)
        print(f"{car.make} {car.model} has been added to the system")

    def display_available_cars(self):
        for car in self.cars:
            if car.available == True:
                car.display_details()

    def rent_bymakemodel(self, make, model):
        for car in self.cars:
            if (car.make == make and car.model == model):
                car.rent_car()
                return 
        print("no car available with this make and model")
    
    def return_car(self, make, model):
        for car in self.cars:
            if (car.make == make and car.model == model):
                car.return_car()
                return
'''

# Student Managment System
'''
class student():

    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age 
        self.student_id = student_id

    def display_info(self):
        print(f"{self.name} , {self.age}, {self.student_id}")


class studentManagementSystem():
         
    def __init__(self):
        self.students = []
        
    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
        
    def show_all_students(self):
        for student in self.students:
            student.display_info()
'''         

# Online Course Management system
'''
class Course():

    def __init__(self, course_name, course_code, credits):
        self.course_name = course_name
        self.course_code = course_code
        self.credits = credits
        self.enrolled_students = []

    def add_students(self, student):
        self.enrolled_students.append(student)

    def remove_student(self, student_id):
        for student in self.enrolled_students:
            if student.student_id == student_id:
                self.enrolled_students.remove(student)
                return

    def display_course_info(self):
        print(f"{self.course_name}, {self.course_code}, {self.credits}, {self.enrolled_students}") 

        
class Student():

    def __init__(self, name , student_id):
        self.name = name
        self.student_id = student_id

    def display_info(self):
        print(f"{self.name}, {self.student_id}")

class courseManagementSystem():

    def __init__(self):
        self.courses = []
    
    def add_course(self, course):
        self.courses.append(course)

    def show_all_courses(self):
        for course in self.courses:
            course.display_course_info()
'''
# Employee Management System 

'''
class Employee():

    def __init__(self, name, employee_ID, position):
        self.name = name
        self.employee_ID = employee_ID
        self.position = position
        self.salary = 0

    def display_info(self):
         print(f"{self.name}, {self.employee_ID}, {self.position}, {self.salary}")

class EmployeeManagmentSystem():

    def __init__(self):
        self.employees = []


    def add_employee(self, employee):
        self.employees.append(employee)
    
    def remove_employee(self, employee_ID):
        for employee in self.employees:
            if employee.employee_ID == employee_ID:
                self.employees.remove(employee)
                return
        print(f"employee with {employee_ID} not found")
        
    def display_all_employees(self):
        if not self.employees:
            print("no employee in the system")
        else:
            for employee in self.employees:
                employee.display_info()

    def total_salary_expense(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expense: {total_salary}")
'''

# Bank Account Management system 
'''
class BankAccount():

    def __init__(self, account_number, owner):
        self.account_number = account_number
        self.owner = owner
        self.balance = 0 
    
    def deposit(self, money):
        self.balance+=money
        print(f"added {money}, new balance is {self.balance}")


    def withdraw(self, money):
        if money > self.balance:
            print("insufficient funds")
        else:
            self.balance-=money
            print(f"withdrew {money}, new balance is {self.balance}")
    
    def display_balance(self):
        print(f" curent balance is {self.balance}")
    
class Saving_account(BankAccount):

    def __init__(self, account_number, owner):
        super().__init__(account_number, owner)
        self.interest_rate = 1.05

    def add_interest(self):
        interest = self.balance*self.interest_rate
        self.balance +=interest
        print(f"added interest: {interest}, New Balance: {self.balance}")


class checking_account(BankAccount):

    def __init__(self, account_number, owner):
        super().__init__(account_number, owner)
        self.overdraft_limit = 1000

    def withdraw(self, money):
        if self.balance - money < -self.overdraft_limit:
            print("exceeds overdraft limit")
        else:
            self.balance -= money
            print(f"Withhdrew {money}, New balance is {self.balance}")
            
'''
