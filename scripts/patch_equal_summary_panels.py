from pathlib import Path

path = Path('PingerApp/PingerApp.py')
text = path.read_text(encoding='utf-8')

replacements = {
    'self.best_avg_btn.setMinimumWidth(104)': 'self.best_avg_btn.setMinimumWidth(92)',
    'self.worst_avg_btn.setMinimumWidth(104)': 'self.worst_avg_btn.setMinimumWidth(92)',
    'self.combined_avg_btn.setMinimumWidth(104)': 'self.combined_avg_btn.setMinimumWidth(92)',
    'alert_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)': 'alert_group.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)',
    'alert_group.setMinimumSize(175,120)': 'alert_group.setMinimumSize(0,120)',
    'stats_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)': 'stats_group.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)',
    'stats_group.setMinimumSize(335,120)': 'stats_group.setMinimumSize(0,120)',
    'sg = QGridLayout(); sg.setContentsMargins(8,8,12,8)': 'sg = QGridLayout(); sg.setContentsMargins(8,8,8,8)',
    'sg.setHorizontalSpacing(12); sg.setVerticalSpacing(6)': 'sg.setHorizontalSpacing(8); sg.setVerticalSpacing(6)',
    'sg.setColumnMinimumWidth(2, 104)': 'sg.setColumnMinimumWidth(2, 92)',
    'jit_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)': 'jit_group.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)',
    'jit_group.setMinimumSize(255,120)': 'jit_group.setMinimumSize(0,120)',
    'panel_h.addWidget(alert_group, 2)': 'panel_h.addWidget(alert_group, 3)',
}

for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f'Expected text not found: {old}')
    text = text.replace(old, new, 1)

# Keep the first three summary panels on identical stretch factors.
if 'panel_h.addWidget(stats_group, 3)' not in text or 'panel_h.addWidget(jit_group, 3)' not in text:
    raise SystemExit('Expected summary stretch factors not found')

path.write_text(text, encoding='utf-8')
