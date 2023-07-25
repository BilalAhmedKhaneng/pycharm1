#how to change finction and update

def hello():
    print("hello world")
    def greet(fx):
        def mfx():
            print("good morning")
            fx()
            print("thanks using function")
            return mfx
        @greet
        def hello():
    print("hello world2")
def add(a,b):
        print(a+b)
hello( )
