#!/usr/bin/python

# combobox.py

import wx

class MyDialog(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size=(250, 270))

        panel = wx.Panel(self, -1, (75, 20), (100, 127),  style=wx.SUNKEN_BORDER)
        self.picture = wx.StaticBitmap(panel)
        panel.SetBackgroundColour(wx.WHITE)

        self.images = ['tolstoy.jpg', 'feuchtwanger.jpg', 'balzac.jpg', 'pasternak.jpg', 'galsworthy.jpg', 'wolfe.jpg', 'zweig.jpg']
        authors = ['Leo Tolstoy', 'Lion Feuchtwanger', 'Honore de Balzac', 'Boris Pasternak', 'John Galsworthy', 'Tom Wolfe', 'Stefan Zweig' ]


        wx.ComboBox(self, -1, pos=(50, 170), size=(150, -1), choices=authors, style=wx.CB_READONLY)
        wx.Button(self, 1, 'Close', (80, 220))

        self.Bind(wx.EVT_BUTTON, self.OnClose, id=1)
        self.Bind(wx.EVT_COMBOBOX, self.OnSelect)

        self.Centre()

    def OnClose(self, event):
        self.Close()

    def OnSelect(self, event):
        item = event.GetSelection()
        self.picture.SetFocus()
        self.picture.SetBitmap(wx.Bitmap('images/' + self.images[item]))


class MyApp(wx.App):
    def OnInit(self):
        dlg = MyDialog(None, -1, 'combobox.py')
        dlg.ShowModal()
        dlg.Destroy()
        return True

app = MyApp(0)
app.MainLoop()
