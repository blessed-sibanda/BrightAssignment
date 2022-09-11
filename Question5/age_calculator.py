def calculateAge(bd, bm, by, d, m, y):
    years = y - by
    months = m - bm
    days = d - bd
    age = years + (months/12) + (days/365)
    return round(age)


if __name__ == '__main__':
    print(calculateAge(15, 8, 1996, 11, 9, 2022))
    print(calculateAge(15, 4, 1998, 25, 1, 2020))
