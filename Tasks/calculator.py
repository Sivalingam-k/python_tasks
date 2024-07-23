def main():
    print('Welcome to calculator !')
    num1=int(input("Enter the value 1 :"))
    num2=int(input('Enter the value 2 :'))
    print('1.Addition 2.Subtraction 3.Multiplication 4.Division')
    option=int(input('Choose the option to perform '))
    if(option==1):
       print(f'{num1} ,{num2} addition is :',num1+num2)
    elif(option==2):
        print(f'{num1} ,{num2} Subtraction is :',num1-num2)  
    elif(option==3):
       
        print(f'{num1} ,{num2} Multiplication is :',num1*num2)  
    elif(option==4):
        print(f'{num1} ,{num2} Division is :',num1/num2)  
    else:
        print('Enter Valid Option')






if __name__=='__main__':
    main()        