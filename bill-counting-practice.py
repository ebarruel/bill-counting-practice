import random
import argparse

def total(num_by_denomination, denominations):
    sum = 0
    for i in range(len(denominations)):
        sum += denominations[i] * num_by_denomination[i]

    return sum

def print_exercise(num_by_denomination, denominations, total):
    for i in range(len(denominations)):
        print("${}\tx {}".format(denominations[i], num_by_denomination[i]))

    print("\nTotal: ${}".format(total))

def bill_counting(num_bills_init):
    num_bills = num_bills_init
    denominations = [100, 50, 20, 10, 5, 1]
    num_by_denomination = [0]*len(denominations)

    for i in range(len(denominations)):
        num_by_denomination[i] = random.randint(0, num_bills)
        num_bills -= num_by_denomination[i]

    total_amount = total(num_by_denomination, denominations)
    print_exercise(num_by_denomination, denominations, total_amount)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(\
        description="Generate arbitrary amounts for each dollar denomination for teller practice"\
    )
    parser.add_argument("num_bills_init", metavar="N",\
                        help="number of bills"\
    )
    args = parser.parse_args()

    bill_counting(int(args.num_bills_init))