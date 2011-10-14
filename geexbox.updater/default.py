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
  global choosenRepo
  optionsAdd = ''
  choosenRepo = '/root/opkg'

  def __init__(self):
    global choosenRepo
    imagelogo = os.path.abspath(os.curdir + '/background.png')
    itemFocus = os.path.abspath(os.curdir + '/focus.png')
    imagewait = os.path.abspath(os.curdir + '/wait.gif')
    screenx = self.getWidth()
    screeny = self.getHeight()
    larg = int(screenx / 3)
    lon = int(screeny / 5 * 4)
    spacex = int(screenx / 24)
    spacey = int(screenx / 24)
    deltax = int(screenx / 48)
    deltay = int(screeny / 48)
    self.addControl(xbmcgui.ControlImage(spacex,spacey,screenx-2*spacex,screeny-2*spacey, imagelogo))
    self.waitimg = xbmcgui.ControlImage(screenx/2-100 ,screeny/2-100,200,200, imagewait)
    self.strActionInfo = xbmcgui.ControlLabel(larg + deltax, 3*deltay, 500, 200, 'GeeXboX packages', 'font24_title', '0xFFFF000F')
    self.addControl(self.strActionInfo)
    self.button0 = xbmcgui.ControlButton(3*deltax, 10*deltay, 250, 30, "Upgrade packages ...")
    self.addControl(self.button0)
    self.button1 = xbmcgui.ControlButton(3*deltax, 15*deltay, 250, 30, "Add a package ...")
    self.addControl(self.button1)
    self.button2 = xbmcgui.ControlButton(3*deltax, 20*deltay, 250, 30, "Remove a package ...")
    self.addControl(self.button2)
    self.button3 = xbmcgui.ControlButton(3*deltax, 25*deltay, 250, 30, "Exit")
    self.addControl(self.button3)
    self.button4 = xbmcgui.ControlButton(4*deltax, 15*deltay, 100, 30, "Options")
    self.addControl(self.button4)
    self.button5 = xbmcgui.ControlButton(4*deltax, 20*deltay, 200, 30, choosenRepo)
    self.addControl(self.button5)
    self.stropt1 = xbmcgui.ControlLabel(4*deltax, 14*deltay, 300, 250, 'Options for opkg :', 'font10', '0xFFBBFFBB')
    self.addControl(self.stropt1)
    self.strFrom = xbmcgui.ControlLabel(4*deltax, 19*deltay, 300, 250, 'Binary location :', 'font10', '0xFFBBFFBB')
    self.addControl(self.strFrom)
    self.strActionRemove = xbmcgui.ControlLabel(larg + 2 * deltax, 6 * deltay, 400, 50, 'Select Package to remove', 'font18', '0xFFBBFFBB')
    self.addControl(self.strActionRemove)
    self.strActionAdd = xbmcgui.ControlLabel(larg + 2 * deltax, 6 * deltay, 400, 50, 'Select Package to add ...', 'font18', '0xFFBBFFBB')
    self.addControl(self.strActionAdd)
    self.list = xbmcgui.ControlList(larg + 4*deltax, 8*deltay, larg, screeny - 10 * deltay, buttonFocusTexture=itemFocus)
    self.addControl(self.list)
    self.listA = xbmcgui.ControlList(larg + 4*deltax, 8*deltay, larg, screeny - 10 * deltay, buttonFocusTexture=itemFocus)
    self.addControl(self.listA)
    self.listA2 = xbmcgui.ControlList(larg + 4*deltax, 8*deltay, larg, screeny - 10 * deltay, buttonFocusTexture=itemFocus)
    self.addControl(self.listA2)
    self.buttonexitR = xbmcgui.ControlButton(4*deltax, 25*deltay, 100, 30, "Exit")
    self.addControl(self.buttonexitR)
    self.buttonexitA = xbmcgui.ControlButton(4*deltax, 25*deltay, 100, 30, "Exit")
    self.addControl(self.buttonexitA)
    self.strActionRemove.setVisible(False)
    self.buttonexitR.setVisible(False)
    self.list.setVisible(False)
    self.listA.setVisible(False)
    self.listA2.setVisible(False)
    self.strActionAdd.setVisible(False)
    self.buttonexitA.setVisible(False)
    self.button4.setVisible(False)
    self.button5.setVisible(False)
    self.stropt1.setVisible(False)
    self.strFrom.setVisible(False)

    self.textbox = xbmcgui.ControlTextBox(5*deltax, 8*deltay, screenx - 10*deltax, screeny - 14*deltay, 'font13', textColor='0xFFFFFFFF')
    self.addControl(self.textbox)
    self.buttontext = xbmcgui.ControlButton(screenx - 10*deltax, screeny - 10*deltay, 200, 30, 'Close')
    self.addControl(self.buttontext)
    self.textbox.setVisible(False)
    self.buttontext.setVisible(False)

    self.basicbutton()

    # Not visible at the beginning
  def ActivatebuttonsR(self):
    l = self.execcmd("opkg list-installed")
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
    global choosenRepo
    self.listA.reset()
    self.listA2.reset()
    l = self.execcmd("find /root/opkg/ -name *.opk")

    if not l == 'error' :  
      if len(l) == 0:
        self.listA.addItem('No package in /root/opkg')
      else:
        for x in range(len(l)):
          l[x] = l[x].strip()
          self.listA.addItem(l[x])
    else:
      self.listA.addItem('No package in /root/opkg')

    ll = self.execcmd("opkg list")
    lli = self.execcmd("opkg list-installed")
    l2 = [ pkg for pkg in ll if pkg not in lli ]
    if len(l2) == 0:
      self.listA2.addItem('All packages are installed')
