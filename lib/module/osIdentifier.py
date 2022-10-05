from platform import system
def os():
    clear = ''
    if system() != 'Windows':
        clear = 'clear'
    else:
        clear = 'cls'
    return clear