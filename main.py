from obsidian_cleaner.cli import AttachmentsCleanerCLI


def main() -> None:
    """
    Entry point for running the Obsidian Attachments Cleaner CLI.
    """
    cli = AttachmentsCleanerCLI()
    cli.run()


if __name__ == "__main__":
    main()
