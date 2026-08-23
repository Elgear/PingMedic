from pathlib import Path

path = Path("PingerApp/PingerApp.py")
text = path.read_text(encoding="utf-8")

import_marker = "from matplotlib.ticker import MultipleLocator, NullFormatter, Locator, NullLocator\n"
version_import = "from version import APP_NAME, APP_VERSION, APP_AUTHOR, GITHUB_REPOSITORY, GITHUB_ISSUES, OFFICIAL_RELEASES\n"
if version_import not in text:
    if import_marker not in text:
        raise SystemExit("Import marker not found")
    text = text.replace(import_marker, import_marker + version_import, 1)

button_marker = '''        self.help_tool_btn = QPushButton("Help")\n        self.help_tool_btn.setFixedSize(135, 30)\n        self.help_tool_btn.setToolTip("Open PingerApp help and field guide")\n        self.help_tool_btn.clicked.connect(self.show_help_window)\n'''
button_block = button_marker + '''        self.about_tool_btn = QPushButton("About")\n        self.about_tool_btn.setFixedSize(135, 30)\n        self.about_tool_btn.setToolTip("Show PingerApp version, author, official download, and issue-reporting information")\n        self.about_tool_btn.clicked.connect(self.show_about_dialog)\n'''
if "self.about_tool_btn = QPushButton(\"About\")" not in text:
    if button_marker not in text:
        raise SystemExit("Help button marker not found")
    text = text.replace(button_marker, button_block, 1)

list_marker = '''            self.report_tool_btn,\n            self.help_tool_btn,\n        ]\n'''
list_replacement = '''            self.report_tool_btn,\n            self.help_tool_btn,\n            self.about_tool_btn,\n        ]\n'''
if "            self.about_tool_btn,\n" not in text:
    if list_marker not in text:
        raise SystemExit("Tool button list marker not found")
    text = text.replace(list_marker, list_replacement, 1)

tip_marker = '''            "help_tool_btn": "Open PingerApp usage help and diagnostic guidance.",\n        }\n'''
tip_replacement = '''            "help_tool_btn": "Open PingerApp usage help and diagnostic guidance.",\n            "about_tool_btn": "Show the installed PingerApp version, author, official download location, and where to report bugs or ideas.",\n        }\n'''
if '"about_tool_btn":' not in text:
    if tip_marker not in text:
        raise SystemExit("Tooltip marker not found")
    text = text.replace(tip_marker, tip_replacement, 1)

method_marker = "    def show_help_window(self):\n"
method = '''    def show_about_dialog(self):\n        """Show version, authorship, official distribution, and reporting details."""\n        box = QMessageBox(self)\n        box.setIcon(QMessageBox.Information)\n        box.setWindowTitle(f"About {APP_NAME}")\n        box.setText(f"<b>{APP_NAME}</b><br>Version {APP_VERSION}")\n        box.setInformativeText(\n            f"Developed by {APP_AUTHOR}.\\n\\n"\n            "Windows network diagnostics and monitoring utility.\\n\\n"\n            f"Official source: {GITHUB_REPOSITORY}\\n"\n            f"Official installers: {OFFICIAL_RELEASES}\\n\\n"\n            "If you find a problem or have an idea for an improvement, please open a GitHub Issue:\\n"\n            f"{GITHUB_ISSUES}\\n\\n"\n            "For security-sensitive reports, follow SECURITY.md in the official repository."\n        )\n        box.setStandardButtons(QMessageBox.Ok)\n        box.exec_()\n\n'''
if "    def show_about_dialog(self):\n" not in text:
    if method_marker not in text:
        raise SystemExit("show_help_window marker not found")
    text = text.replace(method_marker, method + method_marker, 1)

path.write_text(text, encoding="utf-8")
