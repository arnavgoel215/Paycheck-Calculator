import zmq

def calculator_server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print("Server is running on port 5555....")

    while True:
        message = socket.recv_json()
        hours = message.get("hours", 0)
        pay_rate = message.get("pay_rate", 0)
        total_pay = hours * pay_rate

        socket.send_string(str(total_pay))


if __name__ == "__main__":
    calculator_server()