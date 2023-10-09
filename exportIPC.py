# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#                                                                      
# This file is an plugin for KICAD to export IPC-D-356 Netlist       
# MIT License
# 
# Copyright (c) 2023
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#  Author :Mariwan Jalal    mariwan.jalal@gmail.com
# 

import pcbnew
import os
import wx
import datetime

__version_info__ = ('1', '0', '0')
__version__ = '.'.join(__version_info__)

class exportIPC( pcbnew.ActionPlugin ):
 
    def defaults( self ):
        """ 
            Default constructor  -- See KICAD plugin documentation
        """
        self.name = "Export IPC"
        self.category = "Export PCB IPC-D-356"
        self.description = "Export IPC values from PCB"
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), "./exportIPC.png")
        
    def getFileName(self):
        """ 
            Get file name based on date and time

        Returns:
            str: File name start with exportIPC and has date-time stamp
        """
        basename = "exportIPC"
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        filename = "_".join([basename, suffix])
        return filename
    
    def ask(self, parent=None, message='Enter File Path to save', default_value='c:/temp'):
        """
            Function to ask user for selecting a folder to save the generated file

        Args:
            parent (_type_, optional): If there is any parent dialog. Defaults to None.
            message (str, optional): Title of the dialog. Defaults to 'Enter File Path to save'.
            default_value (str, optional): Location to save the file. Defaults to 'c:/temp'.

        Returns:
            str: file path to save
        """
        dlg =wx.DirDialog (None, message, "c:/temp",wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            result = dlg.GetPath()
        if result =="":
            result="c:/temp"
        dlg.Destroy()
        return result

    def Run(self):
        """
            Plugin run function -- see KICAD Documentation for plugins
        """
        filePath=self.ask()
        pcb = pcbnew.GetBoard() 
        netlist_writer = pcbnew.IPC356D_WRITER(pcb)
        filename= "/" + self.getFileName()  +".ipc"
        netlist_writer.Write(filePath +filename )
        # this shouldn't be needed
        #pcbnew.UpdateUserInterface()
