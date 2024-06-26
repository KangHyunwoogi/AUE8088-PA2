import random

def split_data(input_file, train_file, val_file, train_ratio=0.8):
    # Read the data from the input file
    with open(input_file, 'r') as file:
        data = file.readlines()
    
    # Shuffle the data
    random.shuffle(data)
    
    # Calculate the split index
    split_index = int(len(data) * train_ratio)
    
    # Split the data
    train_data = data[:split_index]
    val_data = data[split_index:]
    
    # Write the train data to the train file
    with open(train_file, 'w') as file:
        file.writelines(train_data)
    
    # Write the validation data to the validation file
    with open(val_file, 'w') as file:
        file.writelines(val_data)
    
    print(f"Data split complete. Train data: {len(train_data)} lines, Validation data: {len(val_data)} lines")

# Example usage
input_file = '/home/ailab/Desktop/hyunwook/AUE8088-PA2/datasets/kaist-rgbt/train-all-04.txt'
train_file = '/home/ailab/Desktop/hyunwook/AUE8088-PA2/datasets/kaist-rgbt/train.txt'
val_file = '/home/ailab/Desktop/hyunwook/AUE8088-PA2/datasets/kaist-rgbt/validation.txt'

split_data(input_file, train_file, val_file)