
def add_userhost_segment(powerline):
    import os
    if powerline.args.shell == 'bash':
        user_prompt = ' \\u'
    elif powerline.args.shell == 'zsh':
        user_prompt = ' %n'
    else:
        user_prompt = ' %s' % os.getenv('USER')

    if os.getenv('USER') == 'root':
        bgcolor = Color.USERNAME_ROOT_BG
    else:
        bgcolor = Color.USERNAME_BG

    from socket import gethostname
    hostname = gethostname()

    if powerline.args.shell == 'bash':
        host_prompt = '\\h '
    elif powerline.args.shell == 'zsh':
        host_prompt = '%m '
    else:
        host_prompt = '%s ' % gethostname().split('.')[0]

    if (os.getenv('USER') != powerline.args.default_user and 
        hostname != powerline.args.default_host):
        powerline.append('%s@%s' % (user_prompt, host_prompt), Color.USERNAME_FG, bgcolor)
