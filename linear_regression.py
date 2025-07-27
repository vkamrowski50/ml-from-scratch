class LinearRegression():

    def __init__(self):
        self.inputs = []
        self.outputs = []
        self.slope = 0
        self.y_intercept = 0
    
    def start_interface(self):
        while True:
            print("\nOptions")
            print("1. Add data point")
            print("2. Run cost model and change equation")
            print("3. Give input, predict output")
            print("4. View current linear equation")
            print("5. Exit")

            choice = input("Choose (1-5): ")

            if choice == 1:
                x,y = input("Input a data point in the exact form 'x,y' (x,y both ints):")
                if type(x) != int or type(y) != int:
                    print("Invalid inputs. Must be in form 'x,y' with x and y being ints")
                    continue
                self.inputs.append(x)
                self.outputs.append(y)
                print("Values inputted into data set")
            if choice == 2:
                #implement gradient descent
            if choice == 3:
                x_value = input("Enter an int in form 'x': ")
                predicted_value = self.slope * x_value + self.y_intercept
                print("Predicted output: {predicted_value}")
            if choice == 4:
                print("Current linear equation: y = {self.m}x + {self.y_intercept}")
            if choice == 5:
                print("Exiting...")
                break
            
