# Write a pattern to extract all email addresses from a string.

import re
text = "Please contact us at alice277@gmail.com or visit our website at https://www.alice22.com."

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(pattern, text)
print(emails)
