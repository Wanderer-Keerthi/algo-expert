# O(n) time | O(n) space - where n is the number of asteroids
def collidingAsteroids(asteroids):
    # Write your code here.
    resultStack = []
    for asteroid in asteroids:
        if asteroid > 0:
            resultStack.append(asteroid)
            continue

        while True:
            if len(resultStack) == 0 or resultStack[-1] < 0:
                resultStack.append(asteroid)
                break

            asteroidSize = abs(asteroid)
            if resultStack[-1] > asteroidSize:
                break

            if resultStack[-1] == asteroidSize:
                resultStack.pop()
                break

            resultStack.pop()
            
    return resultStack
