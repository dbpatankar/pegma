from .pegma.main import run_app
from .pegma.plotConfig import plotConfigFiles

data = []
dataDict = {
    "data": data,
    "plotConfigFiles": plotConfigFiles
}
run_app()