import math


def appearence_y(counter):
    return -200 + counter

def level_3_1_x(t):
    if 0 <= t % 1000 < 250:
        #print('a')
        return 250 - (t % 1001)
    elif 251 <= t % 1001 <= 750:
        #print('b')
        return (t % 1001) - 250
    elif 751 <= t % 1001 <= 1000:
        #print('c')
        return 1250 - (t % 1001)
    else:
        return 0

def level_3_2_x(t):
    if 0 <= t % 1001 <= 250:
        return 100*math.cos(t/30) + 100
    elif 251 <= t % 1001 <= 750:
        return 100*math.cos(t/30) + 100
    elif 751 <= t % 1001 <= 1000:
        return 100*math.cos(t/30) + 100

def level_3_2_y(t):
    if 0 <= t % 1001 <= 250:
        return 175*math.sin(t/30) + 250 - (t % 1001)
    elif 251 <= t % 1001 <= 750:
        return 175*math.sin(t/30) + (t % 1001) - 250
    elif 751 <= t % 1001 <= 1000:
        return 175*math.sin(t/30) + 1250 - (t % 1001)

def level_3_3_x(t):
    if 0 <= t % 1001 <= 250:
        return 100*math.cos(t/30 + math.pi) + 100
    elif 251 <= t % 1001 <= 750:
        return 100*math.cos(t/30 + math.pi) + 100
    elif 751 <= t % 1001 <= 1000:
        return 100*math.cos(t/30 + math.pi) + 100

def level_3_3_y(t):
    if 0 <= t % 1001 <= 250:
        return 175*math.sin(t/30 + math.pi) + 250 - (t % 1001)
    elif 251 <= t % 1001 <= 750:
        return 175*math.sin(t/30 + math.pi) + (t % 1001) - 250
    elif 751 <= t % 1001 <= 1000:
        return 175*math.sin(t/30 + math.pi) + 1250 - (t % 1001)

    
program_level_1 = [
    [(0, 250), lambda x: 250, appearence_y],
    #[(201, 450), lambda t: 450 - t, lambda y: 0],
    #[(451, 950), lambda t: t - 451, lambda t: -100 * math.sin((t - 451) * math.pi / 500)],
    #[(951, 1200), lambda t: 1450 - t, lambda y: 0]
    ##[(0, 10), lambda x: 100, lambda y: 100]
    [(250, 10**25), lambda t: 350*math.sin((t - 250)/200) + 250,
     lambda t: 50*math.cos((t - 250)/200)]
    ]
program_level_2_1 = [
    [(0, 250), lambda x: 250, lambda t: -200 + t],
    [(251, 10**25), lambda t: 350*math.sin((t - 250)/200) + 250,
     lambda y: 50],
    ]
program_level_2_2 = [
    [(0, 250), lambda x: 250, lambda t: -150 + t],
    [(251, 10**25), lambda t: 350*math.sin((t - 250)/50) + 250,
     lambda y: 100],
    ]
program_level_3_1 = [
    [(0, 250), lambda x: 250, lambda t: -150 + t],
    [(251, 10**25), lambda t: level_3_1_x(t - 251),
     lambda y: 100]
    ]
program_level_3_2 = [
    [(0, 250), lambda x: 250, lambda t: -50 + t],
    [(251, 10**25), lambda t: level_3_2_y(t - 251),
     lambda t: level_3_2_x(t - 251)]
    ]
program_level_3_3 = [
    [(0, 250), lambda x: 250, lambda t: -250 + t],
    [(251, 10**25), lambda t: level_3_3_y(t - 251),
     lambda t: level_3_3_x(t - 251)]
    ]
program_level_4 = [
    [(0, 400), lambda x: 250, lambda t: -250 + t],
    [(401, 10**25), lambda x: 250, lambda y: 150]
    ]
program_level_5 = [
    [(0, 250), lambda x: 250, lambda t: -200 + t],
    [(251, 10**25), lambda t: 350*math.sin((t - 250)/200) + 250,
     lambda y: 50],
    ]
breakdown_level_1 = 250
breakdown_level_2 = 250
breakdown_level_4 = 400
