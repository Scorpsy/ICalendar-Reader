#!/usr/bin/env python3
#used for commandprompt


import sys
import argparse
import datetime
import copy



def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, help='file to be processed')
    parser.add_argument('--start', type=str, help='start of date range')
    parser.add_argument('--end', type=str, help='end of data range')

    args = parser.parse_args()

    print ('file: {}; start: {}; end: {}'.format( args.file, args.start,
        args.end))

    if not args.file:
        print("Need --file=<ics filename>")

    if not args.start:
        print("Need --start=dd/mm/yyyy")

    if not args.end:
        print("Need --end=dd/mm/yyyy")


    date_start = args.start.split('/')  #['06', '08','2019'] day / month / year
    date_end = args.end.split('/')      #['08', '09','2019'] day / month / year
    info = read_file(args.file,date_start,date_end)

    #format_dates(info)
    print_events(info)
    #print(print_events.rrule)
    #print(info)
    #print(len(info))

if __name__ == "__main__":
    main()