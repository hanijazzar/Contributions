#!/usr/bin/python

import glob
import os

print "Running batch upload.. Please make sure to run this script from the project directory"

path_to_project_info_file = raw_input("Please enter path to 'project-info.plist': ")
path_to_google_info_file = raw_input("Please enter path to 'google-info.plist': ")
path_to_servicekey_file = raw_input("Please enter path to 'google-servicekey.json': ")

print "Reading files.."

with open(path_to_project_info_file, "r") as myfile:
    project_info_file = myfile.read()

with open(path_to_google_info_file, "r") as myfile:
    google_info_file = myfile.read()

with open(path_to_servicekey_file, "r") as myfile:
    service_key_file = myfile.read()

wrong_input = False

if project_info_file == "":
    print "Cannot read project's info.plist file"
    wrong_input = True
if google_info_file == "":
    print "Cannot read google-info.plist file"
    wrong_input = True
if service_key_file == "":
    print "Cannot read serviceKey-file.json"
    wrong_input = True

if wrong_input:
    print "Error reading file(s), exiting.."
    exit(1)

print "Files read successfully"

dysm_files = glob.glob('./*.dysm')

print "Uploading DYSM files.."

for file_name in dysm_files:
    file_name_without_extension = file_name[2:].split('.')[0]
    print "Uploading " + file_name_without_extension

    os.system("../Pods/FirebaseCrash/batch-upload -i " + path_to_project_info_file + " -p " +
              path_to_google_info_file + " " + path_to_servicekey_file + " " + file_name_without_extension)

    print "File" + file_name_without_extension + " Uploaded Successfully"

print "Files uploaded successfully"

