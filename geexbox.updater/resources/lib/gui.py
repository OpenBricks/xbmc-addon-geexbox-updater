import os, sys
import xbmc
import xbmcgui

_ = sys.modules[ "__main__" ].__language__
__scriptname__ = sys.modules[ "__main__" ].__scriptname__
__version__ = sys.modules[ "__main__" ].__version__
__settings__ = sys.modules[ "__main__" ].__settings__


EXIT_SCRIPT = ( 9, 10, 247, 275, 61467, )
CANCEL_DIALOG = EXIT_SCRIPT + ( 216, 257, 61448, )


class GUI( xbmcgui.WindowXMLDialog ):
    
    def __init__( self, *args, **kwargs ):
      
      self.controlId = 0
      self.A = 0
      self.R = 0
      self.choosenrepo = 'GeeXboX repository'
      self.OptionsAdd = ''


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


    def message(self, message):
      dialog = xbmcgui.Dialog()
      dialog.ok(" Info ", message)

    def cleanUi(self):
      if (self.A == 1):
         self.removeControl(self.listA)
         self.removeControl(self.buttonOp)
         self.removeControl(self.buttonRepo)
         self.removeControl(self.strOp)
         self.removeControl(self.strFrom)
         self.removeControl(self.strActionAdd)
         self.A = 0
      if (self.R == 1):
         self.removeControl(self.listR)
         self.removeControl(self.strActionRemove)
         self.R = 0

    def refreshlistA(self):
      self.listA.reset()
      if (self.choosenrepo == '/root/opkg'):
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
      else:
        ll = self.execcmd("opkg list | grep -v '^ ' | grep -v '\-dbg'")
        if len(ll) != 0:
          lstrip = []
          for x in range(len(ll)):
            a = ll[x]
            b = a.split(" ")
            c = b[0]
            lstrip.append(c)
        lli = self.execcmd("opkg list-installed")
        lstrip2 = []
        for x in range(len(lli)):
          a = lli[x]
          b = a.split(" ")
          c = b[0]
          lstrip2.append(c)
        l = [ pkg for pkg in lstrip if pkg not in lstrip2 ]
        if len(l) == 0:
          self.listA.addItem('All packages are installed')
        else:
          for x in range(len(l)):
            l[x] = l[x].strip()
            self.listA.addItem(l[x]) 
      self.setFocus(self.listA)

    def seeLogs(self, txt):
      self.cleanUi()
      self.getControl(30).setVisible(False)
      self.getControl(40).setVisible(False)
      self.getControl(50).setVisible(False)
      self.getControl(60).setVisible(False)
      self.textbox = xbmcgui.ControlTextBox(10, 40, 500, 500, 'font13', textColor='0xFFFFFFFF')
      self.addControl(self.textbox)
      self.buttontext = xbmcgui.ControlButton(350, 550, 100, 40, 'Close')
      self.addControl(self.buttontext)
      self.textbox.setText(txt)
      self.setFocus(self.buttontext)

    def closeLogs(self):
      self.removeControl(self.textbox)
      self.removeControl(self.buttontext)
      self.getControl(30).setVisible(True)
      self.getControl(40).setVisible(True)
      self.getControl(50).setVisible(True)
      self.getControl(60).setVisible(True)
      self.setFocus(self.getControl(60))

##--------- End Script -----------##

    def exit_script( self, restart=False ):
      self.close()

##--------- Click ----------------##

    def onClick( self, controlId ):
     
     if ( controlId == 10 ):
       self.log("Exit")
       self.exit_script()

     if ( controlId == 30 ):
#       self.addControl(self.waitimg)
       self.execcmd("opkg update")
       tm = self.execcmd("opkg upgrade")
#       self.removeControl(self.waitimg)
       self.message('Done')

## Add
     if (controlId == 40):
       self.cleanUi()
       self.buttonOp = xbmcgui.ControlButton(650, 150, 225, 50, "Options")
       self.addControl(self.buttonOp)
#       print self.buttonOp.getId()
       self.buttonRepo = xbmcgui.ControlButton(650, 250, 225, 50, self.choosenrepo)
       self.addControl(self.buttonRepo)
       self.strOp = xbmcgui.ControlLabel(660, 130, 150, 20, 'Options for opkg :', 'font10', '0xFFBBFFBB')
       self.addControl(self.strOp)
       self.strFrom = xbmcgui.ControlLabel(660, 230, 150, 20, 'Binary location :', 'font10', '0xFFBBFFBB')
       self.addControl(self.strFrom)
       self.strActionAdd = xbmcgui.ControlLabel(350, 70, 400, 75, 'Select Package to add ...', 'font18', '0xFFBBFFBB')
       self.addControl(self.strActionAdd)
       self.listA = xbmcgui.ControlList(280, 100, 350, 500, buttonFocusTexture="buttonfocus.png")
       self.addControl(self.listA)
       self.listA.reset()
       self.buttonOp.setNavigation(self.buttonRepo, self.buttonRepo, self.listA, self.listA)
       self.buttonRepo.setNavigation(self.buttonOp, self.buttonOp, self.listA, self.listA)
       self.listA.controlLeft(self.getControl(40))
       self.listA.controlRight(self.buttonRepo)
       self.refreshlistA()
       self.A = 1

