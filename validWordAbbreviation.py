def validWordAbbreviation(word: str, abbr: str) -> bool:
  i,j=0,0
  while i<len(word) and j<len(abbr):
    if abbr[j].isaplpha():
      if word[i]!=abbr[j]:
        return False
      i+=1
      j+=1
    elif abbr[j].isdigit():
      if abbr[j]=='0':
        return False
      num=0
      while j<len(abbr) and abbr[j].isdigit():
        num=num*10+int(abbr[j])
        j+=1
      i+=num
    else:
      return False
  return i==len(word) and j==len(abbr)

# https://leetcode.com/problems/valid-word-abbreviation
