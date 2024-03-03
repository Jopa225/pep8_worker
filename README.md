# pep8_worker
Usage

The pep8_reworker python file takes two arguments:
First one is "--folder_path", "-f" folder path.

Run PEP8 parser on a target folder:

python .\pep8_reworker.py -f pep8_folders

This creates temporary files with sufix "_temp" with changes made from pep8 worker.

Second argument is "--apply_changes", "-a"

python .\pep8_reworker.py -f pep8_folders -a

This applies changes to original file and removes the "_temp" file. 
