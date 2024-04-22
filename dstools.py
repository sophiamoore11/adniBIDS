import os
import glob
from datetime import datetime
import shutil
import sys

def splitsubj(subj):
    # example starting structure:
    # |-- 037_S_5126
    # |   |-- AV1451_Co-registered,_Averaged
    # |   |   |-- 2016-03-30_16_06_52.0
    # |   |   `-- 2021-06-17_16_51_03.0
    # |   |-- AV1451_Coreg, _Avg, _Std_Img_and_Vox_Siz, _Uniform_6mm_Res
    # |   |  | -- 2016-03-30_16_06_52.0
    # |   |   `-- 2021-06-17_16_51_03.0
    #    |       `-- I885589
    #    |           |-- ADNI_941_S_6052_PT_AV1451_Coreg,_Avg,_Std_Img_and_Vox_Siz,_Uniform_Resolution_Br_20170811083745288_58_S591125_I885589.dcm
    # |   `-- MT1__N3m
    # |       |-- 2013-04-25_14_25_45.0
    # |       |-- 2013-04-25_14_31_02.0
    # |       |-- 2013-07-22_15_31_44.0
    # |       `-- 2015-11-30_16_01_14.0
    #            `-- I882756
    #                `-- ADNI_037_S_5126_MR_MT1__N3m_Br_20170804183926749_S585807_I882756.nii

    # example desired structure:
    # adni
    # -- adni_anat
    #   |-- 037_S_5126
    #   |   |-- ses-YYMMDD
    #   |       `-- anat
    #   |           `-- ADNI_037_S_5126_MR_MT1__N3m_Br_20170804183926749_S585807_I882756.nii
    # -- adni_tau
    #   |-- 037_S_5126
    #   |   |-- ses-YYMMDD
    #   |       `-- ADNI_037_S_5126_PT_AV1451_Coreg,_Avg,_Std_Img_and_Vox_Siz,_Uniform_Resolution_Br_20170811083745288_58_S591125_I885589.dcm

    ##ASSUME /adni_tau and /adni_anat exist under /adni
    curr_dir = os.getcwd()  # /gpfs/data/martersteck-lab/home/sophiamoore/adni_testing/adni_all
    os.chdir(curr_dir + "/" + subj)  # adni_all/037_S_5126
    subj_dir = os.getcwd()

    # TAU
    # if subj does not exist in adni_tau, mkdir subj
    pth_to_tau = os.path.abspath(os.path.join(os.getcwd(), '..','..') + "/adni/adni_tau")  # adni_testing/adni_all/037_S_5126 -> adni_testing/adni/adni_tau
    pth_to_subjtau = pth_to_tau + "/" + subj
    if not os.path.exists(pth_to_subjtau):  # if adni_testing/adni/adni_tau/037_S_5126 does not exist
        os.mkdir(pth_to_subjtau)

    # Look for AV1451 uni 6mm
    usixres_tau = glob.glob(subj_dir + '/*Uniform_6mm_Res')

    # for each adni_tau session, mkdir ses-YYMMDD. cp dcms into that.
    if len(usixres_tau) != 0:
        for ses in os.listdir(usixres_tau[0]):  # must get date from ses folder name
            if not ses[0] == ".":
                dt_obj = datetime.strptime(ses[0:10], "%Y-%m-%d").date().strftime("%y%m%d")  # eg: 2021-06-17_16_51_03.0 -> 210617 (string obj)
                # mkdir in adni_tau
                pth_to_ses = pth_to_subjtau + "/" + "ses-" + dt_obj
                if not os.path.exists(pth_to_ses):
                    os.mkdir(pth_to_ses)
                # cp dcms from I###### folder directly into new sesYYMMDD folder
                pth_to_dt = usixres_tau[0] + "/" + ses  #.../...Uniform_6mm_Res/2021-06-17_16_51_03.0
                for dcmset in os.listdir(pth_to_dt):
                    if not dcmset[0] == ".":
                        for dcm in os.listdir(pth_to_dt + "/" + dcmset):
                            if not dcm[0] == ".":
                                source = pth_to_dt + "/" + dcmset + "/" + dcm
                                destination = pth_to_ses + "/" + dcm
                                shutil.copy(source, destination)

    # ANAT
    # if subj does not exist in adni_anat, mkdir subj
    pth_to_anat = os.path.abspath(os.path.join(os.getcwd(), '..','..') + "/adni/adni_anat")  # adni_testing/adni_all/037_S_5126 -> adni_testing/adni/adni_anat
    pth_to_subjanat = pth_to_anat + "/" + subj
    if not os.path.exists(pth_to_subjanat):  # if adni_testing/adni/adni_anat/037_S_5126 does not exist
        os.mkdir(pth_to_subjanat)

    # Look for MT1__N3m
    mt1n3m_anat = glob.glob(subj_dir + '/*MT1__GradWarp__N3m')

    # for each adni_anat session, mkdir ses-YYMMDD. cp niftis into that.
    if len(mt1n3m_anat) != 0:
        for ses in os.listdir(mt1n3m_anat[0]):  # must get date from ses folder name
            if not ses[0] == ".":
                dt_obj = datetime.strptime(ses[0:10], "%Y-%m-%d").date().strftime("%y%m%d")  # eg: 2021-06-17_16_51_03.0 -> 210617 (string obj)
                # mkdir in adni_anat
                pth_to_ses = pth_to_subjanat + "/" + "ses-" + dt_obj
                if not os.path.exists(pth_to_ses):
                    os.mkdir(pth_to_ses)
                # cp nifti from I###### folder directly into new sesYYMMDD folder
                pth_to_dt = mt1n3m_anat[0] + "/" + ses  #.../...MT1__N3/2021-06-17_16_51_03.0
                for niiset in os.listdir(pth_to_dt):
                    if not niiset[0] == ".":
                        for nii in os.listdir(pth_to_dt + "/" + niiset):
                            if not nii[0] == ".":
                                source = pth_to_dt + "/" + niiset + "/" + nii
                                destination = pth_to_ses + "/" + nii
                                shutil.copy(source, destination)



