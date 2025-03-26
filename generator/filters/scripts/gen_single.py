#!/usr/bin/env python3

import argparse
import sys
import os
from math import ceil
from typing import List
from joblib import Parallel, delayed
from evtgen import Pythia8
from filters import Pileup,Particle, SingleParticle

from GenKernel import EventTape
from GaugiKernel import get_argparser_formatter
from GaugiKernel import LoggingLevel
from GaugiKernel import GeV


datapath    = os.environ["LORENZETTI_EVTGEN_DATA_DIR"]
PILEUP_FILE = f'{datapath}/minbias_config.cmnd'


def parse_args():

    parser = argparse.ArgumentParser(
        description='',
        formatter_class=get_argparser_formatter(),
        add_help=False)

    parser.add_argument('-e', '--event-numbers', action='store',
                        dest='event_numbers', required=False,
                        type=str, default=None,
                        help="The event number list separated "
                        "by ','. e.g. --event-numbers '0,1,2,3'")
    parser.add_argument('-o', '--output-file', action='store',
                        dest='output_file', required=True,
                        help="The event file generated by pythia.")
    parser.add_argument('--nov', '--number-of-events', action='store',
                        dest='number_of_events', required=False,
                        type=int, default=1,
                        help="The number of events to be generated.")
    parser.add_argument('--run-number', action='store',
                        dest='run_number', required=False,
                        type=int, default=0,
                        help="The run number.")
    parser.add_argument('-s', '--seed', action='store',
                        dest='seed', required=False,
                        type=int, default=0,
                        help="The pythia seed (zero is the clock system)")
    parser.add_argument('--output-level', action='store',
                        dest='output_level', required=False,
                        type=str, default="INFO",
                        help="The output level messenger.")
    


    parser.add_argument('-p', '--particle',action='store', 
                        dest='particle', required = True, type=str,
                        help = f"The single particle type: {Particle.stringList()}")
    parser.add_argument('--energy-min', action='store', 
                        dest='energy_min', required = False, 
                        type=float, default=-1,
                        help = "Energy min in GeV.")
    parser.add_argument('--energy-max', action='store', 
                        dest='energy_max', required = False, 
                        type=float, default=-1,
                        help = "Energy max in GeV.")
    parser.add_argument('--energy', action='store', 
                        dest='energy', required = False, 
                        type=float, default=-1,
                        help = "Energy in GeV.")
    parser.add_argument('--eta', action='store', 
                        dest='eta', required = False, 
                        type=float, default=0.00,
                        help = "Eta position.")
    parser.add_argument('--phi', action='store', 
                        dest='phi', required = False, 
                        type=float, default=1.52,
                        help = "Phi position.")
    parser.add_argument('--do-eta-ranged', action='store', 
                        dest='do_eta_ranged', required = False, 
                        type=bool, default=False,
                        help = "Enable eta range.")
    parser.add_argument('--eta-min', action='store', 
                        dest='eta_min', required = False, 
                        type=float, default=-2.5,
                        help ="Minimum Eta.")
    parser.add_argument('--eta-max', action='store', 
                        dest='eta_max', required = False, 
                        type=float, default=2.5,
                        help = "Maximum Eta.")
    parser.add_argument('--do-phi-ranged', action='store', 
                        dest='do_phi_ranged', required = False, 
                        type=bool, default=False,
                        help = "Enable phi range.")
    parser.add_argument('--phi-min', action='store', 
                        dest='phi_min', required = False, 
                        type=float, default=-3.14,
                        help = "Minimum Phi.")
    parser.add_argument('--phi-max', action='store', 
                        dest='phi_max', required = False, 
                        type=float, default=3.14,
                        help = "Maximum Phi.")
    parser.add_argument('--pileup-avg', action='store',
                        dest='pileup_avg', required=False,
                        type=float, default=0,
                        help="The pileup average (default is zero).")
    parser.add_argument('--pileup-sigma', action='store',
                        dest='pileup_sigma', required=False,
                        type=float, default=0,
                        help="The pileup sigma (default is zero).")
    parser.add_argument('--bc-id-start', action='store',
                        dest='bc_id_start', required=False,
                        type=int, default=-21,
                        help="The bunch crossing id start.")
    parser.add_argument('--bc-id-end', action='store',
                        dest='bc_id_end', required=False,
                        type=int, default=4,
                        help="The bunch crossing id end.")
    parser.add_argument('--bc-duration', action='store',
                        dest='bc_duration', required=False,
                        type=int, default=25,
                        help="The bunch crossing duration (in nanoseconds).")
    parser.add_argument('-nt', '--number-of-threads', action='store',
                        dest='number_of_threads', required=False,
                        type=int, default=1,
                        help="The number of threads")
    parser.add_argument('--events-per-job', action='store',
                        dest='events_per_job', required=False,
                        type=int, default=None,
                        help="The number of events per job")
    parser.add_argument('--pileup-file', action='store',
                        dest='pileup_file', required=False,
                        type=str, default=PILEUP_FILE,
                        help="The pythia pileup file configuration.")
    parser.add_argument('-m','--merge', action='store_true',
                        dest='merge', required=False,
                        help='Merge all files.')

    return parser


