age=int(input("enter age"))
sex=input("enter sex")
m_s=input("enter m_s")
if sex=="m":
    if age>=40 and age<=60 and  m_s=="y":
        print("work in urban areas")
elif sex=="f":
    if age>=20 and age<=40 and m_s=="y":
        print("work in anywhere")
else:
    print("error")        

