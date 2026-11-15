import math


def parse_booking(text):
    try:
        if not isinstance(text, str):
            return ("", 0.0)

        if text.count(":") != 1:
            return ("", 0.0)

        service, minutes = text.split(":")

        service = service.strip()
        minutes = float(minutes.strip())

        if not service or not math.isfinite(minutes) or minutes < 0:
            return ("", 0.0)

        return service.title(), minutes

    except (ValueError, TypeError):
        return ("", 0.0)


def duration_average(durations_csv):
    try:
        if not isinstance(durations_csv, str):
            return 0

        parts = durations_csv.split(",")

        if not parts or any(not p.strip() for p in parts):
            return 0

        values = [int(p.strip()) for p in parts]

        if any(v < 0 for v in values):
            return 0

        return sum(values) // len(values)

    except (ValueError, TypeError):
        return 0


def payable_bill(text):
    try:
        if not isinstance(text, str) or text.count("|") != 1:
            return 0.0

        bill, discount = text.split("|")

        bill = float(bill.strip())
        discount = float(discount.strip())

        if not math.isfinite(bill) or not math.isfinite(discount):
            return 0.0

        if bill < 0 or discount < 0:
            return 0.0

        total = bill * 1.18 - discount

        return max(total, 0.0)

    except (ValueError, TypeError):
        return 0.0


def main():
    print("==== Running parse_booking ====")
    user_input = input("Enter service:duration in min (e.g. haircut:45): ")
    result = parse_booking(user_input)
    print("Service and Duration:", result)

    print("\n==== Running duration_average ====")
    user_input = input("Enter durations as CSV (e.g. 30,45,60): ")
    result = duration_average(user_input)
    print("Average Duration:", result)

    print("\n==== Running payable_bill ====")
    user_input = input("Enter bill|discount (e.g. 800|100): ")
    result = payable_bill(user_input)
    print("Payable Bill:", result)


if __name__ == "__main__":
    main()