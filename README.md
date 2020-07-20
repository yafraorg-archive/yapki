# yafra.org YAPKI - Yet another PKI system

## Python and OpenSSL/PKI
This repository holds a RESTful server based on Python, Flask and Eve.

Build on top of openssl this is a simple homebrew PKI for you. 
[![Build Status](https://api.shippable.com/projects/54f760fd5ab6cc1352923222/badge?branchName=master)](https://app.shippable.com/projects/54f760fd5ab6cc1352923222/builds/latest)

## Install

* Run CA.pl -newca (for the CA cert a common name is recommended like CA-Admin)
* Publish the new CA public certificate
* Run genwwwcert.sh to generate a Web Server certificate like for apache or nginx
* Generate you cert request through a web interface
* Sign the generated cert requests by the CA
* Run gensshcert.sh to generate a SSH certificate like for Putty or openssh
* Run gencrl.sh to generate a CRL lits to be published


## Run the server
uvicorn server:app --reload

## Version settings
Version string is set in:
* www/js/app.js
* backend/run.py

## Development Environment
 * https://github.com/yafraorg/yafra/wiki/Nodejs using Jetbrains Webstorm IDE

## Automatic build and run environment
 * Shippable: https://app.shippable.com/projects/54f760fd5ab6cc1352923222
 * Docker: https://github.com/yafraorg/docker-yapki
 * Openshift: http://python-yafraorg.rhcloud.com/

## Further information
read more about yafra on:
 * http://www.yafra.org
 * https://github.com/yafraorg/yafra/wiki/Yapki
 * raise a ticket related to yafra.org framework: https://github.com/yafraorg/yafra/issues?state=open
 * raise a ticket related to this nodejs code: https://github.com/yafraorg/yafra-yapki/issues?state=open
 
 
# yapki python server

## setup
pip install -r requirements.txt
uvicorn server:app --reload

fastapi
uvicorn
sqlalchemy

## environment
Crate .env file with the following variables:

```bash
DEBUG=true
DB_USER=user
DB_USER_PWD=pass
DB_HOST=xxxx
DB_NAME=xxxx
JWT_SECRET=a@!$afjk238jif390sfWEERU*"JçR(
```
