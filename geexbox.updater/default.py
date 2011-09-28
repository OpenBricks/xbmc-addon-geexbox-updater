# *
# *      Copyright (C) 2011 Team GeeXboX
# *      http://www.geexbox.org
# *
# *  This Program is free software; you can redistribute it and/or modify
# *  it under the terms of the GNU General Public License as published by
# *  the Free Software Foundation; either version 2, or (at your option)
# *  any later version.
# *
# *  This Program is distributed in the hope that it will be useful,
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# *  GNU General Public License for more details.
# *
# *  You should have received a copy of the GNU General Public License
# *  along with XBMC; see the file COPYING.  If not, write to
# *  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# *  http://www.gnu.org/copyleft/gpl.html
# *
# */

import sys
import os
import xbmcaddon

__scriptname__ = "GeeXboX Updater"
__author__     = "Team GeeXboX"
__GUI__        = "Team GeeXboX"
__scriptId__   = "geexbox.updater"
__settings__   = xbmcaddon.Addon(id=__scriptId__)
__language__   = __settings__.getLocalizedString
__version__    = __settings__.getAddonInfo("version")
__cwd__        = __settings__.getAddonInfo('path')

BASE_RESOURCE_PATH = xbmc.translatePath( os.path.join( __cwd__, "resources", "lib" ) )
sys.path.append (BASE_RESOURCE_PATH)

xbmc.output("##### [%s] - Version: %s" % (__scriptname__,__version__,),level=xbmc.LOGDEBUG )

import xbmcgui

_ = sys.modules[ "__main__" ].__language__
__scriptname__ = sys.modules[ "__main__" ].__scriptname__
__version__ = sys.modules[ "__main__" ].__version__
__settings__ = sys.modules[ "__main__" ].__settings__

CONTROL_APPLY = 98
CONTROL_SAVE = 99

EXIT_SCRIPT = ( 9, 10, 247, 275, 61467, )
CANCEL_DIALOG = EXIT_SCRIPT + ( 216, 257, 61448, )

import xbmc, xbmcgui

#get actioncodes from keymap.xml
ACTION_PREVIOUS_MENU = 10

class MyClass(xbmcgui.Window):
  def __init__(self):
    imagelogo = os.path.abspath(os.curdir + '/logo1.png')
    screenx = self.getWidth()
    screeny = self.getHeight()
    self.addControl(xbmcgui.ControlImage(0,0,screenx,screeny, imagelogo))
    self.strActionInfo = xbmcgui.ControlLabel(300, 50, 200, 200, '', 'font16', '0xFFFF00FF')
    self.addControl(self.strActionInfo)
    self.strActionInfo.setLabel('GeeXboX packages')
    self.button0 = xbmcgui.ControlButton(250, 100, 250, 30, "Upgrade packages ...")
    self.addControl(self.button0)
    self.button1 = xbmcgui.ControlButton(250, 200, 250, 30, "Add a package ...")
    self.addControl(self.button1)
    self.button2 = xbmcgui.ControlButton(250, 300, 250, 30, "Remove a package ...")
    self.addControl(self.button2)
    self.button3 = xbmcgui.ControlButton(250, 400, 250, 30, "Exit")
    self.addControl(self.button3)
#    self.addControl(xbmcgui.ControlImage(10,550,267,600, 'logo2.png',aspectRatio=1))
    self.setFocus(self.button0)
    self.button0.controlDown(self.button1)
    self.button1.controlDown(self.button2)
    self.button2.controlDown(self.button3)
    self.button3.controlDown(self.button0)
    self.button0.controlUp(self.button3)
    self.button1.controlUp(self.button0)
    self.button2.controlUp(self.button1)
    self.button3.controlUp(self.button2)

  def execcmd(self, cmd):
    (child_stdin, child_stdout, child_stderr) = os.popen3(cmd)
    stderr = child_stderr.readlines()
    stdout = child_stdout.readlines()
    child_stdin.close()
    child_stdout.close()
    child_stderr.close()
    if stderr ==[]:
      print " Cmd Ok result is %s" % stdout
      print len(stdout)
      return stdout
    else:
      print "Error: %s" % stderr
      return 'error'

  def onAction(self, action):
    if action == ACTION_PREVIOUS_MENU:
      self.close()

  def onControl(self, control):
    if control == self.button0:
      self.execcmd("opkg update")
      tm = self.execcmd("opkg upgrade")
      self.message("".join(tm))
    if control == self.button1:
      tm = self.execcmd("find /root/opkg/ -name *.opk")
      if not tm == 'error' :
        popup = ChildClass2()
        popup .doModal()
        del popup
      else:
        self.message("No package in /root/opkg ! Can't continue ..." )

    if control == self.button2:
      popup = ChildClass()
      popup .doModal()
      del popup
    if control == self.button3:
      self.close()

  def message(self, message):
    dialog = xbmcgui.Dialog()
    dialog.ok(" Info ", message)

