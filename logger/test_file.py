from logger import Logger

if __name__ == "__main__":
    logger = Logger()
    logger.settings(save_bool=True)
    logger.INFO("info-1", "info-2")
    logger.WARNING("warning-1", "warning-2")
    logger.ERROR("ERROR")
    