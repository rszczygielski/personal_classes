from logger import Logger

if __name__ == "__main__":
    logger = Logger()
    logger.INFO("abc", "efg")
    logger.WARNING("dfas", "dfa")
    logger.ERROR("1234")
    print()
    logger.settings(show_date=False)
    logger.INFO("abc", "efg")
    logger.WARNING("dfas", "dfa")
    logger.ERROR("1234")
    print()
    logger.settings(showLog_level=False, )
    logger.INFO("abc", "efg")
    logger.WARNING("dfas", "dfa")
    logger.ERROR("1234")
    print()
    logger.settings(showLog_level=False, show_date=False)
    logger.INFO("abc", "efg")
    logger.WARNING("dfas", "dfa")
    logger.ERROR("1234")



