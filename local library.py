e_d=int(input("enter exp_date"))
e_m=int(input("enter exp_month"))
e_y=int(input("enter exp_year"))
r_d=int(input("enter return_date"))
r_m=int(input("enter return_month"))
r_y=int(input("enter return_year"))
if  r_m==e_m and r_y==e_y:
    if r_d<=e_d:
        print("no fine")
    elif r_d>=e_d:
        day=e_d-r_d
        fine=15*day
        print(fine) 
    else:
        print("no charge")        
elif r_m >=e_m and r_y==e_y:
    if r_d>=e_d:
        day=e_m-r_m
        fine=500*day
        print(fine)  
    else:
        print("no fine ")  
elif r_m<=e_m and r_y!=e_y:
    if r_d<e_d:
        fixe_fine=10000
        print(fixe_fine)   
    else:
        print("no fixe_fine")   
else:
    print("no charge needed")                   
