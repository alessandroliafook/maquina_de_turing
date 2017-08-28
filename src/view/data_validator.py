
def configuration_path(path):
    try:
        open(path, "r")
        return True
    except IOError:
        return False


def tape(states):
    return True