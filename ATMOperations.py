from AtmExcpt import DepositError,WithDrawError,InSuffFundError
bal=500.00 # here bal is called Global Variable
def deposit():
    damt=float(input("Enter Ur Deposit Amount:")) # ValueError
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("Ur Account xxxxx123 Creadited with INR:{}".format(damt))
        print("Ur Account xxxxx123 Bal After Deposit INR:{}".format(bal))
def withdraw():
    global bal
    wamt = float(input("Enter Ur Withdraw Amount:"))  # ValueError
    if(wamt<=0):
        raise WithDrawError
    elif((wamt+500)>bal):
        raise InSuffFundError
    else:
       bal=bal-wamt
       print("Ur Account xxxxx123 Debitted with INR:{}".format(wamt))
       print("Ur Account xxxxx123 Bal After withdraw INR:{}".format(bal))
def balenq():
    print("Ur Account xxxxx123 Bal After withdraw INR:{}".format(bal))