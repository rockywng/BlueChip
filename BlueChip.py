import tkinter as tk
import yahoo_fin.stock_info as si
from yahoo_fin import options
import os   
import tkinter.font as tkFont

# HEIGHT will be the height of the frame upon which elements
# will be built
HEIGHT = 350
# WIDTH will be the width of the frame upon which elements
# will be built
WIDTH = 500
# base_folder uses os to create a path to the folder this file is in
base_folder = os.path.dirname(__file__)
# image_path searches the base folder for the blueback.gif file which
# is to be the background
image_path = os.path.join(base_folder, 'blueback.gif')

# get_stock consumes a string representing the ticker of some stock
# and produces a statement based on the percentage difference 
# between the market value of the stock and the intrinsic value
# calculated with the pe ratio method
def get_stock(entry):
    try: 
        # fetches the live market price of the stock with the given
        # ticker using yahoo finance
        market = si.get_live_price(entry)
        # obtains a quote table for the stock with the given ticker
        # containing all relevant stock data
        quote_table = si.get_quote_table(entry, dict_result=False)
        # retriees the price to earnings ratio from the quote table
        pe = quote_table.iat[13,1]
        # retrieves the earnings per share value from the quote table
        eps = quote_table.iat[7,1]
        # calculates the intrinsic value of the stock with the given
        # ticker using the pe ratio and the earnings per share
        ivalue1 = pe * eps
        # produces the difference between the intrinsic value and the
        # market value, both rounded to two decimal points
        diff1 = round(ivalue1, 2) - round(market, 2)
        # calculates the percent difference between the intrinsic value
        # and market value by dividing the actual difference by the 
        # market value
        diff1percent = diff1 / market
    
        if diff1percent >= 20:
            statement = "Estimated Intrinsic Value: " + str(round(ivalue1, 2)) + "\nCurrent Market Value: " + str(round(market, 2)) + "\nInteresting! " + str(entry) + " looks like a very strong buy.\nYou should definitely look into making an immediate purchase."
        if diff1percent >= 10:
            statement = "Estimated Intrinsic Value: " + str(round(ivalue1, 2)) + "\nCurrent Market Value: " + str(round(market, 2)) + "\nIntriguing. " + str(entry) + " could be a strong buy, you\nshould definitely consider making a purchase."
        if diff1percent >= 5: 
            statement = "Estimated Intrinsic Value: " + str(round(ivalue1, 2)) + "\nCurrent Market Value: " + str(round(market, 2)) + "\n" + str(entry) + " is definitely trending upwards.\nKeep an eye on it and be on the\nlookout for potential buying opportunities."
        if diff1percent > 0:
            statement = "Estimated Intrinsic Value: " + str(round(ivalue1, 2)) + "\nCurrent Market Value: " + str(round(market, 2)) + "\n" + str(entry) + " seems to be trending in the right direction, but it's too close to call right now.\nHold off on buying until more definitive data is available."
        if diff1percent == 0:
            statement = "Estimated Intrinsic Value: " + str(round(ivalue1, 2))  + "\nCurrent Market Value: " + str(round(market, 2)) + "\n" + str(entry) + " is trading at approximately its intrinsic value. Hold off on making a purchase, as \nthere isn't much value to be found here."
        if diff1percent < 0:
            statement = "Estimated Intrinsic Value: " + str(round(ivalue1, 2))  + "\nCurrent Market Value: " + str(round(market, 2)) + "\n" + str(entry) + " looks to be on the downswing. Don't establish\na position immediately, but keep an eye out\nfor potential buying opportunities in the future."
        else:
            statement = "There is not enough data at the moment to come\n to a conclusive valuation for " + str(entry) + ". Please check back\nlater when our database is updated."
    # an error will only occur if the given ticker does not exist, thus
    # this is the only error that must be handled
    except:
        statement = "The ticker you entered does not exist. Please try again."
    update1 = statement.replace('{', '')
    update2 = update1.replace('}', '')
    # updates the text in the label element with our updated statement
    label['text'] = update2

