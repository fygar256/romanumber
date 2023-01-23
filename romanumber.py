#!/usr/bin/python3
import sys

TABINT=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
TABROMA=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
ERRPAT=['DD','LL','VV', # 500,50,5 がダブらないように
        'CMC','CDC','XCX','XLX','IXI','IVI',
                  #CMCM,CMCのようなエラーパターンは'CMC'にまとめてある
        'DCD','LXL','VIV'] # 515のパターン

def toint(s):
  s=s.upper()
  for i in ERRPAT:
    if (i in s): return(-1)
  a=0
  i=0
  j=0
  while(s):
    if (s.startswith(TABROMA[i])):
      j=j+1
      a+=TABINT[i]
      s=s.replace(TABROMA[i],'',1)
      if (j<3):
        continue
    j=0
    i+=1
    if (i==len(TABROMA)):
      break
  if (s): # IF ILLEGAL FORMAT
    return(-1)
  return(a)

def toroman(a):
  s=""
  i=0
  while(a!=0):
    while((a//TABINT[i])!=0):
      s+=TABROMA[i]
      a-=TABINT[i]
    i+=1
  return s

print("自然数を入力して下さい:",end='')
a=int(input())
if (a>=4000):
  print("too big")
  sys.exit(1)
print(toroman(a))
print("ローマ数字を入力して下さい:",end='')
s=input()
i=toint(s)
if (i==-1):
  print("Invalid Roman Number")
  sys.exit(1)
print(i)
