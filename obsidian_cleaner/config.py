from pathlib import Path
from typing import Set


class Config:
    """Configuration for Obsidian vault paths and exclusions."""

    def __init__(self) -> None:
        self.VAULT_ROOT: Path = self._get_vault_root()
        self.EXCLUDED_DIRS: Set[Path] = self._get_excluded_dirs()
        self.EXCLUDED_FILES: Set[Path] = self._get_excluded_files()

    @staticmethod
    def _get_vault_root() -> Path:
        """Get the absolute path to the Obsidian vault directory.

        Automatically adapts to the current OS for cross-platform compatibility.

        Returns:
            Path: Absolute path to the Obsidian vault directory.
        """
        return Path.home() / "Documents" / "OBSIDIAN_VAULT"

    def _get_excluded_dirs(self) -> Set[Path]:
        """Get a set of directory paths to exclude from processing.

        Returns:
            Set[Path]: Paths of directories to exclude.
        """
        return {
            self.VAULT_ROOT / ".obsidian",
            self.VAULT_ROOT / ".git",
        }

    def _get_excluded_files(self) -> Set[Path]:
        """Get a set of filenames to exclude from processing.

        Returns:
            Set[Path]: Filenames to exclude
        """
        return {
            self.VAULT_ROOT / ".gitignore",
        }