#    l2 = self.execcmd("opkg list")
    else:
      for x in range(len(l2)):
        l2[x] = l2[x].strip()
        self.listA2.addItem(l2[x])

    self.strActionAdd.setVisible(True)
    self.buttonexitA.setVisible(True)
    self.button4.setVisible(True)
    self.button5.setVisible(True)
    self.stropt1.setVisible(True)
    self.strFrom.setVisible(True)
    self.button0.setVisible(False)
    self.button1.setVisible(False)
    self.button2.setVisible(False)
    self.button3.setVisible(False)
    if choosenRepo == '/root/opkg':
      self.listA2.setVisible(False)
      self.listA.setVisible(True)
      self.setFocus(self.listA)
       # setNavigation(up, down, left, right)
      self.button4.setNavigation(self.buttonexitA, self.button5, self.listA, self.listA)
      self.button5.setNavigation(self.button4, self.buttonexitA, self.listA, self.listA)
      self.buttonexitA.setNavigation(self.button5, self.button4, self.listA, self.listA)
      self.listA.controlRight(self.buttonexitA)
      self.listA.controlLeft(self.buttonexitA)
    else:
      self.listA.setVisible(False)
      self.listA2.setVisible(True)
      self.setFocus(self.listA2)
       # setNavigation(up, down, left, right)
      self.button4.setNavigation(self.buttonexitA, self.button5, self.listA2, self.listA2)
      self.button5.setNavigation(self.button4, self.buttonexitA, self.listA2, self.listA2)
      self.buttonexitA.setNavigation(self.button5, self.button4, self.listA2, self.listA2)
      self.listA2.controlRight(self.buttonexitA)
      self.listA2.controlLeft(self.buttonexitA)

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
      return stdout
    else:
      print "Error: %s" % stderr
      return 'error'

  def onAction(self, action):
    if action == ACTION_PREVIOUS_MENU:
      self.close()

  def onControl(self, control):
    global optionsAdd
    global choosenRepo
    if control == self.button0:
      self.addControl(self.waitimg)
      self.execcmd("opkg update")
      tm = self.execcmd("opkg upgrade")
      self.removeControl(self.waitimg)
      self.message('Done')

    if control == self.button1:
      self.ActivatebuttonsA()

    if control == self.list:
      item = self.list.getSelectedItem()
      dialog = xbmcgui.Dialog()
      if dialog.yesno("Warning ...", 'Do you really want to remove '+ item.getLabel() + ' ?' ):
        pkg = item.getLabel()
        pkg2 = pkg.split(" ")
        pkg3 = pkg2[0]
        self.addControl(self.waitimg)
        tm = self.execcmd('opkg remove ' + pkg3 )
        self.removeControl(self.waitimg)
        if tm[0] == 'Collected errors:\n':
          res=''
          for x in range(len(tm)):
            res = res + tm[x]
          self.message('Sorry, You can\'t remove this package !\nSee logs')
          print res
          res = res.replace('print_dependents_warning:','')
          self.strActionRemove.setVisible(False)
          self.buttonexitR.setVisible(False)
          self.list.setVisible(False)
          self.list.reset()
          self.seeLogs(res)
        else:
          self.message('You removed : ' + pkg )
          self.strActionRemove.setVisible(False)
          self.buttonexitR.setVisible(False)
          self.list.setVisible(False)
          self.list.reset()
          self.basicbutton()

    if control == self.listA:
      item = self.listA.getSelectedItem()
      if item.getLabel() != 'No package in /root/opkg':
        dialog = xbmcgui.Dialog()
        if dialog.yesno("Warning ...", 'Do you really want to Install '+ item.getLabel() + ' ?' ):
          pkg = item.getLabel()
          self.addControl(self.waitimg)
          tm = self.execcmd('opkg install ' + optionsAdd + ' ' + pkg )
          self.removeControl(self.waitimg)
 #         print tm
          if tm[1] == 'Collected errors:\n':
            res=''
            for x in range(len(tm)):
              res = res + tm[x]
            self.message('Sorry, You can\'t add this package !\nSee logs')
            print res
            res = res.replace('check_data_file_clashes:','')
            self.strActionAdd.setVisible(False)
            self.buttonexitA.setVisible(False)
            self.listA.setVisible(False)
            self.button4.setVisible(False)
            self.button5.setVisible(False)
            self.stropt1.setVisible(False)
            self.strFrom.setVisible(False)
            self.listA.reset()
            self.listA2.reset()
            self.listA.reset()
            self.seeLogs(res)
          else:
            self.message('You installed : ' + pkg )
            self.strActionAdd.setVisible(False)
            self.buttonexitA.setVisible(False)
            self.listA.setVisible(False)
            self.button4.setVisible(False)
            self.button5.setVisible(False)
            self.stropt1.setVisible(False)
            self.strFrom.setVisible(False)
            self.listA.reset()
            self.listA2.reset()
            self.basicbutton()

    if control == self.listA2:
      item = self.listA2.getSelectedItem()
      if item.getLabel() != 'All packages are installed':
        dialog = xbmcgui.Dialog()
        if dialog.yesno("Warning ...", 'Do you really want to Install '+ item.getLabel() + ' ?' ):
          pkg = item.getLabel()
          self.addControl(self.waitimg)
          tm = self.execcmd('opkg install ' + optionsAdd + ' ' + pkg )
          self.removeControl(self.waitimg)
