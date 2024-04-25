import matplotlib.pyplot as plt
import os

def create_graph(name, position, x_name, x_s, y_name, y_s):
   
    plt.figure(figsize=(10, 3.5))
    plt.plot(x_s, y_s, marker='.', linewidth=5)        
    plt.xlabel(x_name, fontsize=25)
    plt.ylabel(y_name, fontsize=25)
    plt.grid(True)
    plt.xticks(x_s)  
    plt.tick_params(axis='both', which='major', labelsize=25)
    plt.gca().set_position([0.18, 0.3, 0.75, 0.65]) 
    # plt.show()

    if not os.path.exists(position):
        os.makedirs(position)

    file_pdf = os.path.join(position, name)
    plt.savefig(file_pdf, format="pdf")
    plt.close()
