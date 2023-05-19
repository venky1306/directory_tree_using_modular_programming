from directory_tree import DirectoryTree
from loader import load_json

def load_directory_tree_from_json(file_path):
    directory_tree = DirectoryTree()
    json_data = load_json(file_path)
    directory_tree.load_from_json(json_data)
    return directory_tree

def main():
    file_path = 'config.json'
    directory_tree = load_directory_tree_from_json(file_path)
    start = input("Press Enter to continue...")

    while True:
        print("1. Add a folder")
        print("2. Remove a folder")
        print("3. Fetch the path of a folder")
        print("4. Update the name of a folder")
        print("5. Print the updated directory tree")
        print("6. Save and exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                parent_id = int(input("Enter parent id: "))
                folder_name = input("Enter folder name: ")
                directory_tree.add_folder(parent_id, folder_name)
            elif choice == 2:
                folder_id = int(input("Enter folder id: "))
                directory_tree.remove_folder(folder_id)
            elif choice == 3:
                folder_id = int(input("Enter folder id: "))
                folder_path = directory_tree.fetch_path(folder_id)
                print("Folder Path:", folder_path)
            elif choice == 4:
                folder_id = int(input("Enter folder id: "))
                folder_name = input("Enter folder name: ")
                directory_tree.update_folder_name(folder_id, folder_name)
            elif choice == 5:
                print("Directory Tree:", directory_tree.tree)
            elif choice == 6:
                directory_tree.save_to_json(file_path)
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer choice.")

if __name__ == '__main__':
    main()
