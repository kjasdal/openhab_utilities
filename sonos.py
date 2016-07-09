import sys
import argparse
import soco

parser = argparse.ArgumentParser()
parser.add_argument('zone', help='TBD')
parser.add_argument('command', choices=['ON', 'OFF', '?'], help='TBD')

args = parser.parse_args()

#print "Zone   :", args.zone
#print "Command:", args.command

zones = soco.discover();
for zone in zones:
#  print zone.player_name
  if zone.player_name == args.zone:
    break
  zone = None

if not zone:
  sys.exit()
  
if args.command == "ON":
  zone.play()
  sys.exit()
    
if args.command == "OFF":
  zone.stop()
  sys.exit()
  
if args.command == "?":
  state = zone.get_current_transport_info()['current_transport_state']
  while state == 'TRANSITIONING':
    state = zone.get_current_transport_info()['current_transport_state']
    break

#print "State:", state

if state == 'PLAYING':
  print 'ON'
  sys.exit()
  
if state == 'STOPPED':
  print 'OFF'  
  sys.exit()

sys.exit()
