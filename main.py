from numpy import gradient

for test in range(10):
    print('')
    accelerations = []
    for trial in range(5):
        time = []
        distance = []
        currentTrial = 1

        files = ['1book.txt', '2books.txt', '3books.txt', '4books.txt', '5books.txt', '6books.txt', '7books.txt',
                 '8books.txt', '9books.txt', '10books.txt']

        with open(files[test], 'r') as file:
            firstHalf = True
            for line in file:
                if line == '##\n':
                    currentTrial += 1
                elif currentTrial == trial + 1:
                    if line == '#\n':
                        firstHalf = False
                    elif firstHalf:
                        time.append(float(line))
                    else:
                        distance.append(float(line))

        dy = gradient(distance)
        dt = gradient(time)
        velocity = dy / dt

        d2y = gradient(velocity)
        acceleration = d2y / dt

        print("Average acceleration for test", str(test + 1) + " trial", str(trial + 1) + ":",
              sum(acceleration) / len(acceleration))
        accelerations.append(sum(acceleration) / len(acceleration))

    mean = sum(accelerations) / len(accelerations)
    variance = sum([((x - mean) ** 2) for x in accelerations]) / len(accelerations)
    std_dev = variance ** 0.5
    print("Standard deviation of the accelerations for test", str(test + 1) + ":", std_dev)
