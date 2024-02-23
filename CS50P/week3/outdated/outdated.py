months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    try:
        s = input("Date: ")
        month, day, year = s.split("/")
        if 0 < int(day) <= 31 and 0 < int(month) <= 12:
            break
        else:
            raise ValueError

    except:
        try:
            month, day, year = s.split()
            if month in months:
                month = months.index(month) + 1
                if "," in day:
                    day = day.removesuffix(",")
                    if 0 < int(day) <= 31:
                        break
        except:
            pass
    else:
        break


print(f"{int(year)}-{int(month):02}-{int(day):02}")