def nearestScan(subj):
    ##Given a subject, find nearest scans of each type
        ##e.g. nearestScan(002_S_0295)
# adni
# -- adni_anat
#   |-- 037_S_5126
#   |   |-- ses-YYMMDD
#   |       `-- anat
#   |           `-- ADNI_037_S_5126_MR_MT1__N3m_Br_20170804183926749_S585807_I882756.nii
# -- adni_tau
#   |-- 037_S_5126
#   |   |-- ses-YYMMDD
#   |       `-- ADNI_037_S_5126_PT_AV1451_Coreg,_Avg,_Std_Img_and_Vox_Siz,_Uniform_Resolution_Br_20170811083745288_58_S591125_I885589.dcm

    curr_dir = os.getcwd()  # /gpfs/data/martersteck-lab/home/sophiamoore/adni_testing/adni_all
    pth_to_subjtau = os.path.abspath(os.path.join(curr_dir, '..') + "/adni/adni_tau/" + subj)  # adni_testing/adni_all/037_S_5126 -> adni_testing/adni/adni_tau
    sbjtau_dts = sorted(os.listdir(pth_to_subjtau)) #sorting for binary search


    pth_to_subjanat = os.path.abspath(os.path.join(curr_dir, '..') + "/adni/adni_anat/" + subj)  # adni_testing/adni_all/037_S_5126 -> adni_testing/adni/adni_anat
    sbjanat_dts = sorted(os.listdir(pth_to_subjanat))



    def binary_search(arr, target):
        """
        Performs binary search to find the nearest number to the target in the given array.
        """
        left, right = 0, len(arr) - 1
        nearest = float('inf')

        while left <= right:
            mid = left + (right - left) // 2
            diff = abs(int(arr[mid][-6:]) - target)

            if diff < nearest:
                nearest = diff
                result = arr[mid]

            if int(arr[mid][-6:]) < target:
                left = mid + 1
            else:
                right = mid - 1

        return result

    """
    Finds the nearest numbers, one from each of two input arrays. REQUIRES SORTED ARRAYS
    """
    nearest1, nearest2 = float('inf'), float('inf')

    for ses in sbjtau_dts:
        nearest_in_anat = binary_search(sbjanat_dts, int(ses[-6:]))
        diff = abs(int(ses[-6:]) - int(nearest_in_anat[-6:]))

        if diff < nearest1:
            nearest1 = diff
            taudt = ses
            anatdt = nearest_in_anat
    pth_to_subjtaudt = pth_to_subjtau + "/" + taudt
    pth_to_subjanatdt = pth_to_subjanat + "/" + anatdt
    return pth_to_subjtaudt, pth_to_subjanatdt
#return pair of paths
#dictionary or csv
#for...command >> output.txt
#csv with sessions and subjects
'''    
    m = len(sbjtau_dts)
    n = len(sbjanat_dts)
    #for each session, extract date as int, use some search to find nearest pair
    diff = sys.maxsize

    l = 0 #left side of sbjtau_dts
    r = n-1 #right side of subjanat_dts
    while (l < m and r >= 0):
        tdt_int = int(sbjtau_dts[l][-6:])
        adt_int = int(sbjanat_dts[r][-6:])
        mid =
        if abs(tdt_int - adt_int) < diff:
            curr_l = l
            curr_r = r
            diff = abs(tdt_int - adt_int)

        if tdt_int + adt_int > 0:
            r=r-1
        else:
            l=l+1
    print("tau: ", sbjtau_dts[curr_l], "\nanat: ", sbjanat_dts[curr_r])
'''

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])