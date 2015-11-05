Measurements
************

tourbillon-linux collects metrics about cpu, memory, disks and network interfaces.


CPU usage
=========


The ``get_cpu_usage`` collector get the amount of cpu used in percent tagged with the hostname and stores it in the ``cpu_usage`` series.


Tags
----
	* **host**: hostname

Fields
------

	* **value**: percentage of the cpu used


See `http://pythonhosted.org/psutil/#psutil.cpu_percent <http://pythonhosted.org/psutil/#psutil.cpu_percent>`_.

Memory usage
============

The ``get_memory_usage`` collector get info about virtual memory usage and swap usage, tagged with the hostname and stores it in the ``cpu_usage`` series.
The values are expressed in bytes.


Tags
----
	* **host**: hostname

Fields
------

	* **v_available**: the actual amount of available memory that can be given instantly to processes that request more memory in bytes.
	* **v_used**: used virtual memory
	* **v_free**: memory not being used at all (zeroed) that is readily available
	* **v_percent**: the percentage usage calculated as (total - available) / total * 100
	* **s_used**: used swap memory
	* **s_free**: free swap memory
	* **s_percent**: the percentage usage calculated as (total - available) / total * 100


See `http://pythonhosted.org/psutil/#memory <http://pythonhosted.org/psutil/#memory>`_.

Disks usage
===========

The ``get_disks_usage`` collector get info about disk usage for a given partition, tagged with the hostname and the partition name and stores it in the ``disks_usage`` series.
The values are expressed in bytes.


Tags
----
	* **host**: hostname
	* **partition**: partition name

Fields
------
	* **total**: total partition space
	* **used**: used partition space
	* **free**: free partition space
	* **percent**: percentage usage


See `http://pythonhosted.org/psutil/#psutil.disk_usage <http://pythonhosted.org/psutil/#psutil.disk_usage>`_.

Disks I/O stats
===============

The ``get_disks_io_stats`` collector get info about disks I/O.
Each field value express the difference between the current datapoint and the previous.


Tags
----
	* **host**: hostname
	* **disk**: device name

Fields
------
	* **read_count**: number of reads
	* **write_count**: number of writes
	* **read_bytes**: number of bytes read
	* **write_bytes**: number of bytes written
	* **read_time**: time spent reading from disk in milliseconds
	* **write_time**: time spent writing to disk in milliseconds

See `http://pythonhosted.org/psutil/#psutil.disk_io_counters <http://pythonhosted.org/psutil/#psutil.disk_io_counters>`_.


Net I/O stats
=============

The ``get_net_io_stats`` collector get info about network interfaces I/O.
Each field value express the difference between the current datapoint and the previous.


Tags
----
	* **host**: hostname
	* **interface**: interface name

Fields
------
	* **packets_sent**: number of packets sent
	* **packets_recv**: number of packets received
	* **bytes_sent**: number of bytes sent
	* **bytes_recv**: number of bytes received
	* **errin**: number of errors while receiving
	* **errout**: number of errors while sending
	* **dropin**: number of incoming packets which were dropped
	* **dropout**: number of outgoing packets which were dropped

See `http://pythonhosted.org/psutil/#psutil.net_io_counters <http://pythonhosted.org/psutil/#psutil.net_io_counters>`_.
