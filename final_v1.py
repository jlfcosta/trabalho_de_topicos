import matplotlib.pyplot as plt
import numpy as np

# Parâmetros (os valores associados são interpretados como intervalos):
res = 0.5 # Resistência do paciente.

batimento = ['ED', 'D', 'OKD', 'OK', 'OKP', 'P', 'EP'] # Estado do paciente.
heartbeat = [20.0, 40.0, 60.0, 80.0, 100.0, 140.0] # Valores associados à lista "batimento".

estimulo = ['ZERO', 'SMALL', 'MEDIUM', 'DEEP', 'VDEEP', 'EDEEP'] # Estímulo da operação.
stimulus = [0.0, 0.4, 0.6, 0.75, 0.9, 1.0] # Valores associados à lista "estimulo".

anestesia = ['ZERO', 'LOW', 'MEDIUM', 'HIGH', 'VHIGH'] # Nível da anestesia.
anaesthesia = [0.0, 0.4, 0.6, 0.8, 1.0] # Valores associados à lista "anestesia".

paciente = 70 # Batimentos por minuto atual do paciente.
current_anes = 0.0 # Nível de anestesia sendo aplicada atualmente no paciente.

# Função para as regras fuzzy. H = estado do paciente; S = estímulo da operação.
def rules(H, S):

    global res, batimento, heartbeat, estimulo, stimulus, anestesia, anaesthesia, current_anes

    # Ajustando a sensação de dor do paciente.
    for i in range(len(stimulus)):
        stimulus[i] = stimulus[i] - (res - 0.5) if stimulus[i] - (res - 0.5) > 0 else i/1000

    # Dando valores fuzzy para "H".
    if H >= heartbeat[5]: H = batimento[6]
    elif H >= heartbeat[4]: H = batimento[5]
    elif H >= heartbeat[3]: H = batimento[4]
    elif H >= heartbeat[2]: H = batimento[3]
    elif H >= heartbeat[1]: H = batimento[2]
    elif H >= heartbeat[0]: H = batimento[1]
    else: H = batimento[0]

    # Dando valores fuzzy para "S".
    if S == stimulus[0]: S = estimulo[0]
    elif S <= stimulus[1]: S = estimulo[1]
    elif S <= stimulus[2]: S = estimulo[2]
    elif S <= stimulus[3]: S = estimulo[3]
    elif S <= stimulus[4]: S = estimulo[4]
    else: S = estimulo[5]

    if S == 'ZERO':
        if H == 'ED': current_anes = 'ZERO'
        elif H == 'D': current_anes = 'ZERO'
        elif H == 'OKD': current_anes = 'ZERO'
        elif H == 'OK': current_anes = 'LOW'
        elif H == 'OKP': current_anes = 'MEDIUM'
        elif H == 'P': current_anes = 'HIGH'
        else: current_anes = 'VHIGH'
    elif S == 'SMALL':
        if H == 'ED': current_anes = 'ZERO'
        elif H == 'D': current_anes = 'ZERO'
        elif H == 'OKD': current_anes = 'LOW'
        elif H == 'OK': current_anes = 'MEDIUM'
        elif H == 'OKP': current_anes = 'HIGH'
        elif H == 'P': current_anes = 'HIGH'
        else: current_anes = 'VHIGH'
    elif S == 'MEDIUM':
        if H == 'ED': current_anes = 'ZERO'
        elif H == 'D': current_anes = 'ZERO'
        elif H == 'OKD': current_anes = 'LOW'
        elif H == 'OK': current_anes = 'HIGH'
        elif H == 'OKP': current_anes = 'HIGH'
        elif H == 'P': current_anes = 'VHIGH'
        else: current_anes = 'VHIGH'
    elif S == 'DEEP':
        if H == 'ED': current_anes = 'ZERO'
        elif H == 'D': current_anes = 'ZERO'
        elif H == 'OKD': current_anes = 'LOW'
        elif H == 'OK': current_anes = 'HIGH'
        elif H == 'OKP': current_anes = 'VHIGH'
        elif H == 'P': current_anes = 'VHIGH'
        else: current_anes = 'VHIGH'
    elif S == 'VDEEP':
        if H == 'ED': current_anes = 'ZERO'
        elif H == 'D': current_anes = 'ZERO'
        elif H == 'OKD': current_anes = 'MEDIUM'
        elif H == 'OK': current_anes = 'VHIGH'
        elif H == 'OKP': current_anes = 'VHIGH'
        elif H == 'P': current_anes = 'VHIGH'
        else: current_anes = 'VHIGH'
    else:
        if H == 'ED': current_anes = 'ZERO'
        elif H == 'D': current_anes = 'LOW'
        elif H == 'OKD': current_anes = 'MEDIUM'
        elif H == 'OK': current_anes = 'VHIGH'
        elif H == 'OKP': current_anes = 'VHIGH'
        elif H == 'P': current_anes = 'VHIGH'
        else: current_anes = 'VHIGH'

    if current_anes == 'ZERO':
        current_anes = 0.0
        return 0.0
    elif current_anes == 'LOW':
        current_anes = 0.4
        return 0.4
    elif current_anes == 'MEDIUM':
        current_anes = 0.6
        return 0.6
    elif current_anes == 'HIGH':
        current_anes = 0.8
        return 0.8
    elif current_anes == 'VHIGH':
        current_anes = 1.0
        return 1.0


