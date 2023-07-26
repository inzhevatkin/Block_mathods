import os
import matplotlib.pyplot as plt

cur_dir =    "bcgbq" # "cocgrq"
for range_str in ["small-range", "full-range"]:
    plot_data = []
    block_data = list(range(1, 300, 1))
    index_data = list(range(1, 300, 1))
    for block in index_data:
        path = r"C:\Users\konstantin\Documents\GitHub\ADDA-v1.4\src\seq//"
        path += cur_dir
        path += r"\block"
        path += str(block)
        path += "-" + cur_dir + "-" + range_str
        path += r"\log"
        
        if(not os.path.isfile(path)):
            block_data.remove(block)
            continue
        
        print("Current block:", block)
        f = open(path, 'r')
        lines = f.readlines()
        
        for line in lines:
            if "Total number of iterations:" in line:
                it = int(line.split(':')[1])
                print("Total number of iterations:", it)
            if "Total number of matrix-vector products:" in line:
                mvp = int(line.split(':')[1])
                print("Total number of matrix-vector products:", mvp)
                flag = "Yes_data"
                break
            else:
                flag = "No_data"
                
        if block == 1:
            mvp1 = mvp
            it1 = it
        elif(flag == "Yes_data"):
            ratio_mvp = mvp1*block/mvp
            print("Ration M*V(seq)*N/M*V(block) = ", ratio_mvp)
            plot_data.append(ratio_mvp)
        elif(flag == "No_data"):
            block_data.remove(block)
            
        f.close()

    print("Y=", plot_data)
    block_data.remove(1)
    print("X=", block_data)
    if range_str == "small-range":
        plt.plot(block_data, plot_data, marker=".", linewidth=0.5, 
                 label="узкий диапазон")
    elif range_str == "full-range":
        plt.plot(block_data, plot_data, marker="s", markersize=1.5, 
                 linewidth=0.5, 
                 label="полный диапазон")
    

#plt.xlabel("Number of blocks")
#plt.ylabel("Acceleration (matrix-vector product)")
plt.xlabel("Число блоков, $\it{s}$") 
plt.ylabel(r'Ускорение по $N_{\rm MxV}$') 
plt.legend(loc='upper left') #'lower right'
plt.grid()
#plt.show()

file_name=r"C:\Users\konstantin\YandexDisk\Paper Block-iterative methods\Results//"
file_name += cur_dir
file_name += "-"
file_name += "dual-range(rus)" #"dual-range"
plt.savefig(file_name + '.png', dpi=300, format='png')
plt.savefig(file_name + '.pdf', dpi=300, format='pdf')
plt.close()
