import pandas as pd
from sklearn.ensemble import IsolationForest


DATA_FILE = "data/telemetry_sample.csv"


def load_data():
    return pd.read_csv(DATA_FILE)


def detect_anomalies(data):
    features = [
        "speed",
        "battery_voltage",
        "motor_temperature",
        "signal_strength"
    ]

    model = IsolationForest(
        contamination=0.1,
        random_state=42
    )

    data["anomaly"] = model.fit_predict(data[features])

    return data


def main():
    data = load_data()

    print("=== Autonomous Vehicle Cyber Monitor ===")
    print(f"Telemetry records: {len(data)}")

    results = detect_anomalies(data)

    anomalies = results[results["anomaly"] == -1]

    print(f"Anomalies detected: {len(anomalies)}")

    if len(anomalies) > 0:
        print("\n⚠️ Potential cybersecurity anomalies:")
        print(anomalies)


if __name__ == "__main__":
    main()
