
s = "Hello!"

print(s)

# Hello!
print(s[-2:-1])

# o
print(s[-4:-1])

# llo
print(s[-4:0:-1])

# le
print(s.find('l'))

# 2
print(s.isdigit())

False
print(s.isalnum())

False
print(s.upper())

# HELLO!
print(s.lower())

# hello!
S1 = 'spam'

S2 = 'eggs'

print(S1 + S2)

# spameggs
s[:]

# 'Hello!'
# Creating the the string 'spameggs':
s = 'spameggs'
print(s)

# spameggs
s[3:5]

# 'me'
s[3:5:-1]

# ''
s[:]

# 'spameggs'
s = s[0:4] + 'and' + s[4:]

s = s[0:4] + 'and' + s[4:]

print(s)

# spamandandeggs
print(s)

# spamandandeggs
s

# 'spamandandeggs'

s = 'orange green white'
print(s.split())
# Разбиение строки по разделителю, результат - список строк:
# ['orange', 'green', 'white']

colors = 'red green blue'
colors_split = colors.split() # список цветов по отдельности
print(colors_split)
colors_joined = ' and '.join(colors_split) # объединение строк
print(colors_joined)
# red and green and blue