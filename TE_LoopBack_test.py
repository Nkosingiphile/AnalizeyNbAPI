import sys
import pexpect
import time

Lts_IP='192.168.1.254'
urs='admin'
pwd='admin'

child = pexpect.spawn('ssh -o "StrictHostKeyChecking no" %s@%s' % (urs,Lts_IP))
time.sleep(1)
child.timeout = 20
print('script logging in')
child.expect('password:')
child.sendline(pwd)
print('script logged in')
child.expect(':')
child.sendline('session writelock')
child.expect(':')
print('script  is configuring TE LoopBack')
child.sendline('oam add LoopBack port Network state enable')
child.expect(':')
child.sendline('loopback edit LoopBack state enable  persistent enable filter l2 *default swap-mac enable swap-ip enable swap-port enable')
child.expect(':')
child.sendline('loopback edit LoopBack remote-lpbk-veex enable')
child.expect(':')
child.sendline('media-selection select SFP-A_SFP-B')
child.expect(':')
child.sendline('loopback show LoopBack')
child.expect(':')
print('Congradulation,LoopBack Successfully configured.......')
child.sendline('oam show configuration LoopBack')
child.sendline('exit')







