
import re
import argparse
from pathlib import Path
from collections import Counter

BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "logs" / "auth.log"
REPORT_DIR = BASE_DIR / "reports"
REPORT_FILE = REPORT_DIR / "threat_report.txt"

# Detect common SSH authentication events.
FAILED_PATTERN = re.compile(
    r"Failed password for (invalid user )?(\S+) from (\d+\.\d+\.\d+\.\d+)"
)

SUCCESS_PATTERN = re.compile(
    r"Accepted (?:password|publickey) for (\S+) from (\d+\.\d+\.\d+\.\d+)"
)


def analyze_log():
    if not LOG_FILE.exists():
        print(f"[ERROR] Log file not found: {LOG_FILE}")
        return

    failed_ips = Counter()
    invalid_users = Counter()
    successful_logins = []
    failed_events = 0

    with LOG_FILE.open("r", encoding="utf-8") as log:
        for line in log:
            failed_match = FAILED_PATTERN.search(line)

            if failed_match:
                is_invalid = failed_match.group(1) is not None
                username = failed_match.group(2)
                ip_address = failed_match.group(3)

                failed_events += 1
                failed_ips[ip_address] += 1

                if is_invalid:
                    invalid_users[username] += 1

                continue

            success_match = SUCCESS_PATTERN.search(line)

            if success_match:
                username = success_match.group(1)
                ip_address = success_match.group(2)
                successful_logins.append((username, ip_address))

    # Report findings
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    findings = []
    findings.append("===== LOG THREAT DETECTION REPORT =====")
    findings.append(f"Log file: {LOG_FILE.name}")
    findings.append("")

    findings.append("FAILED LOGIN ATTEMPTS")
    findings.append(f"Total failed attempts: {failed_events}")

    for ip, count in failed_ips.most_common():
        findings.append(f"[FAILED LOGIN] {ip}: {count} attempts")

        if count >= 3:
            findings.append(
                f"[ALERT] Repeated failed login attempts from {ip}"
            )

    findings.append("")
    findings.append("INVALID USERNAME ATTEMPTS")

    if invalid_users:
        for username, count in invalid_users.most_common():
            findings.append(
                f"[INVALID USER] {username}: {count} attempts"
            )
    else:
        findings.append("None detected")

    findings.append("")
    findings.append("SUCCESSFUL LOGIN EVENTS")

    if successful_logins:
        for username, ip in successful_logins:
            findings.append(
                f"[SUCCESS] User: {username} | Source IP: {ip}"
            )
    else:
        findings.append("None detected")

    findings.append("")
    findings.append("===== SUMMARY =====")
    findings.append(f"Failed attempts: {failed_events}")
    findings.append(f"Unique source IPs: {len(failed_ips)}")
    findings.append(f"Successful logins: {len(successful_logins)}")
    findings.append(f"Invalid usernames: {len(invalid_users)}")

    report = "\n".join(findings)

    print(report)

    REPORT_FILE.write_text(report + "\n", encoding="utf-8")
    print(f"\n[INFO] Report saved to: {REPORT_FILE}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Defensive Linux authentication log analyzer"
    )
    parser.parse_args()
    analyze_log()

