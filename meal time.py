day=input("enter day")
meal_time=input("enter meal_time")
if day=="monday":
    if meal_time=="breakfast":
        print("poori sabji")
    elif meal_time=="lunch":
        print("sambhi rice")
    elif meal_time=="dinner":
        print("chicke rice")
elif day=="tuesday":
    if meal_time=="breakfast":
        print("poha")
    elif meal_time=="lunch":
        print("rajma rice")
    elif meal_time=="dinner":
        print("roti sadji")
else:
    print("not available")                                