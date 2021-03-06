Configure
*********


Create the tourbillon-linux configuration file
===============================================

You must create the tourbillon-linux configuration file in order to use tourbillon-linux.
By default, the configuration file must be placed in **/etc/tourbillon/conf.d** and its name
must be **linux.conf**.

The tourbillon-linux configuration file looks like: ::

	{
		"database": {
			"name": "linux",
			"duration": "365d",
			"replication": "1"
		},
		"hostname": "localhost",
		"cpu_usage_frequency": 1,
		"memory_usage_frequency": 1,
		"disks_io_stats_frequency": 1,
		"disks_usage_frequency": 1,
		"include_disks":["disk0"],
		"include_partitions":["/dev/disk1"]
	}


You can customize the database name, the hostname with which datapoints are tagged,
the frequency at which measures are collected and the disks and partitions that you want to  colect metrics for.


Enable the tourbillon-linux metrics collectors
==============================================

To enable the tourbillon-linux metrics collectors types the following command: ::

	$ sudo -i tourbillon enable tourbillon.linux=<collector_name>

Where <collector_name> can be one of or a comma separated list of the colectors names within:
	
	* get_cpu_usage
	* get_memory_usage
	* get_disks_usage
	* get_disks_io_stats
	* get_net_io_stats






