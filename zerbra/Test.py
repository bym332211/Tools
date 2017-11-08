import re

pattern = re.compile(r'#[0-9]+')

a = "#1234 5asdf4"
match = pattern.search(a)
print(pattern.split(a))