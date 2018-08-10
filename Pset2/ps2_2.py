def minutes_to_years_days(mins):
    total_days = mins // (24 * 60)
    years = total_days // 365
    remaining_days = total_days - (365 * years)
    return years, remaining_days

if __name__ == "__main__":
    user_input = int(input('Enter the number of minutes: '))
    years, days = minutes_to_years_days(user_input)
    print('{:d} minutes is approximately {:d} years and {:d} days.'.format(user_input, years, days))

# print(minutes_to_years_days(2000000000))