portfolio_setup_runner
======================
setup
-----
Just type:
>python setup.py

It will install executable files (csv2sql, csvLoader, StablePortfolio)
to bin directory from downloaded submodules.

run
---
Just type:
>python runner.py

Firstly It'll download a csv filed frim ftp server.
Next sql files will be generated.
Thirdly database "quotes.db" will created in *bin* directory,
also add sql files in database.
Finally it'll start a stablePortfolio with predefined time period 

NoteBene:

**If script will stunned at step like**

>bin/csvLoader ...............

where " ..............." some string

**run it again with the same parameters**.
It can be occurs because of it lost connection with ftp server

