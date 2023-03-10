import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

manage = os.path.join(BASE_DIR, 'manage.py')
print(manage)
terminal_command = "python " +manage+ " update_ranker"
os.system(terminal_command)
terminal_command = "python " +manage+ " get_matchData"
os.system(terminal_command)
terminal_command = "python " +manage+ " rank_unit"
os.system(terminal_command)
terminal_command = "python " +manage+ " deck_statistics"
os.system(terminal_command)
terminal_command = "python " +manage+ " deck_double"
os.system(terminal_command)