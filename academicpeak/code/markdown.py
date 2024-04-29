import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hongzhe.settings')


class MarkdownDirectoryManager:
    """
    Manages a directory containing Markdown files, typically for an academic content management system.
    """

    def __init__(self, directory_path=None):
        # Initialize the manager with a given directory path, defaulting to a specific path if none is provided.
        self.directory_path = directory_path or os.path.join(settings.BASE_DIR, 'academicpeak', 'static', 'markdown')

    def get_folder_data(self):
        # Check if the markdown directory exists and is a directory; return an empty list if it doesn't exist.
        if not os.path.exists(self.directory_path) or not os.path.isdir(self.directory_path):
            print("Markdown directory does not exist.")
            return []

        folder_data = []
        # Create a list of folders in the directory.
        folder_list = [folder for folder in os.listdir(self.directory_path) if
                       os.path.isdir(os.path.join(self.directory_path, folder))]

        for folder_name in folder_list:
            # Retrieve items in each folder and sort them.
            items = self.get_items_in_folder(folder_name)["items"]
            sorted_items = sorted(items)
            # Append the folder name and its sorted items to the folder_data list.
            folder_data.append({
                "name": folder_name,
                "items": sorted_items
            })

        return folder_data

    def get_items_in_folder(self, folder_name):
        # Construct the path for the folder.
        folder_path = os.path.join(self.directory_path, folder_name)
        # Check if the folder exists and is a directory, return empty list if not.
        if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
            print(f"Folder '{folder_name}' does not exist.")
            return {"items": []}

        # List all markdown file names (without extension) in the folder.
        items = [item.split('.')[0] for item in os.listdir(folder_path) if
                 os.path.isfile(os.path.join(folder_path, item))]
        return {"items": items}

    def get_folder(self):
        # Check if the markdown directory exists and is a directory; if not, return an empty list.
        if not os.path.exists(self.directory_path) or not os.path.isdir(self.directory_path):
            print("Markdown directory does not exist.")
            return []

        # List all directories within the directory_path.
        folders = [folder for folder in os.listdir(self.directory_path) if
                   os.path.isdir(os.path.join(self.directory_path, folder))]
        return folders


if __name__ == "__main__":
    markdown_manager = MarkdownDirectoryManager()
    folder_data = markdown_manager.get_folder_data()
    print(folder_data)
    folder = markdown_manager.get_folder()
    print(folder)
