import os
from typing import Set


class Config:
    """Configuration for Obsidian vault paths and exclusions."""

    def __init__(self) -> None:
        self.VAULT_ROOT: str = self._get_vault_root()
        self.EXCLUDED_DIRS: Set[str] = self._get_excluded_dirs()
        self.EXCLUDED_FILES: Set[str] = self._get_excluded_files()

    @staticmethod
    def _get_vault_root() -> str:
        """Get the absolute path to the Obsidian vault directory.

        Automatically adapts to the current OS for cross-platform compatibility.

        Returns:
            str: Absolute path to the Obsidian vault directory.
        """
        return os.path.join(os.path.expanduser("~"), "Documents", "OBSIDIAN_VAULT")

    def _get_excluded_dirs(self) -> Set[str]:
        """Get a set of directory paths to exclude from processing.

        Returns:
            Set[str]: Paths of directories to exclude.
        """
        return {
            os.path.join(self.VAULT_ROOT, ".obsidian"),
            os.path.join(self.VAULT_ROOT, ".git"),
        }

    @staticmethod
    def _get_excluded_files() -> Set[str]:
        """Get a set of filenames to exclude from processing.

        Returns:
            Set[str]: Filenames to exclude
        """
        return {".gitignore"}
