# 1998 -> 20
# 1991 -> 20
# 356 -> 4
# 89 -> 1
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20
# 2742 --> 28

def countYears(year):
    if year % 100 == 0:
        return(year // 100)
    else:
        return(year // 100 + 1)
print(countYears(89))