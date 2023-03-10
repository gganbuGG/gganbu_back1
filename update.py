import os

terminal_command = "python manage.py update_ranker"
os.system(terminal_command)
terminal_command = "python manage.py get_matchData"
os.system(terminal_command)
terminal_command = "python manage.py rank_unit"
os.system(terminal_command)
terminal_command = "python manage.py deck_statistics"
os.system(terminal_command)
terminal_command = "python manage.py deck_double"
os.system(terminal_command)