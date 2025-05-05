import argparse
from views import AttachmentsCleaner


class AttachmentsCleanerCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog="Obsidian Attachments Cleaner, the CLI utility",
            usage="[-run]",
            description="This simple CLI utility can help you to remove unused attachments in your obsidian vault",
            epilog="""  
        Enjoy the Obsidian Attachments Cleaner ❤ ❤ ❤  
        You can see more information and examples in 'README.md' or GitHub:        https://github.com/zizevskikh-dev/obsidian-attachments-cleaner.git            Obsidian Attachments Cleaner ver.2.0.1  
        Created by Aleksander Zizevskikh, 2025        Email: zizevskikh.dev@gmail.com""",
            formatter_class=argparse.RawTextHelpFormatter,
        )
        self.arguments = self.add_arguments_to_parser()
        self.cleaner = AttachmentsCleaner()

    def add_arguments_to_parser(self):
        self.parser.add_argument(
            "-run",
            "--run_cleaning",
            action="store_true",
            help="""Runs Obsidian Attachments Cleaner utility  
            Optional argument:  
        [--silent] Hide a terminal output""",
        )
        self.parser.add_argument(
            "-s",
            "-silent",
            "--silent_cleaning",
            action="store_false",
            help="""Hide a terminal output"""
        )
        return self.parser.parse_args()



    def run_attachments_cleaner_cli(self):
        if self.arguments.run_cleaning:
            self.cleaner.run_attachments_cleaner()

        if not self.arguments.silent_cleaning:
            self.cleaner.print_terminal_output()
