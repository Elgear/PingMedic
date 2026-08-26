from pathlib import Path

path = Path("PingerApp/PingerApp.py")
text = path.read_text(encoding="utf-8")

old = '''        if   span<=5:    major = 0.5\n        elif span<=10:   major = 1\n        elif span<=20:   major = 2\n        elif span<=50:   major = 5\n        elif span<=100:  major = 10\n        elif span<=200:  major = 20\n        else:            major = 50\n'''

new = '''        if   span <= 5:     major = 0.5\n        elif span <= 10:    major = 1\n        elif span <= 20:    major = 2\n        elif span <= 50:    major = 5\n        elif span <= 100:   major = 10\n        elif span <= 250:   major = 25\n        elif span <= 500:   major = 50\n        elif span <= 1000:  major = 100\n        elif span <= 2500:  major = 250\n        elif span <= 5000:  major = 500\n        elif span <= 10000: major = 1000\n        else:\n            magnitude = 10 ** math.floor(math.log10(max(span, 1)))\n            normalized = span / magnitude\n            if normalized <= 2:\n                major = magnitude / 5\n            elif normalized <= 5:\n                major = magnitude / 2\n            else:\n                major = magnitude\n'''

if old not in text:
    raise SystemExit("Latency tick block not found")

text = text.replace(old, new, 1)
path.write_text(text, encoding="utf-8")
