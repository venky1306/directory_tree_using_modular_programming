import json

# DirectoryTree class
class DirectoryTree:
    def __init__(self):
        self.tree = None
        self.ids = []
        self.names = []
    
    # load json data
    def load_from_json(self, json_data):
        if isinstance(json_data, dict) and "structure" in json_data and "ids" in json_data and "names" in json_data:
            self.tree = json_data["structure"]
            self.ids = json_data["ids"]
            self.names = json_data["names"]
        else:
            self.tree = None
            self.ids = []
            self.names = []

    # add folder to tree and update ids and names lists accordingly. Given parent_id and folder_name
    def add_folder(self, parent_id, folder_name):
        if self.tree is None:
            print("Directory tree is not loaded.")
            return

        parent_folder = self._find_folder(parent_id)
        if parent_folder is None:
            print("Parent folder not found.")
            return

        if folder_name in self.names:
            print("Folder name already exists.")
            return

        new_id = self._generate_unique_id()

        new_folder = {"id": new_id, "name": folder_name, "subfolders": []}
        parent_folder["subfolders"].append(new_folder)

        self.ids.append(new_id)
        self.names.append(folder_name)

    # remove folder in tree given folder_id using helper function _find_parent_folder
    def remove_folder(self, folder_id):
        if self.tree is None:
            print("Directory tree is not loaded.")
            return

        folder = self._find_folder(folder_id)
        if folder is None:
            print("Folder not found.")
            return
        if folder_id ==0:
            print("Can't delete root folder")
            return

        parent_folder = self._find_parent_folder(folder_id)
        if parent_folder is None:
            self.tree["subfolders"] = [subfolder for subfolder in self.tree["subfolders"] if subfolder["id"] != folder_id]
        else:
            parent_folder["subfolders"] = [subfolder for subfolder in parent_folder["subfolders"] if subfolder["id"] != folder_id]

        self.ids.remove(folder_id)
        self.names.remove(folder["name"])


    # fetch path of folder given folder_id using helper function _find_parent_folder by finding parent folder and appending to path
    def fetch_path(self, folder_id):
        if self.tree is None:
            print("Directory tree is not loaded.")
            return None

        folder = self._find_folder(folder_id)
        if folder is None:
            print("Folder not found.")
            return None

        path = [folder["name"]]
        parent_folder = self._find_parent_folder(folder_id)
        print(parent_folder)
        while parent_folder is not None:
            path.append(parent_folder["name"])
            parent_folder = self._find_parent_folder(parent_folder["id"])
        path.append("root")

        path.reverse()
        return "/".join(path)


    # update folder name given folder_id and new_name using helper function _find_folder
    def update_folder_name(self, folder_id, new_name):
        if self.tree is None:
            print("Directory tree is not loaded.")
            return

        folder = self._find_folder(folder_id)
        if folder is None:
            print("Folder not found.")
            return

        if new_name in self.names:
            print("Folder name already exists.")
            return
        if folder_id ==0:
            print("Can't change name of root folder")
            return

        self.names.remove(folder["name"])
        self.names.append(new_name)
        folder["name"] = new_name

    def _find_folder(self, folder_id, search_folder=None):
        if search_folder is None:
            search_folder = self.tree

        if search_folder["id"] == folder_id:
            return search_folder

        for subfolder in search_folder["subfolders"]:
            found_folder = self._find_folder(folder_id, subfolder)
            if found_folder is not None:
                return found_folder

        return None

    def _find_parent_folder(self, folder_id, search_folder=None, parent_folder=None):
        if search_folder is None:
            search_folder = self.tree

        for subfolder in search_folder["subfolders"]:
            if subfolder["id"] == folder_id:
                return parent_folder

            found_parent = self._find_parent_folder(folder_id, subfolder, subfolder)
            if found_parent is not None:
                return found_parent

        return None

    def _generate_unique_id(self):
        new_id = max(self.ids) + 1 if self.ids else 1
        return new_id
    
    def save_to_json(self, file_path):
        if self.tree is None:
            print("Directory tree is not loaded.")
            return

        json_data = {"structure": self.tree, "ids": self.ids, "names": self.names}
        with open(file_path, 'w') as file:
            json.dump(json_data, file, indent=4)
        
    
