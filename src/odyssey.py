# Odyssey host wxPython based GUI
import wx

class odysseyApp(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200,100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)

########################################################################
class SlicePanel(wx.Panel):
    """
    This will be the first notebook tab
    """
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """"""

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        sizer = wx.BoxSizer(wx.VERTICAL)
        ## Load STL/SVG File Button, and text field for displaying file path
        loadFile = wx.Button(self, 1, 'Load STL',(50,130))
        filePath = wx.TextCtrl(self, wx.ID_ANY, "")
        pathLabel = wx.StaticText(self, 1, "File Path:", (100,10))

        ## Slicing/Print Quality Settings

        ## Layer height parameter
        layerLb = wx.StaticText(self, 1, "Layer Height (mm):", (100,20))
        layer = wx.TextCtrl(self, 1, "")
        ## Exposure time parameter
        expLb = wx.StaticText(self, 1, "Exposure Time (s):", (100,30))
        exposure = wx.TextCtrl(self, 1, "")
        ## Blank Time parameter
        blankLb = wx.StaticText(self, 1, "Blank Time (s)", (100,40))
        blank = wx.TextCtrl(self, 1, "")
        ## Print Size Scale factor
        scaleLb = wx.StaticText(self. 1. "Scale:")
        scale = wx.SpinCtrl(self,1 '0.000',(150,75),(60,-1) )
        ## Pre-Lift G-Code
        preLb = wx.StaticText(self, 1, "Pre-Lift G-Code:")
        preGcode = wx.TextCtrl(self, 1, "")
        ## Post-Lift G-code
        postLb = wx.StaticText(self, 1,"Post-Lift G-Code:")
        postGcode = wx.TextCtrl(self, 1, "")
        ## Z Axis Speed
        zspeedLb = wx.StaticText(self, 1, "Z-Speed (mm/s) :")
        zspeed = wx.TextCtrl(self,1,"")

        platterView = wx.StaticBox(self, -1, 'Printer Platter',)

        self.SetSizer(sizer)


########################################################################
class ControlPanel(wx.Panel):
    """
    This will be the first notebook tab
    """
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """"""

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        sizer = wx.BoxSizer(wx.VERTICAL)
        txtOne = wx.TextCtrl(self, wx.ID_ANY, "")
        txtTwo = wx.TextCtrl(self, wx.ID_ANY, "")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(txtOne, 0, wx.ALL, 5)
        sizer.Add(txtTwo, 0, wx.ALL, 5)

        self.SetSizer(sizer)


########################################################################
class MachinePanel(wx.Panel):
    """
    This will be the first notebook tab
    """
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """"""

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        sizer = wx.BoxSizer(wx.VERTICAL)
        txtOne = wx.TextCtrl(self, wx.ID_ANY, "")
        txtTwo = wx.TextCtrl(self, wx.ID_ANY, "")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(txtOne, 0, wx.ALL, 5)
        sizer.Add(txtTwo, 0, wx.ALL, 5)

        self.SetSizer(sizer)





app = wx.App(False) # Create a new application, don't redirect stdout/stderr to a window
frame = wx.Frame(None, wx.ID_ANY, "Odyssey Host 0.1a") # Creates Frame (a top level window)
frame.Show(True) # Makes the Frame Visible
app.MainLoop()
