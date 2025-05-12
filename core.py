import os
import re
from typing import List, Tuple, Set
from config import Config


class AttachmentsCleaner:
    """Cleans unused attachments from an Obsidian vault."""

    def __init__(self) -> None:
        self.config = Config()
        self.markdown_files: List[Tuple[str, str]] = []
        self.attachments: List[Tuple[str, str]] = []
        self.attachments_referenced: Set[str] = set()
        self.stats = {
            "before": 0,
            "after": 0,
        }

    def run(self) -> None:
        """Run the full cleaning workflow."""
        self._scan_vault()
        self.stats["before"] = len(self.attachments)
        self._find_used_attachments()
        self._remove_unused_attachments()
        self.stats["after"] = len(self.attachments)

    def _scan_vault(self) -> None:
        """Recursively scan the vault for markdown and attachment files."""
        for root, _, files in os.walk(self.config.VAULT_ROOT):
            if not any(excluded in root for excluded in self.config.EXCLUDED_DIRS):
                for filename in files:
                    path = os.path.join(root, filename)
                    if filename.endswith(".md"):
                        self.markdown_files.append((filename, path))
                    elif filename not in self.config.EXCLUDED_FILES:
                        self.attachments.append((filename, path))

    def _find_used_attachments(self) -> None:
        """Find all referenced attachments in markdown files."""
        pattern = r"!\[\[.*?\..*?\]\]"
        for _, path in self.markdown_files:
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
            matches = re.findall(pattern, content)
            for reference in matches:
                filename = (reference.replace("![[", "").replace("]]", "").split("|")[0].strip())
                self.attachments_referenced.add(filename)

    def _remove_unused_attachments(self) -> None:
        """Remove files not referenced in markdown files."""
        for filename, path in self.attachments[:]:
            if filename not in self.attachments_referenced:
                os.remove(path)
                self.attachments.remove((filename, path))

    def print_cleaning_report(self) -> None:
        """Print a summary report of the cleaning process."""
        before = self.stats["before"]
        after = self.stats["after"]
        removed = before - after

        if removed > 0:
            print(f"🧹 Scanned {before} attachments")
            print(f"✅ Removed {removed} unused files")
            print(f"📊 Before: {before} | After: {after}")
        else:
            print("🗁 Vault is already clean!")
