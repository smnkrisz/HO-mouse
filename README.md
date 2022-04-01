## You can say that this tool will be the new "Man's best friend". Or should we say Man's best friend for Home Office?

You just push the nearest button and the mouse will move in a rectangle shape for 40 minutes and will prevent the computer to go to slepp & when you press the second button it will reboot the Pico and will stop the program.

![](https://media.giphy.com/media/qMQy929ndmcdtyM6ds/giphy.gif)



### You will need those parts to build your new friend:
- Raspberry Pi Pico
- Jumper wires (4 exactly)
- 2 pcs tactile button
- USB cabel to connect to PC
- Breadboard
> Of course you can build it with PCB if you like soldering



---



### Setup the Pico:

1. You need to download [Circuit Python UF2 file](https://circuitpython.org/board/raspberry_pi_pico/).
2. Push and hold the BOOTSEL button while connecting the your Pico to computer. 
3. Copy the downloaded UF2 file to the Pico (will see it as **RPI-RP2**). It will reboot and will appear as **CIRCUITPY**.
4. Git clone the [HO-mouse repo](https://github.com/smnkrisz/HO-mouse).
5. Copy **lib**, **boot.py** and **code.py** to your Pico and overwrite the existing files.
6. Unplug and plug in the Pico to reboot it.

### Now you connect Pico, breadboard, jumper wires and buttons together:

First you add Pico and the buttons to the breadboard:
![](/pictures/pico1.png)

Connect the "**START**" button:
> You can use different GPIO if you want

![](/pictures/pico2.png)

Connect the "**RESET**" button:
![](/pictures/pico3.png)


### Mine looks like this: 
> I painted the RESET button red to differentiate.

![](/pictures/final_pico.jpg)
