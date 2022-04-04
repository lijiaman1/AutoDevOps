import psutil

# cpu
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))

# memory
print(psutil.virtual_memory())
print(psutil.virtual_memory().percent)

# disk
print(psutil.disk_partitions())
print(psutil.disk_usage("c:/"))

# processlist
print(psutil.pids())

print(psutil.Process(664))
print(psutil.Process(664).exe())
print(psutil.Process(664).connections())

# user info
print(psutil.disk_io_counters(perdisk=True))