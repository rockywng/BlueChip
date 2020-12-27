# BlueChip
BlueChip is a simplistic stock evaluation service that calculates the intrinsic value of any stock that trades on any American stock exchange using the PE Ratio and EPS method. Users can input the ticker of the stock of their choice, and will receive a brief evaluation that includes the intrinsic value of the stock, the live market value of the stock, and a brief statement on if the stock presents a good investment opportunity.


## Packages and Tools Used
BlueChip was built using the tkinter GUI toolkit, the Yahoo Finance API and the OS module. The tkinter toolkit was used to design the GUI, offering an easy, efficient way to produce a simplistic, appealing user interface. The Yahoo Finance API was used to fetch live stock data. When the user inputs a stock ticker, that ticker is used to fetch a table known as a quote table, containing all financial data pertaining to that stock. From this table, the price to earning ratio and earnings per share are retrieved for use in the intrinsic value calculation. The OS module is used to produce the path to an image file that is used as the background for the user interface. 

## Appraisal Process

## Potential Extensions

While BlueChip is a relatively simplistic tool, it has plenty to offer, especially to those navigating the stock market for the first time. New traders will be able to get a second opinion on stocks they are interested in on demand, rather than waiting weeks or even months for a professional outlet to do the same. 
