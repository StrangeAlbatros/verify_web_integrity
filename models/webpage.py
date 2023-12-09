#!/usr/bin/python3
# -*- coding: utf-8 -*-

from time import sleep

from requests import get

from verify_web_integrity.utils import get_hash
from verify_web_integrity.logger import LOGGER

class Webpage():
    """ Class wich represent a webpage """
    def __init__(self, **kwargs) -> None:
        self.url = kwargs.get('url')
        self.original_hash = kwargs.get('original_hash')
        self.actual_hash = None
        self.algorithms = kwargs.get('algorithms')
        self.http_check_status_code = None

    @property
    def url(self) -> str:
        """ Return the url """
        return self._url
    
    @url.setter
    def url(self, url: str) -> None:
        """ Set the url """
        if not isinstance(url, str):
            LOGGER.error(f"Expected str, got {type(url)}")
            raise TypeError(f"Expected str, got {type(url)}")
        self._url = url

    @property
    def original_hash(self) -> str:
        """ Return the original hash """
        return self._original_hash
    
    @original_hash.setter
    def original_hash(self, original_hash: str) -> None:
        """ Set the original hash """
        if not isinstance(original_hash, str):
            raise TypeError(f"Expected str, got {type(original_hash)}")
        self._original_hash = original_hash

    def run(self) -> None:
        """ Function wich run the thread """
        content = self.request()
        self.actual_hash = get_hash(content, self.algorithms)

        if self.actual_hash != self.original_hash:
            LOGGER.error(
                f"Hash changed for url: {self.url}=> {self.actual_hash}!={self.original_hash}"
            )
        else:
            LOGGER.info(f"Hash not changed: {self.url}")

    def request(self):
        """ Function wich request the url and return the response """
        response = get(self.url)
        self.http_check_status_code = response.status_code
        if response.status_code == 200:
            return response.text
        elif response.status_code == 404:
            ind = 0
            while response.status_code == 404 or ind < 6:
                sleep(2)
                response = get(self.url)
                ind += 1
            if response.status_code == 200:
                return response.text
            else:
                return response.status_code
        else:
            return response.status_code
        
    def export_format(self) -> dict:
        """ Return the export format """
        return {
            "url": self.url,
            "original_hash": self.original_hash,
            "actual_hash": self.actual_hash,
            "http_check_status_code": self.http_check_status_code,
            "check": self.actual_hash == self.original_hash,
            "algorithm": self.algorithms,
        }