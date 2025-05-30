# Obsidian Attachments Cleaner 🧹

A lightweight CLI utility that **removes unused attachments** from your Obsidian vault — safely and efficiently.

---

## ✨ Features

- ⚙️ **Configurable**
  - Easily customize ignored directories and files
- 🔍 **Vault Scanning**
  - Recursively analyzes markdown files and attachments
- 🕵️‍♂️ **Smart Detection**
  - Identifies only truly unused attachments
- 🧹 **Safe Cleaning**
  - Preserves files in protected folders like `.obsidian`, `.git`, etc.
- 🖥️ **Flexible Output**
  - Choose between silent or verbose report mode

---

## Installation 📦

### Requirements

- 🐍 Python **3.12+** ([Download Python](https://www.python.org/downloads/))
- 🗁 An existing Obsidian vault

### Clone the Repository

```bash
git clone https://github.com/zizevskikh-dev/obsidian-attachments-cleaner.git
```

---

## Configuration ⚙️

> ⚠️ Before first use, customize the `config.py`.

### 1. Set the vault root path

**Example:**
- *Linux/macOS*: `/home/username/Documents/OBSIDIAN_VAULT`
- *Windows*: `C:\Users\Username\Documents\OBSIDIAN_VAULT`

```python
@staticmethod
def _get_vault_root() -> Path:
    return Path.home() / "Documents" / "OBSIDIAN_VAULT"
```

### 2. Exclude directories and files

```python
def _get_excluded_dirs(self) -> Set[Path]:
    return {
        self.VAULT_ROOT / ".obsidian",
        self.VAULT_ROOT / ".git",
    }
```

```python
def _get_excluded_files(self) -> Set[Path]:
    return {
        self.VAULT_ROOT / ".gitignore",
    }
```

---

## Usage 🚀

### Run in silent mode
```bash
python3 main.py
```

### Run with a detailed cleaning report

```bash
python3 main.py -s
# or
python3 main.py --show
```
	 
---
## Output Examples  📊

### 🔍 Cleaning Report

```bash
🧹 Scanned 25 attachments
✅ Removed 5 unused files
📊 Before: 25 | After: 20
```

### 🏆 Nothing to Remove

```bash
🗁 Vault is already clean!
```

---

## 🧠 How It Works

1. **Scans** all markdown (`.md`) files and attachments in your vault
2. **Extracts references** to attachments used inside markdown
3. **Deletes** any file not referenced — unless it’s excluded

---

## 🛠️ Project Info

- **Version:** 2.2.1
- **Maintainer:** Aleksander Zizevskikh
- **License:** MIT

---

## ❤️ Thank You for Using Obsidian Attachments Cleaner
