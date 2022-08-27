import os
abs = os.path.dirname(__file__)
inp = 'inputfiles\\'
out = 'out\\'
inppath = os.path.join(abs, inp)
outpath = os.path.join(abs, out)
files = next(os.walk(inppath), (None, None, []))[2]

allLines = []
longest = 0
for f in files:
  allLines.append(open(inppath + f, encoding = 'utf-8').read().split('\n'))
  if (len(allLines[-1]) > longest):
    longest = len(allLines[-1])
for x in allLines:
  for i in range(longest):
    x.append('')
rotated = list(zip(*allLines))

outputfile = open(outpath + 'output.txt', 'w', encoding = 'utf-8')
for x in rotated:
  line = ''.join(x)
  if (line != ''):
    outputfile.write(line + '\n')


