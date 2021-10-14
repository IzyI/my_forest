import logging
import logging.config
import coloredlogs
import os
import sys
from settings import COLOR_CONSOLE, LEVEL_LOG, PATH_LOG


def setup_logging(filename="alog.log", default_level=logging.INFO, color_console=False):
    logging.basicConfig(
        filename=filename,
        level=default_level,
        format='[%(asctime)s] %(name)s[%(process)d] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )
    if color_console:
        coloredlogs.install(level=default_level, fmt='[%(asctime)s] %(name)s[%(process)d] %(levelname)s %(message)s')
    logging.getLogger("requests").setLevel(logging.ERROR)
    logging.getLogger("urllib3").setLevel(logging.ERROR)


setup_logging(filename=PATH_LOG,color_console=COLOR_CONSOLE, default_level=LEVEL_LOG)
ROOT_PATH = os.path.abspath(os.path.dirname(sys.argv[0]))
alog = logging.getLogger("alog")
