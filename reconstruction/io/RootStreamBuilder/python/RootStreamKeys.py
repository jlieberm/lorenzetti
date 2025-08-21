

__all__ = ['recordable']

valid_keys = [
            "EventInfo",
            "Hits",
            # CaloCellMerge
            "Cells",
            "TruthCells",
            # CaloClusterMaker
            "Events",
            "Seeds",
            "Clusters",
            "TruthClusters",
            "Particles",
            "TruthParticles",
            # CaloRingsBuilder
            "Rings",
            "TruthRings",
            "Electrons",
            "Conditions"
            ]

def recordable( key ):
  if key not in valid_keys:
    raise RuntimeError(f"Key {key} not allow to be recorded.")
  return key