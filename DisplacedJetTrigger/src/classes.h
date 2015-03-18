#include "DisplacedDijet/DisplacedJetTrigger/interface/jet.h"
#include "DisplacedDijet/DisplacedJetTrigger/interface/pfjet.h"
#include "DataFormats/Common/interface/Wrapper.h"


namespace {

  struct dictionary {
    edm::Wrapper<track> trk; 
    edm::Wrapper<std::vector<track> > trks; 
    edm::Wrapper<jet> j;
    edm::Wrapper<pfjet> pfj;
    edm::Wrapper<std::vector<jet> > jets;
    edm::Wrapper<std::vector<pfjet> > pfjets;
  };

}
