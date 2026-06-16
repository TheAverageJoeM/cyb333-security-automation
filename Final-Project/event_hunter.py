# ============================================================
# CYB333 Final Project
# Windows Event Log Threat Hunting Toolkit
#
# Author: Joseph Martinez
#
# Purpose:
# This script automates the review of Windows Security Event
# Logs by searching for important security-related events and
# generating reports in both CSV and JSON format.
#
# Event IDs Monitored:
# 4625 - Failed Logon Attempts
# 4624 - Successful Logons
# 4720 - New User Account Creation
# 4104 - PowerShell Script Activity
# 7045 - New Service Installation
# ============================================================

# Import required libraries
import csv
import json
import os
import subprocess
from datetime import datetime


# Dictionary containing Event IDs and descriptions
EVENTS_TO_CHECK = {
    4625: "Failed Logon Attempt",
    4624: "Successful Logon",
    4720: "New User Account Created",
    4104: "PowerShell Script Activity",
    7045: "New Service Installed"
}


# ============================================================
# Function: run_powershell_query
#
# Purpose:
# Queries Windows Event Logs using PowerShell and retrieves
# up to 10 recent events for a specified Event ID.
#
# Parameters:
# event_id (int) - Windows Event ID to search for
#
# Returns:
# List containing matching event records
# ============================================================
def run_powershell_query(event_id):

    # Build PowerShell command
    command = [
        "powershell",
        "-Command",
        f"Get-WinEvent -FilterHashtable @{{LogName='Security'; Id={event_id}}} "
        "-MaxEvents 10 | "
        "Select-Object TimeCreated, Id, ProviderName, Message | "
        "ConvertTo-Json"
    ]

    try:
        # Execute PowerShell command
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=20
        )

        # Return empty list if no results are found
        if result.returncode != 0 or not result.stdout.strip():
            return []

        # Convert JSON output into Python objects
        data = json.loads(result.stdout)

        # If a single event is returned, convert it into a list
        if isinstance(data, dict):
            return [data]

        return data

    except Exception as error:
        print(f"Error checking Event ID {event_id}: {error}")
        return []


# ============================================================
# Function: generate_report
#
# Purpose:
# Loops through all Event IDs, collects event counts,
# displays results, and stores findings for reporting.
#
# Returns:
# List of findings
# ============================================================
def generate_report():

    findings = []

    print("\nWindows Event Log Threat Hunting Toolkit")
    print("=" * 50)

    # Check each Event ID in the dictionary
    for event_id, description in EVENTS_TO_CHECK.items():

        events = run_powershell_query(event_id)
        count = len(events)

        print(f"{event_id} - {description}: {count} events found")

        findings.append({
            "event_id": event_id,
            "description": description,
            "count": count,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    return findings


# ============================================================
# Function: save_csv
#
# Purpose:
# Saves report data to a CSV file for easy review.
#
# Parameters:
# findings (list) - Collected event information
# ============================================================
def save_csv(findings):

    # Create reports directory if it doesn't exist
    os.makedirs("reports", exist_ok=True)

    # Output CSV filename
    csv_file = "reports/security_event_report.csv"

    with open(csv_file, "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "event_id",
                "description",
                "count",
                "timestamp"
            ]
        )

        writer.writeheader()
        writer.writerows(findings)

    print(f"\nCSV report saved: {csv_file}")


# ============================================================
# Function: save_json
#
# Purpose:
# Saves report data to a JSON file.
#
# Parameters:
# findings (list) - Collected event information
# ============================================================
def save_json(findings):

    # Create reports directory if needed
    os.makedirs("reports", exist_ok=True)

    # Output JSON filename
    json_file = "reports/security_event_report.json"

    with open(json_file, "w") as file:
        json.dump(findings, file, indent=4)

    print(f"JSON report saved: {json_file}")


# ============================================================
# Function: main
#
# Purpose:
# Main execution point for the toolkit.
# Generates findings and exports reports.
# ============================================================
def main():

    print("\nStarting Security Event Scan...\n")

    findings = generate_report()

    save_csv(findings)

    save_json(findings)

    print("\nThreat Hunting Scan Complete.")
    print("Reports generated successfully.")


# ============================================================
# Program Entry Point
#
# Ensures the script runs only when executed directly.
# ============================================================
if __name__ == "__main__":
    main()