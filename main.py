"""
Autonomous Vehicle Cyber-AI Monitor

AI-assisted cybersecurity monitoring system for
autonomous vehicle telemetry.

This project uses simulated vehicle telemetry for
learning, analysis and research purposes.
"""

import random
from datetime import datetime


APP_NAME = "AUTONOMOUS VEHICLE CYBER-AI MONITOR"
APP_VERSION = "1.0"


# ---------------------------------------------------------
# 1. MAIN MENU
# ---------------------------------------------------------

def show_menu():
    print("\n" + "=" * 60)
    print(f"  {APP_NAME} v{APP_VERSION}")
    print("=" * 60)
    print("1. Generate Telemetry")
    print("2. View Telemetry")
    print("3. Detect Anomalies")
    print("4. Security Risk Analysis")
    print("5. System Summary")
    print("6. Exit")
    print("-" * 60)


# ---------------------------------------------------------
# 2. TELEMETRY GENERATION
# ---------------------------------------------------------

def generate_telemetry():
    """
    Generate simulated autonomous vehicle telemetry.
    """

    telemetry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "speed": round(random.uniform(0, 80), 2),
        "steering_angle": round(random.uniform(-35, 35), 2),
        "brake_pressure": round(random.uniform(0, 100), 2),
        "throttle": round(random.uniform(0, 100), 2),
        "motor_rpm": random.randint(500, 8000),
        "battery_voltage": round(random.uniform(320, 420), 2),
        "battery_temperature": round(random.uniform(25, 70), 2),
        "imu_acceleration": round(random.uniform(0, 5), 2),
        "gps_speed": round(random.uniform(0, 80), 2),
        "wheel_speed_fl": round(random.uniform(0, 80), 2),
        "wheel_speed_fr": round(random.uniform(0, 80), 2),
        "wheel_speed_rl": round(random.uniform(0, 80), 2),
        "wheel_speed_rr": round(random.uniform(0, 80), 2),
    }

    return telemetry


# ---------------------------------------------------------
# 3. VIEW TELEMETRY
# ---------------------------------------------------------

def view_telemetry(telemetry):
    """
    Display the latest vehicle telemetry.
    """

    if telemetry is None:
        print("\n[!] No telemetry available.")
        return

    print("\n" + "-" * 60)
    print("VEHICLE TELEMETRY")
    print("-" * 60)

    for key, value in telemetry.items():
        print(f"{key:<25}: {value}")


# ---------------------------------------------------------
# 4. ANOMALY DETECTION
# ---------------------------------------------------------

def detect_anomalies(telemetry):
    """
    Detect simple abnormal vehicle conditions.
    """

    if telemetry is None:
        print("\n[!] No telemetry available.")
        return []

    anomalies = []

    # Battery temperature
    if telemetry["battery_temperature"] > 65:
        anomalies.append(
            "High battery temperature detected."
        )

    # Battery voltage
    if telemetry["battery_voltage"] < 330:
        anomalies.append(
            "Low battery voltage detected."
        )

    # GPS vs vehicle speed
    speed_difference = abs(
        telemetry["speed"] - telemetry["gps_speed"]
    )

    if speed_difference > 20:
        anomalies.append(
            "GPS speed and vehicle speed mismatch."
        )

    # Wheel speed consistency
    wheel_speeds = [
        telemetry["wheel_speed_fl"],
        telemetry["wheel_speed_fr"],
        telemetry["wheel_speed_rl"],
        telemetry["wheel_speed_rr"],
    ]

    if max(wheel_speeds) - min(wheel_speeds) > 30:
        anomalies.append(
            "Wheel speed sensor inconsistency detected."
        )

    # Brake + throttle conflict
    if (
        telemetry["brake_pressure"] > 80
        and telemetry["throttle"] > 80
    ):
        anomalies.append(
            "Abnormal brake/throttle combination detected."
        )

    return anomalies


# ---------------------------------------------------------
# 5. SECURITY RISK ANALYSIS
# ---------------------------------------------------------

def analyze_security_risk(telemetry):
    """
    Calculate a simple security risk score based on
    detected anomalies.
    """

    anomalies = detect_anomalies(telemetry)

    if not anomalies:
        risk_score = 0
        risk_level = "LOW"
    elif len(anomalies) <= 2:
        risk_score = 40
        risk_level = "MEDIUM"
    else:
        risk_score = 80
        risk_level = "HIGH"

    print("\n" + "=" * 60)
    print("CYBERSECURITY RISK ANALYSIS")
    print("=" * 60)

    print(f"Risk Score : {risk_score}/100")
    print(f"Risk Level : {risk_level}")

    if anomalies:
        print("\nDetected anomalies:")

        for number, anomaly in enumerate(anomalies, start=1):
            print(f"{number}. {anomaly}")
    else:
        print("\nNo suspicious telemetry detected.")

    return risk_score


# ---------------------------------------------------------
# 6. SYSTEM SUMMARY
# ---------------------------------------------------------

def system_summary(telemetry):
    """
    Display a high-level system status.
    """

    if telemetry is None:
        print("\n[!] No telemetry available.")
        return

    anomalies = detect_anomalies(telemetry)

    print("\n" + "=" * 60)
    print("SYSTEM SUMMARY")
    print("=" * 60)

    print(f"Vehicle Speed       : {telemetry['speed']} km/h")
    print(f"Battery Voltage     : {telemetry['battery_voltage']} V")
    print(
        f"Battery Temperature : "
        f"{telemetry['battery_temperature']} °C"
    )

    if not anomalies:
        print("Vehicle Status      : NORMAL")
        print("Security Status     : SAFE")
    else:
        print("Vehicle Status      : ANOMALY DETECTED")
        print("Security Status     : INVESTIGATE")


# ---------------------------------------------------------
# 7. MAIN PROGRAM LOOP
# ---------------------------------------------------------

def main():

    telemetry = None

    while True:

        show_menu()

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":

            telemetry = generate_telemetry()

            print("\n[+] Telemetry generated successfully.")

        elif choice == "2":

            view_telemetry(telemetry)

        elif choice == "3":

            anomalies = detect_anomalies(telemetry)

            print("\n" + "=" * 60)
            print("ANOMALY DETECTION")
            print("=" * 60)

            if anomalies:
                print("[!] Anomalies detected:")

                for anomaly in anomalies:
                    print(f"- {anomaly}")

            else:
                print("[+] No anomalies detected.")

        elif choice == "4":

            analyze_security_risk(telemetry)

        elif choice == "5":

            system_summary(telemetry)

        elif choice == "6":

            print("\nExiting system. Stay safe.")
            break

        else:

            print("\n[!] Invalid option. Please choose 1-6.")


# ---------------------------------------------------------
# PROGRAM ENTRY POINT
# ---------------------------------------------------------

if __name__ == "__main__":
    main()
