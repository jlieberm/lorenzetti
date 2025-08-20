__all__ = ["Zrad"]

from GaugiKernel import Cpp
from ROOT import generator


class Zrad(Cpp):

    def __init__(self, name, gen,
                 EtaMax: float = 1.4,
                 MinPt: float = 0.0,
                 ZeroVertexParticles: bool = False,
                 ForceForwardElectron: bool = False,
                 OutputLevel: int = 0
                 ):

        Cpp.__init__(self, generator.Zrad(name, gen.core()))
        self.__gen = gen

        self.setProperty("EtaMax", EtaMax)
        self.setProperty("MinPt", MinPt)
        self.setProperty("ZeroVertexParticles", ZeroVertexParticles)
        self.setProperty("ForceForwardElectron", ForceForwardElectron)
        # self.setProperty( "OutputLevel"         , OutputLevel         )

    def gun(self):
        return self.__gen
