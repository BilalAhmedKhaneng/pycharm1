st=input("eneter the message")
words=st.split(" ")
coding=True
if(coding):
    nwords=[ ]
    for word in words:
     if(len(word)>=3):
      r1="dfr"
    r2="kjg"
stnew=r1+st[1:]    + word[0]+r2
nwords.append(stnew)
print(("").join(nwords))
