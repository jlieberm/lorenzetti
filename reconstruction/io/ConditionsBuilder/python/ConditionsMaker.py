__all__ = ["ConditionsMaker"]

from GaugiKernel import Cpp
from GaugiKernel.macros import *
from RootStreamBuilder import RootStreamAODFlags as flags
from CaloClusterBuilder import CaloClusterFlags as caloFlags
import ROOT

class ConditionsMaker( Cpp ):

  def __init__( self, name,
                OutputConditionsKey: str=None,
                OutputLevel      : int=0, 
                doBlindReco      : bool=caloFlags.doBlindReco,
                DumpCells        : bool=flags.DumpCells,
              ): 
    
    Cpp.__init__(self, ROOT.ConditionsMaker(name))
    self.setProperty( "OutputConditionsKey", OutputConditionsKey)
    
    self.setProperty( "OutputLevel"     , OutputLevel     ) 
    self.setProperty( "DumpCells"       , DumpCells       )
    self.setProperty( "DoBlindReconstruction", doBlindReco)