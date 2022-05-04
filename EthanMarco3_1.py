# Part 1
# Import the necessary module (use an alias name during importation to help with code readability)
import ethan_marco as areas

def selection():
    print('----------------------')
    print('SELECT SHAPE')
    print('----------------------')
    print('1 - Circle')
    print('2 - Rectangle')
    print('3 - Square')
    print('4 - Triangle')

    # Code to check that a valid shape has been selected
    shape = int(input('Shape number: '))
    while shape < 1 or shape > 4:
        shape = int(input('Shape number (1-4): '))

    return shape


def main():
    while True:
        shape = selection()
        if shape == 1:
            radius = float(input('Circle radius: '))
            shape_area = areas.circle(radius)
            print(f'Circle area = {shape_area:.2f}')
        elif shape == 2:
            length = float(input('Rectangle length: '))
            width = float(input('Rectangle width: '))
            shape_area = areas.rectangle(length, width)
            print(f'Rectangle area = {shape_area:.2f}')
        elif shape == 3:
            length = float(input('Square length: '))
            shape_area = areas.square(length)
            print(f'Square area = {shape_area:.2f}')
        elif shape == 4:
            base = float(input('Triangle base: '))
            height = float(input('Triangle height: '))
            shape_area = areas.triangle(base, height)
            print(f'Triangle area = {shape_area:.2f}')

        repeat = input('Continue (y/n): ')
        while True:
            if repeat.lower().strip() == 'y' or repeat.lower().strip() == 'n':
                break
            else:
                repeat = input('Enter y or n: ')
                continue
        if repeat.lower().strip() == 'y':
            continue
        elif repeat.lower().strip() == 'n':
            print('PROGRAM DONE')
            break

        # Part 2
        # Determine which shape the user selected by calling the selection() function
        # Determine which area should be computed based off the value returned by the selection() function

        # Part 3
        # Ask the user if they want to continue
        # If they enter 'n', break out of the loop and display 'PROGRAM DONE'
        # If they enter 'y' the loop should be repeated (go back to the top of the loop)
        # Use a loop to check that they are entering a valid response (y/n)


if __name__ == '__main__':
    main()
