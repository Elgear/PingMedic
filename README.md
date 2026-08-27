# PingMedic

**Windows Network Diagnostics & Troubleshooting**

PingMedic is an open-source Windows desktop application for diagnosing connection quality, latency, packet loss, jitter, DNS, routing, Wi-Fi, internet speed and local network problems from one interface.

[**Download PingMedic for Windows**](https://github.com/Elgear/PingMedic/releases)

> **Windows note:** current public releases may still be unsigned and Windows SmartScreen can show an unknown-publisher warning. PingMedic has applied to the SignPath Foundation open-source code-signing program. Once approved and integrated, official Windows releases will be signed through SignPath Foundation.

## What PingMedic does

PingMedic combines continuous connection monitoring with practical diagnostic tools so you can investigate where a network problem is happening instead of running separate utilities manually.

- **Ping monitoring** — live latency, packet loss, thresholds, alerts and rolling statistics.
- **Latency & jitter graphs** — adaptive graph scaling, best/worst/combined latency averages and jitter analysis.
- **Host information** — hostname, local IP, gateway, public IP, ISP and primary MAC address.
- **Internet speed testing** — bundled LibreSpeed testing with persistent history.
- **LAN throughput** — bundled iperf3 client/server testing for local network performance.
- **Gateway Stability** — repeated first-hop testing for latency, loss, jitter and spikes.
- **Loaded Latency** — compare idle latency against latency while the connection is under load.
- **Route Health** — compare gateway, ISP first hop and public-target health while traffic is running.
- **Wi-Fi Diagnostics** — SSID, BSSID, signal, band, channel, protocol, rates, authentication and connection diagnosis on Windows.
- **Adapter Info** — link speed, IP, gateway, DNS, MAC, counters and negotiation diagnostics.
- **DNS tools** — DNS / WHOIS lookup and resolver comparison across System DNS, Cloudflare, Google and Quad9.
- **Traceroute & MTU testing** — route visibility and path-MTU troubleshooting.
- **HTTP test** — HTTP/HTTPS requests, redirects, timing, headers and TLS certificate summary.
- **Network Scanner** — safe TCP connect scanning for hosts and IPv4 subnets you are authorized to troubleshoot.
- **Reports** — export troubleshooting results to text or CSV.
- **Offline Help** — built-in guidance for controls, graphs, tools and common diagnostic meanings.

## Download and install

Official Windows builds are published on the GitHub Releases page:

**https://github.com/Elgear/PingMedic/releases**

Download the latest `PingMedic_Setup_<version>.exe`, run the installer, and launch **PingMedic** from the Start Menu or optional desktop shortcut.

PingMedic stores presets, history and generated reports in a writable per-user data location rather than under the Program Files installation directory.

## Typical troubleshooting flow

1. Start a continuous ping to your gateway, a public IP or a service you are troubleshooting.
2. Check latency, packet loss and jitter for instability.
3. Use **Gateway Stability** to establish whether the problem begins inside the local network.
4. Use **Loaded Latency** to check for latency increases under load.
5. Use **Route Health** or **Traceroute** to see whether degradation begins beyond the gateway.
6. Use **Speed Test**, **Wi-Fi Diagnostics**, **Adapter Info** or **LAN Throughput** to isolate internet, wireless, Ethernet or local-network bottlenecks.
7. Export a report if you need to retain or share the results.

## Screenshots

Screenshots of the current PingMedic interface will be added here as the UI is finalized for the first fully branded public release.

## Security and privacy

PingMedic runs locally and does not require an account, API key or subscription. It does not include application telemetry or analytics.

Some diagnostics intentionally contact user-selected targets or external services when you run them, including public DNS resolvers, public IP metadata services and LibreSpeed servers. Presets, test history and reports remain local unless you choose to share them.

Only run **Network Scanner** against networks and hosts that you own or are authorized to troubleshoot.

- [Privacy policy](PRIVACY.md)
- [Security policy](SECURITY.md)
- [Third-party notices](THIRD_PARTY_NOTICES.md)

## Open source

PingMedic is licensed under **GPL-3.0-only**. Third-party components remain under their respective licences and are documented in `THIRD_PARTY_NOTICES.md`.

The repository is public so the source, build process and release history can be independently reviewed. The `main` branch is protected by GitHub rules, changes go through pull requests, and the Windows installer build must pass before merge.

## Build from source

Requirements:

- Windows
- Python
- dependencies from `requirements.txt`

Basic development setup:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python .\PingerApp\PingerApp.py
```

Raw ICMP ping can require elevated network privileges on some systems. If PingMedic cannot create the required raw socket, it reports the error when pinging starts rather than failing before the window opens.

## Packaging

For a local Windows application build:

```powershell
.\scripts\setup_packaging_env.ps1
.\scripts\build_windows.ps1 -Clean
```

PyInstaller writes the packaged application to:

```text
dist\PingMedic\PingMedic.exe
```

To build the Windows installer:

```powershell
.\scripts\build_windows.ps1 -Clean
.\scripts\build_installer.ps1
```

The current internal packaging files retain their historical names (`PingerApp.spec`, `installer\PingerApp.iss` and `PingerApp\PingerApp.py`) while the public product, executable and installer are branded **PingMedic**. These internal paths can be cleaned up separately without affecting the product name.

Full packaging notes are in [PACKAGING.md](PACKAGING.md).

## Bundled diagnostic components

### LibreSpeed

PingMedic bundles LibreSpeed CLI at:

```text
tools/librespeed/librespeed-cli.exe
```

The application can also use `librespeed-cli` from `PATH` when the bundled executable is unavailable. Version, checksum and licence information are kept under `tools/librespeed/`.

### iperf3

PingMedic bundles iperf3 at:

```text
tools/iperf3/iperf3.exe
```

The application can also use `iperf3` from `PATH`. Run an iperf3 server on another machine on your LAN and use PingMedic as the client to distinguish local Ethernet/Wi-Fi performance problems from ISP/WAN problems. Version, checksum and licence information are kept under `tools/iperf3/`.

## Code signing

PingMedic has submitted an application to the **SignPath Foundation** free code-signing program for open-source projects.

Current releases should be treated as unsigned until the integration is approved and the release workflow has been updated. After approval, this section and the release documentation will be updated to identify signed official releases.
