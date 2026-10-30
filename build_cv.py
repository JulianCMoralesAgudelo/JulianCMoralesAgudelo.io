"""Generate the CV using the reviewed two-page sidebar design."""
from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).with_name('build_cv_sidebar.py')), run_name='__main__')
