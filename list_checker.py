#=======================================================================================================================
#!/usr/bin/env python
#title           :oper_conf.py
#description     :Updates to operational.conf with distcp blockset that would target holdem and war clusters
# author            date                version
#rakrishn           2019-12-10          Initial Version
#=======================================================================================================================

import os,fileinput,re

file_nm = 'operational.conf'
check_str_exists = 'distcp:'
chek_str_insert = 'output.acl.owner = data_svc'
dir_name = '/Users/rakrishn/projects/dist_cp_bulk_update/dimension-defs_trunk/dimension-defs/src/foundation-datasets/'
dir_list = ['agg_mars_daily_derived','dim_gco_source_v2']

# print(dir_list)
# print(dir_append)
# print(dir_append.concat(dir_list))

list_num = ['1','2','3']
list_join = ','



for root, dirs, files in os.walk(dir_name):
    for words in dir_list:
        dir_join = dir_name + words
        if root != dir_join:
            print("Processing")
        else:
            print("Skipping")
# for root, dirs, files in os.walk(dir_name):
#     print("Root name is {}".format(root))
#     print("dirs name is {}".format(dirs))
#     print("file name is {}".format(files))
    # for file in files:
    #     if file == file_nm:
    #         ## Check if distcp already exists, if it does, skip
    #         if check_str_exists in open(os.path.join(root, file)).read():
    #             print("Distcp already exists on {}, so skipping file from updates".format(os.path.join(root,file)))
    #             break
    #         else:
    #             print(os.path.join(root, file))
    #             inputfile = open(os.path.join(root, file), 'r').readlines()
    #             write_file = open(os.path.join(root, file), 'w')
    #             for lines in inputfile:
    #                 write_file.write(lines)
    #                 if chek_str_insert in lines:
    #                     write_file.write("\n\tdistcp: {")
    #                     write_file.write("\n\t\tenable: true")
    #                     write_file.write("\n\t\ttargetClusters: [holdem, war]")
    #                     write_file.write("\n\t\tignoreFailure: false")
    #                     write_file.write("\n\t}\n")
    #             print("{} file updated successfully".format(os.path.join(root,file)))
    #         write_file.close()