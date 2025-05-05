import os
from typing import List


class Config:
    def __init__(self):
        self.VAULT_PATH = self.set_obsidian_vault_path()
        self.DIRS_TO_IGNORE = self.set_dirs_to_ignore()
        self.FILES_TO_IGNORE = self.set_files_to_ignore()

    @staticmethod
    def set_obsidian_vault_path() -> str:
        """Sets the absolute path to the obsidian vault.

        Automatically converts path separators to match the current operating system
        (ensuring cross-platform compatibility).

        Returns:
            str: Absolute path to the directory where attachments are stored.
        """
        # Set the absolute path to your obsidian vault
        obsidian_vault_path = os.path.join(
            os.path.expanduser("~"),
            "Documents",
            "OBSIDIAN_VAULT",
        )

        return obsidian_vault_path

    def set_dirs_to_ignore(self) -> List[str]:
        """Set the absolute paths to directories where files will be excluded from removing

        Returns:
            List[str]: Directories paths excluded from removing
        """
        dirs_to_ignore = [
            os.path.join(self.VAULT_PATH, ".obsidian"),
            os.path.join(self.VAULT_PATH, ".git"),
        ]

        return dirs_to_ignore

    @staticmethod
    def set_files_to_ignore() -> List[str]:
        """Set filenames which will be excluded from removing

        Returns:
            List[str]: Filenames excluded from removing
        """
        files_to_ignore = [
            ".gitignore",
        ]

        return files_to_ignore
