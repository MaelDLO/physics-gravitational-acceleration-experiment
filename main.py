import math

from numpy import gradient

xAccelerations = []
yAccelerations = []
pAccelerations = []
pAverageAccelerations = []
pStdDevs = []

for axis in range(2):
    for test in range(10):
        accelerations = []
        print('')
        # print('Test', test + 1, 'axis', axis + 1)
        for trial in range(5):
            time = []
            distance = []
            currentTrial = 1

            if axis == 0:
                files = ['1book_x.txt', '2books_x.txt', '3books_x.txt', '4books_x.txt', '5books_x.txt', '6books_x.txt',
                         '7books_x.txt', '8books_x.txt', '9books_x.txt', '10books_x.txt']
            else:
                files = ['1book_y.txt', '2books_y.txt', '3books_y.txt', '4books_y.txt', '5books_y.txt', '6books_y.txt',
                         '7books_y.txt', '8books_y.txt', '9books_y.txt', '10books_y.txt']

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
            acceleration = (d2y / dt) * 100  # convert from m/s to cm/s

            print("Average acceleration for test", str(test + 1) + " trial", str(trial + 1) + ":",
                  sum(acceleration) / len(acceleration))
            # print(sum(acceleration) / len(acceleration))
            accelerations.append(sum(acceleration) / len(acceleration))
            if axis == 0:
                xAccelerations.append(sum(acceleration) / len(acceleration))
            else:
                yAccelerations.append(sum(acceleration) / len(acceleration))

i = 0
for test in range(10):
    accelerations = []
    print('')
    # print('Test', test + 1)
    for trial in range(5):
        parallelAcceleration = math.sqrt(xAccelerations[i] ** 2 + yAccelerations[i] ** 2)
        print("Parallel acceleration for test", str(test + 1) + " trial", str(trial + 1) + ":", parallelAcceleration)
        # print(parallelAcceleration)
        accelerations.append(parallelAcceleration)
        pAccelerations.append(parallelAcceleration)
        i += 1

    mean = sum(accelerations) / len(accelerations)
    pAverageAccelerations.append(mean)
    variance = sum([((x - mean) ** 2) for x in accelerations]) / len(accelerations)
    std_dev = variance ** 0.5
    # print("Standard deviation of the parallel accelerations for test", str(test + 1) + ":", std_dev)
    print('Standard deviation')
    print(std_dev)
    pStdDevs.append(std_dev)

# print everything in transposed table form where all the values are in new lines
print('')
print('xAccelerations')
for trial in range(5):
    for test in range(10):
        print(round(xAccelerations[trial + test * 5], 2))
    print('')

print('yAccelerations')
for trial in range(5):
    for test in range(10):
        print(round(yAccelerations[trial + test * 5], 2))
    print('')

print('pAccelerations')
for trial in range(5):
    for test in range(10):
        print(round(pAccelerations[trial + test * 5], 2))
    print('')

print('pAverageAccelerations')
for test in range(10):
    print(round(pAverageAccelerations[test], 2))
print('')

print('pStdDevs')
for test in range(10):
    print(round(pStdDevs[test], 1 - int(math.floor(math.log10(abs(pStdDevs[test]))))))
