def add_funtion(veg_starter,add_list,index):
    veg_starter[index]=add_list
    return veg_starter
def update_function(veg_starter,update_list,update_item):
    veg_starter[update_list]=update_item
    return veg_starter
def remove_function(veg_starter,remove_list):
    veg_starter.pop(remove_list)
    return veg_starter
def main():
    menu_options={
        1 : "Dispaly menu list",
        2 : "Add on the menu list",
        3 : "Update on the menu list",
        4 : "remove from the menu list"
    }
    veg_starter={}
    index=1
    size=int(input("Enter the Size: "))
    for i in range(size):
        key=index
        item=input("Enter the item: ")
        veg_starter[key]=item
        index+=1
    
        
    
    
    
    while True:
        print()
        print(menu_options)
        print()
        choice=int(input("enter your choice: "))

        if(choice==1):
            print(veg_starter)
            continue
        elif(choice==2):
            add_list=input("which starter do you want to add in the menu: ")
            print(add_funtion(veg_starter,add_list,index))
            index+=1
            break

            
        elif(choice==3):
            update_list=int(input("enter the number to be update: "))
            update_item=input("enter the item name :")
            print(update_function(veg_starter,update_list,update_item))
        
        elif(choice==4):
            remove_list=int(input("enter the number to be removed: "))
            print(remove_function(veg_starter,remove_list))
            
        else:
            print("you have enter the wrong choice")
            break


if __name__=="__main__":
    main()            