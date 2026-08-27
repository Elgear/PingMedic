from pathlib import Path

path = Path('PingerApp/PingerApp.py')
text = path.read_text(encoding='utf-8')

old = '''    def _data_file_path(self, filename: str):
        root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
        return os.path.join(root, "data", filename)
'''
new = '''    def _data_file_path(self, filename: str):
        """Return a writable per-user data path for presets, history and reports."""
        if platform.system() == "Windows":
            base = os.environ.get("LOCALAPPDATA") or os.environ.get("APPDATA") or os.path.expanduser("~")
            root = os.path.join(base, "PingerApp", "data")
        else:
            base = os.environ.get("XDG_DATA_HOME") or os.path.join(os.path.expanduser("~"), ".local", "share")
            root = os.path.join(base, "PingerApp", "data")
        return os.path.join(root, filename)
'''

if old not in text:
    raise SystemExit('Expected _data_file_path implementation not found')
text = text.replace(old, new, 1)
path.write_text(text, encoding='utf-8')

# trigger
