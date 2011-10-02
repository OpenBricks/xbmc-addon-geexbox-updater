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
ACTION_SELECT_ITEM = 7

class MyClass(xbmcgui.WindowDialog):

  global optionsAdd
  optionsAdd = ''

  def __init__(self):
    imagelogo = os.path.abspath(os.curdir + '/background.png')
    itemFocus = os.path.abspath(os.curdir + '/focus.png')
    screenx = self.getWidth()
    screeny = self.getHeight()
    self.addControl(xbmcgui.ControlImage(50,50,screenx-100,screeny-100, imagelogo))
    self.strActionInfo = xbmcgui.ControlLabel(300, 50, 500, 200, '', 'font24_title', '0xFFFF000F')
    self.addControl(self.strActionInfo)
    self.strActionInfo.setLabel('GeeXboX packages')

    self.button0 = xbmcgui.ControlButton(120, 120, 250, 30, "Upgrade packages ...")
    self.addControl(self.button0)
    self.button1 = xbmcgui.ControlButton(120, 220, 250, 30, "Add a package ...")
    self.addControl(self.button1)
    self.button2 = xbmcgui.ControlButton(120, 320, 250, 30, "Remove a package ...")
    self.addControl(self.button2)
    self.button3 = xbmcgui.ControlButton(120, 420, 250, 30, "Exit")
    self.addControl(self.button3)
    self.button4 = xbmcgui.ControlButton(160, 200, 100, 30, "Options")
    self.addControl(self.button4)
    self.stropt1 = xbmcgui.ControlLabel(160, 170, 300, 250, 'Options for opkg', 'font10', '0xFFBBFFBB')
    self.addControl(self.stropt1)
    self.strActionRemove = xbmcgui.ControlLabel(380, 120, 300, 250, 'Select Package to remove', 'font18', '0xFFBBFFBB')
    self.addControl(self.strActionRemove)
    self.strActionAdd = xbmcgui.ControlLabel(380, 120, 300, 250, 'Select Package to add ...', 'font18', '0xFFBBFFBB')
    self.addControl(self.strActionAdd)
    self.list = xbmcgui.ControlList(380, 150, 300, 400, buttonFocusTexture=itemFocus)
    self.addControl(self.list)
    self.listA = xbmcgui.ControlList(380, 150, 400, 400, buttonFocusTexture=itemFocus)
    self.addControl(self.listA)
    self.buttonexitR = xbmcgui.ControlButton(160, 300, 100, 30, "Exit")
    self.addControl(self.buttonexitR)
    self.buttonexitA = xbmcgui.ControlButton(160, 300, 100, 30, "Exit")
    self.addControl(self.buttonexitA)
    self.strActionRemove.setVisible(False)
    self.buttonexitR.setVisible(False)
    self.list.setVisible(False)
    self.listA.setVisible(False)
    self.strActionAdd.setVisible(False)
    self.buttonexitA.setVisible(False)
    self.button4.setVisible(False)
    self.stropt1.setVisible(False)

    self.basicbutton()

    # Not visible at the beginning
  def ActivatebuttonsR(self):
    l = self.execcmd("opkg list")
    for x in range(len(l)):
      l[x] = l[x].strip()
      self.list.addItem(l[x])
    self.strActionRemove.setVisible(True)
    self.buttonexitR.setVisible(True)
    self.list.setVisible(True)
    self.buttonexitR.controlRight(self.list)
    self.buttonexitR.controlLeft(self.list)
    self.list.controlRight(self.buttonexitR)
    self.list.controlLeft(self.buttonexitR)
    self.setFocus(self.list)
    self.button0.setVisible(False)
    self.button1.setVisible(False)
    self.button2.setVisible(False)
    self.button3.setVisible(False)

  def ActivatebuttonsA(self):
    l = self.execcmd("find /root/opkg/ -name *.opk")
    for x in range(len(l)):
      l[x] = l[x].strip()
      self.listA.addItem(l[x])
    self.strActionAdd.setVisible(True)
    self.buttonexitA.setVisible(True)
    self.listA.setVisible(True)
    self.button4.setVisible(True)
    self.stropt1.setVisible(True)
    self.buttonexitA.controlRight(self.listA)
    self.buttonexitA.controlLeft(self.listA)
    self.buttonexitA.controlUp(self.button4)
    self.buttonexitA.controlDown(self.button4)
    self.button4.controlRight(self.listA)
    self.button4.controlLeft(self.listA)
    self.button4.controlUp(self.buttonexitA)
    self.button4.controlDown(self.buttonexitA)
    self.listA.controlRight(self.buttonexitA)
    self.listA.controlLeft(self.buttonexitA)
    self.setFocus(self.listA)
    self.button0.setVisible(False)
    self.button1.setVisible(False)
    self.button2.setVisible(False)
    self.button3.setVisible(False)

  def basicbutton(self):
    self.button0.setVisible(True)
    self.button1.setVisible(True)
    self.button2.setVisible(True)
    self.button3.setVisible(True)
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
    global optionsAdd
    if control == self.button0:
      self.execcmd("opkg update")
      tm = self.execcmd("opkg upgrade")
      self.message("".join(tm))

    if control == self.button1:
      tm = self.execcmd("find /root/opkg/ -name *.opk")
      if not tm == 'error' :
        self.ActivatebuttonsA()
      else:
        self.message("No package in /root/opkg ! Can't continue ..." )

    if control == self.list:
      item = self.list.getSelectedItem()
      dialog = xbmcgui.Dialog()
      if dialog.yesno("Warning ...", 'Do you really want to remove '+ item.getLabel() + ' ?' ):
        pkg = item.getLabel()
        pkg2 = pkg.split(" ")
        pkg3 = pkg2[0]
        tm = self.execcmd('opkg remove ' + pkg3 )   
        if tm[0] == 'Collected errors:\n':
          print "".join(tm)
          self.message('You can\'t remove this package !\nSee logs')
        else:
          self.message('You removed : ' + pkg )
        self.strActionRemove.setVisible(False)
        self.buttonexitR.setVisible(False)
        self.list.setVisible(False)
        self.list.reset()
        self.basicbutton()

    if control == self.listA:
      item = self.listA.getSelectedItem()
      dialog = xbmcgui.Dialog()
      if dialog.yesno("Warning ...", 'Do you really want to Install '+ item.getLabel() + ' ?' ):
        pkg = item.getLabel()
        tm = self.execcmd('opkg install ' + optionsAdd + ' ' + pkg )
        print tm
        self.message('You installed : ' + pkg )
        self.strActionAdd.setVisible(False)
        self.buttonexitA.setVisible(False)
        self.listA.setVisible(False)
        self.button4.setVisible(False)
        self.stropt1.setVisible(False)
        self.listA.reset()
        self.basicbutton()

    if control == self.buttonexitR:
      self.strActionRemove.setVisible(False)
      self.buttonexitR.setVisible(False)
      self.list.setVisible(False)
      self.basicbutton()

    if control == self.buttonexitA:
      self.strActionAdd.setVisible(False)
      self.buttonexitA.setVisible(False)
      self.button4.setVisible(False)
      self.listA.setVisible(False)
      self.stropt1.setVisible(False)
      self.basicbutton()

    if control == self.button2:
      self.ActivatebuttonsR()
      
    if control == self.button3:
      self.close()

    if control == self.button4:
      k = xbmc.Keyboard()
      k.doModal()
      if (k.isConfirmed()):
        self.button4.setLabel(k.getText())
        optionsAdd = k.getText()

  def message(self, message):
    dialog = xbmcgui.Dialog()
    dialog.ok(" Info ", message)

mydisplay = MyClass()
mydisplay .doModal()
del mydisplay
