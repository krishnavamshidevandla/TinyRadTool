

import numpy as np
import  src.cmd_modules.TinyRad as TinyRad

# --------------------------------------------------
# Connect to radar
# --------------------------------------------------
Brd = TinyRad()

Brd.BrdRst()
Brd.RfRxEna()

# Enable TX1 at full power
Brd.RfTxEna(1, 100)

# --------------------------------------------------
# Configuration
# --------------------------------------------------

dCfg = dict()

dCfg["fStrt"]      = 24.00e9
dCfg["fStop"]      = 24.25e9

dCfg["TRampUp"]    = 1.024e-3      # 1.024 ms
dCfg["Perd"]       = 1.10e-3       # slightly larger than TRampUp

dCfg["N"]          = 1024          # samples/chirp

dCfg["Seq"]        = [1]
dCfg["CycSiz"]     = 1

# start small first
dCfg["FrmMeasSiz"] = 128

# --------------------------------------------------
# Configure radar
# --------------------------------------------------

print("Configuring radar...")

Brd.RfMeas(dCfg)

print("Configuration accepted")

# --------------------------------------------------
# Acquire one frame
# --------------------------------------------------

print("Acquiring frame...")

Dat = Brd.BrdGetData()

print("Frame acquired")

# --------------------------------------------------
# Inspect shape
# --------------------------------------------------

print("Shape:", Dat.shape)
print("dtype:", Dat.dtype)

print("Min:", np.min(Dat))
print("Max:", np.max(Dat))

# --------------------------------------------------
# Save
# --------------------------------------------------

np.save("frame.npy", Dat)

print("Saved frame.npy")