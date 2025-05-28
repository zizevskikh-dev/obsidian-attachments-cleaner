import argparse
from obsidian_cleaner.core import AttachmentsCleaner


class AttachmentsCleanerCLI:
    """Command-line interface for the Obsidian Attachments Cleaner."""

    def __init__(self) -> None:
        self.args = self._create_parser().parse_args()
        self.cleaner = AttachmentsCleaner()

    @staticmethod
    def _create_parser() -> argparse.ArgumentParser:
        """Create and return the argument parser."""
        parser = argparse.ArgumentParser(
            prog="Obsidian Attachments Cleaner CLI",
            usage="[-s | --show]",
            description="Remove unused attachments from your Obsidian vault.",
            epilog="❤️ Thank you for using Obsidian Attachments Cleaner!",
            formatter_class=argparse.RawTextHelpFormatter,
        )
        parser.add_argument(
            "-s",
            "--show",
            dest="show_output",
            action="store_true",
            help="Display the cleaning report after execution",
        )
        return parser

    def run(self) -> None:
        """Run the cleaner and optionally show the report."""
        self.cleaner.run()
        if self.args.show_output:
            self.cleaner.print_cleaning_report()
