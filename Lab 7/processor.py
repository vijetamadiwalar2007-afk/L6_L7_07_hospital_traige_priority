
import math


def parse_vitals_summary(vitals_csv):
    if not isinstance(vitals_csv, str):
        return "Invalid input: vitals must be a string."

    parts = vitals_csv.split(',')

    if len(parts) != 3:
        return "Invalid input: enter HR, SpO2, and temperature."

    try:
        hr = float(parts[0].strip())
        spo2 = float(parts[1].strip())
        temp = float(parts[2].strip())
    except ValueError:
        return "Invalid input: vitals must contain valid numbers."

    if not all(math.isfinite(v) for v in [hr, spo2, temp]):
        return "Invalid input: values must be finite numbers."

    critical = hr > 120 or spo2 < 90 or temp > 39.0

    return f"Vitals: HR={hr}, SpO2={spo2}% - {'CRITICAL' if critical else 'STABLE'}"


def compute_patient_bmi(bmi_string):
    if not isinstance(bmi_string, str):
        return "Invalid input: enter weight/height."

    parts = bmi_string.split('/')

    if len(parts) != 2:
        return "Invalid input: use weight/height format."

    try:
        weight = float(parts[0].strip())
        height = float(parts[1].strip())
    except ValueError:
        return "Invalid input: weight and height must be numbers."

    if not math.isfinite(weight) or not math.isfinite(height):
        return "Invalid input: values must be finite numbers."

    if weight <= 0 or height <= 0:
        return "Invalid input: weight and height must be positive."

    bmi = weight / (height ** 2)
    return round(bmi, 2)


def assign_ward_bed(allocation_code):
    if not isinstance(allocation_code, str):
        return "Invalid input: enter ward-bed format."

    parts = allocation_code.strip().split('-')

    if len(parts) != 2:
        return "Invalid input: use ward-bed format."

    ward, bed_str = parts

    ward_names = {
        "ER": "Emergency Room",
        "ICU": "Intensive Care Unit",
        "GEN": "General Ward",
        "PED": "Pediatrics"
    }

    ward = ward.strip().upper()

    if ward not in ward_names:
        return "Invalid input: unknown ward."

    try:
        bed_num = int(bed_str.strip())
    except ValueError:
        return "Invalid input: bed number must be an integer."

    if bed_num <= 0:
        return "Invalid input: bed number must be positive."

    return f"{ward_names[ward]} Bed #{bed_num}"


def main():
    print("==== Running parse_vitals_summary ====")
    v_input = input("Enter vitals (HR,SpO2,Temp): ")
    print("Summary:", parse_vitals_summary(v_input))

    print("\n==== Running compute_patient_bmi ====")
    b_input = input("Enter weight/height (e.g. 70/1.75): ")
    print("BMI:", compute_patient_bmi(b_input))

    print("\n==== Running assign_ward_bed ====")
    w_input = input("Enter allocation (e.g. ICU-05): ")
    print("Assignment:", assign_ward_bed(w_input))


if __name__ == "__main__":
    main()
