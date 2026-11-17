def calculate_salary(basic_salary):
    hra = basic_salary * 20 / 100
    da = basic_salary * 10 / 100

    return {
        "basic_salary": basic_salary,
        "hra": hra,
        "da": da,
        "gross_salary": basic_salary + hra + da,
    }