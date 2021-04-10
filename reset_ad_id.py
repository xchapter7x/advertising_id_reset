#!/usr/bin/env python

from AppKit import NSWorkspace
from Foundation import NSURL
import atomac

try:
    atomac.getAppRefByLocalizedName('System Preferences')
except ValueError:
    sys_pref_link = 'x-apple.systempreferences:com.apple.preference.security?Privacy_Advertising'
    workspace = NSWorkspace.sharedWorkspace()
    workspace.openURL_(NSURL.URLWithString_(sys_pref_link))

pref = atomac.getAppRefByLocalizedName('System Preferences')
win = pref.AXFocusedWindow
win.findAllR(AXRole='AXButton', AXTitle='Reset Advertising Identifier')[0].Press()
win.findAllR(AXRole='AXButton', AXTitle='Reset Identifier')[0].Press()
# win.AXCloseButton.Press()