class ChildClass(xbmcgui.Window):
  def __init__(self):
    imagelogo = os.path.abspath(os.curdir + '/logo1.png')
    screenx = self.getWidth()
    screeny = self.getHeight()
    self.addControl(xbmcgui.ControlImage(0,0,screenx,screeny, imagelogo))
    self.strActionInfo = xbmcgui.ControlLabel(300, 50, 300, 250, '', 'font18', '0xFFBBFFBB')
    self.addControl(self.strActionInfo)
    self.strActionInfo.setLabel('Select Package to remove')
    tm = self.execcmd("opkg list")
    self.list = xbmcgui.ControlList(200, 150, 300, 400)
    self.addControl(self.list)
    for x in range(len(tm)):
      tm[x] = tm[x].strip()
      self.list.addItem(tm[x])
    self.setFocus(self.list)
    self.buttonexit = xbmcgui.ControlButton(250, 600, 250, 30, "Exit")
    self.addControl(self.buttonexit)
    self.buttonexit.controlRight(self.list)
    self.buttonexit.controlLeft(self.list)
    self.list.controlRight(self.buttonexit)
    self.list.controlLeft(self.buttonexit)

  def execcmd(self, cmd):
    (child_stdin, child_stdout, child_stderr) = os.popen3(cmd)
    stderr = child_stderr.readlines()
    stdout = child_stdout.readlines()
    child_stdin.close()
    child_stdout.close()
    child_stderr.close()
    if stderr ==[]:
      print " Cmd Ok result is %s" % stdout
      print len(stdout)
      return stdout
    else:
      print "Error: %s" % stderr
      return 'error'

  def onControl(self, control):
    if control == self.list:
      item = self.list.getSelectedItem()
      dialog = xbmcgui.Dialog()
      if dialog.yesno("Warning ...", 'Do you really want to remove '+ item.getLabel() + ' ?' ):
        pkg = item.getLabel()
        pkg2 = pkg.split(" ")
        pkg3 = pkg2[0]
        tm = self.execcmd('opkg remove ' + pkg3 )
        print tm
        self.message('You removed : ' + pkg )
        self.close()
    if control == self.buttonexit:
      self.close()

  def message(self, message):
    dialog = xbmcgui.Dialog()
    dialog.ok(" My message title", message)

class ChildClass2(xbmcgui.Window):
  def __init__(self):
    imagelogo = os.path.abspath(os.curdir + '/logo1.png')
    screenx = self.getWidth()
    screeny = self.getHeight()
    self.addControl(xbmcgui.ControlImage(0,0,screenx,screeny, imagelogo))
    self.strActionInfo = xbmcgui.ControlLabel(300, 50, 400, 250, '', 'font18', '0xFFBBFFBB')
    self.addControl(self.strActionInfo)
    self.strActionInfo.setLabel('Select Package to add ...')
    tm = self.execcmd("find /root/opkg/ -name *.opk")
    self.list = xbmcgui.ControlList(200, 150, 300, 400)
    self.addControl(self.list)
    for x in range(len(tm)):
      tm[x] = tm[x].strip()
      self.list.addItem(tm[x])
    self.setFocus(self.list)
    self.buttonexit = xbmcgui.ControlButton(250, 600, 250, 30, "Exit")
    self.addControl(self.buttonexit)
    self.buttonexit.controlRight(self.list)
    self.buttonexit.controlLeft(self.list)
    self.list.controlRight(self.buttonexit)
    self.list.controlLeft(self.buttonexit)

  def execcmd(self, cmd):
    (child_stdin, child_stdout, child_stderr) = os.popen3(cmd)
    stderr = child_stderr.readlines()
    stdout = child_stdout.readlines()
    child_stdin.close()
    child_stdout.close()
    child_stderr.close()
    if stderr ==[]:
      print " Cmd Ok result is %s" % stdout
      print len(stdout)
      return stdout
    else:
      print "Error: %s" % stderr
      return 'error'

  def onControl(self, control):
    if control == self.list:
      item = self.list.getSelectedItem()
      dialog = xbmcgui.Dialog()
      if dialog.yesno("Warning ...", 'Do you really want to Install '+ item.getLabel() + ' ?' ):
        pkg = item.getLabel()
        tm = self.execcmd('opkg install ' + pkg )
        print tm
        self.message('You installed : ' + pkg )
        self.close()
    if control == self.buttonexit:
      self.close()

  def message(self, message):
    dialog = xbmcgui.Dialog()
    dialog.ok(" Info ", message)

mydisplay = MyClass()
mydisplay .doModal()
del mydisplay
