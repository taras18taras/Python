
def arithmetic(arg1, arg2, op):
     if op == '+':
         return arg1 + arg2
     elif op == '-':
         return arg1 - arg2
     elif op == '*':
         return arg1 * arg2
     elif op == '/':
         return arg1 / arg2
     else:
        return "Неизвестная операция"

print(arithmetic(1,2,"+"))
print(arithmetic(1,2,"-"))
print(arithmetic(1,2,"*"))
print(arithmetic(1,2,"/"))
