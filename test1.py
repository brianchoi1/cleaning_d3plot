import os
check_path = 'E:\\d3plot_backup\\1. Drop\\GDOR3'
remainlist_filter = ['d3plot', 'd3plot01', 'd3plot05', 'd3plot10', 'd3plot15', 'd3plot20', 'd3plot25',
'd3plot30', 'd3plot35', 'd3plot40', 'd3plot45', 'd3plot50', 'd3plot55', 'd3plot60',
'd3plot65', 'd3plot70', 'd3plot75', 'd3plot80', 'd3plot85', 'd3plot90', 'd3plot95',
'd3plot100', 'd3plot105', 'd3plot110', 'd3plot115', 'd3plot120', 'd3plot125', 'd3plot130',
'd3plot135', 'd3plot140', 'd3plot145', 'd3plot150', 'd3plot155', 'd3plot160', 'd3plot165', 'd3plot170', 'd3plot175',
'd3plot180', 'd3plot185', 'd3plot190', 'd3plot195', 'd3plot200', 'd3plot205', 'd3plot210', 'd3plot215', 'd3plot220',
'd3plot225', 'd3plot230', 'd3plot235', 'd3plot240', 'd3plot245', 'd3plot250', 'd3plot255', 'd3plot260', 'd3plot265', 'd3plot270',
'd3plot275', 'd3plot280', 'd3plot285', 'd3plot290', 'd3plot295', 'd3plot300', 'd3plot305', 'd3plot310', 'd3plot315', 'd3plot320',
'd3plot325', 'd3plot330', 'd3plot335', 'd3plot340', 'd3plot345', 'd3plot350', 'd3plot355', 'd3plot360', 'd3plot365',
'd3plot370', 'd3plot375', 'd3plot380', 'd3plot385', 'd3plot390', 'd3plot395', 'd3plot400', 'd3plot405', 'd3plot410',
'd3plot415', 'd3plot420', 'd3plot425', 'd3plot430', 'd3plot435', 'd3plot440', 'd3plot445', 'd3plot450', 'd3plot455', 'd3plot460',
'd3plot465', 'd3plot470', 'd3plot475', 'd3plot480', 'd3plot485', 'd3plot490', 'd3plot495', 'd3plot500', 'd3plot505', 'd3plot510',
'd3plot515', 'd3plot520', 'd3plot525', 'd3plot530', 'd3plot535', 'd3plot540', 'd3plot545', 'd3plot550', 'd3plot555',
'd3plot560', 'd3plot565', 'd3plot570', 'd3plot575', 'd3plot580', 'd3plot585', 'd3plot590', 'd3plot595', 'd3plot600',
'd3plot605', 'd3plot610', 'd3plot615', 'd3plot620', 'd3plot625', 'd3plot630', 'd3plot635', 'd3plot640', 'd3plot645', 'd3plot650',
'd3plot655', 'd3plot660', 'd3plot665', 'd3plot670', 'd3plot675', 'd3plot680', 'd3plot685', 'd3plot690', 'd3plot695', 'd3plot700']

key_k = 1
key_lsflog = 1
key_binout = 0
key_d3dump = 1
key_d3thdt = 1
key_dynain = 1
# key_dynain_ini = 1
key_mes0000 = 1
key_messag = 1
key_runrsf = 1
key_status = 1
key_glstat = 1
key_cfile = 1


d3plot_list = []
remainlist_full = []

for (path,dir,files) in os.walk(check_path):
    for elem in files :
        if 'd3plot' in elem:
            try:
                d3plot_list.append(elem.split('.')[1])
            except:
                d3plot_list.append(elem.split('.')[0])

pos = []
for i in range(len(d3plot_list)):
    if d3plot_list[i] == 'd3plot':
        pos.append(i)
pos.append(len(d3plot_list))

for pp in pos:
    if not pp == 0:
        remainlist_filter.append(d3plot_list[pp - 1]) 


