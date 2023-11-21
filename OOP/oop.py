class Employee(object):

	employee_num = 0
	raise_amount = 1.04

	def __init__(self, name, pay):
		self.name = name
		self.pay = pay
		self.name_pay = name + str(pay)

		Employee.employee_num += 1

	def apply_raise(self):
		# when we try to access an attribute on an instances first it will
		# check if the instance contains that attribute. if it dosent then it will see
		# if the class or any other class that it inharite from contains that attribute
		# namespace of class or object can help
		# self.raise_amount
		self.pay = int(self.pay * self.raise_amount)

	@property
	def get_name_pay(self):
		return f'{self.name}, {self.pay}'
		
	# setter method of property decorator
	@get_name_pay.setter
	def get_name_pay(self, name_and_pay):
		name, pay = name_and_pay.split(' ')
		self.name = name
		self.pay = pay

	# property deleter
	@get_name_pay.deleter
	def get_name_pay(self):
		print('Deleter property decorator')
		self.name = None
		self.pay = None

	# we can call this email() method like and attribute
	@property
	def email(self):
		return f'{self.name}@gmail.com'


	@classmethod
	def set_raise_amount(cls, amount):
		cls.raise_amount = amount

	# class method as alternative constructor
	@classmethod
	def from_string(cls, emp_str):
		name, pay = emp_str.split('-')
		pay = int(pay)
		return cls(name, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

	# adding 2 employees pay
	def __add__(self, other):
		return self.pay + other.pay

	# len return the length of emp name
	def __len__(self):
		return len(self.name)

	# called fallback of __str__()
	def __repr__(self):
		return f"<-Employee('{self.name}', {self.pay})->"

	# represent the class
	def __str__(self):
		return f'~ {self.name} get {self.pay}$ ~'

emp_1 = Employee('Mahfuz', 2000)
emp_2 = Employee('Wasim', 3000)

# by changing class variable value using instance it automaticaly add the class 
# variable to it's own namespace
print(emp_1.__dict__)
emp_1.raise_amount = 1.05
print(emp_1.__dict__)

# this method access class vairable from instance
emp_1.apply_raise()

# class method
Employee.set_raise_amount(1.06)

# class method as alternative constructor
new_emp = 'Selim-100000'
emp_3 = Employee.from_string(new_emp)
print(emp_3)

# static method
import datetime
print(Employee.is_workday(datetime.datetime.now()))
print()


# inheritance
class Developer(Employee):
	raise_amount = 1.10

	def __init__(self, name, pay, prog_lang):
		super().__init__(name, pay)
		# Employee.__init__(self, name, pay)
		self.prog_lang = prog_lang

dev_1 = Developer('CoreyMs', 50000, 'python')
dev_2 = Developer('Harison', 60000, 'python')

# print(help(Developer))
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.prog_lang)
print()


# multiple subclass
class Manager(Employee):

	def __init__(self, name, pay, employees=None):
		super().__init__(name, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)	

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print(emp.name)

mgr_1 = Manager('Sueuaua', '90000', [dev_1])
mgr_1.add_emp(dev_2)
mgr_1.print_emps()
print()

mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

# Built in function
print(isinstance(mgr_1, Manager))
print(issubclass(Developer, Employee))
print()


# calling special method
print(repr(mgr_1))
print(str(mgr_1))
print(emp_1 + dev_1)
print(len(mgr_1))
print()


# proparty decorators
# setter property
emp_1.get_name_pay = 'Rahman 500'

print(emp_1.name)
print(emp_1.get_name_pay)

# Delete using property decorator deleter
del emp_1.get_name_pay
print(emp_1.name)