f = open("day01_input.txt", "r")

input_data = []

for line in f:
      input_data.append(int(line.strip()))

for i in range(0, len(input_data)):
    val_01 = input_data[i]

    for j in range(i+1, len(input_data)):
        val_02 = input_data[j]

        for k in range(j+1, len(input_data)):
            val_03 = input_data[k]

            val_sums = val_01 + val_02 + val_03

            if val_sums == 2020:
                print(val_02 * val_01 * val_03)
