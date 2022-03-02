


n = input()
last = int(n)
count = 0
nl = list(n)
if len(nl) < 2:
    nl.append(n)
print(list(str(int(nl[0]) + int(nl[1]))))
while True:
  nl2 = list(str(int(nl[0]) + int(nl[1])))
  if len(nl2) < 2:
    nl2.append(nl2[0])
  nl2 = nl[1] + nl2[1]
  print(int(nl2))
  n = nl2
  nl = list(n)
  count +=1
  if int(nl2) == last:
    break
print(count)