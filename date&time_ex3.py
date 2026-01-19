#Add 30 days to the current date.
from datetime import datetime, timedelta
today = datetime.today()
new_date = today + timedelta(days=30)
print("Current Date:", today.date())
print("Date after 30 days:", new_date.date())

#Output:
#Current Date: 2026-01-19
#Date after 30 days: 2026-02-18