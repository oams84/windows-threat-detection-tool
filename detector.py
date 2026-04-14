from collections import defaultdict


def count_failed_logins(events):
    failed_counts = defaultdict(int)

    for event in events:
        if event["event_id"] == "4625":
            failed_counts[event["source_ip"]] += 1

    return dict(failed_counts)


def count_failed_users(events):
    failed_users = defaultdict(int)

    for event in events:
        if event["event_id"] == "4625":
            failed_users[event["account_name"]] += 1

    return dict(failed_users)


def detect_brute_force(events, threshold=3):
    failed_counts = defaultdict(int)
    latest_timestamp = {}
    alerts = []

    for event in events:
        if event["event_id"] == "4625":
            ip = event["source_ip"]
            failed_counts[ip] += 1
            latest_timestamp[ip] = event["timestamp"]

    for ip, count in failed_counts.items():
        if count >= threshold:
            alerts.append({
                "type": "Windows Brute Force Suspected",
                "source_ip": ip,
                "failed_attempts": count,
                "timestamp": latest_timestamp[ip]
            })

    return alerts


def detect_targeted_account_attack(events, threshold=3):
    failed_users = defaultdict(int)
    latest_timestamp = {}
    alerts = []

    for event in events:
        if event["event_id"] == "4625":
            user = event["account_name"]
            failed_users[user] += 1
            latest_timestamp[user] = event["timestamp"]

    for user, count in failed_users.items():
        if count >= threshold:
            alerts.append({
                "type": "Targeted Account Attack Suspected",
                "account_name": user,
                "failed_attempts": count,
                "timestamp": latest_timestamp[user]
            })

    return alerts

