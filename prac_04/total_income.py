def main():
    """Display income report for incomes over a given number of NumberOfMonths."""
    incomes = []
    NumberOfMonths = int(input("How many months? "))

    for month in range(1, NumberOfMonths + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    PrintReport(incomes)


def PrintReport(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()