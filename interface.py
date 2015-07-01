import os       #For commands
import sys      #For who-knows-what

interfaces = {}
print('INTERFACES:')
if sys.platform.startswith('win'):
    print('\tWindows OS features available')
    interfaces['os'] = 'win'
elif sys.platform.startswith('linux') or os.platform.startswith('darwin'):
    print('\t*nix features available')
    interfaces['os'] = '*nix'
else:
    print('\tOS-specific interface not available')
    interfaces['os'] = None

try:
    import requests #For APIs
    interfaces['web'] = True
    print('\tWeb API interface available')
except ImportError:
    print('\tWeb API interface not available')
    interfaces['web'] = False
try:
    import Skype4Py #For skype interfacing
    interfaces['skype'] = True
    print('\tSkype interface available')
except ImportError:
    print('\tSkype interface not available.')
    interfaces['skype'] = False

try:
    import tkMessageBox #For skype interfacing
    interfaces['messagebox'] = True
    print('\tMessage Box interface available')
except ImportError:
    print('\tMessage Box interface not available.')
    interfaces['messagebox'] = False

if interfaces['os'] == 'win':
    try:
        import speech   #Not available on all platforms and not in the standard library, but useful
        interfaces['speech'] = True
        print('\tVoice interface available')
    except ImportError:
        print('\tVoice interface not available')
        interfaces['speech'] = False
