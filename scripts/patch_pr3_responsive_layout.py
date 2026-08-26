from pathlib import Path

path = Path("PingerApp/PingerApp.py")
text = path.read_text(encoding="utf-8")

replacements = [
    (
        '''        self.move(100,100)\n        self.resize(1460, 900)\n        self.setMinimumSize(1440, 940)\n''',
        '''        self.move(60, 40)\n        # Start large enough to show the full diagnostic layout comfortably,\n        # while keeping the window resizable for laptops, DPI scaling and\n        # larger desktop displays.\n        screen = QApplication.primaryScreen()\n        if screen is not None:\n            available = screen.availableGeometry()\n            start_width = min(1600, max(1200, int(available.width() * 0.96)))\n            start_height = min(1000, max(760, int(available.height() * 0.94)))\n            self.resize(start_width, start_height)\n        else:\n            self.resize(1500, 940)\n        self.setMinimumSize(1180, 740)\n'''
    ),
    (
        '''        alert_group.setMinimumSize(165,120)\n''',
        '''        alert_group.setMinimumSize(175,120)\n'''
    ),
    (
        '''        stats_group.setMinimumSize(235,120)\n''',
        '''        stats_group.setMinimumSize(280,120)\n'''
    ),
    (
        '''        jit_group.setMinimumSize(215,120)\n''',
        '''        jit_group.setMinimumSize(255,120)\n'''
    ),
    (
        '''        host_info_group.setMinimumSize(260,120)\n''',
        '''        host_info_group.setMinimumSize(320,120)\n'''
    ),
    (
        '''        hi = QGridLayout(); hi.setContentsMargins(8,8,8,8)\n        hi.setHorizontalSpacing(8); hi.setVerticalSpacing(4)\n''',
        '''        hi = QGridLayout(); hi.setContentsMargins(8,8,8,8)\n        hi.setHorizontalSpacing(8); hi.setVerticalSpacing(4)\n        hi.setColumnStretch(0, 0)\n        hi.setColumnStretch(1, 1)\n'''
    ),
    (
        '''        host_info_group.setLayout(hi)\n\n        # combine panels\n        panel_h = QHBoxLayout(); panel_h.setAlignment(Qt.AlignLeft)\n        panel_h.addWidget(alert_group, 1)\n        panel_h.addWidget(stats_group, 2)\n        panel_h.addWidget(jit_group, 2)\n        panel_h.addWidget(host_info_group, 2)\n''',
        '''        host_info_group.setLayout(hi)\n\n        # Keep the summary row visually balanced. Host Info has the most rows,\n        # so use the tallest natural size for all four panels.\n        summary_group_height = max(\n            alert_group.sizeHint().height(),\n            stats_group.sizeHint().height(),\n            jit_group.sizeHint().height(),\n            host_info_group.sizeHint().height(),\n        )\n        for group in (alert_group, stats_group, jit_group, host_info_group):\n            group.setFixedHeight(summary_group_height)\n\n        # combine panels\n        panel_h = QHBoxLayout(); panel_h.setAlignment(Qt.AlignLeft)\n        panel_h.setSpacing(8)\n        panel_h.addWidget(alert_group, 2)\n        panel_h.addWidget(stats_group, 3)\n        panel_h.addWidget(jit_group, 3)\n        panel_h.addWidget(host_info_group, 4)\n'''
    ),
]

for old, new in replacements:
    if old not in text:
        raise SystemExit(f"Expected layout block not found:\n{old[:120]}")
    text = text.replace(old, new, 1)

path.write_text(text, encoding="utf-8")
