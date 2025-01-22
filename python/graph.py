import matplotlib.pyplot as plt

# Function to read data from performances.md
def read_data(file_path):
    data = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip() and not line.startswith('#'):
                parts = line.split(':')
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = float(parts[1].strip())
                    data[key] = value
    return data

# Read data from performances.md
file_path = 'C:/Users/adria/OneDrive/Bureau/Travail-Cours/Semestre_9/Software_testing/kata-contacts-quartz/python/performances.md'
data = read_data(file_path)
print("Data:", data)    
# Plot the data
if data:
    plt.figure(figsize=(15, 7))
    plt.bar(data.keys(), data.values(), color='blue')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Performance Data')
    plt.xticks(rotation=45)
    plt.ylim(0, max(data.values()) + 10)  # Adjust y-axis limits
    plt.tight_layout()
    plt.show()
else:
    print("No data to plot.")
