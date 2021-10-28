#!/usr/bin/env python3

from logger import Logger

log = Logger().logger

def main():

    log.debug('This is a DEBUG msg')
    log.info('This is an INFO msg')
    log.warning('This is a WARNING msg')
    log.error('This is an ERROR msg')
    log.critical('This is a CRITICAL msg')

if __name__ == "__main__":
    main()
