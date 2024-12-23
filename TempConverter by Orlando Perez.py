print("Welcome to Orlando P. Temp Converter!")
fltTemperature = float(input("Enter a temperature: "))
strTempScale = input("Is the temp F for Fahrenheit or C for Celsius? ").strip().lower()
if strTempScale != 'f' and strTempScale != 'c':
    print("You must enter F or C")
else:
    if strTempScale == 'f':
        if fltTemperature > 212:
            print("Temp cannot be > 212")
        else:
            fltCelsius = (5.0 / 9.0) * (fltTemperature - 32)
            print(f"The Celsius equivalent is: {fltCelsius:.1f}")
    elif strTempScale == 'c':
        if fltTemperature > 100:
            print("Temp cannot be > 100")
        else:
            fltFahrenheit = ((9.0 / 5.0) * fltTemperature) + 32
            print(f"The Fahrenheit equivalent is: {fltFahrenheit:.1f}")
