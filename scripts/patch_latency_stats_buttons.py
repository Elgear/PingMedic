from pathlib import Path

path = Path("PingerApp/PingerApp.py")
text = path.read_text(encoding="utf-8")

old = '''        stats_group.setMinimumSize(280,120)\n        sg = QGridLayout(); sg.setContentsMargins(8,8,8,8)\n        sg.setHorizontalSpacing(12); sg.setVerticalSpacing(6)\n'''
new = '''        stats_group.setMinimumSize(330,120)\n        sg = QGridLayout(); sg.setContentsMargins(8,8,8,8)\n        sg.setHorizontalSpacing(12); sg.setVerticalSpacing(6)\n        sg.setColumnStretch(0, 2)\n        sg.setColumnStretch(1, 1)\n        sg.setColumnStretch(2, 0)\n        sg.setColumnMinimumWidth(2, 112)\n'''
if old not in text:
    raise SystemExit("Latency Stats layout block not found")
text = text.replace(old, new, 1)

for attr in ("best_avg_btn", "worst_avg_btn", "combined_avg_btn"):
    marker = f"        self.{attr}.setCheckable(True)"
    if marker not in text:
        raise SystemExit(f"Button marker not found: {attr}")
    text = text.replace(marker, f"        self.{attr}.setMinimumWidth(112)\n" + marker, 1)

path.write_text(text, encoding="utf-8")
