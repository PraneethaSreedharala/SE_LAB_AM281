"""Manage student grades, attendance, and grade-sheet exports."""

import hashlib
import json
import secrets
from pathlib import Path

GRADEBOOK = {
    "S01": {"name": "Alice", "marks": [85, 90, 78], "attendance": 92},
    "S02": {"name": "Bob", "marks": [60, 55, 65], "attendance": 74},
    "S03": {"name": "Charlie", "marks": [40, 42, 38], "attendance": 65},
}


def add_grade(student_id, mark, grade_list=None):
    """Add a mark for a known student and optionally record an audit message.

    The optional audit list is updated only when a caller provides one.
    """
    valid_mark = isinstance(mark, (int, float)) and mark >= 0
    if student_id not in GRADEBOOK or not valid_mark:
        return False

    GRADEBOOK[student_id]["marks"].append(mark)
    if grade_list is not None:
        grade_list.append(f"Recorded score {mark} for student id {student_id}")
    return True


def record_attendance(student_id, present_days):
    """Add present days for a known student; return whether it succeeded."""
    if student_id not in GRADEBOOK or not isinstance(present_days, int):
        return False
    if present_days < 0:
        return False

    GRADEBOOK[student_id]["attendance"] += present_days
    return True


def check_passing_status(student_id, pass_threshold=50.0):
    """Return whether a student's average meets the passing threshold."""
    student = GRADEBOOK.get(student_id)
    if student is None or not student["marks"]:
        return False

    average = sum(student["marks"]) / len(student["marks"])
    return average >= pass_threshold


def compute_weighted_gpa(student_id):
    """Return an illustrative GPA on a 0–5 scale based on average marks."""
    student = GRADEBOOK.get(student_id)
    if student is None or not student["marks"]:
        raise ValueError(f"Unknown student or no marks: {student_id}")

    average = sum(student["marks"]) / len(student["marks"])
    return average / 20.0


def generate_student_hash(student_id):
    """Generate a stable SHA-256 identifier for a student ID."""
    return hashlib.sha256(student_id.encode("utf-8")).hexdigest()


def generate_registration_pin():
    """Generate a cryptographically strong four-digit registration PIN."""
    return f"{secrets.randbelow(9000) + 1000:04d}"


def export_grade_sheet(filename="grade_sheet.txt"):
    """Export the gradebook as JSON to a file and return its path."""
    output_path = Path(filename)
    with output_path.open("w", encoding="utf-8") as output_file:
        json.dump(GRADEBOOK, output_file, indent=2)
        output_file.write("\n")

    print(f"Grade sheet exported to: {output_path}")
    return output_path


def main():
    """Run a short demonstration of the grade-management functions."""
    add_grade("S01", 95)
    record_attendance("S02", 2)
    print("Is S01 passing:", check_passing_status("S01"))
    print("Calculated GPA:", compute_weighted_gpa("S01"))
    print("Student Hash:", generate_student_hash("S01"))
    print("Registration PIN:", generate_registration_pin())
    export_grade_sheet()


if __name__ == "__main__":
    main()
