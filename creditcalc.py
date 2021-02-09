import math
import argparse
import sys

parser = argparse.ArgumentParser(description="This program is a loan calculator.")

parser.add_argument("-t", "--type", choices=["annuity", "diff"])
parser.add_argument("-pr", "--principal")
parser.add_argument("-pa", "--payment")
parser.add_argument("-i", "--interest")
parser.add_argument("-pe", "--periods")

arg = sys.argv
args = parser.parse_args()

def function():
    typ = args.type
    if args.principal is not None:
        pozyczka = int(args.principal)
    else:
        pozyczka = args.principal
    if args.payment is not None:
        wyplata = int(args.payment)
    else:
        wyplata = args.payment
    if args.interest is not None:
        odsetki = float(args.interest)
    else:
        odsetki = args.interest
    if args.periods is not None:
        n = int(args.periods)
    else:
        n = args.periods

    if typ == "annuity":
        if n is None:
            i = odsetki / (12 * 100)
            n = math.ceil(math.log(wyplata / (wyplata - i * pozyczka), 1 + i))
            if 12 > n > 1:
                print("It will take ", n, " months to repay this loan!")
            elif n == 12:
                print("It will take 1 year to repay this loan!")
            elif n < 24 and n % 12 == 1:
                print("It will take 1 year and 1 month to repay this loan!")
            elif n < 24 and n % 12 != 1:
                print("It will take 1 year and ", n % 12, " months to repay this loan!")
            elif n % 12 == 0:
                print("It will take ", int(math.floor(n / 12)), " years to repay this loan!")
            elif n % 12 == 1:
                print("It will take ", int(math.floor(n / 12)), " years and 1 month to repay this loan!")
            else:
                print("It will take ", int(math.floor(n / 12)), " years and ", n % 12, "months to repay this loan!")
        elif wyplata is None:
            i = odsetki / (12 * 100)
            wyplata = pozyczka * i * math.pow(1 + i, n) / (math.pow(1 + i, n) - 1)
            print("Your monthly payment = ", math.ceil(wyplata), "!")
        elif pozyczka is None:                                 #else
            i = odsetki / (12 * 100)
            pozyczka = wyplata / (i * math.pow(1 + i, n) / (math.pow(1 + i, n) - 1))
            print("Your loan principal = ", round(pozyczka), "!")
        nadplata = math.ceil(n * math.ceil(wyplata) - pozyczka)
        print("Overpayment = ", nadplata)
    else:
        if wyplata is None:
            i = odsetki / (12 * 100)
            w2 = 0
            m = 1
            for x in range(n):
                wyplata = int(math.ceil(pozyczka / n + i * (pozyczka - pozyczka * ( m - 1) / n)))
                print("Month ", m ,": payment is ", wyplata)
                w2 += wyplata
                m+=1
            nadplata = math.ceil(w2 - pozyczka)
            print("Overpayment = ", nadplata)
        else:
            print("Incorrect parameters.")

if len(arg) != 5:
    print("Incorrect parameters.")
elif args.type is None or args.interest is None:
    print("Incorrect parameters")
else:
    function()
