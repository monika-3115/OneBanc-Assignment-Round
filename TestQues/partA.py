# checking if the pin is common or not by ignoring demographics

common_pins = { 
    "0000", "0011", "1111", "1122", "1212", "0101", "1010", "2233", "3344", "4455", "5566", "7788", "8899", "1234", "4321", "9999", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999",
    "123456", "654321", "111111", "000000", "121212", "112233", "111222", "222111", "222333", "232323", "123123", "456456", "789789", "444444"
}

def is_commonpin(pin: str) -> bool:
    return pin in common_pins

# Input

n = input("Enter the pin:")
if is_commonpin(n):
    print("common pin")
else:
    print("pin is not common")