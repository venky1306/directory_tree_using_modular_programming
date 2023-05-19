# Directory tree using modular programming - Python

To run the code for the directory tree using modular programming, you will need the following packages:
1. JSON

To run the code 
- python3 main.py

### Things to improve
1. I used ids of folders to remove/add folders. we can do better with directly giving the folder name.
2. Can use tkinter for better gui than command line.
3. Can optimize by using parent_id in the folder meta data.

### Corner cases handled
1. Checking the list before adding new folder, to avoid multiple folders with same name.
2. Cannot delete or modify the root directory.
3. exception handling to avoid code crashing when asking user for prompt.


### Config file
`{
    "structure": {
        "id": 0,
        "name": "Root",
        "subfolders": [
            {
                "id": 1,
                "name": "Folder1",
                "subfolders": [
                    {
                        "id": 3,
                        "name": "Folder5",
                        "subfolders": []
                    }
                ]
            },
            {
                "id": 2,
                "name": "Folder2",
                "subfolders": []
            }
        ]
    },
    "ids": [
        0,
        1,
        2,
        3
    ],
    "names": [
        "Root",
        "Folder1",
        "Folder2",
        "Folder5"
    ]
}`

### Adding Folder
<img width="345" alt="Screenshot 2023-05-18 at 11 43 12 PM" src="https://github.com/venky1306/directory_tree_using_modular_programming/assets/47674519/07a0d4b2-526c-4c9d-94ef-ef30a34d8abd">

### Remove Folder
<img width="1121" alt="Screenshot 2023-05-18 at 11 45 51 PM" src="https://github.com/venky1306/directory_tree_using_modular_programming/assets/47674519/5902c315-9523-4b1e-bd8b-7861ae4875cf">

### Getting Path
<img width="484" alt="Screenshot 2023-05-18 at 11 46 26 PM" src="https://github.com/venky1306/directory_tree_using_modular_programming/assets/47674519/80e79aa6-7083-4f2b-8937-eac229d06d8d">

### Changing name of the folder
<img width="1099" alt="Screenshot 2023-05-18 at 11 48 01 PM" src="https://github.com/venky1306/directory_tree_using_modular_programming/assets/47674519/5be728cc-2237-4d23-9d24-22beb48c50d3">
