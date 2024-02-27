#Q2B
    
# def read_text(text):
#     space = text.split(" ")
#     date = space[1]
#     region = " ".join(space[6:])
#     magnitude = space[0]
#     return date, region, magnitude

    

# file = open('earthquake.txt')
# earthquake_file = file.readlines()

# seismic_data = {}
# for i in earthquake_file:
#         date, region, magnitude = read_text(i)
#         earthquake_file[region].append([date, magnitude])
        

# def format_data(earthquake_file, ):
#     with open("earthquakefmt.txt", 'w') as f:
#         for date, region in earthquake_file.items():
#             formatted_data = "[" + region + ", " + ", ".join(["[" + d[0] + ", " + d[1] + "]" for d in date]) + "]"
#             f.write(formatted_data + "\n")
            
            
            
# print(format_data(seismic_data, "earthquakefmt.txt"))
        
        
    
    
def read_text(text):
    space = text.split(" ")
    date = space[1]
    # region = " ".join(space[6:]).strip()
    region = space[-1].strip()
    magnitude = space[0]

    return date, region, magnitude


with open('earthquake.txt') as file:
    earthquake_file = file.readlines()

seismic_data = {}
for line in earthquake_file:
    date, region, magnitude = read_text(line)

    if region not in seismic_data:
        seismic_data[region] = []

    seismic_data[region].append([date, magnitude])

# print(seismic_data)

def format_data(seismic_data):
    with open("earthquakefmt.txt", 'w') as f:
        for region, data in seismic_data.items():
            formatted_data = "[" + region + ", " + ", ".join(["[" + d[0] + ", " + d[1] + "]" for d in data]) + "]"
            f.write(formatted_data + "\n")

# format_data(seismic_data)

        
        
    


    
    
        
        


