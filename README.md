# YAPKI - Yet another PKI system

Build on top of openssl this is a simple homebrew PKI for you. It uses Python Flask backend and AngularJS Material Design frontent. In addition several bash shell scripts and Perl scripts are provided.

[![Build Status](https://api.shippable.com/projects/54f760fd5ab6cc1352923222/badge?branchName=master)](https://app.shippable.com/projects/54f760fd5ab6cc1352923222/builds/latest)

## Install

* Run CA.pl -newca (for the CA cert a common name is recommended like CA-Admin)
* Publish the new CA public certificate
* Run genwwwcert.sh to generate a Web Server certificate like for apache or nginx
* Generate you cert request through a web interface
* Sign the generated cert requests by the CA
* Run gensshcert.sh to generate a SSH certificate like for Putty or openssh
* Run gencrl.sh to generate a CRL lits to be published


## Version settings
Version string is set in:
* www/js/app.js
* backend/run.py

## Development Environment
 * https://github.com/yafraorg/yafra/wiki/Nodejs using Jetbrains Webstorm IDE

## Automatic build and run environment
 * Shippable: https://app.shippable.com/projects/54f760fd5ab6cc1352923222
 * Docker: https://github.com/yafraorg/docker-yapki

## Further information
read more about yafra on:
 * http://www.yafra.org
 * https://github.com/yafraorg/yafra/wiki/Yapki
 * raise a ticket related to yafra.org framework: https://github.com/yafraorg/yafra/issues?state=open
 * raise a ticket related to this nodejs code: https://github.com/yafraorg/yafra-yapki/issues?state=open
