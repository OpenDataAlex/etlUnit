### Oracle dependencies

Tips on setting up cx_Oracle on Linux...

Install the following RPMs:

* oracle-instantclient11.1-basic-11.1.0.7.0-1.x86_64.rpm
* oracle-instantclient11.1-devel-11.1.0.7.0-1.x86_64.rpm

Link to those RPMs: http://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html

After that, add the following line to /etc/ld.so.conf.d/oracle.conf:

    /usr/lib/oracle/11.1/client64/lib/
    
And execute:

    $ ldconfig

Then setup ORACLE_HOME:

    $ export ORACLE_HOME=/usr/lib/oracle/11.1/client64

After that, you can pip install cx_Oracle:

    $ pip install cx_Oracle

You're done!
