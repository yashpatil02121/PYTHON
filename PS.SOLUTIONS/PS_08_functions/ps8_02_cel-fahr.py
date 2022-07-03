def fahr(cel):
    # (0°C × 9/5) + 32 = 32°F
    fah=(cel*1.8)+32
    return fah

cel=int(input("enter temperature in celcius:"))
print(f"{cel} degree celcius = {fahr(cel)} degree fahrenheit")