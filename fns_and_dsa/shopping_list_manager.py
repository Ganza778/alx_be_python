def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add = input("Enter item to add: ")
            shopping_list.append(add)
        
        elif choice == '2':
            remove = input("Enter item to remove: ")
            if remove not in shopping_list:
                print("Invalid option: Item not found in the list.")
            else:
             shopping_list.remove(remove)
        
        elif choice == '3':
            for item in shopping_list:
                print(item)
          
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()