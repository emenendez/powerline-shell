
def add_saltenv_segment(powerline):    
    SALT_GRAINS_FILE = '/etc/salt/grains'
    try:
        with open(SALT_GRAINS_FILE) as inp:
            line = inp.readline().strip().lower()
            if line.startswith('env: '):
                powerline.append(' %s ' % line[5:], Color.SALTENV_FG, Color.SALTENV_BG)
    except Exception:
        pass
