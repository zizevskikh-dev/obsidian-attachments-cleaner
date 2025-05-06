"""Configuration module for the Obsidian Attachments Cleaner.

This module contains the Config class which handles all configuration settings
for the cleaning unused attachments, including:
    - path to the Obsidian vault directory;
    - paths to the ignored directories;
    - ignored files.
"""

import os
from typing import List


class Config:
    """Handles configuration settings for the Obsidian Attachments Cleaner.

    Attributes:
        VAULT_PATH (str): Path to the Obsidian vault directory.
        DIRS_TO_IGNORE (List[str]): List of directories to exclude from processing.
        FILES_TO_IGNORE (List[str]): List of files to exclude from processing.
    """

    def __init__(self) -> None:
        """Initialize Config with default paths and ignore settings."""
        self.VAULT_PATH = self.set_obsidian_vault_path()
        self.DIRS_TO_IGNORE = self.set_dirs_to_ignore()
        self.FILES_TO_IGNORE = self.set_files_to_ignore()

    @staticmethod
    def set_obsidian_vault_path() -> str:
        """Sets the absolute path to the Obsidian vault.

        Automatically converts path separators to match the current operating system
        (ensuring cross-platform compatibility).

        Returns:
            str: Absolute path to the Obsidian vault directory.
        """
        obsidian_vault_path = os.path.join(
            os.path.expanduser("~"),
            "Documents",
            "OBSIDIAN_VAULT",
        )
        return obsidian_vault_path

    def set_dirs_to_ignore(self) -> List[str]:
        """Set directories to exclude from processing.

        These directories will not be scanned for attachments or markdown files.

        Returns:
            List[str]: Absolute paths of directories to ignore.
        """
        dirs_to_ignore = [
            os.path.join(self.VAULT_PATH, ".obsidian"),
            os.path.join(self.VAULT_PATH, ".git"),
        ]
        return dirs_to_ignore

    @staticmethod
    def set_files_to_ignore() -> List[str]:
        """Set files to exclude from processing.

        These files will not be removed.

        Returns:
            List[str]: Names of files to ignore.
        """
        files_to_ignore = [
            ".gitignore",
        ]
        return files_to_ignore
