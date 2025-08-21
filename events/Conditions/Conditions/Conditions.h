#ifndef Conditions_h
#define Conditions_h

#include "CaloCluster/CaloCluster.h"
#include "CaloCell/CaloCell.h"
#include "GaugiKernel/EDM.h"
#include "GaugiKernel/macros.h"
#include <cmath>


// Event Object Data
namespace xAOD{
  
  class Conditions: public Gaugi::EDM
  {  
    public:
      
      /*! Contructor */
      Conditions();
      /*! Destructor */
      ~Conditions()=default;
      /*! The eta center of the cluster given by the simulation (RoI) */ 
      PRIMITIVE_SETTER_AND_GETTER( float, m_isBlindReconstruction, setBlindReconstruction, blindReconstruction );

    private:
      bool m_isBlindReconstruction;
  };


  

}
#endif
