################################################################################
## PEGMA
## Copyright (C) 2023  Digvijay Patankar
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <https://www.gnu.org/licenses/>.
################################################################################
import os
from pathlib import Path
import matplotlib as mpl

mplConfigDir = mpl.get_configdir()
pegmaConfigDir = Path(mplConfigDir).parent / "pegma"

if not pegmaConfigDir.exists():
    os.makedirs(pegmaConfigDir)

tsConfigFile = pegmaConfigDir / "_ts.rc"
itsConfigFile = pegmaConfigDir / "_its.rc"
iitsConfigFile = pegmaConfigDir / "_iits.rc"
psaConfigFile = pegmaConfigDir / "_psa.rc"
tripartiteConfigFile = pegmaConfigDir / "_tripartite.rc"
fsAmpConfigFile = pegmaConfigDir / "_fsAmp.rc"
psAmpConfigFile = pegmaConfigDir / "_psAmp.rc"
fsPhaseConfigFile = pegmaConfigDir / "_fsPhase.rc"
fsUnwrappedPhaseConfigFile = pegmaConfigDir / "_fsUnwrappedPhase.rc"
designSpectrumConfigFile = pegmaConfigDir / "_designSpec.rc"
stretchedTsConfigFile = pegmaConfigDir / "_stretchedTsConfig.rc"
stretchedFsConfigFile = pegmaConfigDir / "_stretchedFsConfig.rc"
stretchedRsConfigFile = pegmaConfigDir / "_stretchedRsConfig.rc"

plotConfigFiles = {
    "ts": tsConfigFile,
    "its": itsConfigFile,
    "iits": iitsConfigFile,
    "psa": psaConfigFile,
    "tripartite": tripartiteConfigFile,
    "fsAmp": fsAmpConfigFile,
    "psAmp": psAmpConfigFile,
    "fsPhase": fsPhaseConfigFile,
    "fsUnwrappedPhase": fsUnwrappedPhaseConfigFile,
    "designSpectrum": designSpectrumConfigFile,
    "stretchedTs": stretchedTsConfigFile,
    "stretchedFs": stretchedFsConfigFile,
    "stretchedRs": stretchedRsConfigFile,
}

