import json
import subprocess

from ..utils import BasicSegment, warn


class Segment(BasicSegment):
    def add_to_powerline(self):
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
                self.powerline.append(' %s.%s ' % (current_context, namespace),
                                      self.powerline.theme.AWS_PROFILE_FG,
                                      self.powerline.theme.AWS_PROFILE_BG)
        except Exception:
            pass
