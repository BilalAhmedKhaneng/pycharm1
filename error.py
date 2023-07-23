#error handling
a=input("enter the number ")
print(f"multiplaction table of {a} is:")
try:
for i in range(1,11):
 print(f"{int(a)} x {i} ={int(a)*i}")
 except exception as e:
 print(e)

 print("some important line of code")
 print("end of programme")
