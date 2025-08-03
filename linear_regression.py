class LinearRegression():

    def __init__(self):
        self.inputs = []
        self.outputs = []
        self.m = 0 #slope
        self.b = 0 #y-intercept
        self.points = 0 # amount of points
    
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
                    self.points += 1
                except:
                    print("Invalid format. Must be 'x,y' with both as ints.")

            elif choice == 2:
                try:
                    epochs, learning_rate = input("Input the amount of gradient descent trials to run (epochs, int) and at what learning rate (float) in form 'epochs,learning_rate").split(",")
                    epochs = int(epochs)
                    learning_rate = float(learning_rate)
                    self.run_gradient_descent(epochs,learning_rate)
                    print(f"Training done. New equation is: y = {self.m}x + {self.b}")
                except:
                    print("Invalid format. Must be 'epochs,learning_rate' with epochs as int and learning_rate as float")
            elif choice == 3:
                try:
                    x_value = int(input("Enter an int in form 'x': "))
                    predicted_value = self.m * x_value + self.b
                    print(f"Predicted output: {predicted_value}")
                except:
                    print("Invalid input, must be an int.")

            elif choice == 4:
                print(f"Current linear equation: y = {self.m}x + {self.b}")
            
            elif choice == 5:
                print("Exiting...")
                break
            
            else:
                print("Invalid choice. Enter a number from 1 to 5")

    def partial_derivative_mse_respect_to_m(self):
        gradient = 0
        for x,y in zip(self.inputs,self.outputs):
            gradient += x * (y - (self.m * x + self.b))
        gradient *= -2 / self.points
        return gradient

    def partial_derivative_mse_respect_to_b(self):
        gradient = 0
        for x,y in zip(self.inputs,self.outputs):
            gradient += y - (self.m * x + self.b)
        gradient *= -2 / self.points
        return gradient
    
    def run_gradient_descent(self, epochs=1000, learning_rate=0.01):
        # add initial mse and final to see how much has changed
        for i in range(epochs):
            self.m -= self.partial_derivative_mse_respect_to_m() * learning_rate
            self.b -= self.partial_derivative_mse_respect_to_b() * learning_rate
