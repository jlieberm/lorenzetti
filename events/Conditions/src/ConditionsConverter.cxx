
#include "Conditions/ConditionsConverter.h"
//#include "G4Kernel/macros.h"

#include<iostream>
using namespace xAOD;
using namespace std;


bool ConditionsConverter::convert( const Conditions *conditions, Conditions_t &conditions_t )
{
  if(conditions){
    
    conditions_t.isBlindReconstruction = conditions->blindReconstruction();
    return true;
  }
  return false;
}

bool ConditionsConverter::convert( const Conditions_t &conditions_t, Conditions *&conditions)
{
  
    conditions = new xAOD::Conditions();
    conditions->setBlindReconstruction(conditions_t.isBlindReconstruction);
    return true;
}