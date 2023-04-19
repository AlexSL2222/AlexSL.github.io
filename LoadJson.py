# Welcome to Cursor



# 1. Try generating with command K on a new line. Ask for a pytorch script of a feedforward neural network
# 2. Then, select the outputted code and hit chat. Ask if there's a bug. Ask how to improve.
# 3. Try selecting some code and hitting edit. Ask the bot to add residual layers.
# 4. To try out cursor on your own projects, go to the file menu (top left) and open a folder.

import json

def find_num_points(json_file):
    with open(json_file) as f:
        data = json.load(f)
        for key, value in data.items():
            if key == "num_points":
                print(value)

        frames =  data["cache_data"]["frames"]

        for frame in frames:
            print(frame["num_points"])
            
        
        


if __name__ == "__main__":
    find_num_points("sphere7.hbjson")
