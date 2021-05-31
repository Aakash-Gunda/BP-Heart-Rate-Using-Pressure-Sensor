# BP-Heart-Rate-Using-Pressure-Sensor

Our aim of this project is to semiautomate the blood pressure and heart rate measuring device using an STM microcontroller and an mpr pressure sensor.

# Components used:
  1. Stm-32 microcontroller
  2. Honeywell MPRLS0300YG00001BB pressure sensor
  3. Manually inflatable blood pressure cuff
  4. Silicone Tubing
  5. F-F wire jumpers

# Steps to get BP/HR

  1. <b> measure pressure values from the Honeywell sensor:</b> Use a 8.3 Kohm pull-up resistor, SCL and SDA are connected to PB-7 and PB-6 respectively("main.cpp").
  2. <b> Read the pressure data:</b> Read the pressure data from serial using a python code "PY-serial.py" 800 pressure samples are taken.
  3. <b> Plot the pressure graph and check for uniform inflation and deflation rate.</b>: Data samples from 150-650 has all the information needed("Sys_Dias_from_data.py").
  4. <b> detect and quantify pulse oscillations: </b> Create an Oscillometric waveform using detrending.
  5. <b> Calculate Diastolic and Systolic values from oscillations.</b>: Pressure sample with the highest frequency is the Mean arterial pressure, 80% of that is the diastolic                   pressure and 50% frquency gives the Systolic. 
  6. <b> Calculate Heart Rate from oscillations.</b>: heart rate is the distance between the peaks per minute. I am taking the average distance b/w 5 peaks and converting it to                 beats per minute
