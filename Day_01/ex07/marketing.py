import sys

def call_center_handler(clients, recipients):
    return list(clients - recipients)

def potential_clients_handler(participants, clients):
    return list(participants - clients)

def call_loyalty_program(clients, participants):
    return list(clients - participants)

def handler(command):
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com'] #клиенты
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com'] #участники мероприятия
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is'] #посмотрели рекламное письмо
    
    if command == 'call_center':
        print(call_center_handler(set(clients), set(recipients)))
    elif command == 'potential_clients':
        print(potential_clients_handler(set(participants), set(clients)))
    elif command == 'loyalty_program':
        print(call_loyalty_program(set(clients), set(participants)))
    else:
        raise Exception('Wrong argument. Use one of these: call_center, potential_clients, loyalty_program')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            handler(sys.argv[1])
        except Exception as e:
            print(e, file=sys.stderr)