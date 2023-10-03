import pygame
from tabulate import tabulate
import time

pygame.joystick.init()
print(pygame.joystick.get_count())
joysticks = {}
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
joyindex = 0
done = False
joyName = 'Logitech MOMO Racing'
#joyName = 'Xbox 360 Controller'
logitechMap= {'Ax0': 'steering wheel', 'Ax1': 'pedal',
              'But0': '0', 'But1': '1', 'But2': '2',
              'But3': '3', 'But4': '4', 'But5': '5',
              'But6': '6', 'But7': '7',
              'But8': '-', 'But9': '+'}

xboxMap = {'Ax0': 'Left_RIGHTLEFT', 'Ax1': 'Left_UPDOWN',
            'Ax2': 'Right_RIGHTLEFT', 'Ax3': 'Right_UPDOWN',
            'Ax4': 'Left_Shift', 'Ax5': 'Right_Shift',
            'But0': 'A', 'But1': 'B', 'But2': 'A',
            'But3': 'Y', 'But4': 'LEFT', 'But5': 'RIGHT',
            'But6': 'BACK', 'But7': 'START', 'But8': 'RIGHT_STICK',
            'But9': 'LEFT_STICK', 'But10': '', 'hat0': '0'}

for item in joysticks:
    if item.get_name() == 'Logitech MOMO Racing':
        print(tabulate([["Name: ", item.get_name()],
                        ["ENABLE: ", item.get_init()],
                        ["id: ", item.get_id()],
                        ["GUID: ", item.get_guid()],
                        ["instance: ", item.get_instance_id()],
                        ["POWER LEVEL: ", item.get_power_level()],
                        ["AXES COUNT: ", item.get_numaxes()],
                        ["BUTTONS COUNT: ", item.get_numbuttons()],
                        ],
                       headers=['Name', 'Value']))
    if item.get_name() == 'Xbox 360 Controller':
        print(tabulate([["Name: ", item.get_name()],
                        ["ENABLE: ", item.get_init()],
                        ["id: ", item.get_id()],
                        ["GUID: ", item.get_guid()],
                        ["instance: ", item.get_instance_id()],
                        ["POWER LEVEL: ", item.get_power_level()],
                        ["AXES COUNT: ", item.get_numaxes()],
                        ["BUTTONS COUNT: ", item.get_numbuttons()],
                        ["GET BUTTON: ", item.get_button(1)],
                        ["HAT (+ BUTTON) COUNTS: ", item.get_numhats()],
                        ["GET HAT: ", item.get_hat(0)],
                        ],
                       headers=['Name', 'Value']))
    if item.get_name() == joyName:
        joyindex = item.get_instance_id()
        print(joyindex)

pygame.init()
joy = joysticks[joyindex]
joy.init()
axes = joy.get_numaxes()
buttons = joy.get_numbuttons()
try:
    if joy.get_numhats() > 0:
        hats = joy.get_numhats()
except Exception:
    pass


while not done:
    pygame.event.get()
    # logitech.rumble(0, 0.2, 1)
    for i in range(axes):
       axis = joy.get_axis(i)
       print("Angle #" + str(i), float(axis))

    for i in range(buttons):
        button = joy.get_button(i)
        print("Button #" + str(i), button)

    try:
        if hats > 0:
            for i in range(hats):
                hat = joy.get_hat(i)
                print("Hat #" + str(i), hat)
    except Exception:
        pass


    #logitech.rumble(0, 0.2, 1)
    #time.sleep(1)
    #logitech.rumble(0, 0, 1)

    print("----------------------------------------------")

    time.sleep(2)

joy.quit()
pygame.quit()