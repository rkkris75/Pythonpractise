#=======================================================================================================================
#!/usr/bin/env python
#title           :oper_conf.py
#description     :Updates to operational.conf with distcp blockset that would target holdem and war clusters
# author            date                version
#rakrishn           2019-12-10          Initial Version
#=======================================================================================================================

import os,fileinput,re

def bulk_update(file_name,check_str,check_str_ins,dir_list,dir_name):
    """Updates operational.conf with distcp blockset that would hit holdem and war clusters.
    Args :
        dir_name : Pass the complete dir for the function to lookup for operational.conf.
        file_name : File name that needs to be updated.
        check_str : Check for the string that exists, if it does, then skip the file update.
        dir_list :  List of dirs that needs to be excluded from updates.
        check_str_ins : Check for the string where the file needs to be amended right beneath the check string.

    Returns :
        Print traces the list of files that got updated with distcp and as well as the the dir
        didn't get updated with complete path
    """
    file_nm = file_name
    check_str_exists = check_str
    chek_str_insert = check_str_ins
    dir_list = dir_list
    for root, dirs, files in os.walk(dir_name):
        for words in dir_list:
            dir_join = dir_name + words
            if root != dir_join:
                for file in files:
                    if file == file_nm:
                        ## Check if distcp already exists, if it does, skip
                        if check_str_exists in open(os.path.join(root, file)).read():
                            print("{1} block already exists on {0}, so skipping file from updates".format(os.path.join(root,file),check_str))
                            break
                        else:
                            # print(os.path.join(root, file))
                            inputfile = open(os.path.join(root, file), 'r').readlines()
                            write_file = open(os.path.join(root, file), 'w')
                            for lines in inputfile:
                                write_file.write(lines)
                                if chek_str_insert in lines:
                                    write_file.write("\n\tdistcp: {")
                                    write_file.write("\n\t\tenable: true")
                                    write_file.write("\n\t\ttargetClusters: [holdem, war]")
                                    write_file.write("\n\t\tignoreFailure: false")
                                    write_file.write("\n\t}\n")
                            print("{} file updated successfully".format(os.path.join(root,file)))
                        write_file.close()
            else:
                print("No need to update the file, as the distcp block already exists in {}".format(os.path.join(root)))
            # else:
            #     break

##Instantiating function call
if __name__ == "__main__":
    file_name = 'operational.conf'
    check_str = 'distcp:'
    check_str_ins = 'output.acl.owner = data_svc'
    dir_list = ['agg_mars_daily_derived', 'dim_gco_source_v2']
    dir_list_scan = ['/Users/rakrishn/projects/dist_cp_bulk_update/dimension-defs_trunk/dimension-defs/src/foundation-datasets/'
                     ,'/Users/rakrishn/projects/dist_cp_bulk_update/dimension-defs_trunk/dimension-defs/src/hp/foundation-datasets/'
                     ]
    for dir_list_upd in dir_list_scan:
        bulk_update(file_name,check_str,check_str_ins,dir_list,dir_list_upd)