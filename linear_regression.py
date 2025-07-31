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
                try:
                    x_str,y_str = input("Input a data point in the exact form 'x,y' (x,y both ints): ").split(",")
                    x = int(x_str)
                    y = int(y_str)
                    self.inputs.append(x)
                    self.outputs.append(y)
                    print("Values inputted into data set")
                except:
                    print("Invalid format. Must be 'x,y' with both as ints.")

            elif choice == 2:
                
                #implement gradient descent

            elif choice == 3:
                try:
                    x_value = int(input("Enter an int in form 'x': "))
                    predicted_value = self.slope * x_value + self.y_intercept
                    print(f"Predicted output: {predicted_value}")
                except:
                    print("Invalid input, must be an int.")

            elif choice == 4:
                print(f"Current linear equation: y = {self.slope}x + {self.y_intercept}")
            
            elif choice == 5:
                print("Exiting...")
                break
            
            else:
                print("Invalid choice. Enter a number from 1 to 5")
