import os
class ManualsManager:
    def __init__(self):
        path_to_list = self.root_path_generator('static\manuals')
        # Get the list of folders in the specified path
        self.folders_list = [f for f in os.listdir(path_to_list) if os.path.isdir(os.path.join(path_to_list, f))]
        self.folder_file_dict = {}
        for folder_name in self.folders_list:
            opened_path = path_to_list +"\\"+ folder_name
            files = os.listdir(opened_path)
            # Filter out only files (excluding directories)
            
            self.file_urls_dict = {}
            for file in files:
                if os.path.isfile(os.path.join(opened_path, file)):
                    self.file_urls_dict[file] = os.path.join(opened_path, file)
                else:
                    print(f"Error reading directory {opened_path}")
            self.folder_file_dict[folder_name] = self.file_urls_dict

    def get_manual_path(self, folder: str):
        # Return the path for the specified folder, or None if not found
        return self.folder_file_dict.get(folder)
    

    def root_path_generator(self, current_folder_name: str) -> str:
        current_path = os.getcwd()
        # Combine the current path with the specific folder you want to list
        path_to_list = os.path.join(current_path, current_folder_name)
        return path_to_list
