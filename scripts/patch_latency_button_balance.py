from pathlib import Path

path = Path("PingerApp/PingerApp.py")
text = path.read_text(encoding="utf-8")

replacements = {
    "self.best_avg_btn.setMinimumWidth(112)": "self.best_avg_btn.setMinimumWidth(104)",
    "self.worst_avg_btn.setMinimumWidth(112)": "self.worst_avg_btn.setMinimumWidth(104)",
    "self.combined_avg_btn.setMinimumWidth(112)": "self.combined_avg_btn.setMinimumWidth(104)",
    "stats_group.setMinimumSize(330,120)": "stats_group.setMinimumSize(335,120)",
    "sg = QGridLayout(); sg.setContentsMargins(8,8,8,8)": "sg = QGridLayout(); sg.setContentsMargins(8,8,12,8)",
    "sg.setColumnMinimumWidth(2, 112)": "sg.setColumnMinimumWidth(2, 104)",
}

for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f"Expected text not found: {old}")
    text = text.replace(old, new, 1)

path.write_text(text, encoding="utf-8")

# trigger
