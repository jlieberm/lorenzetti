#ifndef ConditionsConverter_h
#define ConditionsConverter_h

/** simulator includes **/
#include "Conditions/Conditions.h"
#include "CaloCluster/CaloClusterConverter.h"

namespace xAOD{

    struct Conditions_t{
        bool isBlindReconstruction;
    };

    class ConditionsConverter{

        public:
            ConditionsConverter()=default;
            ~ConditionsConverter()=default;

            // convert a class object into a struct
            bool convert( const Conditions *, Conditions_t & ) ;
            bool convert( const Conditions_t &conditions_t, Conditions *&conditions );

        private:

    };



}
#endif


