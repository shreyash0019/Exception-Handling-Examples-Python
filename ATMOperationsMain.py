from AtmExcpt import DepositError, WithDrawError, InSuffFundError
from AtmMenu import menu
from ATMOperations import deposit, withdraw, balenq
import sys
while(True):
    menu()
    try:
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("\tDon't Try to deposit -VE and Zero Values")
                except ValueError:
                    print("\tDon't Try to deposit alnums,strs and symbols")
            case 2:
                try:
                    withdraw()
                except WithDrawError:
                    print("\tDon't Try to Withdraw -VE and Zero Values")
                except InSuffFundError:
                    print("\tUr Account does not have Funds--Read Python Notes")
                except ValueError:
                    print("\tDon't Try to withdraw alnums,strs and symbols")

            case 3:
                balenq()
            case 4:
                print("Thx for Using App--visit again")
                sys.exit()
            case _:
                print("Ur Selection of Operations is wrong--try again")
    except ValueError:
        print("\tUr Choice Should Not be alnums,strs,symbols-enter int value")
