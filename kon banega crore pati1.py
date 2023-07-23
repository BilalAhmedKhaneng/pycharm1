questions =[
    [" which langue was used to create fb?",
             "java","c++","html","php","none",4],

    [" which langue was used to create fb?",
             "java","c++","html","php","none",4],

    [" which langue was used to create fb?",
             "java","c++","html","php","none",4],

    [" which langue was used to create fb?",
             "java","c++","html","php","none",4],

    ]
levels=[100,200,300,400,500,600,700]
for i in range(0,len(questions)):
    question = questions [i]
    print(f"questions for RS.{levels[i]}")
    print(f"a.{questions[1]}        b.{questions [2]}")
    print(f"c.{questions[3]}         d.{questions[4]}")
    reply= int(input("select the option"))
if (reply==questions[-1]):
        print("correct answrr")
if(i==4):
    money=100
      else if(i==9):
          money=200
else:
    print("wrong answers")
