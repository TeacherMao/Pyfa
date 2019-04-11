import wx
from service.fit import Fit

import gui.mainFrame
from gui import globalEvents as GE
from .calc.fitToggleFighterAbility import FitToggleFighterAbilityCommand


class GuiToggleFighterAbilityCommand(wx.Command):

    def __init__(self, fitID, position, effectID, isProjected):
        wx.Command.__init__(self, True, "")
        self.mainFrame = gui.mainFrame.MainFrame.getInstance()
        self.internal_history = wx.CommandProcessor()
        self.fitID = fitID
        self.position = position
        self.effectID = effectID
        self.isProjected = isProjected

    def Do(self):
        if self.internal_history.Submit(FitToggleFighterAbilityCommand(self.fitID, self.position, self.effectID, self.isProjected)):
            Fit.getInstance().recalc(self.fitID)
            wx.PostEvent(self.mainFrame, GE.FitChanged(fitID=self.fitID))
            return True
        return False

    def Undo(self):
        for _ in self.internal_history.Commands:
            self.internal_history.Undo()
        Fit.getInstance().recalc(self.fitID)
        wx.PostEvent(self.mainFrame, GE.FitChanged(fitID=self.fitID))
        return True