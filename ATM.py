ATM_card=input("insert ATM card")
if ATM_card=="Right side" or ATM_card=="right side":
    language=input("enter language")
    if language=="english" or language=="hindi":
        pin=int(input("enter 4 digit pin"))
        if pin>=1000 and pin<=9999:
            transaction_type=input("enter transaction type")
            if transaction_type=="withdrawal" or transaction_type=="withdrawal":
                account_type=input("enter account type")
                if account_type=="current" or account_type=="saving":
                    amount=int(input("enter amount"))
                    if amount>=500 and amount<=2000 and amount%500==0:
                        a=amount//2000
                        b=amount%2000
                        c=b//500
                        d=b%500
                        print("note of 2000",a,"note of 500",c)
                        key_name=input("enter ok")
                        if key_name=="ok" or "Ok":
                         print("succesful")
                    else:
                        print("limited amount")
            elif transaction_type=="balance enquiry" or transaction_type=="Balance enquiry":
              account_type=input("enter account type")
              if account_type=="saving" or account_type=="current":
                 key_name=input("enter ok")                  
                 print("total amount")
              if key_name=="ok" or key_name=="Ok":
                 print("thanks for enquiry")
              else:
                  print("invalid key")
            elif transaction_type=="deposit money" or transaction_type=="Deposit money":
                account_no=int(input("enter account_no"))
                if account_no>=100000000000 and account_no<=999999999999:
                  amount=int(input("enter amount"))
                  key_name=input("enter ok")
                  if key_name=="ok" or key_name=="Ok":
                       print("successful")
                  else:
                       print("unsuccessful")
            elif transaction_type=="bill payment" or transaction_type=="Bill payment":
                 account_no=int(input("enter account_no"))
                 if account_no>=100000000000 and account_no<=999999999999:
                      bill_id=int(input("enter bill_id"))
                      if bill_id>=100000000000 and bill_id<=999999999999:
                         amount=int(input("enter amount"))
                         key_name=input("enter ok")
                         print("successful")
                      else:
                          print("unsuccessful")
                 else:
                    print("not successful")
            
        else:
             print("invalid pin")
    
    else:
        print("no bengali")
else:
    print("rejected")


