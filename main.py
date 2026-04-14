import csv
import json
from parser import parse_windows_log
from detector import (
    count_failed_logins,
    count_failed_users,
    detect_brute_force,
    detect_targeted_account_attack,
)


def save_alerts_txt(alerts, file_path="reports/alerts.txt"):
    with open(file_path, "w", encoding="utf-8") as file:
        for alert in alerts:
            line = (
                f"Timestamp: {alert.get('timestamp', '')} | "
                f"Alert Type: {alert.get('type', '')} | "
                f"Source IP: {alert.get('source_ip', '')} | "
                f"Account Name: {alert.get('account_name', '')} | "
                f"Failed Attempts: {alert.get('failed_attempts', '')}\n"
            )
            file.write(line)


def save_alerts_csv(alerts, file_path="reports/alerts.csv"):
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Alert Type", "Source IP", "Account Name", "Failed Attempts"])

        for alert in alerts:
            writer.writerow([
                alert.get("timestamp", ""),
                alert.get("type", ""),
                alert.get("source_ip", ""),
                alert.get("account_name", ""),
                alert.get("failed_attempts", ""),
            ])


def save_alerts_json(alerts, file_path="reports/alerts.json"):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(alerts, file, indent=4)


def main():
    log_file = "logs/windows_security.csv"

    print("[*] Parsing Windows security log...")
    events = parse_windows_log(log_file)

    print(f"[*] Total parsed events: {len(events)}")

    print("\n[*] Failed Login Count by Source IP:")
    failed_counts = count_failed_logins(events)
    for ip, count in failed_counts.items():
        print(f"Source IP: {ip} | Failed Attempts: {count}")

    print("\n[*] Failed Login Count by Account:")
    failed_users = count_failed_users(events)
    for user, count in failed_users.items():
        print(f"Account: {user} | Failed Attempts: {count}")

    print("\n[*] Running detections...")
    ip_alerts = detect_brute_force(events, threshold=3)
    user_alerts = detect_targeted_account_attack(events, threshold=3)

    alerts = ip_alerts + user_alerts

    if alerts:
        print("\n[ALERTS DETECTED]")
        for alert in alerts:
            print(
                f"Timestamp: {alert.get('timestamp', '')} | "
                f"Type: {alert.get('type', '')} | "
                f"Source IP: {alert.get('source_ip', '')} | "
                f"Account Name: {alert.get('account_name', '')} | "
                f"Failed Attempts: {alert.get('failed_attempts', '')}"
            )

        save_alerts_txt(alerts)
        save_alerts_csv(alerts)
        save_alerts_json(alerts)

        print("\n[+] Alerts saved to reports/alerts.txt")
        print("[+] Alerts saved to reports/alerts.csv")
        print("[+] Alerts saved to reports/alerts.json")

    else:
        print("\n[OK] No suspicious activity detected.")


if __name__ == "__main__":
    main()
