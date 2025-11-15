
def map_month(month):
    month = int(month)
    months = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr",
              5: "May", 6: "Jun", 7: "Jul", 8: "Aug",
              9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}
    for m in months:
        if m == month:
            return months.get(m, "Not in Month Range")
        
def map_day(day):
    day = int(day)
    if day >= 1 and day <= 31:
        if day % 10 == 1 and day != 11:
            extension = "st"
        elif day % 10 == 2 and day != 12:
            extension = "nd"
        else:
            extension = "th"
        return str(day) + extension
    else:
        return "Not in Day Range"
    

def datetime_to_nametime(date_string):
    date_list = date_string.split("-")
    # print(date_list)
    mapped_day = map_day(date_list[2])
    mapped_month = map_month(date_list[1])
    return (f"{mapped_month} {mapped_day}, {date_list[0]}")
     

def main():
    # print("Hello World")
    date_string = str(input("Enter your date in this format: YYYY-MM-DD\n"))
    print("Your Date is:", datetime_to_nametime(date_string))

if __name__ == "__main__":
    main()