"""Configuration handler for Obsidian Attachments Cleaner.

This module provides the AttachmentCleanerConfig class which manages all configuration
settings for the attachment cleanup process, including vault paths and exclusion settings.
"""

from pathlib import Path
from typing import Set


class AttachmentCleanerConfig:
    """Manages configuration settings for the Obsidian attachments cleaner.

    Attributes:
        OBSIDIAN_VAULT_ROOT (Path): Path to the root directory of the Obsidian vault.
        EXCLUDED_DIRECTORIES (Set[Path]): Set of directories paths to exclude from processing.
        EXCLUDED_FILES (Set[str]): Set of filenames to exclude from processing.
    """

    def __init__(self) -> None:
        """Initialize configuration with default paths and exclusion settings."""
        self.OBSIDIAN_VAULT_ROOT = self.get_obsidian_vault_root()
        self.EXCLUDED_DIRECTORIES = self.get_default_excluded_dirs()
        self.EXCLUDED_FILES = self.get_default_excluded_files()

    @staticmethod
    def get_obsidian_vault_root() -> Path:
        """Get the absolute path to the Obsidian vault directory.

        Returns:
            Path: Absolute path to the Obsidian vault directory.
        """
        return Path.home() / "Documents" / "OBSIDIAN_VAULT"

    def get_default_excluded_dirs(self) -> Set[Path]:
        """Get directories excluded by default.

        Returns:
            Set[Path]: Default excluded directories
        """
        return {
            self.OBSIDIAN_VAULT_ROOT / ".obsidian",
            self.OBSIDIAN_VAULT_ROOT / ".git",
        }

    @staticmethod
    def get_default_excluded_files() -> Set[str]:
        """Get files excluded by default.

        Returns:
            Set[str]: Default excluded filenames
        """
        return {
            ".gitignore",
        }
