import serial
import time

# https://problemsolvingwithpython.com/11-Python-and-External-Hardware/11.04-Reading-a-Sensor-with-Python/

# Reading the data from serial
ser = serial.Serial(
    port='COM6',
    baudrate=9600,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0)

data =[]                       # empty list to store the data
while(1):
    
    b = ser.read()         # read a byte string
    string_n = b.decode()  # decode byte string into Unicode  
    string = string_n.rstrip() # remove \n and \r
    temp = ''
    # Ignoring all the empty values from serial
    while bool(string):
        temp = temp+string
        b = ser.read()      
        string_n = b.decode() 
        string = string_n.rstrip() 
    data.append(temp)          
    # Filtering empty values we get because of the time difference in transmission
    new_list = list(filter(None, data))
    # Taking 800 samples
    if len(new_list)>800:
        break
    time.sleep(0.01)
    
# Printing the list
#print(new_list)
# Writing the data in text file
file1 = open("pressure_data.txt","w+") #Write mode
file1.write(str(new_list))
file1.close()