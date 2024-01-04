# generálk N db szelvényt. (luxor játék). 2
# 0 db számot amiből, 4 darbot 1-15 között és 5 db-t 16-30ig és így tovább.

import random


def generate_luxor_ticket():
    ticket = []

    ticket.extend(random.sample(range(4, 15), 4))
    ticket.extend(random.sample(range(16, 30), 5))

    return ticket


def generate_multiple_tickets(N):
    tickets = []

    for i in range(N):
        ticket = generate_luxor_ticket()
        tickets.append(ticket)
    return tickets


print(generate_multiple_tickets(3))
