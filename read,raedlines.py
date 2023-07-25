f=open("my file .txt","r")
 while True:
           line=f.readline( )
           m1=f.split("")[0]
            m2=f.split("")[1]
            m3=f.split("")[2]

           print("marks of student {i} in maths  is:{m1}")
           print("marks of student {i} in english is:{m2}")
             print("marks of student {i} in sst  is:{m3}    ")
           if not line:
               print(line,type (line))
           break
