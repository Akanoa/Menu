#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

MIGRATION_FILE = 'migrations/create_tables.sql'
EXIT_ERROR   = 2
EXIT_WARNING = 1
EXIT_SUCCESS = 0


def migration_task():
    print "%s Starting tables creation"%(unichr(0x25ba).encode('utf-8'))

    conn = sqlite3.connect('application.db')

    c = conn.cursor()
    with open(MIGRATION_FILE) as fd:
        migration = "".join(fd.readlines())

    try:
        c.executescript(migration)
    except sqlite3.OperationalError, e:
        print "  %s Something has failed during tables creation"%(unichr(0x00d7).encode('utf-8'))
        print str(e)
        return EXIT_ERROR

    conn.commit()
    conn.close()
    print "  %s Tables creation done with success"%(unichr(0x2713).encode('utf-8'))
    return EXIT_SUCCESS

tasks = [migration_task]

def install():
    for task in tasks:
        return_value = task()
        if return_value:
            print "  %s Installation failed"%(unichr(0x00d7).encode('utf-8'))
            exit(EXIT_ERROR)
    print "-"*80
    print "%s Install success"%(unichr(0x2713).encode('utf-8'))
    print "-"*80
install()

