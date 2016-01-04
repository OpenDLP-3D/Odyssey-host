# Odyssey host wxPython based GUI
import wx

class odysseyApp(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200,100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)

########################################################################
class PrinterSettingsPanel(wx.Panel):
    """
    First Tab of GUI, Print Settings and Slicer Panel
    """
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """"""

        slic3rPanel = wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        sizer = wx.BoxSizer(wx.VERTICAL)
        ## Load STL/SVG File Button, and text field for displaying file path
        loadFile = wx.Button(self, 1, 'Load File',(50,130))
        pathLabel = wx.StaticText(self, 1, "File Path:", (100,10))
        filePath = wx.TextCtrl(self, wx.ID_ANY, "")

        ## Printer Settings
        ## Left Side of Panel
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
        scaleLb = wx.StaticText(self, 1, "Scale:")
        scale = wx.SpinCtrl(self,1 '0.000',(150,75),(60,-1) )
        ## Direction
        directionLb = wx.StaticText(self, 1, "Direction:")
        directionCh = ["Top Down", "Bottom Up"]
        directionMnu = wx.ComboBox(self, -1, pos=(50, 170), size=(150, -1), choices=directionCh, style=wx.CB_READONLY)
        ## Overshoot
        overshootLb = wx.StaticText(self, 1, "Overshoot (mm) :")
        overshootMnu = wx.SpinCtrl(self, -1, '',  (150, 75), (60, -1))
        ## Pre-Lift G-Code
        preLb = wx.StaticText(self, 1, "Pre-Lift G-Code:")
        preGcode = wx.TextCtrl(self, 1, "")

        ## Right side of Panel
        ## X(px) X Pixele
        xPxLb = wx.StaticText(self, 1,"X(px):")
        xPxMnu = wx.SpinCtrl(self, -1, '', (150,75),(60,-1))
        ## Y(px) Y Pixels
        yPxLb = wx.StaticText(self, 1, "Y(px):")
        yPxMnu = wx.SpinCtrl(self, -1, '', (150,75),(60,-1))
        ## OffSet
        offsetLb = wx.StaticText(self, 1, "Offset:")
        offsetMnu = wx.SpinCtrl(self, -1, '', (150,75),(60,-1))
        ## Projected X
        prjctXLb = wx.StaticText(self, 1, "ProjectedX (mm) ")
        ## Z Axis Speed
        zspeedLb = wx.StaticText(self, 1, "Z-Speed (mm/s) :")
        zspeed = wx.TextCtrl(self,1,"")
        ## Post-Lift G-code
        postLb = wx.StaticText(self, 1,"Post-Lift G-Code:")
        postGcode = wx.TextCtrl(self, 1, "")

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

        ## Connecting to Printer (BeaglbeonBlack w/ DLP-CAPE)
        printCntLb = wx.StaticText(self, 1, "Printer Connection: ")
        portLb = wx.StaticText(self, 1, "Port:")
        port = wx.SpinCtrl(self, -1, '', (150,75),(60,-1))
        atLb = wx.StaticText(self,1,"@")
        baudrate = wx.SpinCtrl(self, -1, '', (150,75),(60,-1))
        connect = wx.Button(self, 1,'Connect',(50,120))
        reset = wx.Button(self,1,'Reset',(50,120))
        disconnect = wx.Button(self,1,'Disconnect',(50,120))

        ## Load presliced SVG
        loadFileSVG = wx.Button(self, 1, 'Load File',(50,130))
        pathLabelSVG = wx.StaticText(self, 1, "File Path:", (100,10))
        filePathSVG = wx.TextCtrl(self, wx.ID_ANY, "")
        ## Start a print, pause a print, stop/cancel a print
        printPart = wx.Button(self, 1,'Print',(50,120))
        pausePrint = wx.Button(self,1,'Pause',(50,120))
        stopPrint = wx.Button(self,1,'Stop',(50,120))

        ## Manual Z Jog and Tily Jog controls? Expert mode?

        ## Printer Console - For debugging pritner and sending it commands manually
        pronsoleLb = wx.StaticText(self,1,"Printer Console:")
        pronsole = wx.TextCtrl(self,1,"")
        sendCmd = wx.Button(self,1,'Send Command',(100,10))
        cmdBox = wx.StaticText(self,1,"")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(txtOne, 0, wx.ALL, 5)
        sizer.Add(txtTwo, 0, wx.ALL, 5)

        self.SetSizer(sizer)


#######################################################################
class SlicingPanel(wx.Panel):
    """
    This is the 3rd tab, for Slicing STLs into SVGs and autoloading them
    to the print queue
    """
    #----------------------------------------------------------------------
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        sizer = wx.BoxSizer(wx.VERTICAL)
        ## Slice it!
        ## Layer Height
        layerHLb = wx.StaticText(self,1,"Layer Height (mm) :")
        layerHeight = wx.SpinCtrl(self, -1, '', (150,75),(60,-1))
        ## Slice To File
        sliceToFile = wx.Button(self, 1, 'Slice to File',(50,130))
        ## Slice To Print
        sliceToPrint = wx.Button(self, 1, 'Slice to Print',(50,130))


        self.SetSizer(sizer)



app = wx.App(False) # Create a new application, don't redirect stdout/stderr to a window
frame = wx.Frame(None, wx.ID_ANY, "Odyssey Host 0.1a") # Creates Frame (a top level window)
frame.Show(True) # Makes the Frame Visible
app.MainLoop()
