from pathlib import Path

replacements = {
    Path('PingerApp/PingerApp.py'): [
        ('headers={"User-Agent": "PingerApp/1.0"}', 'headers={"User-Agent": "PingMedic/1.0"}'),
        ('self.setWindowTitle("Home Pinger")', 'self.setWindowTitle("PingMedic")'),
        ('Open PingerApp help and field guide', 'Open PingMedic help and field guide'),
        ('Open PingerApp usage help and diagnostic guidance.', 'Open PingMedic usage help and diagnostic guidance.'),
        ('<h1>PingerApp Help</h1>', '<h1>PingMedic Help</h1>'),
        ('<p>PingerApp is a local network troubleshooting tool.', '<p>PingMedic is a local network troubleshooting tool.'),
        ('PingerApp includes iperf3 at', 'PingMedic includes iperf3 at'),
        ('PingerApp_Report_', 'PingMedic_Report_'),
    ],
    Path('PingerApp.spec'): [('name="PingerApp"', 'name="PingMedic"')],
    Path('installer/PingerApp.iss'): [
        ('#define MyAppName "PingerApp"', '#define MyAppName "PingMedic"'),
        ('#define MyAppDisplayName "Home Pinger"', '#define MyAppDisplayName "PingMedic"'),
        ('#define MyAppPublisher "PingerApp"', '#define MyAppPublisher "PingMedic"'),
        ('#define MyAppExeName "PingerApp.exe"', '#define MyAppExeName "PingMedic.exe"'),
        ('DefaultDirName={autopf}\\PingerApp', 'DefaultDirName={autopf}\\PingMedic'),
        ('OutputBaseFilename=PingerApp_Setup_{#MyAppVersion}', 'OutputBaseFilename=PingMedic_Setup_{#MyAppVersion}'),
        ('Source: "..\\dist\\PingerApp\\*"', 'Source: "..\\dist\\PingMedic\\*"'),
    ],
    Path('scripts/build_windows.ps1'): [('dist\\PingerApp\\PingerApp.exe', 'dist\\PingMedic\\PingMedic.exe')],
    Path('scripts/build_installer.ps1'): [
        ('dist\\PingerApp\\PingerApp.exe', 'dist\\PingMedic\\PingMedic.exe'),
        ('installer_output\\PingerAppSetup-0.1.0.exe', 'installer_output\\PingMedicSetup-0.1.0.exe'),
    ],
    Path('README.md'): [
        ('# PingerApp', '# PingMedic'),
        ('PingerAppSetup-0.1.0.exe', 'PingMedic_Setup_0.1.0.exe'),
        ('PingerApp is a local troubleshooting tool', 'PingMedic is a local troubleshooting tool'),
        ('PingerApp source code', 'PingMedic source code'),
        ('dist\\PingerApp\\PingerApp.exe', 'dist\\PingMedic\\PingMedic.exe'),
    ],
}

for path, pairs in replacements.items():
    text = path.read_text(encoding='utf-8')
    for old, new in pairs:
        if old not in text:
            raise SystemExit(f'Expected text not found in {path}: {old}')
        text = text.replace(old, new)
    path.write_text(text, encoding='utf-8')

# trigger 5
