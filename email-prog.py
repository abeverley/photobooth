#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import wx
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.image import MIMEImage		
from subprocess import Popen, PIPE
import sqlite3
import glob, time

def sendmail( to ):
  msg = MIMEMultipart()
  msg['From'] = 'A & M Photobooth <m@rkbev.com>'
  msg['To'] = to
  msg['Subject'] = "Your photobooth pic!"
  body = "Enjoy the photos :)"

  img = MIMEImage(open("/home/abeverley/git/photobooth/photo.jpg", "rb").read())
  img.add_header('Content-Disposition', 'attchment; filename="photobooth.jpg"')
  msg.attach(img)

  msg.attach(MIMEText(body, 'plain'))

  p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)
  p.communicate(msg.as_string()) 

def button_code( self, num ):
  con = sqlite3.connect('email_list.db')
  c = con.cursor() 
  c.execute('SELECT email FROM emails ORDER BY name LIMIT ?,1', (num,))  
  a = c.fetchone()  
  b = str(a[0])
  sendmail( b )
  dlg = wx.MessageDialog(self, "Email has been sent!", "Notification", wx.OK)
  result = dlg.ShowModal()
  dlg.Destroy()

def db_name( self, num ):
  con = sqlite3.connect('email_list.db')
  c = con.cursor() 
  c.execute('SELECT name FROM emails ORDER BY name LIMIT ?,1', (num,))  
  a = c.fetchone()
  a = str(a[0])
  con.close()
  return a

class simpleapp_wx(wx.Frame):
  def __init__(self,parent,id,title):	
    wx.Frame.__init__(self,parent,id,title)
    self.parent = parent
    self.initialize()
	
  def initialize(self):

    self.sizer = wx.GridBagSizer() 

    self.label = wx.StaticText(self,-1,label=u'Click on your name to email yourself the photo')
    label_font = wx.Font(32, wx.DECORATIVE, wx.ITALIC, wx.BOLD)
    self.label.SetFont(label_font)
    self.sizer.Add(self.label,(0,0),(1,8),wx.EXPAND)	
 
    # Set font to be used for buttons:
    button_font = wx.Font(28, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)

    self.timer = wx.Timer(self)
    self.Bind(wx.EVT_TIMER, self.update, self.timer)
    
    self.MaxImageSize = 800

    self.Image = wx.StaticBitmap(self, bitmap=wx.EmptyBitmap(self.MaxImageSize, self.MaxImageSize))    
    self.timer.Start(1000)
 

    a = db_name(self,1)
    b = db_name(self,2)
    c = db_name(self,3)
#    d = db_name(self,4)
#    e = db_name(self,5)
#    f = db_name(self,6)
#    g = db_name(self,7)
#    h = db_name(self,8)
#    i = db_name(self,9)
#    j = db_name(self,10)
#    k = db_name(self,11)
#    l = db_name(self,12)
#    m = db_name(self,13)
#    n = db_name(self,14)
#    o = db_name(self,15)
#    p = db_name(self,16)
#    q = db_name(self,17)
#    r = db_name(self,18)
#    s = db_name(self,19)
#    t = db_name(self,20)
#    u = db_name(self,21)
#    v = db_name(self,22)
#    w = db_name(self,23)
#    x = db_name(self,24)
#    y = db_name(self,25)
#    z = db_name(self,26)
#    aa = db_name(self,27)
#    ab = db_name(self,28)
#    ac = db_name(self,29)
#    ad = db_name(self,30)
#    ae = db_name(self,31)
#    af = db_name(self,32)
#    ag = db_name(self,33)
#    ah = db_name(self,34)
#    ai = db_name(self,35)
#    aj = db_name(self,36)
#    ak = db_name(self,37)
#    al = db_name(self,38)
#    am = db_name(self,39)
#    an = db_name(self,40)
#    ao = db_name(self,41)
#    ap = db_name(self,42)
#    aq = db_name(self,43)
#    ar = db_name(self,44)
#    at = db_name(self,45)
#    au = db_name(self,46)
#    av = db_name(self,47)
#    aw = db_name(self,48)
#    ax = db_name(self,49)
#    ay = db_name(self,50)
#    az = db_name(self,51)
#    ba = db_name(self,52)
#    bb = db_name(self,53)
#    bc = db_name(self,54)
#    bd = db_name(self,55)
#    be = db_name(self,56)
#    bf = db_name(self,57)
#    bg = db_name(self,58)
#    bh = db_name(self,59)
#    bi = db_name(self,60)
#    bj = db_name(self,61)
#    bk = db_name(self,62)
#    bl = db_name(self,63)
#    bm = db_name(self,64)
#    bn = db_name(self,65)
#    bo = db_name(self,66)
#    bp = db_name(self,67)
#    bq = db_name(self,68)
#    br = db_name(self,69)
#    bs = db_name(self,70)
#    bt = db_name(self,71)
#    bu = db_name(self,72)
#    bv = db_name(self,73)
#    bw = db_name(self,74)
#    bx = db_name(self,75)
#    by = db_name(self,76)
#    bz = db_name(self,77)
#    ca = db_name(self,78)
#    cb = db_name(self,79)
#    cc = db_name(self,80)
#    cd = db_name(self,81)

    button1 = wx.Button(self,-1,label=a)
    button2 = wx.Button(self,-1,label=b)
    button3 = wx.Button(self,-1,label=c)
