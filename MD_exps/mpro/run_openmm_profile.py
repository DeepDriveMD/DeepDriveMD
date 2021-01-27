import simtk.unit as u
import sys, os, shutil 
import argparse 

from MD_utils.openmm_simulation import openmm_simulate_amber_npt 

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--pdb_file", dest="f", help="pdb file")
parser.add_argument("-p", "--topol", dest='p', help="topology file")
parser.add_argument("-r", "--lres", dest='r', help="json file for interested list of residues") 
parser.add_argument("-c", help="check point file to restart simulation")
parser.add_argument("-l", "--length", default=10, help="how long (ns) the system will be simulated")
parser.add_argument("-g", "--gpu", default=0, help="id of gpu to use for the simulation")
parser.add_argument("-o", "--output")
args = parser.parse_args() 

if args.f: 
    pdb_file = os.path.abspath(args.f) 
else: 
    raise IOError("No pdb file assigned...") 

if args.p: 
    top_file = os.path.abspath(args.p) 
else: 
    top_file = None 

if args.r: 
    res_list_file = os.path.abspath(args.r) 
else: 
    res_list_file = None 

if args.c: 
    check_point = os.path.abspath(args.c) 
else: 
    check_point = None 

output_path = os.path.abspath("./")
if args.output:
    output_path = os.path.abspath(args.output)
    print(output_path)

# pdb_file = os.path.abspath('./pdb/100-fs-peptide-400K.pdb')
# ref_pdb_file = os.path.abspath('./pdb/fs-peptide.pdb')

gpu_index = args.gpu # os.environ["CUDA_VISIBLE_DEVICES"]

# check_point = None
openmm_simulate_amber_npt(pdb_file, top_file,
                         res_file=res_list_file, 
                         check_point=check_point,
                         GPU_index=gpu_index,
                         temperature=310,
                         output_traj=output_path + "/output.dcd",
                         output_log=output_path + "/output.log",
                         output_cm=output_path + "/output_cm.h5",
                         report_time=50*u.picoseconds,
                         sim_time=float(args.length)*u.nanoseconds)


