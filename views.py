import re
import os
from config import set_path


class AttachmentCleaner:
    def __init__(self):
        self.VALUE_DIR, self.ATTACHMENT_DIR = set_path()
        self.MARKDOWN_FILE_PATHS = []
        self.ATTACHMENT_FILE_NAMES_AND_PATHS =[]
        self.ATTACHMENT_FILES_IN_LINKS = []
        self.USABLE_ATTACHMENT_FILE_PATHS = []

    def run(self):
        files_before_cleaning = self.count_attachment_files()
        self.add_file_paths()
        self.catch_links_in_text()
        self.add_usable_attachment_file_paths()
        self.clean()
        files_after_cleaning = self.count_attachment_files()
        files_diff = files_before_cleaning - files_after_cleaning

        if files_diff:
            print("🧹" * 25)
            print(f"\nCleaned {files_diff} unused attachment file(-s)", end="\n\n")
            print("Files before cleaning:", files_before_cleaning)
            print("Files after cleaning:", files_after_cleaning, end="\n\n")
            print("🧹" * 25)
        else:
            print("🗇 " * 25)
            print("\nThere aren't unused attachment files to clean", end="\n\n")
            print("🗇 " * 25)

    def count_attachment_files(self):
        files_amount = 0
        for root, dirs, files in os.walk(self.ATTACHMENT_DIR):
            files_amount += len(files)
        return files_amount

    def add_file_paths(self):
        for root, dirs, files in os.walk(self.VALUE_DIR):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                if file_name.endswith(".md"):
                    self.MARKDOWN_FILE_PATHS.append(file_path)
                else:
                    self.ATTACHMENT_FILE_NAMES_AND_PATHS.append((file_name, file_path))

    def catch_links_in_text(self):
        for md_file_path in self.MARKDOWN_FILE_PATHS:
            with open(md_file_path, mode="r", encoding="utf-8") as file:
                content = file.read()

            pattern = r"!\[\[.*?\..*?\]\]"
            matches = re.findall(pattern, content)

            for match in matches:
                if match not in self.ATTACHMENT_FILES_IN_LINKS:
                    link_file_name = match.replace("![[", "").replace("]]", "").split("|")[0].strip()
                    self.ATTACHMENT_FILES_IN_LINKS.append(link_file_name)

    def add_usable_attachment_file_paths(self):
        for link_file_name in self.ATTACHMENT_FILES_IN_LINKS:
            for file_name, file_path in self.ATTACHMENT_FILE_NAMES_AND_PATHS:
                if file_name in link_file_name:
                    self.USABLE_ATTACHMENT_FILE_PATHS.append(file_path)

    def clean(self):
        for file_name, file_path in self.ATTACHMENT_FILE_NAMES_AND_PATHS:
            if file_path not in self.USABLE_ATTACHMENT_FILE_PATHS:
                os.remove(file_path)
