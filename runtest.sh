#!/bin/sh

# clean up from previous runs if necessary
\rm -rf testrun1 testrun2

# create staging area for new test runs
\cp -r testdata1 testrun1
\cp -r testdata2 testrun2


# run tests
./playlist_sequencer.py testrun1
./playlist_sequencer.py testrun2

# display test results
ls -l testrun1
ls -l testrun2
