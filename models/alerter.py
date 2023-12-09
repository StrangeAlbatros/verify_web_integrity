#!/usr/bin/python3
# -*- coding: utf-8 -*-

from json import dumps

from jinja2 import Environment
from requests import Session

from verify_web_integrity.logger import LOGGER

class Alerter:
    """ Class wich alert the user if the hash changed """
    def __init__(self, **kwargs) -> None:
        self.url = kwargs.get('scheme') + "://" + kwargs.get('url')

        self.session = Session(
            # timeout=kwargs.get('timeout', 5),
        )

        self.session.headers.update({'Content-Type': 'application/json'})
        if kwargs.get('header', None):
            self.session.headersupdate(kwargs.get('header'))

        # auth = (username, password)
        if kwargs.get('basic_auth', None):
            self.session.auth = (kwargs.get('user'), kwargs.get('password'))

        # token = "token"
        if kwargs.get('token', None):
            self.session.headers.update(
                {'Authorization': f"Bearer {kwargs.get('token')}"}
            )

        if not kwargs.get('ssl_verify', True):
            self.session.verify = False

        if kwargs.get('ca_cert', None):
            self.session.verify = kwargs.get('ca_cert')

        self.method = kwargs.get('method', None)
        LOGGER.debug("method: {}".format(self.method))

        self.template = kwargs.get('template', None)

        self.set_content(**kwargs)

    @property
    def url(self) -> str:
        """ Get url """
        return self.__url
    
    @url.setter
    def url(self, url: str) -> None:
        """ Set url """
        if not isinstance(url, str):
            LOGGER.error("url must be a string")
            raise TypeError("url must be a string")
        self.__url = url

    @property
    def content(self) -> str:
        """ Get content """
        return self.__content
    
    @content.setter
    def content(self, content: dict) -> None:
        """ Set content """
        if not isinstance(content, dict):
            LOGGER.error("content must be a dict")
            raise TypeError("content must be a dict")
        
        content['message'] = self.render_content(
            **content
        )
        self.__content = content

    def set_content(self, **kwargs) -> None:
        """ Set data """        
        if kwargs.get('data', None):
            self.content = kwargs.get('data')
        else:
            self.content = {}

    def render_content(self, **kwargs) -> None:
        """ Render the content """
        if not self.template:
            LOGGER.warning("No template")
            return None
        environment = Environment()
        template = environment.from_string(self.template)
        return template.render(**kwargs)

    def send_alert(self) -> None:
        """ Send alert to the user """
        if self.method == "POST":
            LOGGER.debug("POST with data: {}".format(self.content))
            response = self.session.post(
                self.url,
                data=dumps(self.content),
            )
        elif self.method == "PUT":
            LOGGER.debug("PUT with data: {}".format(self.content))
            response = self.session.put(
                self.url,
                data=dumps(self.content),
            )
        elif self.method == "PATCH":
            LOGGER.debug("PATCH with data: {}".format(self.content))
            response = self.session.patch(
                self.url,
                data=dumps(self.content),
            )
        
        if response.status_code == 200:
            LOGGER.debug("Alert send")
        elif response.status_code == 404:
            LOGGER.error("Alert not sent, url not found")
        else:
            LOGGER.error(f"Alert not sent, error: {response.text}")