for (path,dir,files) in os.walk(check_path):
    for elem in files :
        if 'd3plot' in elem:
            try:
                remainlist_full.append(elem.split('.')[1])
            except:
                remainlist_full.append(elem.split('.')[0])
        if key_k == 1:
            try:
                if 'k' == elem.split('.')[1] or 'key' == elem.split('.')[1] or 'dyn' == elem.split('.')[1]:
                    remainlist_filter.append(elem)
            except:
                if 'k' == elem.split('.')[0] or 'key' == elem.split('.')[0] or 'dyn' == elem.split('.')[0]:
                    remainlist_filter.append(elem)
        if key_lsflog == 1:
            try:
                if 'lsflog' in elem.split('.')[1]:
                    remainlist_filter.append(elem)
            except:
                if 'lsflog' in elem.split('.')[0]:
                    remainlist_filter.append(elem)
        if key_binout == 1:
            try:
                if 'binout' in elem.split('.')[1]:
                    remainlist_filter.append(elem)
            except:
                if 'binout' in elem.split('.')[0]:
                    remainlist_filter.append(elem)
        if key_d3dump == 1:
            try:
                if 'd3dump' in elem.split('.')[1]:
                    remainlist_filter.append(elem)
            except:
                if 'd3dump' in elem.split('.')[0]:
                    remainlist_filter.append(elem)
        if key_d3thdt == 1:
            try:
                if 'd3thdt' in elem.split('.')[1]:
                    remainlist_filter.append(elem)
            except:
                if 'd3thdt' in elem.split('.')[0]:
                    remainlist_filter.append(elem)
        if key_dynain == 1:
            try:
                if 'dynain' in elem.split('.')[1]:
                    remainlist_filter.append(elem)
            except:
                if 'dynain' in elem.split('.')[0]:
                    remainlist_filter.append(elem)
        if key_mes0000 == 1:
            try:
                if 'mes0000' in elem.split('.')[1]:
                    remainlist_filter.append(elem)
            except:
                if 'mes0000' in elem.split('.')[0]:
                    remainlist_filter.append(elem)
        if key_runrsf == 1:
            try:
                if 'runrsf' in elem.split('.')[1]:
                    remainlist_filter.append(elem)
            except:
                if 'runrsf' in elem.split('.')[0]:
                    remainlist_filter.append(elem)
        if key_status == 1:
            try:
                if 'status' in elem.split('.')[1]:
                    remainlist_filter.append(elem)
            except:
                if 'status' in elem.split('.')[0]:
                    remainlist_filter.append(elem)
        if key_glstat == 1:
            try:
                if 'glstat' in elem.split('.')[1]:
                    remainlist_filter.append(elem)
            except:
                if 'glstat' in elem.split('.')[0]:
                    remainlist_filter.append(elem)
        if key_cfile == 1:
            try:
                if 'cfile' in elem.split('.')[1]:
                    remainlist_filter.append(elem)
            except:
                if 'cfile' in elem.split('.')[0]:
                    remainlist_filter.append(elem)

        remainlist_full.append(elem)



removelist = list(set(remainlist_full) - set(remainlist_filter))

len = len(removelist)
for (path,dir,files) in os.walk(check_path):
    for elem in files :
        try:
            elems = elem.split('.')[1]
            if elems in removelist:
                print('remove  ' + elem)
        except:
            elems = elem.split('.')[0]
            if elems in removelist:
                print('remove  ' + elem)


        # if 'd3plot' == elems:
        #     continue
        # if 'd3plot' in elems:
        #     # i = 0
        #     for item in remainlist:
        #         if item in elems :
        #             # i += 1
        #     # if i == len:
        #             print('remove  ' + elem)
print('dd')




        # dirname, basename = os.path.split(check_path + '\\' + elem)
        # name, ext = os.path.splitext(check_path + '\\' + elem)
        # print(ext)
        # print(name)
        # print(os.path.basename(check_path + '\\' + elem))
        # print(os.path.dirname(check_path + '\\' + elem))
        # if elem not in remainlist :
        #     if elem[-1:] == 'k' :
        #         print('remain k file', path+'/'+elem)
        #     else:
        #     #    os.remove(path+'/'+elem)
        #         print('deleted', path+'/'+elem)

