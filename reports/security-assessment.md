# Linux Log Threat Detection — Security Assessment Report

## 1. Project Overview

The Linux Log Threat Detection Tool is a Python-based defensive cybersecurity application designed to analyse authentication logs and identify suspicious login activity.

## 2. Objective

The objective is to demonstrate how security analysts can use automated log analysis to identify repeated failed login attempts, invalid usernames, and successful authentication events.

## 3. Tools and Technologies

- Kali Linux
- Python 3
- Regular Expressions
- Python Collections
- Linux SSH authentication log format

## 4. Testing Methodology

A simulated SSH authentication log was created containing failed login attempts, invalid usernames, and successful login events.

The Python application analysed the sample log and generated a security report.

## 5. Test Results

| Test | Expected Result | Actual Result |
|---|---|---|
| Failed login detection | Identify failed attempts | Passed |
| Repeated failure detection | Alert on 3 or more failures from one IP | Passed |
| Invalid username detection | Identify invalid usernames | Passed |
| Successful login detection | Record successful logins | Passed |
| Report generation | Save findings to a text file | Passed |

## 6. Findings

The analysis identified:

- 5 failed login attempts.
- 2 successful login events.
- 2 unique source IP addresses associated with failed attempts.
- 4 distinct invalid usernames.
- 3 failed attempts from source IP `192.0.2.10`.

The application generated an alert for repeated failed login attempts from that address.

## 7. Security Recommendations

- Investigate repeated authentication failures.
- Review successful logins following suspicious activity.
- Use multi-factor authentication where available.
- Apply appropriate account lockout and rate-limiting policies.
- Monitor authentication logs regularly.
- Protect log files against unauthorized modification.

## 8. Limitations

- The tool currently analyses a predefined log file.
- It uses basic text-pattern matching.
- It does not establish whether an IP address represents a real attacker.
- It does not block IP addresses or prevent login attempts.
- Its findings require review by a security analyst.

## 9. Conclusion

The project successfully demonstrated automated analysis of Linux authentication logs.

The application identified failed login attempts, repeated failures, invalid usernames, and successful login events.

It demonstrates practical knowledge of Python programming, authentication log analysis, and defensive security monitoring.

**Testing note:** All events used in this assessment were simulated for educational purposes.

