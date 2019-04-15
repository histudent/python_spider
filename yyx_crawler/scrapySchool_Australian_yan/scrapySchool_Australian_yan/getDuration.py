import re

def getIntDuration(durationStr):
    # 匹配课程长度
    duration_re = re.findall(r"([a-zA-Z0-9\.]+\s)(year|month|week|yr|yft|semester){1}|([0-9\.]+)(yr|yft|\-month){1}",
                             durationStr, re.I)
    # 英文数字对应的数字
    d_dict = {"One": "1",
              "Two": "2",
              "Three": "3",
              "Four": "4",
              "Five": "5",
              "Six": "6",
              "Seven": "7",
              "Eight": "8",
              "Nine": "9",
              "Ten": "10",
              "one": "1",
              "two": "2",
              "three": "3",
              "four": "4",
              "five": "5",
              "six": "6",
              "seven": "7",
              "eight": "8",
              "nine": "9",
              "ten": "10",
              }
    duration = None
    duration_per = None
    # print(duration_re, "-----duration_re")
    if len(duration_re) > 0:
        # 匹配是数字形式的
        d_int = re.findall(r"\d+.\d+|\d+", ''.join(duration_re[0]))
        if "." in ''.join(d_int):
            d_int_l = ''.join(d_int).split(".")
            d_int = str(int(d_int_l[0])*12 + int(d_int_l[-1])/10*12)
            print(d_int, " 888")
        if len(d_int) > 0:
            duration = int(''.join(d_int).strip('.0').strip())
        else:
            # 英文数字表示的
            d = re.findall(
                r"(One)|(Two)|(Three)|(Four)|(Five)|(Six)|(Seven)|(Eight)|(Nine)|(Ten)|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(ten)",
                ', '.join(duration_re[0]))
            # print("d = ", d)
            if len(d) > 0:
                duration = int(d_dict.get(''.join(d[0]).strip()))

        # 判断课程长度单位：课程长度单位：1年 ，2学期， 3月 ，4周
        if len(duration_re[0]) > 1:
            if "y" in ''.join(duration_re[0][1]) or "Y" in ''.join(duration_re[0][1]):
                duration_per = 1
            elif "s" in ''.join(duration_re[0][1]) or "S" in ''.join(duration_re[0][1]):
                duration_per = 2
            elif "m" in ''.join(duration_re[0][1]) or "M" in ''.join(duration_re[0][1]):
                duration_per = 3
            elif "w" in ''.join(duration_re[0][1]) or "W" in ''.join(duration_re[0][1]):
                duration_per = 4
        else:
            if "y" in ''.join(duration_re[0]) or "Y" in ''.join(duration_re[0]):
                duration_per = 1
            elif "s" in ''.join(duration_re[0]) or "S" in ''.join(duration_re[0]):
                duration_per = 2
            elif "m" in ''.join(duration_re[0]) or "M" in ''.join(duration_re[0]):
                duration_per = 3
            elif "w" in ''.join(duration_re[0]) or "W" in ''.join(duration_re[0]):
                duration_per = 4
        if "." in ''.join(d_int):
            duration_per = 3
    return [duration, duration_per]

#
def getTeachTime(teachTimeStr):
    teach_time = ""
    if "full" in teachTimeStr or "Full" in teachTimeStr or "FT" in teachTimeStr or "ft" in teachTimeStr:
        teach_time = "fulltime"
    return teach_time