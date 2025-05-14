import datetime
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

common_pins = { 
    "0000", "0011", "1111", "1122", "1212", "0101", "1010", "2233", "3344", "4455", "5566", "7788", "8899", "1234", "4321", "9999", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999", 
    "1000", "2000", "3000", "4000", "5000", "6000", "7000", "8000", "9000",
    "123456", "654321", "111111", "000000", "121212", "112233", "111222", "222111", "222333", "232323", "123123", "456456", "789789", "444444", "222222", "333333", "555555", "666666", "777777", "888888", "999999",
    "333222", "333444", "444333", "444555", "555666", "555444", "666555", "666777","777666", "777888", "888777", "888999", "999888"
}

def is_commonpin(pin: str) -> bool:
    return pin in common_pins

def date_pins(datestr: str) -> set:
    try:
        date = datetime.datetime.strptime(datestr, "%d-%m-%Y")
    except ValueError:
        return set()
    
    dd = f"{date.day:02d}"
    mm = f"{date.month:02d}"
    yyyy = f"{date.year:04d}"
    yy1 = yyyy[2:]
    yy2 = yyyy[:2]
    
    return {
        # 4-digit combinations
        dd+dd, mm+mm, dd+mm, mm+dd, dd+yy1, mm+yy1, yy1+mm, yy1+dd, yy1+yy2, yy2+yy1, yy1+yy1, yy2+yy2, dd+yy2, mm+yy2, yy2+mm, yy2+dd,
        # 6-digit combinations
        dd+yyyy, yyyy+dd, mm+yyyy, yyyy+mm, dd+mm+yy1, dd+mm+yy2, mm+dd+yy1, mm+dd+yy2,
        dd+yy1+mm, dd+yy2+mm, mm+yy1+dd, mm+yy2+dd, yy1+dd+mm, yy2+dd+mm, yy1+mm+dd, yy2+mm+dd,
        yy1+yyyy, yy2+yyyy, yyyy+yy1, yyyy+yy2,
    }

def check_demos(pin: str, dob = None, dob_spouse = None, anniversary = None) -> list:
    reasons = []
    if dob and pin in date_pins(dob):
        reasons.append("DEMOGRAPHIC_DOB_SELF")
    if dob_spouse and pin in date_pins(dob_spouse):
        reasons.append("DEMOGRAPHIC_DOB_SPOUSE")
    if anniversary and pin in date_pins(anniversary):
        reasons.append("DEMOGRAPHIC_ANNIVERSARY")
    return reasons

def evaluate_mpin(pin: str, dob = None, dob_spouse = None, anniversary = None) -> dict:
    reasons = []

    if len(pin) not in {4, 6} or not pin.isdigit():
        reasons.append("INVALID_PIN_FORMAT")

    if is_commonpin(pin):
        reasons.append("COMMONLY_USED")

    reasons.extend(check_demos(pin, dob, dob_spouse, anniversary))

    return {
        "strength": "WEAK" if reasons else "STRONG",
        "reasons": reasons
    }

def tests(filepath):
    with open(filepath, "r") as f:
        test_cases = json.load(f)

    passed = 0
    for i, case in enumerate(test_cases):
        pin = case["pin"]
        expected = sorted(case["expected"])
        result = evaluate_mpin(
            pin,
            dob=case.get("dob"),
            dob_spouse=case.get("dob_spouse"),
            anniversary=case.get("anniversary")
        )
        actual = sorted(result["reasons"])
        if actual == expected:
            print(f"Test case {i+1} passed.🟢")
            passed += 1
        else:
            print(f"Test case {i+1} failed.🔴 Expected {expected}, got {actual}")

    print(f"\nPassed {passed}/{len(test_cases)} test cases.")

#main function
if __name__ == "__main__":
    tests("test_cases.json")
