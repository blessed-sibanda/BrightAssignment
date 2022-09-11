def calculateAge(bd, bm, by, d, m, y):
    years = y - by
    months = m - bm
    if months < 0:
        months += 12
        years -= 1
    days = d - bd
    if days < 0:
        days += 30
        months -= 1
    age = years + (months/12) + (days/365)
    return round(age)


if __name__ == '__main__':
    print(calculateAge(15, 8, 1996, 11, 9, 2022))
