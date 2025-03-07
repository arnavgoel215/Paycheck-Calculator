import zmq

def calculate_wage(hourly_rate: float, hours_worked: int) -> float:
    return hourly_rate * hours_worked

def calculate_salary(yearly_salary: float) -> float:
    weekly_rate = yearly_salary / 52  # dividing by 52 since there are 52 weeks in a year
    return round(weekly_rate, 2)

def calculator_server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*5555")

    print("Server is running on port 5555....")

    while True:
        message = socket.recv_string()
        if message == "CALC_SALARY":
            try:
                yearly_salary = float(socket.recv_string())
                print(f"Received a yearly salary value of {yearly_salary}")
                total_pay = calculate_salary(yearly_salary)
                socket.send_string(str(total_pay))
            except ValueError:
                socket.send_string("Error: Received invalid value")
        elif message == "CALC_WAGE":
            try:
                hourly_rate = float(socket.recv_string())
                hours_worked = int(socket.recv_string())
                print(f"Received hourly rate value of {hourly_rate} and working hours of {hours_worked}")
                total_pay = calculate_wage(hourly_rate, hours_worked)
                socket.send_string(str(total_pay))
            except ValueError:
                socket.send_string("Error: Received invalid value")
        else:
            socket.send_string("Error: Invalid command")


if __name__ == "__main__":
    calculator_server()