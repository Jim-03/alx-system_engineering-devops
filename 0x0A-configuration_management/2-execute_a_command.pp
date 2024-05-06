# Kills a process "killmenow"
exec { 'kill_killmenow':
  command => 'pkill -f killmenow',  # Kills the process by name
  path    => ['/bin', '/usr/bin', '/usr/sbin'],  # Ensure the path includes standard locations for `pkill`
  unless  => 'pgrep -f killmenow',  # Only execute if the process is running
}
