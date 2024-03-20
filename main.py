import logging

# ANSI escape codes for colors
COLORS = {
    'HEADER': '\033[95m',
    'OKBLUE': '\033[94m',
    'OKCYAN': '\033[96m',
    'OKGREEN': '\033[92m',
    'WARNING': '\033[93m',
    'FAIL': '\033[91m',
    'ENDC': '\033[0m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m'
}

def setup_logging():
    # Create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create console handler and set level to debug
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create formatter with colored output
    class ColoredFormatter(logging.Formatter):
        def format(self, record):
            log_color = ''
            if record.levelname == 'DEBUG':
                log_color = COLORS['OKBLUE']
            elif record.levelname == 'INFO':
                log_color = COLORS['OKGREEN']
            elif record.levelname == 'WARNING':
                log_color = COLORS['WARNING']
            elif record.levelname == 'ERROR':
                log_color = COLORS['FAIL']
            elif record.levelname == 'CRITICAL':
                log_color = COLORS['FAIL'] + COLORS['BOLD']
            msg = super().format(record)
            return f"{log_color}[function: {record.funcName}] {msg}{COLORS['ENDC']}"

    formatter = ColoredFormatter('%(asctime)s - %(message)s')

    # Add formatter to console handler
    console_handler.setFormatter(formatter)

    # Add console handler to logger
    logger.addHandler(console_handler)

    return logger

def main123():
    logger = setup_logging()

    # Logging examples
    try:
        x = 0/0
    except Exception as e:
        logger.debug(f'This is a debug message: {e}')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

if __name__ == "__main__":
    main123()
