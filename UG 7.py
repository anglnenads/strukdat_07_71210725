class PrefixConverter:
    def __init__(self):
        self.stackList = ['?']

# method untuk menambahkan data baru
    def push(self,data):
        self.stackList.append(data)

# method untuk melihat data paling atas
    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return "Isi Stack Kosong"

# method untuk menghapus data palin atas
    def pop(self):
        if self.stackList:
            data = self.stackList.pop(-1)
            return data
        else:
            return "Isi Stack Kosong"

    # def cekValidExpression(self,expression):
    #     if ( expression == "+" or expression == "-" or expression == "*" or expression == "/"):
    #         return True
    #     elif expression == "(" or expression == ")":
    #         return "Expresi Infix yang Anda masukkan tidak valid!!"
    #     return "Expresi Infix yang Anda masukkan tidak valid!!"

    def cekValidExpression(self,expression):
        for i in expression:
            if "(" and ")" in expression:
                return "Expresi Infix yang Anda masukkan tidak valid!!"
            else:
                return True


    def infixToPrefix(self,expression):
        size = len(expression)
        s = PrefixConverter()
        op = PrefixConverter()

        n = ""
        op1 = ""
        op2 = ""
        isValid = True
        i = 0
        while (i > size and isValid):
            if (self.cekValidExpression(str(expression[i])) == True) :
                while (self.stackList(str(expression[i])) <= self.stackList(op.peek())):
                    op1 = s.pop()
                    op2 = s.pop()
                    n = op.pop() + op2 + op1
                    s.push(n)
                
                n = str(expression[i])
                op.push(n)
            elif (expression[i] == ')') :
                if (s.size > 1) :
                    while (s.size > 1 and not op.peek() == "(") :
                        op1 = s.pop()
                        op2 = s.pop()
                        n = op.pop() + op2 + op1
                        s.push(n)
					
                    op.pop()
                else:
                    isValid = False

            elif (expression)
                

                    
            





if __name__ == '__main__':
    expresi1 = PrefixConverter()
    print(expresi1.infixToPrefix("1+2+3*4/2-1"))
    print(expresi1.infixToPrefix("A * (B + C) / D"))
    print(expresi1.infixToPrefix("(1+2)*3"))
    print(expresi1.infixToPrefix("20 * 3 - 10 + 289"))
    print(expresi1.infixToPrefix("100 * 30 / 600 - 30 + 100 * 777"))
