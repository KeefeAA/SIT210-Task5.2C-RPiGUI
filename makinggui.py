from gpiozero import LED
import RPi.GPIO 
from tkinter import *
import tkinter.font
RPi.GPIO.setmode(RPi.GPIO.BCM)

# Hardware
redLed = LED(21)
blueLed = LED(20)
greenLed = LED(16)

# GUI DEFINITIONS
win = Tk()
win.title("LED Toggle")
myFont = tkinter.font.Font(family = 'Comic Sans', size = 12, weight = "bold")

# Event Functions #

def toggleRedLED():
    if redLed.is_lit:
        redLed.off()
        ledRedButton["text"] = "LED ON"
    else:
        redLed.on()
        ledRedButton["text"] = "LED OFF"
        
        blueLed.off()
        ledBlueButton["text"] = "LED ON"       
        greenLed.off()
        ledGreenButton["text"] = "LED ON"  
        
def toggleBlueLED():
    if blueLed.is_lit :
        blueLed.off()
        ledBlueButton["text"] = "LED ON"         
    else:
        blueLed.on()
        ledBlueButton["text"] = "LED OFF"
        
        greenLed.off()
        ledGreenButton["text"] = "LED ON"
        redLed.off()
        ledRedButton["text"] = "LED On"
      
def toggleGreenLED():
    if greenLed.is_lit :
        greenLed.off()
        ledGreenButton["text"] = "LED ON"         
    else:
        greenLed.on()
        ledGreenButton["text"] = "LED OFF"
        
        redLed.off()
        ledRedButton["text"] = "LED On"
        blueLed.off()
        ledBlueButton["text"] = "LED ON"   
  
def closeApp():
    RPi.GPIO.cleanup()
    win.destroy()
        
# WIDGETS
ledRedButton = Button(win, text = 'LED ON', font = myFont, command = toggleRedLED, bg = 'red', height = 1, width = 24)
ledRedButton.grid(row=0, column=1)

ledBlueButton = Button(win,text = 'LED ON', font = myFont, command = toggleBlueLED, bg = 'blue', height = 1, width = 24)
ledBlueButton.grid(row=1, column=1)

ledGreenButton = Button(win,text = 'LED ON', font = myFont, command = toggleGreenLED, bg = 'green', height = 1, width = 24)
ledGreenButton.grid(row=2, column=1)

exitButton = Button(win,text = 'Exit', font = myFont, command = closeApp, bg = 'red', height = 1, width = 6)
exitButton.grid(row=3, column=1)

# Clean exit
win.protocol("WM_DELETE_WINDOW", closeApp)

# Loops events, keeps gui running
win.mainloop()
