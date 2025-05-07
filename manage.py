"""Main entry point for the Obsidian Attachments Cleaner.

Initializes and runs the command line interface.
"""


from cli import AttachmentsCleanerCLI


if __name__ == "__main__":
    """Entry point for the command line interface."""
    cli_controller = AttachmentsCleanerCLI()
    cli_controller.run_attachments_cleaner_cli()
