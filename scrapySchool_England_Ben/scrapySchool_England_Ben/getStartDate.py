import re

# 改开学时间的格式
def getStartDate(startdateStr):
    if startdateStr == None:
        startdateStr = ""
    year_re = re.findall(r"20\d+", startdateStr)
    month_re = re.findall(r"[a-zA-Z]+", startdateStr)
    day_re = re.findall(r"^\d{1,2}$|^\d{1,2}|\d{1,2},", startdateStr)
    # print(month_re, "===")
    monthDict = {"january": "01", "february": "02", "march": "03", "april": "04", "may": "05", "june": "06",
                "july": "07", "august": "08", "september": "09", "october": "10", "november": "11", "december": "12",
                 "jan": "01", "feb": "02",  "mar": "03", "apr": "04", "may": "05", "jun": "06",
                "jul": "07","aug": "08","sep": "09","oct": "10","nov": "11","dec": "12",
                 "sept": "09",}
    # print(''.join(month_re).strip().lower())
    month = ""
    if len(month_re) > 0:
        for m in month_re:
            month = monthDict.get(m.strip().lower())
            if month != None:
                break
            if month == None:
                month = ""
    year = ""
    if len(year_re) > 0:
        year = ''.join(year_re[0])
    start_date = year + "-" + month + "-" + ''.join(day_re).replace(",", "")
    # print(start_date)
    # print("year-month-day = "+ ''.join(year_re) + "-" + month + ''.join(day_re))
    return start_date.strip().strip("-").strip()
