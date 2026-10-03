"""
>>> chr(41)
')'
>>> ord(')')
41
>>>
"""

# due to ascii values
# 'a' > 'A'
name = "Wesley James Chastain"

print('a' > 'A')
for index in range(len(name)):
    ascii_value = ord(name[index])
    print(ascii_value, end=" ")
    print(chr(ascii_value))