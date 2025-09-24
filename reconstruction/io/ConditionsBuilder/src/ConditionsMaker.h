#ifndef ConditionsMaker_h
#define ConditionsMaker_h

#include "Conditions/Conditions.h"
#include "Conditions/ConditionsContainer.h"
#include "GaugiKernel/StatusCode.h"
#include "GaugiKernel/DataHandle.h"
#include "GaugiKernel/Algorithm.h"
#include "GaugiKernel/DataHandle.h"



class ConditionsMaker : public Gaugi::Algorithm
{

  public:
    /** Constructor **/
    ConditionsMaker( std::string );
    
    virtual ~ConditionsMaker();
    
    virtual StatusCode initialize() override;

    virtual StatusCode bookHistograms( SG::EventContext &ctx ) const override;
    
    virtual StatusCode pre_execute( SG::EventContext &ctx ) const override;
    
    virtual StatusCode execute( SG::EventContext &ctx , const G4Step *step) const override;
    
    virtual StatusCode execute( SG::EventContext &ctx , int /*evt*/ ) const override;

    virtual StatusCode post_execute( SG::EventContext &ctx ) const override;
    
    virtual StatusCode fillHistograms( SG::EventContext &ctx ) const override;
    
    virtual StatusCode finalize() override;



  private:
 
    std::string m_conditionsKey;

    bool m_dumpCells;
    int  m_outputLevel;
    bool m_doBlindReco;
};

#endif