#    button4 = wx.Button(self,-1,label=d)
#    button5 = wx.Button(self,-1,label=e)
#    button6 = wx.Button(self,-1,label=f)
#    button7 = wx.Button(self,-1,label=g)
#    button8 = wx.Button(self,-1,label=h)
#    button9 = wx.Button(self,-1,label=i)
#    button10 = wx.Button(self,-1,label=j)
#    button11 = wx.Button(self,-1,label=k)
#    button12 = wx.Button(self,-1,label=l)
#    button13 = wx.Button(self,-1,label=m)
#    button14 = wx.Button(self,-1,label=n)
#    button15 = wx.Button(self,-1,label=o)
#    button16 = wx.Button(self,-1,label=p)
#    button17 = wx.Button(self,-1,label=q)
#    button18 = wx.Button(self,-1,label=r)
#    button19 = wx.Button(self,-1,label=s)
#    button20 = wx.Button(self,-1,label=t)
#    button21 = wx.Button(self,-1,label=u)
#    button22 = wx.Button(self,-1,label=v)
#    button23 = wx.Button(self,-1,label=w)
#    button24 = wx.Button(self,-1,label=x)
#    button25 = wx.Button(self,-1,label=y)
#    button26 = wx.Button(self,-1,label=z)
#    button27 = wx.Button(self,-1,label=aa)
#    button28 = wx.Button(self,-1,label=ab)
#    button29 = wx.Button(self,-1,label=ac)
#    button30 = wx.Button(self,-1,label=ad)
#    button31 = wx.Button(self,-1,label=ae)
#    button32 = wx.Button(self,-1,label=af)
#    button33 = wx.Button(self,-1,label=ag)
#    button34 = wx.Button(self,-1,label=ah)
#    button35 = wx.Button(self,-1,label=ai)
#    button36 = wx.Button(self,-1,label=aj)
#    button37 = wx.Button(self,-1,label=ak)
#    button38 = wx.Button(self,-1,label=al)
#    button39 = wx.Button(self,-1,label=am)
#    button40 = wx.Button(self,-1,label=an)
#    button41 = wx.Button(self,-1,label=ao)
#    button42 = wx.Button(self,-1,label=ap)
#    button43 = wx.Button(self,-1,label=aq)
#    button44 = wx.Button(self,-1,label=ar)
#    button45 = wx.Button(self,-1,label=at)
#    button46 = wx.Button(self,-1,label=au)
#    button47 = wx.Button(self,-1,label=av)
#    button48 = wx.Button(self,-1,label=aw)
#    button49 = wx.Button(self,-1,label=ax)
#    button50 = wx.Button(self,-1,label=ay)
#    button51 = wx.Button(self,-1,label=az)
#    button52 = wx.Button(self,-1,label=ba)
#    button53 = wx.Button(self,-1,label=bb)
#    button54 = wx.Button(self,-1,label=bc)
#    button55 = wx.Button(self,-1,label=bd)
#    button56 = wx.Button(self,-1,label=be)
#    button57 = wx.Button(self,-1,label=bf)
#    button58 = wx.Button(self,-1,label=bg)
#    button59 = wx.Button(self,-1,label=bh)
#    button60 = wx.Button(self,-1,label=bi)
#    button61 = wx.Button(self,-1,label=bj)
#    button62 = wx.Button(self,-1,label=bk)
#    button63 = wx.Button(self,-1,label=bl)
#    button64 = wx.Button(self,-1,label=bm)
#    button65 = wx.Button(self,-1,label=bn)
#    button66 = wx.Button(self,-1,label=bo)
#    button67 = wx.Button(self,-1,label=bp)
#    button68 = wx.Button(self,-1,label=bq)
#    button69 = wx.Button(self,-1,label=br)
#    button70 = wx.Button(self,-1,label=bs)
#    button71 = wx.Button(self,-1,label=bt)
#    button72 = wx.Button(self,-1,label=bu)
#    button73 = wx.Button(self,-1,label=bv)
#    button74 = wx.Button(self,-1,label=bw)
#    button75 = wx.Button(self,-1,label=bx)
#    button76 = wx.Button(self,-1,label=by)
#    button77 = wx.Button(self,-1,label=bz)
#    button78 = wx.Button(self,-1,label=ca)
#    button79 = wx.Button(self,-1,label=cb)
#    button80 = wx.Button(self,-1,label=cc)
#    button81 = wx.Button(self,-1,label=cd)

    self.sizer.Add(button1,(1,0),(1,1),wx.EXPAND)
    self.sizer.Add(button2,(1,1),(1,1),wx.EXPAND)
    self.sizer.Add(button3,(1,2),(1,1),wx.EXPAND)
