# Verify Webpage integrity

[![made-with-python](https://img.shields.io/badge/Made%20with-Python%203.10-1f425f.svg?logo=python)](https://www.python.org/)
![GitHub License](https://img.shields.io/github/license/StrangeAlbatros/verify_web_integrity)
![GitHub repo size](https://img.shields.io/github/repo-size/StrangeAlbatros/verify_web_integrity)

This software is made to monitor the integrity of web page.

It's check the hash of webpage and compare it with the hash in dataset file and send the resut as http request.

---

## Table of content

[1. Installation](#1-installation)

[2. Setting](#2-setting)

[3. Using](#3-using)

## 1. Installation

### Linux
```
python3 -m venv .venv
source .venv
pip3 install -r requirements.txt
```
## 2. Setting

For configuration, refer to the [setting documentation](./doc/setting.md)

## 3. Using
You need to be in the **verify_web_integrity** folder.

```
python3 -m verify_web_integrity
```

```
usage: Verify Web Integrity [-h] [-c CONFIG] [-d DATA] [-a {md5,sha1,sha256,sha512} [{md5,sha1,sha256,sha512} ...]] [-v] [--version]

Verify the integrity of a web site

options:
  -h, --help            show this help message and exit
  -c CONFIG, --config-file CONFIG
                        config file
  -d DATA, --data-file DATA
                        Path of dataset file
  -a {md5,sha1,sha256,sha512} [{md5,sha1,sha256,sha512} ...], --algorithms {md5,sha1,sha256,sha512} [{md5,sha1,sha256,sha512} ...]
                        hash algorithms to use
  -v, --verbose         Increase output verbosity
  --version             show program's version number and exit

An application wich verify the integrity of a web page
```
