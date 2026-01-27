#Replace all whitespace in a string with hyphens.
import re

text = "Hello, i am a intern at v-ex tech solutions."
result = re.sub(r"\s", "-", text)
print(result)

#Output :
#Hello,-i-am-a-intern-at-v-ex-tech-solutions
