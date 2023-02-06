import json
import re
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

                # Example long cluster name: gke_megaphone-prod_us-central1_megaphone-prod
                if current_context.startswith('gke_'):
                    # self.powerline.append(' %s ' % self.powerline.lock,
                    #                       self.powerline.theme.READONLY_FG,
                    #                       self.powerline.theme.READONLY_BG)
                    match = re.match(r'^gke_([^_]+)_([^_]+)_([^_]+)', current_context)
                    current_project = match.group(1)
                    current_region = (
                        match.group(2)
                        .replace("us-central", "usc")
                        .replace("us-east", "use")
                    )
                    current_context = match.group(3)

                    self.powerline.append(' %s ' % current_project,
                                            self.powerline.theme.AWS_PROFILE_FG,
                                            self.powerline.theme.AWS_PROFILE_BG,
                                            self.powerline.separator_thin,
                                            self.powerline.theme.AWS_PROFILE_FG)
                    self.powerline.append(' %s ' % current_region,
                                            self.powerline.theme.AWS_PROFILE_FG,
                                            self.powerline.theme.AWS_PROFILE_BG,
                                            self.powerline.separator_thin,
                                            self.powerline.theme.AWS_PROFILE_FG)
                self.powerline.append(' %s ' % current_context,
                                      self.powerline.theme.AWS_PROFILE_FG,
                                      self.powerline.theme.AWS_PROFILE_BG,
                                      self.powerline.separator_thin,
                                      self.powerline.theme.AWS_PROFILE_FG)
                self.powerline.append(' %s ' % namespace,
                                      self.powerline.theme.AWS_PROFILE_FG,
                                      self.powerline.theme.AWS_PROFILE_BG)
        except Exception:
            pass
