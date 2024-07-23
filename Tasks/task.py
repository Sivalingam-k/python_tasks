#create an menu card list
# 1) Create a menu_card list
# veg_starter = ['paneer 65','chilly paneer','veg crispy']
# 1) Display menu card
# 2)Add Starter in the menu card
# 3)Update Starter in the menu card
# 4)Remove Starter in the menu card
 
# Example:
# Add : Which starter you want to add in menu?
# paneer roll
# ['Paneer 65','Chilly paneer','Veg crispy','Paneer roll']
# Added Successfully


    
def add_food(veg_starter):
    food=input('Enter the food :')
    add_menu=veg_starter.append(food)
    print('Food Addded Successfully!!!')
    print('See The food Menu ',veg_starter)

def update_food(veg_starter,update_list,update_item):
    veg_starter[update_list]=update_item
    return veg_starter
    
def remove_food(veg_starter,remove_food_item):
    veg_starter.remove(remove_food_item)
    return veg_starter

    

def main():
   print(f'1.Display Menu card\n 2.Add Starter\n 3.Update Starter\n 4.Remove Starter')
   veg_starter = ['paneer 65','chilly paneer','veg crispy']
   value=int(input("choose the option :"))
   if(value==1):
    print(menu_list())
   elif(value==2):
    veg_starter=add_food(veg_starter)
    print()
   elif(value==3):
    print('Food Menu :',veg_starter)
    update_list=int(input("enter the index of the Food :"))
    update_item=input("enter the item :")
    print(update_food(veg_starter,update_list,update_item))
    print('Food Updated Successfully!!')
    print()
   elif(value==4):
    print('Food Menu :',veg_starter)
    remove_food_item=input("enter the food to  removed : ")
    print(remove_food(veg_starter,remove_food_item))
    print('Food Deleted Successfully!!')
   else:
    print('Enter Valid Option!')

        





if __name__=='__main__':
    main()
