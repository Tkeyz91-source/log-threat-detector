# Linux Log Threat Detection Tool

## Project Overview

A Python-based defensive cybersecurity tool that analyses Linux SSH authentication logs to identify suspicious login activity and generate security reports.

## Features

- Detects failed login attempts.
- Identifies repeated failed attempts from the same IP address.
- Detects attempts involving invalid usernames.
- Records successful login events.
- Generates a readable security report.
- Uses Python's built-in libraries.

## Technologies Used

- Kali Linux
- Python 3
- Regular Expressions
- Collections module

## Project Structure

```text
log-threat-detector/
├── log_analyzer.py
├── README.md
├── logs/
│   └── auth.log
├── reports/
│   ├── security-assessment.md
│   └── threat_report.txt
└── screenshots/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Tkeyz91-source/log-threat-detector.git
cd log-threat-detector
```

No third-party Python packages are required.

## Usage

Run the analyzer:

```bash
python3 log_analyzer.py
```

The program reads:

```text
logs/auth.log
```

It generates the report at:

```text
reports/threat_report.txt
```

## Sample Detection Results

| Detection | Result |
|---|---:|
| Failed login attempts | 5 |
| Successful login events | 2 |
| Unique failed-login source IPs | 2 |
| Invalid usernames | 4 |
| Repeated failures detected | Yes |

## Security Assessment

Read the [Security Assessment Report](reports/security-assessment.md).

## Limitations

- Analyses a predefined log file.
- Uses basic pattern matching.
- Does not determine whether an IP address is malicious.
- Does not block login attempts.
- Requires analyst review of findings.

## Disclaimer

This project uses simulated authentication logs for educational and defensive cybersecurity training. It is not intended to monitor systems without authorization.

## Author

GitHub: [Tkeyz91-source](https://github.com/Tkeyz91-source)

