from pathlib import Path
import re

path = Path('PingerApp/PingerApp.py')
text = path.read_text(encoding='utf-8')

pattern = re.compile(r"def route_health_diagnosis\(result\):\n.*?(?=\ndef [A-Za-z_]\w*\(|\nclass [A-Za-z_]\w*)", re.S)
replacement = '''def route_health_diagnosis(result):
    paths = (result or {}).get("paths", {}) or {}
    gateway = paths.get("gateway", {}) or {}
    isp = paths.get("isp", {}) or {}
    public = paths.get("public", {}) or {}

    def unhealthy(item):
        return float(item.get("loss_pct") or 0) > 0 or int(item.get("spike_count") or 0) > 0

    gateway_bad = unhealthy(gateway)
    isp_bad = unhealthy(isp)
    public_bad = unhealthy(public)

    if gateway_bad:
        return (
            "A latency spike or packet loss was detected at the local gateway during load. "
            "Because the issue is already visible before the ISP hop, investigate the local network first: "
            "Wi-Fi or Ethernet quality, adapter/driver, cable, switch/router LAN port, or router load."
        )
    if isp_bad:
        return (
            "The local gateway stayed stable, but degradation appeared at the ISP first hop during load. "
            "This points beyond the local LAN toward the router WAN link, ISP access network, or upstream congestion."
        )
    if public_bad:
        return (
            "The gateway and ISP first hop stayed stable, but the public target degraded during load. "
            "This points further upstream toward internet routing, peering, congestion, or the selected public target."
        )
    return (
        "Route health looked stable during the load window. No packet loss or configured-threshold spikes were detected "
        "at the gateway, ISP first hop, or public target."
    )
'''
text, n = pattern.subn(replacement, text, count=1)
if n != 1:
    raise SystemExit('Could not replace route_health_diagnosis')

text = text.replace('QGroupBox("Ping Log / Speed Test JSON")', 'QGroupBox("Technical Details / Raw Output")')
text = text.replace('self.route_raw_box.setMinimumHeight(220)', 'self.route_raw_box.setMinimumHeight(110)')
text = text.replace('self.route_raw_box.setMinimumHeight(200)', 'self.route_raw_box.setMinimumHeight(110)')
text = text.replace('self.route_raw_box.setMinimumHeight(180)', 'self.route_raw_box.setMinimumHeight(110)')
text = text.replace('QTableWidget(3, 9)', 'QTableWidget(3, 10)')
text = text.replace('["Path", "Target", "Sent", "Received", "Loss", "Avg", "Max", "Jitter", "Spikes"]', '["Path", "Target", "Sent", "Received", "Loss", "Avg", "Max", "Jitter", "Spikes", "Assessment"]')

needle = '    def _set_route_health_result(self, result: dict):\n'
if needle in text and '    def _route_path_assessment(self, stats: dict):\n' not in text:
    helper = '''    def _route_path_assessment(self, stats: dict):
        loss = float((stats or {}).get("loss_pct") or 0)
        spikes = int((stats or {}).get("spike_count") or 0)
        if loss >= 5 or spikes >= 3:
            return "Poor"
        if loss > 0 or spikes > 0:
            return "Watch"
        return "Healthy"

'''
    text = text.replace(needle, helper + needle, 1)

old = '''                f"{stats.get('spike_count', 0)} over {stats.get('spike_threshold_ms', 0):.0f} ms",
            ]'''
new = '''                f"{stats.get('spike_count', 0)} over {stats.get('spike_threshold_ms', 0):.0f} ms",
                self._route_path_assessment(stats),
            ]'''
text = text.replace(old, new)

text = text.replace('self._set_route_status("Route health test completed.", "error")', 'self._set_route_status("Completed - attention recommended.", "running")')
text = text.replace('self._set_route_status("Route health test completed.", level)', 'self._set_route_status("Route health test completed." if level == "ok" else "Completed - attention recommended.", "ok" if level == "ok" else "running")')

path.write_text(text, encoding='utf-8')
print('Route Health UI patch applied')
# trigger v2
