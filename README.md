portfolio_setup_runner
======================
Depends
-------
You should have:
>**git**;

>**python2.7**;

>>*sqalchemy*

>**sqlite3**

>**ghc** (*haskel platform*):

>>**cabal**;
>>*ftphs*;
>>*filepath*;
>>*directory*;
>>*regex-posix*;
>>*old-locale*;
>>*split*;
>>*GA*;
>>*random*;
>>*containers*;
>>*time*
>>*HDBC-sqlite3*;
>>*HDBC*

>>you can get it on ***http://hackage.haskell.org/packages/archive/pkg-list.html***

setup
-----
Just type:
>python setup.py

It will install executable files (csv2sql, csvLoader, StablePortfolio)
to *bin* directory from downloaded submodules.

run
---
***Before starting you must have a environment variables *EOD_USER* (user name on eoddata ftp-server) and *EOD_PSSWD* (users password on eoddata ftpserver).***

Just type:
>python runner.py

**Firstly** It'll download a csv filed frim ftp server in directory *csvs*.

**Next** sql files will be generated in directory *sqls*..

**Thirdly** database "quotes.db" will created in *bin* directory,
also add sql files in database.

**Finally** it'll start a stablePortfolio with predefined time period 

NoteBene:

**If script will stunned at step like**

>bin/csvLoader ...............

where " ..............." some string

**run it again with the same parameters**.
It can be occurs because of it lost connection with ftp server

