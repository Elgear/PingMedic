from pathlib import Path

path = Path("PingerApp/PingerApp.py")
text = path.read_text(encoding="utf-8")


def replace_once(old: str, new: str, label: str):
    global text
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one match, found {count}")
    text = text.replace(old, new, 1)


replace_once(
'''        def style_summary_cell(widget):
            widget.setStyleSheet(summary_cell_style)
            widget.setMinimumHeight(24)
            return widget
''',
'''        SUMMARY_CELL_HEIGHT = 28

        def style_summary_cell(widget):
            widget.setStyleSheet(summary_cell_style)
            widget.setFixedHeight(SUMMARY_CELL_HEIGHT)
            return widget
''',
"summary cell height",
)

replace_once(
'''        ag = QGridLayout(); ag.setContentsMargins(8,8,8,8)
        ag.setHorizontalSpacing(8); ag.setVerticalSpacing(6)
        ag.setColumnStretch(0, 1)
        ag.setColumnStretch(1, 1)
''',
'''        ag = QGridLayout(); ag.setContentsMargins(8,8,8,8)
        ag.setHorizontalSpacing(8); ag.setVerticalSpacing(6)
        ag.setAlignment(Qt.AlignTop)
        ag.setColumnStretch(0, 1)
        ag.setColumnStretch(1, 1)
        self.reset_btn.setFixedHeight(SUMMARY_CELL_HEIGHT)
''',
"alert summary layout",
)

replace_once(
'''        sg.setColumnStretch(2, 0)
        sg.setColumnMinimumWidth(2, 92)
        style_summary_cell(self.avg_low_label)
''',
'''        sg.setColumnStretch(2, 0)
        sg.setColumnMinimumWidth(2, 92)
        sg.setAlignment(Qt.AlignTop)
        for button in (self.best_avg_btn, self.worst_avg_btn, self.combined_avg_btn):
            button.setFixedHeight(SUMMARY_CELL_HEIGHT)
        style_summary_cell(self.avg_low_label)
''',
"latency summary layout",
)

replace_once(
'''        jl = QGridLayout(); jl.setContentsMargins(8,8,8,8)
        jl.setHorizontalSpacing(12); jl.setVerticalSpacing(6)
        style_summary_cell(self.jit_low_label)
''',
'''        jl = QGridLayout(); jl.setContentsMargins(8,8,8,8)
        jl.setHorizontalSpacing(8); jl.setVerticalSpacing(6)
        jl.setAlignment(Qt.AlignTop)
        jl.setColumnStretch(0, 2)
        jl.setColumnStretch(1, 1)
        jl.setColumnStretch(2, 0)
        jl.setColumnMinimumWidth(2, 92)
        for button in (self.jit_min_btn, self.jit_max_btn, self.jit_avg_btn):
            button.setFixedHeight(SUMMARY_CELL_HEIGHT)
        style_summary_cell(self.jit_low_label)
''',
"jitter summary layout",
)

replace_once(
'''        kwargs = {
            "capture_output": True,
            "text": True,
            "timeout": 10,
            "encoding": "utf-8",
            "errors": "replace",
        }
        if hasattr(subprocess, "CREATE_NO_WINDOW"):
            kwargs["creationflags"] = subprocess.CREATE_NO_WINDOW
        completed = subprocess.run(
            ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", script],
            **kwargs,
        )
''',
'''        kwargs = {
            "capture_output": True,
            "text": True,
            "timeout": 20,
            "encoding": "utf-8",
            "errors": "replace",
        }
        if hasattr(subprocess, "CREATE_NO_WINDOW"):
            kwargs["creationflags"] = subprocess.CREATE_NO_WINDOW
        try:
            completed = subprocess.run(
                ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", "-"],
                input=script,
                **kwargs,
            )
        except subprocess.TimeoutExpired:
            raise RuntimeError("Windows PowerShell adapter query timed out. Try Refresh Adapter Info again.")
        except FileNotFoundError:
            raise RuntimeError("Windows PowerShell was not found on this system.")
''',
"adapter PowerShell invocation",
)

replace_once(
'''    def _set_adapter_info_error(self, message: str):
        fallback = {
''',
'''    def _set_adapter_info_error(self, message: str):
        safe_message = re.sub(r"\\s+", " ", str(message or "")).strip()
        if not safe_message:
            safe_message = "Windows could not return adapter details."
        if "Command '['powershell'" in safe_message or len(safe_message) > 240:
            safe_message = "Windows PowerShell could not return adapter details."

        fallback = {
''',
"adapter error sanitization",
)

replace_once(
'''                f"{message}\\n\\n"
                "The app could not read Windows adapter link-speed data. "
''',
'''                f"{safe_message}\\n\\n"
                "The app could not read Windows adapter link-speed data. "
''',
"adapter diagnosis message",
)

path.write_text(text, encoding="utf-8")
print("Diagnostic UI polish applied successfully.")
