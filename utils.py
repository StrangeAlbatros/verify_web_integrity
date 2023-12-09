#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
from hashlib import md5, sha1, sha256, sha512

from yaml import safe_load
from yaml import YAMLError

from .logger import LOGGER


ALGORITHMS = ['md5', 'sha1', 'sha256', 'sha512']

def read_yml(filepath='file.yaml'):
    """ Function wich read a yaml file and return a dict """
    try:
        with open(filepath, 'r', encoding='utf8') as stream:
            try:
                data = safe_load(stream)
            except YAMLError:
                LOGGER.exception(f"Error in reading the file {filepath}")
    except FileNotFoundError:
        LOGGER.exception(f"File not found: {filepath}")
        return None

    return data

def read_json(filepath='file.json'):
    """ Function wich read a json file and return a dict """
    try:
        with open(filepath, 'r', encoding='utf8') as stream:
            try:
                data = json.load(stream)
            except json.JSONDecodeError:
                LOGGER.exception(f"Error in reading the file {filepath}")
    except FileNotFoundError:
        LOGGER.exception(f"File not found: {filepath}")
        return None

    return data

### Hash functions ###

def get_md5(data):
    """ Returns the MD5 hash of the data """
    if isinstance(data, list):
        data = ''.join(data)
    elif isinstance(data, dict):
        data = ''.join([str(v) for v in data.values()])

    return md5(data.encode('utf-8')).hexdigest()

def get_sha1(data):
    """ Returns the SHA1 hash of the data """
    if isinstance(data, list):
        data = ''.join(data)
    elif isinstance(data, dict):
        data = ''.join([str(v) for v in data.values()])

    return sha1(data.encode('utf-8')).hexdigest()

def get_sha512(data):
    """ Returns the SHA512 hash of the data """
    if isinstance(data, list):
        data = ''.join(data)
    elif isinstance(data, dict):
        data = ''.join([str(v) for v in data.values()])

    return sha512(data.encode('utf-8')).hexdigest()

def get_sha256(data):
    """ Returns the SHA256 hash of the data """
    if isinstance(data, list):
        data = ''.join(data)
    elif isinstance(data, dict):
        data = ''.join([str(v) for v in data.values()])

    return sha256(data.encode('utf-8')).hexdigest()

def get_hash(data, algorithm='all'):
    """ Returns the hash of the data """
    if algorithm == 'md5':
        return get_md5(data)
    elif algorithm == 'sha1':
        return get_sha1(data)
    elif algorithm == 'sha256':
        return get_sha256(data)
    elif algorithm == 'sha512':
        return get_sha512(data)
    elif algorithm == 'all':
        return {
            'md5': get_md5(data),
            'sha1': get_sha1(data),
            'sha256': get_sha256(data),
            'sha512': get_sha512(data)
        }