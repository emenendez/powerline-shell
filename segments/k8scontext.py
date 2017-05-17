import subprocess

def add_k8scontext_segment(powerline):    
    try:
        p = subprocess.Popen(['kubectl', 'config', 'current-context'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = p.communicate()[0].decode("utf-8").rstrip('\n')
        if p.returncode == 0:
            powerline.append(' %s ' % output, Color.K8SCONTEXT_FG, Color.K8SCONTEXT_BG)
    except Exception:
        pass
