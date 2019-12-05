import matplotlib.pyplot as plt

# Parâmetros:
anaesthesia = 'off'
heartbeat = 90
time = 100

'''
Tipos de dosagem da anestesia:
>>> off
>>> quite light
>>> light
>>> so much light
>>> on
'''

def fuzzy(heart = heartbeat, time = time):
    global anaesthesia
    histo = []

    for i in range(time):
        if heart > 70: anaesthesia = 'on'
        elif heart > 65: anaesthesia = 'quite light'
        elif heart > 62: anaesthesia = 'light'
        elif heart > 60: anaesthesia = 'so much light'
        else: anaesthesia = 'off'

        if anaesthesia == 'on': heart -= 1
        elif anaesthesia == 'quite light': heart -= 0.5
        elif anaesthesia == 'light': heart -= 0.25
        elif anaesthesia == 'so much light': heart -= 0.1
        else: heart += 1

        histo.append(heart)

    return histo

plt.plot(range(time), fuzzy())
plt.show()