class Calc:
    def add(x,y):
        answer = x + y
        print(answer)
        return answer

    def sub (x,y):
        answer = x - y
        print(answer)
    
    def mult(x,y):
        answer = x * y
        print(answer)

    def div(x,y):
        answer = x / y
        print(answer) 

# testing functions in Calc class
addittion =Calc.add(4,6)
print(f"4 plus 6 is {addittion}")