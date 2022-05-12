# normally run with "conda index" or bin/conda-index
# CONDA_DEBUG=1 python -m conda_build index --verbose ...
import logging

# sets up timestamped log lines nicely but can conflict with conda logging by
# printing messages twice
logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
    level=logging.INFO
)
import conda_build.cli.main_index   # must import *after* logging config
conda_build.cli.main_index.main()
