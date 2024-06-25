
__all__ = ["RootStreamHITFlags", "RootStreamESDFlags", "RootStreamAODFlags"]


from GaugiKernel import EnumStringification


class RootStreamHITFlags(EnumStringification):

    OnlyRoI          = True
    EtaWindow        = 0.4
    PhiWindow        = 0.4
    doSlicedHIT      = False
    EtaMin           = 0
    EtaMax           = 3.2
    OnlyForward      = True
class RootStreamESDFlags(EnumStringification):
    
    EtaWindow        = 0.4
    PhiWindow        = 0.4


class RootStreamAODFlags(EnumStringification):

    DumpCells = True