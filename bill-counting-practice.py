import random
import argparse

def total(num_100, num_50, num_20, num_10, num_5, num_1):
    return (100*num_100) + (50*num_50) + (20*num_20) + (10*num_10) + (5*num_5) + num_1

def print_exercise(num_100, num_50, num_20, num_10, num_5, num_1, total):
    print("$100\tx", num_100)
    print("$50\tx", num_50)
    print("$20\tx", num_20)
    print("$10\tx", num_10)
    print("$5\tx", num_5)
    print("$1\tx", num_1)

    print("\nTotal: ${}".format(total))

def bill_counting(num_bills_init):
    num_bills = num_bills_init

    num_100 = random.randint(0, num_bills)
    num_bills -= num_100

    num_50 = random.randint(0, num_bills)
    num_bills -= num_50

    num_20 = random.randint(0, num_bills)
    num_bills -= num_20

    num_10 = random.randint(0, num_bills)
    num_bills -= num_10

    num_5 = random.randint(0, num_bills)
    num_bills -= num_5

    # num_1 = num_bills

    total_amount = total(num_100, num_50, num_20, num_10, num_5, num_bills)
    print_exercise(num_100, num_50, num_20, num_10, num_5, num_bills, total_amount)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(\
        description="Generate arbitrary amounts for each dollar denomination for teller practice"\
    )
    parser.add_argument("num_bills_init", metavar="N",\
                        help="number of bills"\
    )
    args = parser.parse_args()

    bill_counting(int(args.num_bills_init))