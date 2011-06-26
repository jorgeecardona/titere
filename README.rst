
Titere
======

Titere is a configuration management tool that can be used from as shell or as library for pyhton programs.

Installation
------------

Currently extreamly beta please use github.com/jorgeecardona/titere


Usage
-----

For now it only configure files, create a configuration file:

::
    [file:nginx-configuration]
    path = /etc/nginx/nginx.conf
    content = write your configuration here (templates in near future.) 

and run the command:

::
   titere file.cfg

RoadMap
-------

There are a lot of missing things here, please write me if you want some particular feature.

Files
.....

- Templates
 
Users
.....
 
- Create user. 
- Delete users.

Packages
........

- Install.
- Configure.
- Uninstall.


