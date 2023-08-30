import os
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hongzhe.settings')

class AcademyDirectoryManager:
    def __init__(self, directory_path=None):
        self.directory_path = directory_path or os.path.join(settings.BASE_DIR, 'academicpeak', 'static', 'academy')

    def get_folder_data(self):
        if not os.path.exists(self.directory_path) or not os.path.isdir(self.directory_path):
            print("Markdown directory does not exist.")
            return []

        folder_data = []
        folder_list = [folder for folder in os.listdir(self.directory_path) if
                       os.path.isdir(os.path.join(self.directory_path, folder))]

        for folder_name in folder_list:
            unique_items = self.get_unique_items_in_folder(folder_name)["items"]
            sorted_items = sorted(unique_items)  # Sort items here
            folder_data.append({
                "name": folder_name,
                "items": sorted_items
            })

        return folder_data

    def get_unique_items_in_folder(self, folder_name):
        folder_path = os.path.join(self.directory_path, folder_name)
        if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
            print(f"Folder '{folder_name}' does not exist.")
            return {"items": []}

        unique_items = set()
        for item in os.listdir(folder_path):
            item_name, item_extension = os.path.splitext(item)
            if os.path.isfile(os.path.join(folder_path, item)):
                unique_items.add(item_name)

        return {"items": list(unique_items)}

# 使用示例
if __name__ == '__main__':
    directory_manager = AcademyDirectoryManager()
    folder_data = directory_manager.get_folder_data()
    print(folder_data)
