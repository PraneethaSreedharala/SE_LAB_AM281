from hypothesis import given, strategies as st

from salon_booking import (
    parse_booking,
    duration_average,
    payable_bill
)


# Test 1: Fuzz testing for parse_booking()
@given(st.text() | st.none())
def test_parse_booking_no_crash(s):
    try:
        parse_booking(s)
    except Exception as e:
        assert False, f"parse_booking crashed with input {s!r}: {e}"


# Test 2: Fuzz testing for duration_average()
@given(st.text() | st.none())
def test_duration_average_no_crash(s):
    try:
        duration_average(s)
    except Exception as e:
        assert False, f"duration_average crashed with input {s!r}: {e}"


# Test 3: Fuzz testing for payable_bill()
@given(st.text() | st.none())
def test_payable_bill_no_crash(s):
    try:
        payable_bill(s)
    except Exception as e:
        assert False, f"payable_bill crashed with input {s!r}: {e}"