def main():
  name=input("enter the string: ") #Siva
  list={}
  for i in name:
    if i in list:
      list[i]=list[i]+1
    else:
      list[i]=1
  print(list)      







if __name__=="__main__":
    main()