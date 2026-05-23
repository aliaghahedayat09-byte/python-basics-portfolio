def percent_to_float(p):
    # TODO
    clean_percent = p.replace("%","")
    return float(clean_percent)


def dollars_to_float(d):
    # TODO
    clean_dollor = d.replace("$","")
    return float(clean_dollor) /100


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")



main()
