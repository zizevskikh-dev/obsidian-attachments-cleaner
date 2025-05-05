from views import AttachmentsCleaner


if __name__ == "__main__":
    cleaner = AttachmentsCleaner()
    cleaner.run_attachments_cleaner()
    cleaner.print_terminal_output()