#    self.sizer.Add(button4,(1,3),(1,1),wx.EXPAND)
#    self.sizer.Add(button5,(1,4),(1,1),wx.EXPAND)
#    self.sizer.Add(button6,(1,5),(1,1),wx.EXPAND)
#    self.sizer.Add(button7,(2,0),(1,1),wx.EXPAND)
#    self.sizer.Add(button8,(2,1),(1,1),wx.EXPAND)
#    self.sizer.Add(button9,(2,2),(1,1),wx.EXPAND)
#    self.sizer.Add(button10,(2,3),(1,1),wx.EXPAND)
#    self.sizer.Add(button11,(2,4),(1,1),wx.EXPAND)
#    self.sizer.Add(button12,(2,5),(1,1),wx.EXPAND)
#    self.sizer.Add(button13,(3,0),(1,1),wx.EXPAND)
#    self.sizer.Add(button14,(3,1),(1,1),wx.EXPAND)
#    self.sizer.Add(button15,(3,2),(1,1),wx.EXPAND)
#    self.sizer.Add(button16,(3,3),(1,1),wx.EXPAND)
#    self.sizer.Add(button17,(3,4),(1,1),wx.EXPAND)
#    self.sizer.Add(button18,(3,5),(1,1),wx.EXPAND)
#    self.sizer.Add(button19,(4,0),(1,1),wx.EXPAND)
#    self.sizer.Add(button20,(4,1),(1,1),wx.EXPAND)
#    self.sizer.Add(button21,(4,2),(1,1),wx.EXPAND)
#    self.sizer.Add(button22,(4,3),(1,1),wx.EXPAND)
#    self.sizer.Add(button23,(4,4),(1,1),wx.EXPAND)
#    self.sizer.Add(button24,(4,5),(1,1),wx.EXPAND)
#    self.sizer.Add(button25,(5,0),(1,1),wx.EXPAND)
#    self.sizer.Add(button26,(5,1),(1,1),wx.EXPAND)
#    self.sizer.Add(button27,(5,2),(1,1),wx.EXPAND)
#    self.sizer.Add(button28,(5,3),(1,1),wx.EXPAND)
#    self.sizer.Add(button29,(5,4),(1,1),wx.EXPAND)
#    self.sizer.Add(button30,(5,5),(1,1),wx.EXPAND)
#    self.sizer.Add(button31,(6,0),(1,1),wx.EXPAND)
#    self.sizer.Add(button32,(6,1),(1,1),wx.EXPAND)
#    self.sizer.Add(button33,(6,2),(1,1),wx.EXPAND)
#    self.sizer.Add(button34,(6,3),(1,1),wx.EXPAND)
#    self.sizer.Add(button35,(6,4),(1,1),wx.EXPAND)
#    self.sizer.Add(button36,(6,5),(1,1),wx.EXPAND)
#    self.sizer.Add(button37,(7,0),(1,1),wx.EXPAND)
#    self.sizer.Add(button38,(7,1),(1,1),wx.EXPAND)
#    self.sizer.Add(button39,(7,2),(1,1),wx.EXPAND)
#    self.sizer.Add(button40,(7,3),(1,1),wx.EXPAND)
#    self.sizer.Add(button41,(7,4),(1,1),wx.EXPAND)
#    self.sizer.Add(button42,(7,5),(1,1),wx.EXPAND)
#    self.sizer.Add(button43,(8,0),(1,1),wx.EXPAND)
#    self.sizer.Add(button44,(8,1),(1,1),wx.EXPAND)
#    self.sizer.Add(button45,(8,2),(1,1),wx.EXPAND)
#    self.sizer.Add(button46,(8,3),(1,1),wx.EXPAND)
#    self.sizer.Add(button47,(8,4),(1,1),wx.EXPAND)
#    self.sizer.Add(button48,(8,5),(1,1),wx.EXPAND)
#    self.sizer.Add(button49,(9,0),(1,1),wx.EXPAND)
#    self.sizer.Add(button50,(9,1),(1,1),wx.EXPAND)
#    self.sizer.Add(button51,(9,2),(1,1),wx.EXPAND)
#    self.sizer.Add(button52,(9,3),(1,1),wx.EXPAND)
#    self.sizer.Add(button53,(9,4),(1,1),wx.EXPAND)
#    self.sizer.Add(button54,(9,5),(1,1),wx.EXPAND)
#    self.sizer.Add(button55,(10,0),(1,1),wx.EXPAND)
#    self.sizer.Add(button56,(10,1),(1,1),wx.EXPAND)
#    self.sizer.Add(button57,(10,2),(1,1),wx.EXPAND)
#    self.sizer.Add(button58,(10,3),(1,1),wx.EXPAND)
#    self.sizer.Add(button59,(10,4),(1,1),wx.EXPAND)
#    self.sizer.Add(button60,(10,5),(1,1),wx.EXPAND)
#    self.sizer.Add(button61,(11,0),(1,1),wx.EXPAND)
#    self.sizer.Add(button62,(11,1),(1,1),wx.EXPAND)
#    self.sizer.Add(button63,(11,2),(1,1),wx.EXPAND)
#    self.sizer.Add(button64,(11,3),(1,1),wx.EXPAND)
#    self.sizer.Add(button65,(11,4),(1,1),wx.EXPAND)
#    self.sizer.Add(button66,(11,5),(1,1),wx.EXPAND)
#    self.sizer.Add(button67,(12,0),(1,1),wx.EXPAND)
#    self.sizer.Add(button68,(12,1),(1,1),wx.EXPAND)
#    self.sizer.Add(button69,(12,2),(1,1),wx.EXPAND)
#    self.sizer.Add(button70,(12,3),(1,1),wx.EXPAND)
#    self.sizer.Add(button71,(12,4),(1,1),wx.EXPAND)
#    self.sizer.Add(button72,(12,5),(1,1),wx.EXPAND)
#    self.sizer.Add(button73,(13,0),(1,1),wx.EXPAND)
#    self.sizer.Add(button74,(13,1),(1,1),wx.EXPAND)
#    self.sizer.Add(button75,(13,2),(1,1),wx.EXPAND)
#    self.sizer.Add(button76,(13,3),(1,1),wx.EXPAND)
#    self.sizer.Add(button77,(13,4),(1,1),wx.EXPAND)
#    self.sizer.Add(button78,(13,5),(1,1),wx.EXPAND)
#    self.sizer.Add(button79,(14,0),(1,1),wx.EXPAND)
#    self.sizer.Add(button80,(14,1),(1,1),wx.EXPAND)
#    self.sizer.Add(button81,(14,2),(1,1),wx.EXPAND)
    self.Bind(wx.EVT_BUTTON, self.OnButtonClick1, button1)
    self.Bind(wx.EVT_BUTTON, self.OnButtonClick2, button2)
    self.Bind(wx.EVT_BUTTON, self.OnButtonClick3, button3)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick4, button4)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick5, button5)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick6, button6)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick7, button7)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick8, button8)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick9, button9)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick10, button10)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick11, button11)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick12, button12)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick13, button13)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick14, button14)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick15, button15)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick16, button16)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick17, button17)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick18, button18)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick19, button19)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick20, button20)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick21, button21)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick22, button22)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick23, button23)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick24, button24)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick25, button25)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick26, button26)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick27, button27)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick28, button28)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick29, button29)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick30, button30)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick31, button31)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick32, button32)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick33, button33)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick34, button34)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick35, button35)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick36, button36)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick37, button37)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick38, button38)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick39, button39)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick40, button40)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick41, button41)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick42, button42)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick43, button43)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick44, button44)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick45, button45)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick46, button46)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick47, button47)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick48, button48)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick49, button49)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick50, button50)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick51, button51)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick52, button52)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick53, button53)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick54, button54)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick55, button55)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick56, button56)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick57, button57)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick58, button58)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick59, button59)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick60, button60)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick61, button61)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick62, button62)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick63, button63)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick64, button64)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick65, button65)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick66, button66)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick67, button67)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick68, button68)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick69, button69)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick70, button70)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick71, button71)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick72, button72)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick73, button73)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick74, button74)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick75, button75)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick76, button76)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick77, button77)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick78, button78)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick79, button79)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick80, button80)
