playlist_sequencer


Fixes (renames) music and podcast files so that mp3 players will play numerically named files in the (proper) lexical order

Running playlist_sequencer:

./playlist_sequencer.py <dir>

Directory must contain similar named files and it will pre-append a letter code to each file so that they can be played on a mp3 player in the correct order

Testing:

To test the playlist sequencer run the runtest.sh script.

===============================================

Problem statement:

When playing a series of multiple music files that are numbered some mp3 players do not play them in the correct order, this is because there is a difference between lexical and numerical listings.

Most file management systems use lexical ordering of files and this can be a problem.


Here is an example which will illustrate the problem:

For the list of files below

Disk10_Track1.mp3 Disk1_Track1.mp3  Disk2_Track1.mp3  Disk3_Track1.mp3  Disk3_Track1.mp3  Disk5_Track1.mp3  Disk6_Track1.mp3  Disk7_Track1.mp3  Disk8_Track1.mp3  Disk9_Track1.mp3
Disk10_Track2.mp3 Disk1_Track2.mp3  Disk2_Track2.mp3  Disk3_Track2.mp3  Disk3_Track2.mp3  Disk5_Track2.mp3  Disk6_Track2.mp3  Disk7_Track2.mp3  Disk8_Track2.mp3  Disk9_Track2.mp3

My mp3 player will play these files in this order:


Disk10_Track1.mp3
Disk10_Track2.mp3
Disk1_Track1.mp3
Disk1_Track2.mp3
Disk2_Track1.mp3
Disk2_Track2.mp3
Disk3_Track1.mp3
Disk3_Track2.mp3
Disk4_Track1.mp3
Disk4_Track2.mp3
Disk5_Track1.mp3
Disk5_Track2.mp3
Disk6_Track1.mp3
Disk6_Track2.mp3
Disk7_Track1.mp3
Disk7_Track2.mp3
Disk8_Track1.mp3
Disk8_Track2.mp3
Disk9_Track1.mp3
Disk9_Track2.mp3

The playlist_sequencer will examine the files in a directory and pre-append a letter code to each file so that the files are in the correct order when viewed lexically.  
After running the playlist_sequencer on the list of files my mp3 player will play the files in this order:


aaa_Disk1_Track1.mp3
aab_Disk1_Track2.mp3
aac_Disk2_Track1.mp3
aad_Disk2_Track2.mp3
aae_Disk3_Track1.mp3
aaf_Disk3_Track2.mp3
aag_Disk4_Track1.mp3
aah_Disk4_Track2.mp3
aai_Disk5_Track1.mp3
aaj_Disk5_Track2.mp3
aak_Disk6_Track1.mp3
aal_Disk6_Track2.mp3
aam_Disk7_Track1.mp3
aan_Disk7_Track2.mp3
aao_Disk8_Track1.mp3
aap_Disk8_Track2.mp3
aaq_Disk9_Track1.mp3
aar_Disk9_Track2.mp3
aas_Disk10_Track1.mp3
aat_Disk10_Track2.mp3


