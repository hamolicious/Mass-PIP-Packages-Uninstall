# Mass-PIP-Packages-Uninstall
Quickly and easily removes [almost] all packages installed

I keep forgetting to create a virtual env for my packages and end up with thousands of different packages installed. This simple script aims to make cleanup easier by removing all but the [whitelisted](https://github.com/hamolicious/Mass-PIP-Packages-Uninstall/blob/master/whitelist.json) packages.


## How To Use
Extremely simple, modify the [whitelist.json](https://github.com/hamolicious/Mass-PIP-Packages-Uninstall/blob/master/whitelist.json) file by adding only the packages you want to be kept... then run:

```bash
python main.py
```

Sit back and wait for mass massacre to finish and you will be left with a beautiful `pip list` output.

```
Package    Version
---------- -------
pip        22.0.4
requests   2.27.1
setuptools 62.1.0
wheel      0.37.1
```
