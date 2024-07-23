def main():
  name=input("enter the string: ")
  for i in range(len(name)-1):
    count=1
    for j in range(i+1,len(name)):
        if(name[i]==name[j]):
           count+=1
    print(f'{name[i]} is repeated {count}')





if __name__=="__main__":
    main()