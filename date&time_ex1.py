# Print today’s date in 'DD/MM/YYYY' format.
from datetime import datetime
today = datetime.now()
formatted_date = today.strftime("%d/%m/%Y")
print("Today's date:", formatted_date)

# Output:
#Today's date: 19/01/2026
