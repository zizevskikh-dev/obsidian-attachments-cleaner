import argparse
from views import AttachmentsCleaner


class AttachmentsCleanerCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog="Obsidian Attachments Cleaner, the CLI utility",
            usage="[-r | -run] [-s | -show]",
            description="This simple CLI utility can help you to remove unused attachments in your obsidian vault",
            epilog="""Enjoy the Obsidian Attachments Cleaner ❤ ❤ ❤\nYou can see more information and examples in 'README.md' or GitHub:\nhttps://github.com/zizevskikh-dev/obsidian-attachments-cleaner.git\n\nObsidian Attachments Cleaner ver.2.0.1\nCreated by Aleksander Zizevskikh, 2025\nEmail: zizevskikh.dev@gmail.com""",
            formatter_class=argparse.RawTextHelpFormatter,
        )
        self.arguments = self.add_arguments_to_parser()
        self.cleaner_view = AttachmentsCleaner()

    def add_arguments_to_parser(self):
        self.parser.add_argument(
            "-r",
            "-run",
            "--run_cleaning",
            action="store_true",
            help="run obsidian attachments cleaner utility",
        )
        self.parser.add_argument(
            "-s",
            "-show",
            "--show_output",
            action="store_true",
            help="show a terminal output",
        )
        return self.parser.parse_args()

    def run_attachments_cleaner_cli(self):
        if self.arguments.run_cleaning:
            self.cleaner_view.run_attachments_cleaner()

        if self.arguments.show_output:
            self.cleaner_view.print_terminal_output()
