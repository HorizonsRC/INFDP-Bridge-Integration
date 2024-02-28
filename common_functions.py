import logging
import configparser

# This file is for functions that are very generic

def output_string_to_file(file_name, file_contents, mode):
    file = open(str(file_name), mode)
    file.write(str(file_contents))
    file.close()

def init_logger(log_level, name):

    if log_level == "info":
        log_level = logging.INFO
    elif log_level == "warning":
        log_level = logging.WARNING
    else:
        log_level = logging.DEBUG
        
    logging.basicConfig(level=log_level,
                format='%(asctime)s : %(levelname)s : %(message)s',
                handlers=[logging.FileHandler(name+".log"),
                          logging.StreamHandler()])
    
    logging.info(f"Starting {name}...")
    
def load_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config