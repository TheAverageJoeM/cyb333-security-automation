# CYB333 Security Automation

This repository contains coursework, notes, screenshots, labs, and project files completed for CYB333 Security Automation. The repository demonstrates hands-on experience with Python scripting, PowerShell automation, network programming, and security automation concepts covered throughout the course.

## Repository Structure

* `Week1-Environment-Setup` - Files and screenshots related to the Week 1 development environment setup.
* `Midterm` - Midterm assignment files, including socket programming and port scanning exercises.
* `Final-Project` - Windows Event Log Threat Hunting Toolkit project files.
* `Screenshots` - Supporting screenshots for assignments and documentation.
* `notes` - Course notes, planning documents, and reference material.

## Final Project

### Windows Event Log Threat Hunting Toolkit

The final project for this course is a Python-based Windows Event Log Threat Hunting Toolkit that uses PowerShell to query Windows Security Event Logs and generate automated reports.

The tool automates the review of Windows event logs by searching for specific security-related Event IDs, counting matching events, and exporting findings to structured report formats. This reduces the manual effort required to review Event Viewer and demonstrates how automation can improve efficiency in security operations.

### Purpose

The purpose of this project is to demonstrate how Python and PowerShell can be combined to automate basic threat hunting and security monitoring tasks. The script collects event data, summarizes findings, and generates reports that can be reviewed by administrators or security analysts.

### Event IDs Monitored

* **4625** - Failed Logon Attempts
* **4624** - Successful Logons
* **4720** - New User Account Creation
* **4104** - PowerShell Script Activity
* **7045** - New Service Installation

### Technologies Used

* Python 3
* PowerShell
* Windows Event Logs
* JSON
* CSV Reporting

### Running the Project

From the repository root directory:

```bash
python Final-Project/event_hunter.py
```

### Project Output

The script generates reports inside the `Final-Project/reports` directory:

* `security_event_report.csv`
* `security_event_report.json`

These reports contain event counts, event descriptions, and timestamps for each monitored Event ID.

### Security Automation Concepts Demonstrated

* Python scripting and automation
* PowerShell integration
* Windows Event Log analysis
* Threat hunting fundamentals
* Automated report generation
* Security monitoring workflows

## Security Notice

No passwords, API keys, tokens, private keys, or other sensitive credentials should be uploaded to this repository. All project files should be reviewed before committing and pushing changes to GitHub.

## Author

Joseph Martinez

National University

CYB333 Security Automation
