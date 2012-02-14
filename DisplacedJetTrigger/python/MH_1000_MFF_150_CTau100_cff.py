import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_100_1_LxF.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_10_1_pje.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_11_1_RIo.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_12_1_nNP.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_13_1_mGc.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_14_1_tZ7.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_15_1_9Nh.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_16_1_Qp0.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_17_1_R72.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_18_1_psU.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_19_1_qHY.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_20_1_Mkn.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_21_1_OjU.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_22_1_2UA.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_23_1_M2O.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_24_1_H39.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_28_1_tHl.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_29_1_GOT.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_30_1_6d6.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_31_1_y50.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_32_1_MeS.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_33_1_d3G.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_34_1_cuR.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_35_1_YfA.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_36_1_esU.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_37_1_Uyz.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_38_1_oWT.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_39_1_Alp.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_40_1_fKd.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_47_1_E59.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_48_1_BTa.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_49_1_j56.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_51_1_HDa.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_52_1_iKF.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_53_1_6M9.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_54_1_t6j.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_56_1_k3b.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_58_1_qig.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_59_1_lM1.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_60_1_CWo.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_61_1_Fjl.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_62_1_puL.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_63_1_Fah.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_69_1_n3n.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_70_1_C0i.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_71_1_0U6.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_72_1_5DM.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_73_1_L4i.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_74_1_Vcy.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_75_1_gIo.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_76_1_vMa.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_79_1_Inr.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_80_1_bUP.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_81_1_kTH.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_82_1_qQA.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_83_1_GbO.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_84_1_pYG.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_85_1_8gQ.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_86_1_nwC.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_87_1_7Dk.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_88_1_4W3.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_89_1_eKY.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_90_1_qsi.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_97_1_4Px.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_98_1_7F4.root',
       '/store/user/zuranski/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/MH_1000_MFF_150_CTau100_7TeVGEN_SIM_RAWDEBUG/dd38ef844932447e6a1aec87fc9ad080/GEN-SIM-RAWDEBUG_99_1_mdK.root' ] );


secFiles.extend( [
               ] )

