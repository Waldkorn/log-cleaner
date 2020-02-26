#!/usr/bin/python3
from datetime import date, datetime

from os import listdir, remove, removedirs
from os.path import basename, dirname, isdir, isfile, islink, join

import tarfile


def main():
    log_folder = '/var/www/python/tmp'
    archive_folder = '/var/www/python/tmp/archive'
    days_to_keep_archives = 7

    current_date = get_current_date()
    make_archive_of_current_logs(get_file_names_in_folder(log_folder, 'log'), archive_folder, current_date)
    remove_old_archives(archive_folder, current_date, days_to_keep_archives)


def make_archive_of_current_logs(file_names, archive_folder, current_date):
    with tarfile.open(join(archive_folder, current_date) + ".tar.gz", "w:gz") as tar:
        for file_name in file_names:
            tar.add(file_name, arcname=file_name)
    remove_old_logs(file_names)


def remove_old_logs(file_names):
    for file_name in file_names:
        remove(file_name)
        if len(listdir(dirname(file_name))) == 0 and not islink(dirname(file_name)):
            removedirs(dirname(file_name))


def remove_old_archives(archive_folder, current_date, days_to_keep_archives):
    archives = get_file_names_in_folder(archive_folder, 'tar.gz')
    current_date = datetime.strptime(current_date, '%d-%m-%Y')
    for archive in archives:
        file_name = archive.replace(archive_folder + '/', '').replace('.tar.gz', '')
        file_date = datetime.strptime(file_name, '%d-%m-%Y')
        if (current_date - file_date).days > days_to_keep_archives:
            remove(archive)


def get_file_names_in_folder(log_folder, extension):
    files = get_file_names_recursive(log_folder)
    return [join(log_folder, file) for file in files if isfile(join(log_folder, file)) and file.endswith('.' + extension)]


def get_file_names_recursive(log_folder):
    files = []
    for x in listdir(log_folder):
        if isdir(join(log_folder, x)):
            files.extend(get_file_names_recursive(join(log_folder, x)))
        elif isfile(join(log_folder, x)):
            files.append(join(log_folder, x))
    return files


def get_current_date():
    return date.today().strftime("%d-%m-%Y")    


if __name__ == "__main__":
    main()