root = tk.Tk()
# makes the window size static
root.resizable(False, False)

# produces a blank canvas upon which elements can be added and positioned
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# the font style for the text that will appear displaying the service name
titlestyle=tkFont.Font(family= "Lucida Grande", size=40)

# makes the background photo found previously an element that can be added
background_image = tk.PhotoImage(file=image_path)

# creates a label element with background_image as its image
background_label = tk.Label(root, image=background_image)

# places the background label such that it takes up the entire canvas
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# creates a frame element with a given background colour and border width 5
frame = tk.Frame(root, bg='#2575C6', bd=5)

# places the frame such that it is centred at 50% of the width of the canvas
# and 27.5% of the height of the canvas, and has a width equal to 75% of
# the width of the canvas and a height of 10% of the height of the canvas
frame.place(relx=0.5, rely=0.275, relwidth=0.75, relheight=0.1, anchor='n')

# creates a frame element that will contain the service title
upper_frame = tk.Frame(root, bg='#003366', bd=10)

# places the frame such that it is centred at 50% of the width and 7% of the height,
# and has a width equal to 60% of the canvas and 20% of the height of the canvas
upper_frame.place(relx=0.5, rely=0.07, relwidth=0.6, relheight=0.2, anchor='n')

# creates a label element containing the string "BlueChip" with font being the
# previously defined titlestyle
upper_label = tk.Label(upper_frame, fg="#ffffff", bg="#003366", text="BlueChip", font=titlestyle)

# places the label in the upper_frame element such that it has identical width and height
# to upper_frame
upper_label.place(relwidth=1, relheight=1)

# creates a frame element that will contain details related to the creator of this 
# service (me!)
name_frame = tk.Frame(root, bg='#003366', bd=10)

# places the frame such that it is centred at 85% of the canvas width and the highest
# point of the canvas height while having width equal to 30% of the canvas width 
# and height equal to 15% of the canvas height
name_frame.place(relx=0.85, rely=0, relwidth=0.3, relheight=0.15, anchor='n')

# creates a label element that contains details pertaining to the creator of the service
# that will exist within the name_frame frame
name_label = tk.Label(name_frame, fg="#ffffff", bg="#003366", text="Designed by Rocky Wang\nr533wang@uwaterloo.ca")

# places the label element in the name_frame frame with height and width both equal to 100%
# of the frame
name_label.place(relwidth=1, relheight=1)

# creates an entry element that will consume the user input with a given font size and colour
entry = tk.Entry(frame, fg="#16589B", font=40)

# places the entry element into the frame element with width equal to 57.5% of the frame and 
# 100% of the frame height
entry.place(relwidth=0.575, relheight=1)

# creates a button element that, when pressed will submit the user input as the entry element
# for get_stock
button = tk.Button(frame, text="Submit", font=1, fg='#FFFFFF', bg='#16589B', command=lambda: get_stock(entry.get()))

# places the button element in the frame element centred at 60% of the frame width with height 
# equal to 100% of the frame height and width equal to 40% of the frame width
button.place(relx=0.6, relheight=1, relwidth=0.4)

# creates a frame element with a given background colour and border width
lower_frame = tk.Frame(root, bg='#2575C6', bd=10)

# places the lower_frame element centered at 50% of the canvas width and 40% of the canvas height
# with width equal to 75% of the canvas width and height equal to 55% of the canvas height
lower_frame.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.55, anchor='n')

# creates a label element that will be used to display the welcome message to users and 
# to display the response to user inputs to the user
label = tk.Label(lower_frame, fg="#16589B", text="Welcome to the BlueChip stock advisory system. \nEnter the ticker for the stock you'd like assessed,\nand an evaluation will appear in this box.")\

# places the response label element in the lower_frame element with width equal to 100% of the 
# lower_frame width and height equal to 100% of the lower_frame height
label.place(relwidth=1, relheight=1)

root.mainloop()