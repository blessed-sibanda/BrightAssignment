SPEEDING_FINE = 500
MILE_PER_HOUR_PENALTY = 10
PENALTY_OVER_90 = 2000


def check_speed(clocked_speed, speed_limit):
    if clocked_speed < speed_limit:
        print(f"{clocked_speed} is legal")
    else:
        fine = SPEEDING_FINE + (clocked_speed - speed_limit) * MILE_PER_HOUR_PENALTY
        if clocked_speed > 90:
            fine += PENALTY_OVER_90
        print("The fine is ZWL{:.2f}".format(fine))


try:
    speed = float(input("Enter the clocked speed: "))
    limit = float(input("Enter the speed limit: "))
    check_speed(speed, limit)
except ValueError:
    print("Please enter a valid number for speed")
