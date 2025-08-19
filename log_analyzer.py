# log_analyzer.py

import re
import pandas as pd
from collections import defaultdict

LOG_FILE = 'bot_activity.log'

def parse_log_file(log_file_path):
    """
    Parses the bot activity log to extract generated trade plans.
    """
    print(f"Analyzing log file: {log_file_path}...")
    
    # Regex to find lines containing a full trade p