#          print tm
          if tm[1] == 'Collected errors:\n':
            res=''
            for x in range(len(tm)):
              res = res + tm[x]
            self.message('Sorry, You can\'t add this package !\nSee logs')
            print res
            res = res.replace('check_data_file_clashes:','')
            self.strActionAdd.setVisible(False)
            self.buttonexitA.setVisible(False)
            self.listA2.setVisible(False)
            self.button4.setVisible(False)
            self.button5.setVisible(False)
            self.stropt1.setVisible(False)
            self.strFrom.setVisible(False)
            self.listA.reset()
            self.listA2.reset()
            self.listA.reset()
            self.seeLogs(res)
          else:
            self.message('You installed : ' + pkg )
            self.strActionAdd.setVisible(False)
            self.buttonexitA.setVisible(False)
            self.listA2.setVisible(False)
            self.button4.setVisible(False)
            self.button5.setVisible(False)
            self.stropt1.setVisible(False)
            self.strFrom.setVisible(False)
            self.listA.reset()
            self.listA2.reset()
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
      self.button5.setVisible(False)
      self.listA.setVisible(False)
      self.listA2.setVisible(False)
      self.stropt1.setVisible(False)
      self.strFrom.setVisible(False)
      self.basicbutton()

    if control == self.button2:
      self.ActivatebuttonsR()
      
    if control == self.button3:
      self.close()

    if control == self.button4:
      k = xbmc.Keyboard(optionsAdd)
      k.doModal()
      if (k.isConfirmed()):
        self.button4.setLabel(k.getText())
        optionsAdd = k.getText()

    if control == self.button5:
      if choosenRepo == '/root/opkg':
        choosenRepo = 'GeeXboX repositorie'
      else:
        choosenRepo = '/root/opkg'
      self.button5.setLabel(choosenRepo)
      self.ActivatebuttonsA()

    if control == self.buttontext:
       self.textbox.setVisible(False)
       self.buttontext.setVisible(False)
       self.textbox.reset()
       self.basicbutton()

  def message(self, message):
    dialog = xbmcgui.Dialog()
    dialog.ok(" Info ", message)

  def seeLogs(self, txt):
    self.textbox.setText(txt)
    self.textbox.setVisible(True)
    self.buttontext.setVisible(True)
    self.setFocus(self.buttontext)
    

mydisplay = MyClass()
mydisplay .doModal()
del mydisplay
