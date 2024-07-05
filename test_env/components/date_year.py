import datetime

def get_year():
    current_year = datetime.date.today().year
    return f"- {current_year}" if current_year > 2023 else " "