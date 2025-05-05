import re
import os
from config import Config


class AttachmentsCleaner:
    def __init__(self):
        self.config = Config()
        self.markdown = []
        self.attachments = []
        self.attachments_used = []
        self.attachments_counter = {
            "before_cleaning": 0,
            "after_cleaning": 0,
        }

    def run_attachments_cleaner(self):
        self.walk_obsidian_vault()
        self.attachments_counter["before_cleaning"] = len(self.attachments)
        self.catch_attachments_links_in_markdown_files()
        self.remove_unused_attachments()
        self.attachments_counter["after_cleaning"] = len(self.attachments)

    def walk_obsidian_vault(self):
        for root, dirs, files in os.walk(self.config.VAULT_PATH):
            if not any(
                dir_ignored in root for dir_ignored in self.config.DIRS_TO_IGNORE
            ):
                for file in files:
                    if file.endswith(".md"):
                        self.markdown.append((file, os.path.join(root, file)))
                    else:
                        if not any(
                            file_ignored in file
                            for file_ignored in self.config.FILES_TO_IGNORE
                        ):
                            self.attachments.append((file, os.path.join(root, file)))

    def catch_attachments_links_in_markdown_files(self):
        for markdown_filename, markdown_path in self.markdown:
            with open(markdown_path, mode="r", encoding="utf-8") as file:
                content = file.read()
                pattern = r"!\[\[.*?\..*?\]\]"
                markdown_attachment_links = re.findall(pattern, content)

            if markdown_attachment_links:
                for link in markdown_attachment_links:
                    attachment_filename = (
                        link.replace("![[", "").replace("]]", "").split("|")[0].strip()
                    )
                    if attachment_filename not in self.attachments_used:
                        self.attachments_used.append(attachment_filename)

    def remove_unused_attachments(self):
        for attachment_index, attachment in enumerate(self.attachments):
            attachment_filename = attachment[0]
            attachment_path = attachment[1]
            if attachment_filename not in self.attachments_used:
                os.remove(attachment_path)
                self.attachments.remove(attachment)

    def print_terminal_output(self):
        attachments_removed = (
            self.attachments_counter["before_cleaning"]
            - self.attachments_counter["after_cleaning"]
        )

        if attachments_removed:
            print("🧹" * 25)
            print(f"\nCleaned {attachments_removed} unused attachment(-s)", end="\n\n")
            print("Attachments before cleaning:", attachments_removed)
            print("Attachments after cleaning:", attachments_removed, end="\n\n")
            print("🧹" * 25)
        else:
            print("🗇 " * 25)
            print("\nThere aren't unused attachments to clean", end="\n\n")
            print("🗇 " * 25)
