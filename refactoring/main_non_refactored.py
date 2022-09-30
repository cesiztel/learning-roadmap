from datetime import timedelta, date


def print_owing(invoice):
    outstanding = 0

    print('*********************')
    print('*** Customer Owes ***')
    print('*********************')

    for o in invoice['orders']:
        outstanding += o['amount']

    invoice['dueDate'] = date.today() + timedelta(days=30)

    print(f"name: {invoice['customer']}")
    print(f"amount: {outstanding}")
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
