# A simple script to read the CAT Interface of my FT-710 and output the frequency and mode the radio is currently set to.

import serial

def read_yaesu_freq(port, baudrate):
    """Reads data from a Yaesu transceiver using the CAT interface.
    
    Returns:
        A tuple containing the frequency (in MHz) and the mode as a string.
    """

    with serial.Serial(port, baudrate, timeout=1) as ser:
        # Send a command to the transceiver (example: get frequency)
        ser.write(b"IF;\r") 

        # Read the response from the transceiver
        response = ser.readline().decode("ascii").strip()
        print("Radio response: " + response)
        
        freq = int(response[2:-14])/1000000
        mode_code = response[21:-6]
        
        # Dictionary to map mode codes to mode names
        mode_dict = {
            "1": "LSB", "2": "USB", "3": "CW-U", "4": "FM", "5": "AM",
            "6": "RTTY-L", "7": "CW-L", "8": "DATA-L", "9": "RTTY-U",
            "A": "DATA-FM", "B": "FM-N", "C": "DATA-U", "D": "AM-N",
            "F": "D-FM-N", "E": "PSK"
        }
        
        mode = mode_dict.get(mode_code, "Unknown Mode")  # Get mode name or "Unknown Mode"

        return freq, mode


# Call the function and print the values
frequency, mode = read_yaesu_freq("COM5", 38400)
print(f"Frequency: {frequency} MHz")
print(f"Mode: {mode}")
