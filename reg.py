import re
text="ab ab c34 cc67"
k=re.sub("\s","#",text)
print(k)