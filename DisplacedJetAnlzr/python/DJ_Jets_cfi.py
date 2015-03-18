import FWCore.ParameterSet.Config as cms

jetColl = "selectedPatJets"

djjets = cms.EDProducer('DJ_Jets',
    patJetCollectionTag = cms.InputTag(jetColl)
)
