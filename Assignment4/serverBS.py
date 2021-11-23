import json

Pins = {

    "Pin 4": "Neopixel",
    "Pin 12": "Button",
    "Pin 14": "Green LED",
    "Pin 15": "RED LED",
    "Pin 32": "YELLOW LED",
    "Pin 17,21": "Temperature Sensor",
    "Pin 39": "Potentiometer"
    
    
}

# # Get a JSON formatted string
Pins_JSON = json.dumps(Pins, indent=4)

print(Pins_JSON)