def main(events: List[int],
         logging_level: str,
         output_file: str,
         run_number: int,
         seed: int,
         particle: str,
         eta: float,
         phi: float, 
         eta_min: float,
         eta_max: float,
         phi_min: float,
         phi_max: float,
         energy: float,
         energy_min:float,
         energy_max:float,
         do_eta_ranged: bool,
         do_phi_ranged: bool,
         pileup_avg: float,
         pileup_sigma: float,
         mb_file: str,
         bc_id_start: int,
         bc_id_end: int):

    outputLevel = LoggingLevel.toC(logging_level)

    tape = EventTape("EventTape", OutputFile=output_file,
                     RunNumber=run_number)

  
    part = SingleParticle( particle,
                               Pythia8("Generator", Seed=seed),
                               Eta          = eta,
                               Phi          = phi,
                               EnergyMin    = energy_min*GeV,
                               EnergyMax    = energy_max*GeV,
                               Energy       = energy*GeV,
                               Particle     = Particle.fromstring(particle), 
                               DoRangedEta  = do_eta_ranged,
                               EtaMin       = eta_min,
                               EtaMax       = eta_max,
                               DoRangedPhi  = do_phi_ranged,
                               PhiMin       = phi_min,
                               PhiMax       = phi_max,
                               OutputLevel  = outputLevel)

    tape += part

    if args.pileup_avg > 0:

        pileup = Pileup("Pileup",
                        Pythia8("MBGenerator", 
                                File=mb_file,
                                Seed=seed),
                        EtaMax=3.2,
                        Select=2,
                        PileupAvg=pileup_avg,
                        PileupSigma=pileup_sigma,
                        BunchIdStart=bc_id_start,
                        BunchIdEnd=bc_id_end,
                        OutputLevel=outputLevel,
                        DeltaEta=0.22,
                        DeltaPhi=0.22,
                        )

        tape += pileup
    tape.run(events)


def get_events_per_job(args):
    if args.events_per_job is None:
        return ceil(args.number_of_events/args.number_of_threads)
    else:
        return args.events_per_job


def get_job_params(args, force:bool=False):
    if args.event_numbers:
        event_numbers_list = args.event_numbers.split(",")
        args.number_of_events = len(event_numbers_list)
        events_per_job = get_events_per_job(args)
        event_numbers = (
            event_numbers_list[start:start+events_per_job]
            for start in range(0, args.number_of_events, events_per_job)
        )
    else:
        events_per_job = get_events_per_job(args)
        event_numbers = (
            list(range(start, start+events_per_job))
            for start in range(0, args.number_of_events, events_per_job)
        )

    splitted_output_filename = args.output_file.split(".")
    for i, events in enumerate(event_numbers):
        output_file = splitted_output_filename.copy()
        output_file.insert(-1, str(i))
        output_file = '.'.join(output_file)
        if not force and os.path.exists(output_file):
            print(f"{i} - Output file {output_file} already exists. Skipping.")
            continue
        yield events, output_file



def merge(args):
    files = [f"{os.getcwd()}/{f}" for _, f in list(get_job_params(args, force=True))]
    if args.merge or len(files)==1:
        os.system(f"hadd -f {args.output_file} {' '.join(files)}")
        [os.remove(f) for f in files]


def run(args):
    pool = Parallel(n_jobs=args.number_of_threads)
    pool(delayed(main)(
        events=events,
        logging_level=args.output_level,
        output_file=output_file,
        run_number=args.run_number,
        seed=args.seed,
        particle=args.particle,
        eta=args.eta,
        phi=args.phi, 
        eta_min=args.eta_min,
        eta_max=args.eta_max,
        phi_min=args.phi_min,
        phi_max=args.phi_max,
        energy=args.energy,
        energy_min=args.energy_min,
        energy_max=args.energy_max,
        do_eta_ranged=args.do_eta_ranged,
        do_phi_ranged=args.do_phi_ranged,
        pileup_avg=args.pileup_avg,
        pileup_sigma=args.pileup_sigma,
        mb_file=args.pileup_file,
        bc_id_start=args.bc_id_start,
        bc_id_end=args.bc_id_end
    )
        for events, output_file in get_job_params(args))
    
    merge(args)




if __name__ == "__main__":
    parser=parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    run(args)