from settings import DB,DB_BACKUP,DB_ACTIVITY,PATH_LOG
import os
if os.path.exists(DB):
    os.remove(DB)
if os.path.exists(DB_BACKUP):
    os.remove(DB_BACKUP)
if os.path.exists(DB_ACTIVITY):
    os.remove(DB_ACTIVITY)
if os.path.exists(PATH_LOG):
    os.remove(PATH_LOG)