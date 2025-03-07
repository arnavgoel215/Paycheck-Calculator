import zmq

def calculate_wage(hourly_rate: float, hours_worked: float) -> float:
    return hourly_rate * hours_worked

def calculate_salary(yearly_salary: float) -> float:
    weekly_rate = yearly_salary / 52  # dividing by 52 since there are 52 weeks in a year
    return round(weekly_rate, 2)
