print('Enter C or F to indicate Celsius or Fahrenheit:')
scale = input()
print('Enter the number of degrees:')
degrees = int(input())
if (scale == "C" and degrees > 60.8) or (scale == "F" and degrees >= 100.4):
    print('Safe')
else:
    print('Dangerous')