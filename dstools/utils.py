import glob
import os

def findT1(subj_dir):
    rankedT1 = ["Spatially_Normalized,_Masked_and_N3_corrected_T1_image", "MT1__GradWarp__N3m",
                                        "MT1__N3m", "Accelerated_SAG_IR-FSPGR", "Accelerated_SAG_IR-SPGR",
                                        "Accelerated_Sag_IR-FSPGR", "Accelerated_Sag_IR-SPGR",
                                        "Accelerated_Sagittal_IR-FSPGR", "Accelerated_Sagittal_MPRAGE",
                                        "Accelerated_Sagittal_MPRAGE_MPR_Tra"
        , "Accelerated_Sagittal_MPRAGE_ND"
        , "Accelerated_Sagittal_MPRAGE_Phase_A-P"
        , "Accelerated_Sagittal_MPRAGE_REPEAT"
        , "IR-SPGR"
        , "IR-SPGR_w_acceleration"
        , "MPRAGE"
        , "MPRAGE_GRAPPA2"
        , "MPRAGE_GRAPPA2_S4_DIS3D"
        , "MPRAGE_GRAPPA2_rpt"
        , "MPRAGE_GRAPPA_2"
        , "MPRAGE_GRAPPA_2_ND"
        , "MPRAGE_ND"
        , "MPRAGE_P2_NO_ANGLE="
        , "MPRAGE_S2_DIS3D"
        , "MPRAGE_SENSE"
        , "MPRAGE_SENSE2"
        , "MPRAGE_SENSE2_SENSE"
        , "MPRAGE__NO_ANGLE"
        , "MPRAGE__NO_ANGLE="
        , "MPRAGE__Sag__-_NO_ANGLE="
        , "ORIG_Accelerated_Sag_IR-FSPGR"
        , "SAG_IR-SPGR"
        , "SAG_MPRAGE_GRAPPA2_NO_ANGLE"
        , "SAG_MPRAGE_NO_ANGLE"
        , "Sag_Accel_IR-FSPGR"
        , "Sag_IR-FSPGR"
        , "Sag_IR-FSPGR_Repeat"
        , "Sag_IR-SPGR"
        , "Sagittal_3D_Accelerated_0_angle_MPRAGE"
        , "Sagittal_3D_Accelerated_MPRAGE"]  # pd.read_csv("adni_T1_names.csv")
    # T1string = rankedT1["t1proc"]

    for scan_type in rankedT1:  # curr dir should be subject folder in adni_all
        matches = glob.glob(os.path.join(subj_dir, scan_type))
        if matches:
            return matches
        """if len(glob.glob(scan_type)) > 0:
            desiredT1 = glob.glob(subj_dir + "/" + scan_type)
            return desiredT1"""

    return None

    # #switch outer of double nested loop
    # for t1 in rankedT1:
    #     for s in os.listdir(os.getcwd()): #curr dir should be subject folder in adni_all
    #
    # return T1string[]
