Simple Virtualhost LAMPP
===========
## Installation ##
1. Download the file
2. Change perrmision to execute :
```bash
$ chmod+x /path/to/virtualhost
```
3. Copy to /usr/bin/ for use for globally
```bash
$ sudo cp /path/to/virtualhost /usr/bin/virtualhost
```

## Usage ##

```bash
usage: virtualhost [-h] [-H DOMAIN] [-l LOC]

Simple Virtualhost in Lampp Linux

optional arguments:
  -h, --help            show this help message and exit
  -H DOMAIN, --host DOMAIN
                        Masukan domain virtual kalian
  -l LOC, --loc LOC     Letak folder yang ingin divirtualkan di htdocs
```
example to create new virtualhost :
```bash
$ virtualhost projek.dev projek
```