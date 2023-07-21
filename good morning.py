import time
t = time.strftime('%H:,%M :,%S')
hour=int(time.strftime('%H'))
hour= int(input("enter the number"))
print(hour)
if(hour>=0 and hour <12):
 print("good morning")
elif(hour>=12 and hour<17):
 print("good after noon")
if(hour<=17 and hour<0):
        print("good nit")

