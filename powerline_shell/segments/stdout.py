import subprocess
from ..utils import ThreadedSegment


class Segment(ThreadedSegment):
    def run(self):
        cmd = self.segment_def["command"]
        try:
            self.output = subprocess.check_output(cmd, stderr=subprocess.PIPE).decode("utf-8").strip()
        except Exception:
            self.output = None

    def add_to_powerline(self):
        self.join()
        if self.output:
            self.powerline.append(
                " %s " % self.output,
                self.segment_def.get("fg_color", self.powerline.theme.PATH_FG),
                self.segment_def.get("bg_color", self.powerline.theme.PATH_BG))
