#include "Conditions/ConditionsContainer.h"

#include "TTree.h"
#include "ConditionsMaker.h"
#include "GaugiKernel/EDM.h"


using namespace SG;
using namespace Gaugi;



ConditionsMaker::ConditionsMaker( std::string name ) : 
  IMsgService(name),
  Algorithm()
{
  declareProperty( "OutputConditionsKey"     , m_conditionsKey="Conditions"     );
  declareProperty( "OutputLevel"             , m_outputLevel=1                        );
  declareProperty( "DumpCells"               , m_dumpCells=false                      );
  declareProperty( "DoBlindReconstruction"   , m_doBlindReco=false                    );
}

//!=====================================================================

ConditionsMaker::~ConditionsMaker()
{;}

//!=====================================================================

StatusCode ConditionsMaker::initialize()
{
  CHECK_INIT();
  setMsgLevel(m_outputLevel);
  return StatusCode::SUCCESS;
}

//!=====================================================================

StatusCode ConditionsMaker::bookHistograms( SG::EventContext &ctx ) const
{
  return StatusCode::SUCCESS;
}

//!=====================================================================

StatusCode ConditionsMaker::pre_execute( EventContext &/*ctx*/ ) const
{
  return StatusCode::SUCCESS;
}

//!=====================================================================

StatusCode ConditionsMaker::execute( EventContext &/*ctx*/, const G4Step * /*step*/ ) const
{
  return StatusCode::SUCCESS;
}

//!=====================================================================

StatusCode ConditionsMaker::execute( EventContext & ctx, int /*evt*/ ) const
{
  return post_execute(ctx);
}

//!=====================================================================

StatusCode ConditionsMaker::post_execute( EventContext & ctx ) const
{
  SG::WriteHandle<xAOD::ConditionsContainer> conditions(m_conditionsKey, ctx);
  conditions.record( std::unique_ptr<xAOD::ConditionsContainer>(new xAOD::ConditionsContainer()) );
  xAOD::Conditions *cond = new xAOD::Conditions();
  cond->setBlindReconstruction(m_doBlindReco);
  conditions->push_back(cond);

  return StatusCode::SUCCESS;
}

//!=====================================================================

StatusCode ConditionsMaker::fillHistograms( EventContext &ctx ) const
{
  return StatusCode::SUCCESS;
}

//!=====================================================================

StatusCode ConditionsMaker::finalize()
{
  return StatusCode::SUCCESS;
}

//!=====================================================================

