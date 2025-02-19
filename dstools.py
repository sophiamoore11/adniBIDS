import argparse
from dstools.core import splitsubj, nearestScan


def main():
    parser = argparse.ArgumentParser(description="ADNI to BIDSy Tools")
    subparsers = parser.add_subparsers(dest="command")

    # parser for splitsubj
    splitsubj_parser = subparsers.add_parser("splitsubj", help="Restructure subject data into anat and tau folders")
    splitsubj_parser.add_argument("subj", help="Subject ID (e.g., 037_S_5126)")
    splitsubj_parser.add_argument("source_dir", help="Source directory, where subj lives")
    splitsubj_parser.add_argument("targ_dir", help="Target directory")
    splitsubj_parser.add_argument("--tau_ls", nargs="+", default=['Uniform_6mm_Res'], help="List of tau scan types. "
                                                                                           "default='Uniform_6mm_Res'")
    splitsubj_parser.add_argument("--anat_ls", nargs="+", default=['bestT1'], help="List of anatomical scan types. "
                                                                                   "default='bestT1'. "
                                                                                   "add that keyword to list to search for T1")

    # parser for nearestScan
    nearestScan_parser = subparsers.add_parser("nearestScan", help="Find the nearest anat scan to tau scan for a given subject")
    nearestScan_parser.add_argument("subj", help="Subject ID")

    args = parser.parse_args()

    # Call the specified function
    if args.command == "splitsubj":
        splitsubj(args.subj, args.source_dir, args.targ_dir, tau_ls=args.tau_ls, anat_ls=args.anat_ls)
    elif args.command == "nearestScan":
        nearestScan(args.subj)

if __name__ == "__main__":
    main()

"""if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])"""