def coracebo(dor):
    global paciente, current_anes

    if current_anes == 0.0: paciente -= 0.0
    elif current_anes == 0.4: paciente -= 0.125
    elif current_anes == 0.6: paciente -= 0.25
    elif current_anes == 0.8: paciente -= 0.5
    else: paciente -= 0.7
    paciente += dor


if __name__ == '__main__':

    batimentos = []
    quant_anestesia = []
    operation = [0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.0, 0.1, 0.1, 0.2, 0.3, 0.3, 0.2, 0.3, 0.4, 0.3, 0.4,
                 0.4, 0.3, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.6, 0.6, 0.7, 0.7, 0.6, 0.5, 0.5, 0.6, 0.5, 0.5,
                 0.5, 0.5, 0.4, 0.5, 0.5, 0.6, 0.5, 0.6, 0.5, 0.6, 0.5, 0.4, 0.5, 0.6, 0.6, 0.5, 0.6, 0.5,
                 0.4, 0.4, 0.4, 0.4, 0.3, 0.3, 0.3, 0.3, 0.3, 0.2, 0.2, 0.1, 0.0, 0.1, 0.2, 0.2, 0.3, 0.2,
                 0.2, 0.3, 0.3, 0.4, 0.3, 0.2, 0.1, 0.0, 0.1, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                 0.1, 0.0, 0.0, 0.1, 0.2, 0.2, 0.3, 0.2, 0.1, 0.2, 0.2, 0.1, 0.1, 0.2, 0.3, 0.4, 0.5, 0.4,
                 0.3, 0.2, 0.2, 0.1, 0.0, 0.1, 0.0, 0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0, 0.1, 0.0, 0.1,
                 0.1, 0.1, 0.2, 0.3, 0.2, 0.3, 0.3, 0.4, 0.3, 0.4, 0.5, 0.6, 0.6, 0.6, 0.6, 0.7, 0.8, 0.9,
                 0.9, 1.0, 0.9, 1.0, 0.9, 0.8, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.1, 0.0]
    bins = [int(i) for i in list(np.linspace(1, len(operation), len(operation)))]

    fig, ax1 = plt.subplots()
    ax1.set_xlabel('Período da operação')

    for i in range(len(bins)):
        batimentos.append(paciente)
        quant_anestesia.append(rules(paciente, current_anes))
        coracebo(operation[i])

    ax1.plot(bins, batimentos, color=(0.7, 0, 0.3), label='Batimentos')
    ax1.legend(loc=3, bbox_to_anchor=(0., 1.))
    ax2 = ax1.twinx()
    ax2.plot(bins, quant_anestesia, color=(0.2, 0.9, 0.2), label='Anestesia')
    ax2.plot(bins, operation, color=(1, 0.5, 0, 1), label='Estímulo da operação')
    ax2.legend(loc=4, bbox_to_anchor=(1., 1.))

    plt.show()