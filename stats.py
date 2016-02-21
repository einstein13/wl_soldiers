def get_min_attack(tribe=1, level=0):
    if level < 0:
        return 0
    if tribe == 1:
        if level > 5:
            return 0
        return 12.0+7.0*level
    elif tribe == 2:
        if level > 4:
            return 0
        return 13.0+8.0*level
    elif tribe == 3:
        if level > 5:
            return 0
        return 12.0+8.0*level
    return 0

def get_max_attack(tribe=1, level=0):
    if level < 0:
        return 0
    if tribe == 1:
        if level > 5:
            return 0
        return 16.0+7.0*level
    elif tribe == 2:
        if level > 4:
            return 0
        return 15.0+8.0*level
    elif tribe == 3:
        if level > 5:
            return 0
        return 16.0+8.0*level
    return 0

def get_defense(tribe=1, level=0):
    if level < 0:
        return 0
    if tribe == 1:
        if level > 0:
            return 0
        return 1.0 - 0.03
    elif tribe == 2:
        if level > 0:
            return 0
        return 1.0 - 0.05
    elif tribe == 3:
        if level > 2:
            return 0
        return 1.0 - (0.06 + 0.08*level)
    return 0

def get_evade(tribe=1, level=0):
    if level < 0:
        return 0
    if level > 2:
        return 0
    if tribe == 1:
        return 0.75 - 0.15*level
    elif tribe == 2:
        return 0.7 - 0.16*level
    elif tribe == 3:
        return 0.7 - 0.17*level
    return 0

def get_health(tribe=1, level=0):
    if level < 0:
        return 0
    if tribe == 1:
        if level > 3:
            return 0
        return 130.0 + 28.0*level
    elif tribe == 2:
        if level > 4:
            return 0
        return 130.0 + 21.0*level
    elif tribe == 3:
        if level > 1:
            return 0
        return 135.0 + 40.0*level
    return 0
