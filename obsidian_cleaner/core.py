from pathlib import Path
import re
from typing import Dict, List, Set, Tuple
from obsidian_cleaner.config import Config


class AttachmentsCleaner:
    """Cleans unused attachments from an Obsidian vault."""

    def __init__(self) -> None:
        self.config = Config()
        self.markdown_files: List[Tuple[str, Path]] = []
        self.attachments: List[Tuple[str, Path]] = []
        self.attachments_referenced: Set[str] = set()
        self.stats: Dict[str, int] = {
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
        for item in self.config.VAULT_ROOT.rglob("*"):
            if self._should_include_item(item):
                if item.suffix == ".md":
                    self.markdown_files.append((item.name, item))
                elif item.is_file():
                    self.attachments.append((item.name, item))

    def _should_include_item(self, item: Path) -> bool:
        """Check if item should be included in processing."""
        # Skip excluded directories
        if any(excluded in item.parents for excluded in self.config.EXCLUDED_DIRS):
            return False

        # Skip excluded files
        if item in self.config.EXCLUDED_FILES:
            return False

        return True

    def _find_used_attachments(self) -> None:
        """Find all referenced attachments in markdown files."""
        pattern = re.compile(r"!\[\[([^|\]]+)(?:\|.*?)*]]")
        for _, md_file in self.markdown_files:
            try:
                content = md_file.read_text(encoding="utf-8")
                for match in pattern.finditer(content):
                    filename = match.group(1).strip()
                    self.attachments_referenced.add(filename)
            except UnicodeDecodeError:
                continue

    def _remove_unused_attachments(self) -> None:
        """Remove files not referenced in markdown files."""
        for filename, filepath in self.attachments[:]:
            if filename not in self.attachments_referenced:
                try:
                    filepath.unlink()
                    self.attachments.remove((filename, filepath))
                except OSError as e:
                    print(f"Error deleting {filepath}: {e}")

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
