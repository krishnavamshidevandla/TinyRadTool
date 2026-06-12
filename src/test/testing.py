

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

dCfg["fStrt"] = 24.00e9
dCfg["fStop"] = 24.25e9

dCfg["TRampUp"] = 1.024e-3

# give plenty of margin
dCfg["Perd"] = 1.5e-3

dCfg["N"] = 1024

dCfg["Seq"] = [1]

dCfg["CycSiz"] = 1

dCfg["FrmMeasSiz"] = 64
dCfg["FrmSiz"] = 64

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
