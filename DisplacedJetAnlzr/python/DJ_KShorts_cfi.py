import FWCore.ParameterSet.Config as cms
from DisplacedDijet.DisplacedJetAnlzr.DJ_Jets_cfi import jetColl

djkshorts = cms.EDProducer('DJ_KShorts',
    patJetCollectionTag = cms.InputTag(jetColl),
    PromptTrackDxyCut = cms.double(0.05), # 500 microns
    TrackPtCut = cms.double(1.),
)
