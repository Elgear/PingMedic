from pathlib import Path

path = Path("PingerApp/PingerApp.py")
text = path.read_text(encoding="utf-8")

old = '''        # §3.B.c Alert-Counts panel
        alert_group = QGroupBox("Alert Counts")
'''
new = '''        # §3.B.c Alert-Counts panel
        # Give summary values a subtle cell treatment for clearer row scanning
        # without making the interface visually heavy.
        summary_cell_style = (
            "QLabel { border: 1px solid #d8d8d8; border-radius: 2px; "
            "padding: 3px 6px; background-color: #fafafa; }"
        )

        def style_summary_cell(widget):
            widget.setStyleSheet(summary_cell_style)
            widget.setMinimumHeight(24)
            return widget

        def summary_caption(text):
            label = QLabel(text)
            return style_summary_cell(label)

        alert_group = QGroupBox("Alert Counts")
'''
if old not in text:
    raise SystemExit("Alert Counts section marker not found")
text = text.replace(old, new, 1)

repls = {
'''        ag.addWidget(QLabel("Latency breaches:"), 0,0)\n        ag.addWidget(self.lat_count_label,        0,1)\n        ag.addWidget(QLabel("Loss breaches:"),    1,0)\n        ag.addWidget(self.loss_count_label,       1,1)\n        ag.addWidget(QLabel("Packet Loss (%):"),  2,0)\n        ag.addWidget(self.loss_value_label,       2,1)\n''':
'''        style_summary_cell(self.lat_count_label)\n        style_summary_cell(self.loss_count_label)\n        style_summary_cell(self.loss_value_label)\n        ag.addWidget(summary_caption("Latency breaches:"), 0,0)\n        ag.addWidget(self.lat_count_label,                     0,1)\n        ag.addWidget(summary_caption("Loss breaches:"),    1,0)\n        ag.addWidget(self.loss_count_label,                    1,1)\n        ag.addWidget(summary_caption("Packet Loss (%):"),  2,0)\n        ag.addWidget(self.loss_value_label,                    2,1)\n''',
'''        sg.addWidget(QLabel("Avg best 10:"),  0,0)\n        sg.addWidget(self.avg_low_label,      0,1)\n''':
'''        style_summary_cell(self.avg_low_label)\n        sg.addWidget(summary_caption("Avg best 10:"),  0,0)\n        sg.addWidget(self.avg_low_label,                    0,1)\n''',
'''        sg.addWidget(QLabel("Avg worst 10:"), 1,0)\n        sg.addWidget(self.avg_high_label,     1,1)\n''':
'''        style_summary_cell(self.avg_high_label)\n        sg.addWidget(summary_caption("Avg worst 10:"), 1,0)\n        sg.addWidget(self.avg_high_label,                    1,1)\n''',
'''        sg.addWidget(QLabel("Avg combined:"), 2,0)\n        sg.addWidget(self.avg_comb_label,     2,1)\n''':
'''        style_summary_cell(self.avg_comb_label)\n        sg.addWidget(summary_caption("Avg combined:"), 2,0)\n        sg.addWidget(self.avg_comb_label,                    2,1)\n''',
'''        jl.addWidget(QLabel("Min jitter:"),   0,0)\n        jl.addWidget(self.jit_low_label,      0,1)\n''':
'''        style_summary_cell(self.jit_low_label)\n        jl.addWidget(summary_caption("Min jitter:"), 0,0)\n        jl.addWidget(self.jit_low_label,                 0,1)\n''',
'''        jl.addWidget(QLabel("Max jitter:"),   1,0)\n        jl.addWidget(self.jit_high_label,     1,1)\n''':
'''        style_summary_cell(self.jit_high_label)\n        jl.addWidget(summary_caption("Max jitter:"), 1,0)\n        jl.addWidget(self.jit_high_label,                 1,1)\n''',
'''        jl.addWidget(QLabel("Avg jitter:"),   2,0)\n        jl.addWidget(self.jit_avg_label,      2,1)\n''':
'''        style_summary_cell(self.jit_avg_label)\n        jl.addWidget(summary_caption("Avg jitter:"), 2,0)\n        jl.addWidget(self.jit_avg_label,                 2,1)\n''',
'''            hi.addWidget(QLabel(label_text), row, 0)\n            hi.addWidget(value_label, row, 1)\n''':
'''            style_summary_cell(value_label)\n            hi.addWidget(summary_caption(label_text), row, 0)\n            hi.addWidget(value_label, row, 1)\n'''
}

for old_block, new_block in repls.items():
    if old_block not in text:
        raise SystemExit(f"Expected summary block not found: {old_block[:80]!r}")
    text = text.replace(old_block, new_block, 1)

path.write_text(text, encoding="utf-8")

# trigger
