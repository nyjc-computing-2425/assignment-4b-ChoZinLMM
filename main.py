stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

stdform_list = list(stdform)
valid = list("0123456789x.^eE-")
caret_find = int(stdform.find('^'))
exponent = stdform[caret_find + 1:]
error = "Error converting to scientific E notation."

for x in range(len(stdform)):
  if stdform[x] not in valid:
    print(error)
    exit()

if ' ' in stdform:
  print(error)

for sign in ['.', 'x', '^']:
  if stdform_list.count(sign) > 1:
    print(error)
    exit()

for x in range(len(exponent)):
  if exponent[x] not in "0123456789-":
    print(error)
    exit()

else :
  notation = stdform.replace('x10^', 'E')
  print('This number in E notation is '+ notation + '.')