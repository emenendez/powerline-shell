import json
import subprocess

def add_k8scontext_segment(powerline):
    try:
        p = subprocess.Popen(['kubectl', 'config', 'view', '-o', 'json'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = p.communicate()[0].decode("utf-8")
        if p.returncode == 0:
            config = json.loads(output)
            current_context = config['current-context']
            for context in config['contexts']:
                if context['name'] == current_context:
                    namespace = context['context'].get('namespace', 'default')
                    break
            powerline.append(' %s.%s ' % (current_context, namespace),
                             Color.K8SCONTEXT_FG, Color.K8SCONTEXT_BG)
    except Exception:
        pass
