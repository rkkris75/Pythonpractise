#=======================================================================================================================
#!/usr/bin/env python
#title           :oper_conf.py
#description     :Updates to operational.conf with distcp blockset that would target holdem and war clusters
#author            date                version
#rakrishn           2019-12-10          Initial Version
#=======================================================================================================================

import os,fileinput,re

def bulk_update(file_name,check_str,check_str_ins,exclusion_list,dir_name,loop_break,num_pct_check,num_flow_to_process,loop_break_threshold):
    """Updates operational.conf with distcp blockset that would hit holdem and war clusters.
    Args :
        dir_name : Pass the complete dir for the function to lookup for operational.conf.
        file_name : File name that needs to be updated.
        check_str : Check for the string that exists, if it does, then skip the file update.
        dir_list :  List of dirs that needs to be excluded from updates.
        check_str_ins : Check for the string where the file needs to be amended right beneath the check string.
        exclusion_list : List of flows that doesn't need to be processed.
        dir_name : List of absolute paths, could be array, eg.[dir1,dir].
        loop_break : Paramemter for variable check to break the os.walk() outer loop, if the number of flows to process
                    is satisfied.
        num_pct_check : Param to break the file processing loop.
        num_flow_to_process : Params that dictates to process the n number of files, it is derived
                    based on the user inputs.
        loop_break_threshold : Some high random number to break the outer os.walk method call, to exit the process.
    Returns :
        Print traces the list of files that got updated with distcp and as well as the the dir
        didn't get updated with complete path
    """
    file_nm = file_name
    check_str_exists = check_str
    chek_str_insert = check_str_ins
    exclusion_list = exclusion_list
    loop_break = loop_break
    num_pct_check = num_pct_check
    num_flow_to_process = num_flow_to_process
    for root, dirs, files in os.walk(dir_name):
        flow_name = root[root.rindex("/") + 1:]
        loop_break += 1
        if loop_break < loop_break_threshold: ## This if condition is to exit the process if the set threshold limit is met
            if flow_name not in exclusion_list:
                for file in files:
                    if file == file_nm:
                        ## Check if distcp already exists, if it does, skip
                        if check_str_exists in open(os.path.join(root, file)).read():
                            print("{1} block already exists on {0}, so skipping file from updates".format(os.path.join(root,file),check_str[:check_str.index(":")]))
                            break
                        else:
                            # print(os.path.join(root, file))
                            inputfile = open(os.path.join(root, file), 'r').readlines()
                            write_file = open(os.path.join(root, file), 'w')
                            num_pct_check += 1
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
                            if num_pct_check > (num_flow_to_process-1): ## This is the number of flows to process based on the pct
                                loop_break = loop_break_threshold+1 # force exit the outer thresold check loop
                                break
            else:
                print("{} Flow is part of exclusion list".format(flow_name))
        else:
            print("Number of file processing is exceeded the input limit, so exiting the process")
            break
    # else:
    #     break

##Instantiating function call
if __name__ == "__main__":
    loop_break = 0
    num_pct_check = 0
    loop_break_threshold = 100000
    num_flows = int(input("Total number of flows in whole numbers:"))
    inp_pct = int(input("Please input the percentage of data set that you wanna process in whole numbers:"))
    num_flow_to_process = round(num_flows * (inp_pct / 100))
    print("Number of flows to process is {}".format(num_flow_to_process))
    file_name = 'operational.conf'
    check_str = 'distcp:'
    check_str_ins = 'output.acl.owner = data_svc'
    exclusion_list = ['agg_mars_daily_derived', 'dim_gco_source_v2']
    dir_list_scan = ['/Users/rakrishn/projects/dist_cp_bulk_update/dimension-defs_trunk/dimension-defs/src/foundation-datasets/'
#                     ,'/Users/rakrishn/projects/dist_cp_bulk_update/dimension-defs_trunk/dimension-defs/src/hp/foundation-datasets/'
                     ]
    for dir_list_upd in dir_list_scan:
        bulk_update(file_name,check_str,check_str_ins,exclusion_list,dir_list_upd,loop_break,num_pct_check,num_flow_to_process,loop_break_threshold)