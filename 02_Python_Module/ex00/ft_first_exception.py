#!/usr/bin/python3

def check_temperature(temp_str: str) -> str:
    try:
        temp_int = int(temp_str)

        if temp_int < 0:
            return f"Error: {temp_int}ºC is too cold for plants (min 0ºC)"
        if temp_int > 40:
            return f"Error: {temp_int}ºC is too hot for plants (max 40ºC)"
        return f"Temperature {temp_int}ºC is perfect for plants!"
    except ValueError:
        return f"Error: '{temp_str}' is not a valid number"

def test_temperature_input():
    print("=== Garden Temperature Checker ===")

    test_cases = ["25", "abc", "100", "-50"]
    for case in test_cases:
        print(f"\nTesting temperature: {case}")
        print(check_temperature(case))

    print("\nAll tests completed - program didn't crash!")

def main():
    test_temperature_input()

if __name__ == "__main__":
    main()
