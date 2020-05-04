#! /bin/sh

### BEGIN INIT INFO
# Provides:          pwr_vol_buttons.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

# If you want a command to always run, put it here

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting pwr_vol_buttons.py"
    /usr/local/bin/pwr_vol_buttons.py &
    ;;
  stop)
    echo "Stopping pwr_vol_buttons.py"
    pkill -f /usr/local/bin/pwr_vol_buttons.py
    ;;
  *)
    echo "Usage: /etc/init.d/pwr_vol_buttons.sh {start|stop}"
    exit 1
    ;;
esac

exit 0
