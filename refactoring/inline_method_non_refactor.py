def reportLines(a_customer):
    lines = []
    gatherCustomerData(lines, a_customer)
    return lines


def gatherCustomerData(out, a_customer):
    out.append(["name", a_customer["name"]])
    out.append(["location", a_customer["location"]])


if __name__ == '__main__':
    customer = {
        "name": "ACME",
        "location": "Gotham"
    }
    print(reportLines(customer))
