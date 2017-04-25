from subprocess import Popen, PIPE

def get_all_stats():
  grep_process = Popen(["vmstat", "-s","-S","m"], stdout=PIPE,stderr=PIPE)
  listado_stats= Popen(["awk", '-F', ':','{print $1}' ],stdin=grep_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
  
  print(listado_stats)
  return filter(None, listado_stats)


def get_cpu():
  grep_process = Popen(["mpstat", "", ""], stdout=PIPE, stderr=PIPE)
  return filter(None, grep_process)



