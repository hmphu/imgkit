# -*- coding: utf-8 -*-
import subprocess
import sys


class Config(object):
    def __init__(self, wkhtmltoimage='', xvfb=None, meta_tag_prefix='imgkit-'):
        self.meta_tag_prefix = meta_tag_prefix

        self.wkhtmltoimage = wkhtmltoimage

        if not self.wkhtmltoimage:
            if sys.platform == 'win32':
                self.wkhtmltoimage = subprocess.Popen(['where', 'wkhtmltoimage'],
                                                      stdout=subprocess.PIPE).communicate()[0].strip()
            else:
                self.wkhtmltoimage = subprocess.Popen(['which', 'wkhtmltoimage'],
                                                      stdout=subprocess.PIPE).communicate()[0].strip()

        try:
            with open(self.wkhtmltoimage):
                pass
        except IOError:
            raise IOError('No wkhtmltoimage executable found: "{0}"\n'
                          'If this file exists please check that this process can '
                          'read it. Otherwise please install wkhtmltopdf - '
                          'http://wkhtmltopdf.org\n'.format(self.wkhtmltoimage))

        self.xvfb = xvfb
        if self.xvfb is not None and not self.xvfb:
            if sys.platform == 'win32':
                self.xvfb = subprocess.Popen(['where', 'xvfb-run'],
                                            stdout=subprocess.PIPE).communicate()[0].strip()
            else:
                self.xvfb = subprocess.Popen(['which', 'xvfb-run'],
                                            stdout=subprocess.PIPE).communicate()[0].strip()
            try:
                with open(self.xvfb):
                    pass
            except IOError:
                raise IOError('No xvfb executable found: "{0}"\n'
                                'If this file exists please check that this process can '
                                'read it. Otherwise please install xvfb -'.format(self.xvfb))
