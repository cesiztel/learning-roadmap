from datetime import timedelta, date


def print_owing(invoice): # Extract method
    print_banner()
    outstanding = calculate_outstanding(invoice)
    invoice['outstanding'] = outstanding
    record_due_date(invoice)
    print_details(invoice)


def print_banner():
    print('*********************')
    print('*** Customer Owes ***')
    print('*********************')


def calculate_outstanding(invoice):
    result = 0
    for order in invoice['orders']:
        result += order['amount']
    return result


def record_due_date(invoice):
    invoice['dueDate'] = date.today() + timedelta(days=30)


def print_details(invoice):
    print(f"name: {invoice['customer']}")
    print(f"amount: {invoice['outstanding']}")
    print(f"date: {invoice['dueDate'].strftime('%c')}")


def getInvoice():
    return {
        'orders': [
            {
                'amount': 100
            },
            {
                'amount': 120
            }
        ],
        'customer': 'John Doe'
    }


if __name__ == '__main__':
    print_owing(getInvoice())
