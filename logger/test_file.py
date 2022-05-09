from logger import Logger
from inspect import currentframe, getframeinfo

if __name__ == "__main__":
    Logger.settings(save_bool=True)
    Logger.INFO("info-1", "info-2")
    Logger.WARNING("warning-1", "warning-2")
    Logger.ERROR("ERROR")

    