#ifndef Evtgen_Zrad_h
#define Evtgen_Zrad_h

#include "GenKernel/IAlgorithm.h"
#include "GenKernel/IGenerator.h"

namespace generator{

  class Zrad : public IAlgorithm
  {
    public:
    
      Zrad(const std::string , IGenerator *);
      ~Zrad();
  
      virtual StatusCode initialize() override;
      virtual StatusCode execute( Event& ) override;
      virtual StatusCode finalize() override;
  
    private:
      /**
       * @brief Minimum pT required for the electron/positron pair
       * 
       */
      float m_minPt;
      /**
       * @brief Maximum eta allowed for the electron/positron pair
       * 
       */
      float m_etaMax;
      /**
       * @brief If true, includes original pz position  (zero) without fluctuations
       * Useful for calibration purposes
       * 
       */
      bool  m_zeroVertexParticles;
      /**
       * @brief If true, forces one and only one electron/positron to be forward
       * 
       */
      bool  m_forceForwardElectron;
     
  };

}
#endif
