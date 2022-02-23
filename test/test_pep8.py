#!/usr/bin/python3

import os
import subprocess
import unittest

# E126: I don't even know what its supposed to tell me :(
IGNORE = "E126,E265,E402,W503"


class PackagePep8TestCase(unittest.TestCase):

    def test_pep8_clean(self):
        top_src_dir = os.path.join(os.path.dirname(__file__), "..")
        targets = [
            top_src_dir,
            os.path.join(top_src_dir, "unattended-upgrade"),
            os.path.join(top_src_dir, "unattended-upgrade-shutdown"),
        ]
        try:
            subprocess.check_call(["pycodestyle",
                                   "--repeat",
                                   "--ignore=%s"
                                   % IGNORE] + targets)
        except FileNotFoundError:
            subprocess.check_call(
                ["pep8", "--repeat", "--ignore=%s" % IGNORE] + targets)


if __name__ == "__main__":
    unittest.main()
