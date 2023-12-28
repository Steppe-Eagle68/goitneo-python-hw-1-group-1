from datetime import datetime, timedelta
from collections import defaultdict

users = [
    {"name": "Chris Redfield", "birthday": datetime(1970, 1, 1)},
    {"name": "William Blazkowicz", "birthday": datetime(1967, 1, 4)},
    {"name": "Sam Stone", "birthday": datetime(1985, 12, 29)},
    {"name": "Solomon Reed", "birthday": datetime(1996, 1, 2)},
]

def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)

    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            day_of_week = (today + timedelta(days=delta_days)).strftime("%A")
            
            if day_of_week in ['Saturday','Sunday']:
                day_of_week = 'Monday'

            birthdays_per_week[day_of_week].append(name)

    for day, names in birthdays_per_week.items():
        print(f"{day}: {', '.join(names)}")
        
get_birthdays_per_week(users)