#!/usr/bin/python3
# -*- coding: utf-8 -*-

from .logger import LOGGER
from .utils import read_yml

from .models import Webpage
from .models import Alerter

class VerifyWebIntegrity:
    """ Verify the integrity of a webpage """
    def __init__(self, args) -> None:
        self.algorithms = args.algorithms

        self.config = read_yml(args.config)
        if not self.algorithms:
            self.algorithms = self.config['algorithm']

        if self.data:
            self.config['data_file'] = args.data

        if args.debug:
            LOGGER.set_debug()

        self.data = None
        self.webpages = []
        self.load_data()

        self.run()

    def load_data(self):
        """ Load the url and hash from the data file """
        r_data = read_yml(self.config['data_file'])
        if not r_data:
            return False
        
        self.data = r_data

    def notify(self, webpage_export) -> bool:
        """ test if notify the user or not """
        key_conf = self.config.get('send_alert_if_check')

        if key_conf == 'all':
            return True

        if not isinstance(key_conf, bool):
            LOGGER.error("send_alert_if_check must be a bool or 'all'")
            return TypeError("send_alert_if_check must be a bool or 'all'")
        
        return key_conf == webpage_export['check']

    def run(self):
        """ Run the program """
        if not self.data:
            LOGGER.error("No url:hash to verify")
            return
        
        for url, hash in self.data.items():
            self.webpages.append(Webpage(
                url=url,
                original_hash=hash,
                algorithms=self.algorithms
            ))

        conf = self.config['alerter']
        conf['template'] = self.config['template'].get('data', None)
        alerter = Alerter(**conf)
        for webpage in self.webpages:
            webpage.run()
            data = webpage.export_format()
            if self.notify(data):
                alerter.set_content(
                    data=data
                )
                alerter.send_alert()
