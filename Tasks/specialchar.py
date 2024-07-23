def special_character(s):
    # Define special characters
    special_characters = "!@#$%^&*()-+?_=,<>/"
    
    # Check if string contains any special characters
    for char in s:
        if char in special_characters:
            return True
    
    return False
def main():
     input_string = input("Enter a string: ")
    
     if special_character(input_string):
        print("String contains special characters.")
     else:
        print("String does not contain any special characters.")


if __name__ == "__main__":
    main()
   