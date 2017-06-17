#!/usr/bin/python

import glob
import os

print "Running batch upload script\nFollow the following carefully\n1.Paste the dsym folder inside your PROJECT'S MAIN  directory.\n2.Paste this script inside dSYM folder\n3.Follow carefully."


BASE_DIR =  os.path.dirname(os.getcwd())
GLOBAL_BASE_DIR =  BASE_DIR+'/'
print(GLOBAL_BASE_DIR)

files = []
for root, dirnames, filenames in os.walk(GLOBAL_BASE_DIR):
    files.extend(glob.glob(root + "*/GoogleService-Info.plist"))
if not files:
    print("Can't find 'GoogleService-Info.plist', please place 'GoogleService-Info.plist' in your project directory")
    exit(1)


path_to_google_info_file = files[0]

files = []

for root, dirnames, filenames in os.walk(GLOBAL_BASE_DIR):
    files.extend(glob.glob(root + "*/Info.plist"))
if not files:
    print("Can't find your project's 'Info.plist' in your project directory")
    exit(1)

path_to_project_info_file = files[0]

files = []

for root, dirnames, filenames in os.walk(GLOBAL_BASE_DIR):
    files.extend(glob.glob(root + "*/ServiceKey.json"))
if not files:
    print("Can't find your Google's 'ServiceKey.json' in your project directory")
    exit(1)


path_to_servicekey_file = files[0]


files = []

for root, dirnames, filenames in os.walk(GLOBAL_BASE_DIR):
    files.extend(glob.glob(root + "*/batch-upload"))
if not files:
    print("Can't find FirebaseCrash Installed")
    exit(1)

path_to_batch_upload = files[0]


# path_to_batch_upload = '"{0}"'.format(path_to_batch_upload)
path_to_batch_upload = path_to_batch_upload.replace(" ", "\ ")
# path_to_project_info_file = path_to_project_info_file.replace(" ", "\ ")
# path_to_google_info_file = path_to_google_info_file.replace(" ", "\ ")
# path_to_servicekey_file = path_to_servicekey_file.replace(" ", "\ ")

path_to_project_info_file = '"{0}"'.format(path_to_project_info_file)
path_to_google_info_file = '"{0}"'.format(path_to_google_info_file)
path_to_servicekey_file = '"{0}"'.format(path_to_servicekey_file)

print path_to_batch_upload
print path_to_project_info_file
print path_to_google_info_file
print path_to_servicekey_file

print "Files read successfully"

dsym_files = glob.glob('./*.dSYM')

print "Uploading dSYM files.."

for file_name in dsym_files:
    file_name_without_extension = file_name[2:].split('.')[0]
    # print "Uploading file '" + file_name_without_extension + "'.."
    try:
        print(path_to_batch_upload + ' -i ' + path_to_project_info_file + ' -p ' + path_to_google_info_file + ' ' + path_to_servicekey_file + ' "' + file_name_without_extension + '"')
        os.system(path_to_batch_upload + ' -i ' + path_to_project_info_file + ' -p ' + path_to_google_info_file + ' ' + path_to_servicekey_file + ' "' + file_name_without_extension + '"')
    except:
        print "Failed to upload file '" + file_name_without_extension + "'"

print "Files uploaded successfully"
