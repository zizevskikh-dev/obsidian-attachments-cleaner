import os


def set_path():
    home_path = os.path.expanduser("~")
    VALUE_DIR = f"{home_path}/Documents/OBSIDIAN_VAULT/IT"
    ATTACHMENT_DIR = f"{VALUE_DIR}/attachment_files"

    if os.name != "posix":
        VALUE_DIR = VALUE_DIR.replace("/", "\\")
        ATTACHMENT_DIR = ATTACHMENT_DIR.replace("/", "\\")

    return VALUE_DIR, ATTACHMENT_DIR
