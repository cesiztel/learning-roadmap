def reportLines(a_customer):
    lines = []
    lines.append(["name", a_customer["name"]])
    lines.append(["location", a_customer["location"]])
    return lines


if __name__ == '__main__':
    customer = {
        "name": "ACME",
        "location": "Gotham"
    }
    print(reportLines(customer))
