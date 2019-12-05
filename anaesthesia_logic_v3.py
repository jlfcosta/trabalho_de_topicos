import matplotlib.pyplot as plt

# Parâmetros:
anaesthesia = 1.0
heartbeat = 90
time = 100

def fuzzy(heartbeat = heartbeat, time = time):
    global anaesthesia
    histo = []

    for i in range(time):

        if heartbeat > 80: anaesthesia = 1.0
        elif heartbeat < 60: anaesthesia = 0.0
        else:
            razao = (heartbeat - 60)/20
            anaesthesia *= razao

        heartbeat -= anaesthesia

        histo.append(heartbeat)
    return histo

plt.plot(range(time), fuzzy())
plt.show()