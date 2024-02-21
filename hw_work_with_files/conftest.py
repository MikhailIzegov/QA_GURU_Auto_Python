import os


CURRENT_FILE_PATH = os.path.dirname(__file__)
print(CURRENT_FILE_PATH)
PROJECT_ROOT_PATH = os.path.dirname(CURRENT_FILE_PATH)
print(PROJECT_ROOT_PATH)
TEMP_PATH = os.path.join(PROJECT_ROOT_PATH, 'temp')