#    self.Bind(wx.EVT_BUTTON, self.OnButtonClick81, button81)
#
    button1.SetFont(button_font)
    button2.SetFont(button_font)
    button3.SetFont(button_font)
#    button4.SetFont(button_font)
#    button5.SetFont(button_font)
#    button6.SetFont(button_font)
#    button7.SetFont(button_font)
#    button8.SetFont(button_font)
#    button9.SetFont(button_font)
#    button10.SetFont(button_font)
#    button11.SetFont(button_font)
#    button12.SetFont(button_font)
#    button13.SetFont(button_font)
#    button14.SetFont(button_font)
#    button15.SetFont(button_font)
#    button16.SetFont(button_font)
#    button17.SetFont(button_font)
#    button18.SetFont(button_font)
#    button19.SetFont(button_font)
#    button20.SetFont(button_font)
#    button21.SetFont(button_font)
#    button22.SetFont(button_font)
#    button23.SetFont(button_font)
#    button24.SetFont(button_font)
#    button25.SetFont(button_font)
#    button26.SetFont(button_font)
#    button27.SetFont(button_font)
#    button28.SetFont(button_font)
#    button29.SetFont(button_font)
#    button30.SetFont(button_font)
#    button31.SetFont(button_font)
#    button32.SetFont(button_font)
#    button33.SetFont(button_font)
#    button34.SetFont(button_font)
#    button35.SetFont(button_font)
#    button36.SetFont(button_font)
#    button37.SetFont(button_font)
#    button38.SetFont(button_font)
#    button39.SetFont(button_font)
#    button40.SetFont(button_font)
#    button41.SetFont(button_font)
#    button42.SetFont(button_font)
#    button43.SetFont(button_font)
#    button44.SetFont(button_font)
#    button45.SetFont(button_font)
#    button46.SetFont(button_font)
#    button47.SetFont(button_font)
#    button48.SetFont(button_font)
#    button49.SetFont(button_font)
#    button50.SetFont(button_font)
#    button51.SetFont(button_font)
#    button52.SetFont(button_font)
#    button53.SetFont(button_font)
#    button54.SetFont(button_font)
#    button55.SetFont(button_font)
#    button56.SetFont(button_font)
#    button57.SetFont(button_font)
#    button58.SetFont(button_font)
#    button59.SetFont(button_font)
#    button60.SetFont(button_font)
#    button61.SetFont(button_font)
#    button62.SetFont(button_font)
#    button63.SetFont(button_font)
#    button64.SetFont(button_font)
#    button65.SetFont(button_font)
#    button66.SetFont(button_font)
#    button67.SetFont(button_font)
#    button68.SetFont(button_font)
#    button69.SetFont(button_font)
#    button70.SetFont(button_font)
#    button71.SetFont(button_font)
#    button72.SetFont(button_font)
#    button73.SetFont(button_font)
#    button74.SetFont(button_font)
#    button75.SetFont(button_font)
#    button76.SetFont(button_font)
#    button77.SetFont(button_font)
#    button78.SetFont(button_font)
#    button79.SetFont(button_font)
#    button80.SetFont(button_font)
#    button81.SetFont(button_font)
#
    self.sizer.Add(self.Image,(2,6),(15,3),wx.EXPAND | wx.LEFT, 20)
    self.sizer.AddGrowableCol(0)
    self.SetSizerAndFit(self.sizer)
    self.SetSizeHints(self.GetSize().x,self.GetSize().y,self.GetSize().x,self.GetSize().y);
    self.Show(True)

  def update(self, event):
    # load the image
    Img = wx.Image('/home/abeverley/git/photobooth/photo.jpg', wx.BITMAP_TYPE_JPEG)

    # scale the image, preserving the aspect ratio
    W = Img.GetWidth()
    H = Img.GetHeight()
    if W > H:
      NewW = self.MaxImageSize
      NewH = self.MaxImageSize * H / W
    else:
      NewH = self.MaxImageSize
      NewW = self.MaxImageSize * W / H
    Img = Img.Scale(NewW,NewH)
 
    # convert it to a wx.Bitmap, and put it on the wx.StaticBitmap
    self.Image.SetBitmap(wx.BitmapFromImage(Img))

    # You can fit the frame to the image, if you want.
    #self.Fit()
    #self.Layout()

    self.Refresh()

  def OnButtonClick1(self,event):
    button_code(self, 1)

  def OnButtonClick2(self,event):
    button_code(self, 2)

  def OnButtonClick3(self,event):
    button_code(self, 3)

  def OnButtonClick4(self,event):
    button_code(self, 4)

  def OnButtonClick5(self,event):
    button_code(self, 5)

  def OnButtonClick6(self,event):
    button_code(self, 6)

  def OnButtonClick7(self,event):
    button_code(self, 7)

  def OnButtonClick8(self,event):
    button_code(self, 8)

  def OnButtonClick9(self,event):
    button_code(self, 9)

  def OnButtonClick10(self,event):
    button_code(self, 10)

  def OnButtonClick11(self,event):
    button_code(self, 11)

  def OnButtonClick12(self,event):
    button_code(self, 12)

  def OnButtonClick13(self,event):
    button_code(self, 13)

  def OnButtonClick14(self,event):
    button_code(self, 14)

  def OnButtonClick15(self,event):
    button_code(self, 15)

  def OnButtonClick16(self,event):
    button_code(self, 16)

  def OnButtonClick17(self,event):
    button_code(self, 17)

  def OnButtonClick18(self,event):
    button_code(self, 18)

  def OnButtonClick19(self,event):
    button_code(self, 19)

  def OnButtonClick20(self,event):
    button_code(self, 20)

  def OnButtonClick21(self,event):
    button_code(self, 21)

  def OnButtonClick22(self,event):
    button_code(self, 22)

  def OnButtonClick23(self,event):
    button_code(self, 23)

  def OnButtonClick24(self,event):
    button_code(self, 24)

  def OnButtonClick25(self,event):
    button_code(self, 25)

  def OnButtonClick26(self,event):
    button_code(self, 26)

  def OnButtonClick27(self,event):
    button_code(self, 27)

  def OnButtonClick28(self,event):
    button_code(self, 28)

  def OnButtonClick29(self,event):
    button_code(self, 29)

  def OnButtonClick30(self,event):
    button_code(self, 30)

  def OnButtonClick31(self,event):
    button_code(self, 31)

  def OnButtonClick32(self,event):
    button_code(self, 32)

  def OnButtonClick33(self,event):
    button_code(self, 33)

  def OnButtonClick34(self,event):
    button_code(self, 34)

  def OnButtonClick35(self,event):
    button_code(self, 35)

  def OnButtonClick36(self,event):
    button_code(self, 36)

  def OnButtonClick37(self,event):
    button_code(self, 37)

  def OnButtonClick38(self,event):
    button_code(self, 38)

  def OnButtonClick39(self,event):
    button_code(self, 39)

  def OnButtonClick40(self,event):
    button_code(self, 40)

  def OnButtonClick41(self,event):
    button_code(self, 41)

  def OnButtonClick42(self,event):
    button_code(self, 42)

  def OnButtonClick43(self,event):
    button_code(self, 43)

  def OnButtonClick44(self,event):
    button_code(self, 44)

  def OnButtonClick45(self,event):
    button_code(self, 45)

  def OnButtonClick46(self,event):
    button_code(self, 46)

  def OnButtonClick47(self,event):
    button_code(self, 47)

  def OnButtonClick48(self,event):
    button_code(self, 48)

  def OnButtonClick49(self,event):
    button_code(self, 49)

  def OnButtonClick50(self,event):
    button_code(self, 50)

  def OnButtonClick51(self,event):
    button_code(self, 51)

  def OnButtonClick52(self,event):
    button_code(self, 52)

  def OnButtonClick53(self,event):
    button_code(self, 53)

  def OnButtonClick54(self,event):
    button_code(self, 54)

  def OnButtonClick55(self,event):
    button_code(self, 55)

  def OnButtonClick56(self,event):
    button_code(self, 56)

  def OnButtonClick57(self,event):
    button_code(self, 57)

  def OnButtonClick58(self,event):
    button_code(self, 58)

  def OnButtonClick59(self,event):
    button_code(self, 59)

  def OnButtonClick60(self,event):
    button_code(self, 60)

  def OnButtonClick61(self,event):
    button_code(self, 61)

  def OnButtonClick62(self,event):
    button_code(self, 62)

  def OnButtonClick63(self,event):
    button_code(self, 63)

  def OnButtonClick64(self,event):
    button_code(self, 64)

  def OnButtonClick65(self,event):
    button_code(self, 65)

  def OnButtonClick66(self,event):
    button_code(self, 66)

  def OnButtonClick67(self,event):
    button_code(self, 67)

  def OnButtonClick68(self,event):
    button_code(self, 68)

  def OnButtonClick69(self,event):
    button_code(self, 69)

  def OnButtonClick70(self,event):
    button_code(self, 70)

  def OnButtonClick71(self,event):
    button_code(self, 71)

  def OnButtonClick72(self,event):
    button_code(self, 72)

  def OnButtonClick73(self,event):
    button_code(self, 73)

  def OnButtonClick74(self,event):
    button_code(self, 74)

  def OnButtonClick75(self,event):
    button_code(self, 75)

  def OnButtonClick76(self,event):
    button_code(self, 76)

  def OnButtonClick77(self,event):
    button_code(self, 77)

  def OnButtonClick78(self,event):
    button_code(self, 78)

  def OnButtonClick79(self,event):
    button_code(self, 79)

  def OnButtonClick80(self,event):
    button_code(self, 80)

  def OnButtonClick81(self,event):
    button_code(self, 81)


if __name__ == "__main__":
  app = wx.App()
  frame = simpleapp_wx(None,-1,'Photo Booth')
  #frame2 = simpleapp_wx(frame,-1,'test')
  app.MainLoop()
