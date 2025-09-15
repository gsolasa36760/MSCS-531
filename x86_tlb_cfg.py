# lab/x86_tlb_cfg.py
from m5.objects import *
from configs.deprecated.example.se import *
import os, sys
GEM5_ROOT = os.path.expanduser('~/gem5')   # adjust if needed
sys.path.insert(0, GEM5_ROOT)              # enables `import configs`
sys.path.insert(0, os.path.join(GEM5_ROOT, 'configs'))  # enables `import common`

if __name__ == "__m5_main__":
    (options, args) = get_options()
    root = build_test_system(options, None, None, Ruby=False)
    # Set ITLB/DTLB entries per core (simple in-order CPU has single core here)
    itb = int(getattr(options, "itb_entries", 64))
    dtb = int(getattr(options, "dtb_entries", 64))
    root.system.cpu[0].mmu.itb.size = itb
    root.system.cpu[0].mmu.dtb.size = dtb
    m5.instantiate()
    exit_event = m5.simulate()
    print("Exiting @ tick {} because {}".format(m5.curTick(), exit_event.getCause()))
