"""Main entry point for Obsidian Attachments Cleaner."""

from cli import AttachmentsCleanerCLI


if __name__ == "__main__":
    """Entry point for the CLI application."""
    cli_controller = AttachmentsCleanerCLI()
    cli_controller.run_attachments_cleaner_cli()
