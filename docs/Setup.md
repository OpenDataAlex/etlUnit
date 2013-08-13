Tips on setting up cx_Oracle...

If on Linux, install the following RPMs:

    oracle-instantclient11.1-basic-11.1.0.7.0-1.x86_64.rpm
    oracle-instantclient11.1-devel-11.1.0.7.0-1.x86_64.rpm

After that, add the following line to /etc/ld.so.conf.d/oracle.conf:

    /usr/lib/oracle/11.1/client64/lib/

Then setup ORACLE_HOME:

    export ORACLE_HOME=/usr/lib/oracle/11.1/client64

After that, you can pip install cx_Oracle:

    pip install cx_Oracle

You're done!