def inp_num():
    return float(input("Введіть число: "))

def act():
    return str(input("Обери дію (+,-,*,/): "))

def answ(a,b,c):
    if c == '+' : 
        return(a+b)
    elif c == '-' : 
        return(a-b)
    elif c == '*' : 
        return(a*b)
    elif c == '/' : 
        if b == 0:
            print("Ділити на нуль неможливо!")
            return "error"
        return a / b
    else:
        print("Не правильно введено дію!")
        return "error"



def main():
    a = inp_num()
    b = inp_num()

    while True:
        c = act()
        d = answ(a, b, c)
        
        if d != "error":
            print("Відповідь:", d)
            break

if __name__ == "__main__":
    main()