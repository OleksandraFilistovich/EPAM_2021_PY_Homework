"""
Task 7_2
Create classes Employee, SalesPerson, Manager and Company with predefined functionality.

Create basic class Employee and declare following content:
• Attributes – `name` (str), `salary` and `bonus` (int), set with property decorator
• Constructor - parameters `name` and `salary`
• Method `bonus` - sets bonuses to salary, amount of which is delegated as `bonus`
• Method `to_pay` - returns the value of summarized salary and bonus.

Create class SalesPerson as class Employee inheritor and declare within it:
• Constructor with parameters: `name`, `salary`, `percent` – percent of plan performance (int, without the % symbol), first two of which are passed from basic class constructor
• Redefine method of parent class `bonus` in the following way: if the sales person completed the plan more than 100%, their bonus is doubled (is multiplied by 2), and if more than 200% - bonus is tripled (is multiplied by 3)

Create class Manager as Employee class inheritor, and declare within it:
• Constructor with parameters: `name`, `salary` and `client_number` (int, number of served clients), first two of which are passed to basic class constructor.
• Redefine method of parent class `bonus` in the following way: if the manager served over 100 clients, their bonus is increased by 500, and if more than 150 clients – by 1000.

Create class Company and declare within it:
• Constructor with parameters: `employees` – list of company`s employees (made up of Employee/SalesPerson/Manager classes instances) with arbitrary length `n`
• Method `give_everybody_bonus` with parameter company_bonus (int) that sets the amount of basic bonus for each employee.
• Method `total_to_pay` that returns total amount of salary of all employees including awarded bonus
• Method `name_max_salary` that returns name of the employee, who received maximum salary including bonus.

Note:
Class attributes and methods should bear exactly the same names as those given in task description
Methods should return only target values, without detailed explanation within `return`
"""


class Employee:
    " Method `to_pay` - returns the value of summarized salary and bonus."

    def __init__(self, name, salary):
        """
        Class object constructor.
        :param name: string
        :param salary: int
        """
        self._name = name
        self._salary = salary
        self._bonus = 0

    def __str__(self):
        """
        Returns string representation of employee.
        :return: name: salary: salary, bonus: bonus
        """
        return f'{self._name}: salary:{self._salary}, bonus:{self._bonus}'

    @property
    def name(self):
        """
        Getter of name parameter.
        :return: name as string
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets parameter name to the given one.
        :param name: string
        :return: None
        """
        self._name = name

    @property
    def salary(self):
        """
        Getter of salary parameter.
        :return: salary as int
        """
        return self._salary

    @salary.setter
    def salary(self, salary):
        """
        Sets parameter salary to the given one.
        :param salary: int
        :return: None
        """
        self._salary = salary

    def bonus(self, bonus):
        """
        Sets bonus value to given.
        :param bonus: int
        :return: None
        """
        self._bonus = bonus

    def to_pay(self):
        """
        Returns summarized salary and bonus.
        :return: int
        """
        return self._salary + self._bonus


class SalesPerson(Employee):
    def __init__(self, name, salary, percent):
        """
        Class object constructor.
        :param name: string
        :param salary: int
        :param percent: int without '%' sign
        """
        super().__init__(name, salary)
        self._percent = percent
    
    def __str__(self):
        """
        Returns string representation of employee.
        :return: 'name: salary:{salary}, bonus:{bonus}, percent:{percent}'
        """
        return f'{self._name}: salary:{self._salary}, bonus:{self._bonus}, percent:{self._percent}'

    def bonus(self, bonus):
        """
        Sets bonus value to given (coralating with percent).
        :param bonus: int
        :return: None
        """
        coef = 1
        if self._percent > 200:
            coef = 3
        elif self._percent > 100:
            coef = 2
        self._bonus = bonus * coef
    
    
class Manager(Employee):
    def __init__(self, name, salary, client_number):
        """
        Class object constructor.
        :param name: string
        :param salary: int
        :param client_number: int, number of served clients
        """
        super().__init__(name, salary)
        self._client_number = client_number
    
    def __str__(self):
        """
        Returns string representation of employee.
        :return: 'name: salary:{salary}, bonus:{bonus}, number_of_clients:{client_number}'
        """
        return f'{self._name}: salary:{self._salary}, bonus:{self._bonus}, number_of_clients:{self._client_number}'

    def bonus(self, bonus):
        """
        Sets bonus value to given (coralating with client_number).
        :param bonus: int
        :return: None
        """
        over_bonus = 0
        if self._client_number > 150:
            over_bonus = 1000
        elif self._client_number > 100:
            over_bonus = 500
        self._bonus = bonus + over_bonus
    

class Company:
    def __init__(self, *employees):
        """
        Constructor of employees array.
        :param employees: list of employees
        """
        if isinstance(employees[0], list):
            self.employees = []
            self.employees += employees[0]
        else:
            self.employees = list(employees)
    
    def __str__(self):
        """
        Returns string representation of array of employees (as strings in list).
        :return: string with array
        """
        l = [str(x) for x in self.employees]
        return str(l)
    
    def give_everybody_bonus(self, company_bonus):
        """
        Sets the amount of basic bonus for each employee.
        :param company_bonus: int
        """
        for empl in self.employees:
            empl.bonus(company_bonus)
    
    def total_to_pay(self):
        """
        Returns summarized salary and bonus of all employees.
        :return: int
        """
        summa = 0
        for empl in self.employees:
            summa += empl.to_pay()
        return summa
    
    def name_max_salary(self):
        """
        Returns name of the employee, who received maximum salary including bonus.
        :return: string with name
        """
        l = [empl.to_pay() for empl in self.employees]
        max_salary = max(l)
        index = l.index(max_salary)
        return self.employees[index].name
