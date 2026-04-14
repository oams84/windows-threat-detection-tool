import csv


def parse_windows_log(file_path):
    events = []

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            events.append({
                "timestamp": row["timestamp"],
                "event_id": row["event_id"],
                "account_name": row["account_name"],
                "source_ip": row["source_ip"],
                "status": row["status"]
            })

    return events
