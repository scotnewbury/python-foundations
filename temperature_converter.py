import sys

# Ensure the user entered the correct number of arguments
if len(sys.argv) != 3:
    print(
        "Incorrect number of arguments, "
        "please include both the temperature and unit (F, C, or K)"
    )
    sys.exit(1)

# Check that the temperature entered is a valid number
temp = sys.argv[1]

if temp.startswith("-") and len(temp) > 1:
    temp_str = temp[1:]
else:
    temp_str = temp

if temp_str.replace(".", "", 1).isdigit():
    temperature = float(temp)
else:
    print("Temperature must be a numeric value.")
    sys.exit(1)


# Validate user input
temperature_unit = sys.argv[2].lower()
if temperature_unit not in ("c", "f", "k"):
    print("The temperature unit should be just the letter C, F, or K")
    sys.exit(1)

# Calculate and set print strings
if temperature_unit == "c":
    temperature_c = temperature
    if temperature_c < -273.15:
        print("Temperatures below -273.15°C are not possible")
        sys.exit(1)
    temperature_f = temperature * 9 / 5 + 32
    temperature_k = temperature + 273.15
    value_print_order = (
        f"{temperature_c:.2f}°C = {temperature_f:.2f}°F = {temperature_k:.2f}K"
    )
elif temperature_unit == "f":
    temperature_f = temperature
    if temperature_f < -459.67:
        print("Temperatures below -459.67°F are not possible")
        sys.exit(1)
    temperature_c = (temperature - 32) * (5 / 9)
    temperature_k = temperature_c + 273.15
    value_print_order = (
        f"{temperature_f:.2f}°F = {temperature_c:.2f}°C = {temperature_k:.2f}K"
    )
else:
    temperature_k = temperature
    if temperature_k < 0:
        print("Temperatures below 0K are not possible")
        sys.exit(1)
    temperature_c = temperature - 273.15
    temperature_f = (temperature_c * (9 / 5)) + 32
    value_print_order = (
        f"{temperature_k:.2f}K = {temperature_c:.2f}°C = {temperature_f:.2f}°F"
    )

print(value_print_order)
