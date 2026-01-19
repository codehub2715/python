#Convert a datetime to a timestamp and back.
from datetime import datetime
now = datetime.now()
timestamp = now.timestamp()
print("Current DateTime:", now)
print("Timestamp:", timestamp)


dt_from_timestamp = datetime.fromtimestamp(timestamp)
print("DateTime from Timestamp:", dt_from_timestamp)


#Output:
#Current DateTime: 2026-01-19 13:49:27.892050
#Timestamp: 1768810767.89205
#DateTime from Timestamp: 2026-01-19 13:49:27.892050
