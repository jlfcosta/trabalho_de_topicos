import matplotlib.pyplot as plt

# Parâmetros:
anaesthesia = 'off'
heartbeat = 90
time = 100

def fuzzy(heart = heartbeat, time = time):
    global anaesthesia
    histo = []
    for i in range(time):
        if heart > 60:
            anaesthesia = 'on'
        else: anaesthesia = 'off'
        if anaesthesia == 'on':
            heart -= 1
        else: heart += 1
        histo.append(heart)
    return histo

plt.plot(range(time), fuzzy())
plt.show()