import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hongzhe.settings')


class AcademyDirectoryManager:
    """Manage the video directory of AP Academy"""

    def __init__(self, directory_path=None):
        # If no directory path is provided, set the default path using settings.BASE_DIR
        self.directory_path = directory_path or os.path.join(settings.BASE_DIR, 'academicpeak', 'static', 'academy')

    def get_folder_data(self):
        # Check if the directory exists and is a directory, return empty list if not
        if not os.path.exists(self.directory_path) or not os.path.isdir(self.directory_path):
            return []

        folder_data = []
        # List all folders in the directory
        folder_list = [folder for folder in os.listdir(self.directory_path) if
                       os.path.isdir(os.path.join(self.directory_path, folder))]

        for folder_name in folder_list:
            # Retrieve unique items in each folder
            unique_items = self.get_unique_items_in_folder(folder_name)["items"]
            # Sort the items alphabetically
            sorted_items = sorted(unique_items)
            # Append the folder name and its sorted items to the folder_data list
            folder_data.append({
                "name": folder_name,
                "items": sorted_items
            })

        return folder_data

    def get_unique_items_in_folder(self, folder_name):
        # Construct the path for the folder
        folder_path = os.path.join(self.directory_path, folder_name)
        # Check if the folder exists and is a directory, return empty list if not
        if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
            print(f"Folder '{folder_name}' does not exist.")
            return {"items": []}

        unique_items = set()
        # Iterate over the items in the folder
        for item in os.listdir(folder_path):
            # Split the item name and extension
            item_name, item_extension = os.path.splitext(item)
            # Add the item name to the set if it's a file
            if os.path.isfile(os.path.join(folder_path, item)):
                unique_items.add(item_name)

        return {"items": list(unique_items)}


# 使用示例
if __name__ == '__main__':
    directory_manager = AcademyDirectoryManager()
    folder_data = directory_manager.get_folder_data()
    print(folder_data)
