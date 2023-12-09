import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hongzhe.settings')


class MarkdownDirectoryManager:
    """Define the MarkdownDirectoryManager class for managing Markdown directories"""
    def __init__(self, directory_path=None):
        """Constructor which creates a new instance of the Manager class if no directory path is provided"""
        self.directory_path = directory_path or os.path.join(settings.BASE_DIR, 'academicpeak', 'static', 'markdown')

    def get_folder_data(self):
        """Retrieve all subdirectories under the specified Markdown directory"""
        if not os.path.exists(self.directory_path) or not os.path.isdir(self.directory_path):
            print("Markdown directory does not exist.")
            return []

        folder_data = []
        folder_list = [folder for folder in os.listdir(self.directory_path) if
                       os.path.isdir(os.path.join(self.directory_path, folder))]

        for folder_name in folder_list:
            items = self.get_items_in_folder(folder_name)["items"]
            sorted_items = sorted(items)
            folder_data.append({
                "name": folder_name,
                "items": sorted_items
            })

        return folder_data

    def get_items_in_folder(self, folder_name):
        """Retrieve all files under the specified folder"""
        folder_path = os.path.join(self.directory_path, folder_name)
        if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
            print(f"Folder '{folder_name}' does not exist.")
            return {"items": []}

        items = [item.split('.')[0] for item in os.listdir(folder_path) if
                 os.path.isfile(os.path.join(folder_path, item))]
        return {"items": items}


if __name__ == "__main__":
    markdown_manager = MarkdownDirectoryManager()
    folder_data = markdown_manager.get_folder_data()
    print(folder_data)