## Remove
     if (controlId == 50):
       self.cleanUi()
       self.strActionRemove = xbmcgui.ControlLabel(350, 70, 400, 75, 'Select Package to remove', 'font18', '0xFFBBFFBB')
       self.addControl(self.strActionRemove)
       self.listR = xbmcgui.ControlList(280, 100, 350, 500, buttonFocusTexture="buttonfocus.png")
       self.addControl(self.listR)
       self.listR.reset()
       l = self.execcmd("opkg list-installed")
       for x in range(len(l)):
         l[x] = l[x].strip()
         self.listR.addItem(l[x])
       self.setFocus(self.listR)
       self.listR.controlRight(self.getControl(50))
       self.listR.controlLeft(self.getControl(50))
       self.R = 1

     if (controlId == 60):
       self.log("Exit")
       self.exit_script()

     try:
       if (controlId == self.listR.getId()):
         item = self.listR.getSelectedItem()
         dialog = xbmcgui.Dialog()
         if dialog.yesno("Warning ...", 'Do you really want to remove '+ item.getLabel() + ' ?' ):
           pkg = item.getLabel()
           pkg2 = pkg.split(" ")
           pkg3 = pkg2[0]
       #   self.addControl(self.waitimg)
           tm = self.execcmd('opkg remove ' + pkg3 )
       #   self.removeControl(self.waitimg)
           if tm[0] == 'Collected errors:\n':
             res=''
             for x in range(len(tm)):
               res = res + tm[x]
             self.message('Sorry, You can\'t remove this package !\nSee logs')
             print res
             res = res.replace('print_dependents_warning:','')
             self.cleanUi()
             self.setFocus(self.getControl(50))
             self.seeLogs(res)
           else:
             self.message('You removed : ' + pkg )
             self.cleanUi()
             self.setFocus(self.getControl(50))
     except:
       pass

     try:
       if (controlId == self.buttonRepo.getId()):
         if self.choosenrepo == '/root/opkg':
           self.choosenrepo = 'GeeXboX repositorie'
         else:
           self.choosenrepo = '/root/opkg'
         self.buttonRepo.setLabel(self.choosenrepo)
         self.refreshlistA()
     except:
       pass

     try:
       if (controlId == self.buttonOp.getId()):
         k = xbmc.Keyboard(self.OptionsAdd)
         k.doModal()
         if (k.isConfirmed()):
           self.buttonOp.setLabel(k.getText())
           self.OptionsAdd = k.getText()
     except:
       pass

     try:
       if (controlId == self.listA.getId()):
        item = self.listA.getSelectedItem()
        if not (item.getLabel() == 'No package in /root/opkg' or item.getLabel() == 'All packages are installed'):
          dialog = xbmcgui.Dialog()
          if dialog.yesno("Warning ...", 'Do you really want to Install '+ item.getLabel() + ' ?' ):
            pkg = item.getLabel()
         #   self.addControl(self.waitimg)
            tm = self.execcmd('opkg install ' + self.OptionsAdd + ' ' + pkg )
         #   self.removeControl(self.waitimg)
            if tm[1] == 'Collected errors:\n':
              res=''
              for x in range(len(tm)):
                res = res + tm[x]
              self.message('Sorry, You can\'t add this package !\nSee logs')
              print res
              res = res.replace('check_data_file_clashes:','')
              self.cleanUi()
              self.setFocus(self.getControl(40))
              self.seeLogs(res)
            else:
              self.message('You installed : ' + pkg )
              self.cleanUi()
              self.setFocus(self.getControl(40))
     except:
       pass   

     try:
       if (controlId == self.buttontext.getId()):
         self.closeLogs()
     except:
       pass
        
##--------  Log  ------------##
       
    def log(self, msg):
      xbmc.log("##### [%s] - Debug msg: %s" % (__scriptname__,msg,),level=xbmc.LOGDEBUG )        
        
##--------- End Script ------##
    
    def onAction( self, action ):   
        
      if ( action.getId() in CANCEL_DIALOG ):
        self.log("Exit")
        self.exit_script()


