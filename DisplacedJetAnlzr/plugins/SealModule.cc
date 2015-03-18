#include "FWCore/Framework/interface/MakerMacros.h"

//#include "DisplacedDijet/DisplacedJetAnlzr/interface/DJTree.h"
#include "DisplacedDijet/DisplacedJetAnlzr/interface/DJ_Triggers.h"
#include "DisplacedDijet/DisplacedJetAnlzr/interface/DJ_TriggerObjects.h"
#include "DisplacedDijet/DisplacedJetAnlzr/interface/DJ_PileupSummary.h"
#include "DisplacedDijet/DisplacedJetAnlzr/interface/DJ_Event.h"
#include "DisplacedDijet/DisplacedJetAnlzr/interface/DJ_GenEvent.h"
#include "DisplacedDijet/DisplacedJetAnlzr/interface/DJ_EventFilters.h"
#include "DisplacedDijet/DisplacedJetAnlzr/interface/DJ_Jets.h"
#include "DisplacedDijet/DisplacedJetAnlzr/interface/DJ_DiJets.h"
#include "DisplacedDijet/DisplacedJetAnlzr/interface/DJ_JetVertices.h"
#include "DisplacedDijet/DisplacedJetAnlzr/interface/DJ_DiJetVertices.h"
#include "DisplacedDijet/DisplacedJetAnlzr/interface/DJ_Muons.h"
#include "DisplacedDijet/DisplacedJetAnlzr/interface/DJ_KShorts.h"

//DEFINE_FWK_MODULE(DJTree);
DEFINE_FWK_MODULE(DJ_Triggers);
DEFINE_FWK_MODULE(DJ_TriggerObjects);
DEFINE_FWK_MODULE(DJ_PileupSummary);
DEFINE_FWK_MODULE(DJ_Event);
DEFINE_FWK_MODULE(DJ_GenEvent);
DEFINE_FWK_MODULE(DJ_EventFilters);
DEFINE_FWK_MODULE(DJ_Jets);
DEFINE_FWK_MODULE(DJ_DiJets);
DEFINE_FWK_MODULE(DJ_JetVertices);
DEFINE_FWK_MODULE(DJ_DiJetVertices);
DEFINE_FWK_MODULE(DJ_Muons);
DEFINE_FWK_MODULE(DJ_KShorts);

