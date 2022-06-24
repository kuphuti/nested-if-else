age=int(input("enter age"))
sex=input("enter sex")
m_s=input("enter m_s")
if sex=="m":
    if age>=20 and age<=40 and m_s=="y":
        print("work in any where")
    elif age>=40 and age<=60 and m_s=="y":
        print("work in urban area")      
elif sex=="f":
    print("work in urban areas")  
else:
    print("not available")          