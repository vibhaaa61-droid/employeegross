# Employee Salary Calculator

def calculate_salary(basic_salary):

    hra = basic_salary * 20 / 100
    da = basic_salary * 10 / 100

    gross_salary = basic_salary + hra + da

    return {
        "basic_salary": basic_salary,
        "hra": hra,
        "da": da,
        "gross_salary": gross_salary
    }


# Main program
basic_salary = 50000

result = calculate_salary(basic_salary)

print("EMPLOYEE SALARY DETAILS")
print("-----------------------")
print("Basic Salary:", result["basic_salary"])
print("HRA (20%):", result["hra"])
print("DA (10%):", result["da"])
print("Gross Salary:", result["gross_salary"])