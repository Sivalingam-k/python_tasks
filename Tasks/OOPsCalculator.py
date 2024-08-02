class Salary:
    def __init__(self,salary):
        self.base_salary=salary

    def getSalary(self):
        print("Base Salary :",self.base_salary)    

class Allowance(Salary):
    def calculator(self):
        self.HRA=(self.base_salary/100)*20
        self.DA=(self.base_salary/100)*40
        self.TA=(self.base_salary/100)*25

    def getAllowance(self):
        self.total=self.HRA+self.DA+ self.TA
        print("Total Allowances :",self.total)

class deduction(Salary):
    def deductions(self):
        self.insurance=5000
        self.pf=(self.base_salary/100)*12
        self.grad=(self.base_salary/100)*5
        self.deduction_total=self.insurance+self.pf+self.grad
class CalculateSalarySlip(Allowance,deduction):
    def get_salary_slip(self):
        self.calculator()
        self.getAllowance()
        deduction.deductions(self)
       
        print("Base Salary: ", self.base_salary)
        
        print("total allocation: ", self.total)
        
        print("Total Dedection: ", self.deduction_total)
        
        print("Gross Salary: ", self.base_salary + self.total)
        self.gross_salary = self.base_salary + self.total
        print("Net Salary: ", self.gross_salary - self.deduction_total)
def oopscalculator():
    final = CalculateSalarySlip(int(input("Enter the base salary: ")))
    final.get_salary_slip()
def main():
    oopscalculator()
if __name__=='__main__':
    main()





                
                   











