#Extract all hashtags (#) from a sentence.

import re

sentence = "I am learning #Python and #DataScience"

hashtags = re.findall(r"#\w+", sentence)
print(hashtags)