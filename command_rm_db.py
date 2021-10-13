from settings import DB,DB_BACKUP,DB_ACTIVITY
import os
if os.path.exists(DB):
    os.remove(DB)
if os.path.exists(DB_BACKUP):
    os.remove(DB_BACKUP)
if os.path.exists(DB_ACTIVITY):
    os.remove(DB_ACTIVITY)