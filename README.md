# BlueChip
BlueChip is a simplistic stock evaluation service that calculates the intrinsic value of any stock that trades on any American stock exchange using the PE Ratio and EPS method. Users can input the ticker of the stock of their choice, and will receive a brief evaluation that includes the intrinsic value of the stock, the live market value of the stock, and a brief statement on if the stock presents a good investment opportunity.
BlueChip is currently only available Windows 10 64-bit. 

## Motivation
When I first began learning to trade stocks, I had no idea how to determine if a stock was a solid buy. I also remember struggling to grasp the meaning of values like EPS, PE Ratio and other confusing acronyms that only served to make the stock market seem all the more daunting. In an attempt to make up for my lack of knowledge, I turned to various stock analysts offering stock ratings. 
As I traded more and more, I realized that relying on analysts could only get me so far. While there seemed to be an unending number of ratings for stocks like AAPL, AMZN, and TSLA, there were almost none for more niche stocks I was interested in. I recall trying to find ratings for CSOD (Cornerstone OnDemand), an online employee training service. There were only two ratings published for the stock, and the most recent one had been published several months before. I realized, there had to be a better way for novices like myself to get some guidance when navigating the markets.
After looking into the methods used by many analysts, I realized that while they do take into account external factors when evaluating a stock, the majority of their work is done analyzing the company's financials to produce an intrinsic value estimate. From further research I realized how many methods there are to calculate a stock's intrinsic value. I decided to use the PE Ratio and EPS method. Not only is it an incredibly reliable method, having been used in stock evaluation for a long time, but I appreciated its focus on company earnings in its evaluation process. From my experience trading I'm of the belief that stocks prices tend not to deviate much from the financial data backing them.
With BlueChip, beginner traders won't have to wait weeks or months for an analyst to provide an evaluation of a stock they are interested in. They can simply enter the ticker of the stock they're interested in into the system and receive a response immediately! I hope this tool helps anyone getting into trading for the first time, and I hope it makes the prospect of trading stocks much less frightening! 

## Screenshots
<img width="377" alt="bluechip1" src="https://user-images.githubusercontent.com/55059833/103178415-a489a600-4850-11eb-85fa-505aec071efa.PNG">


## Packages and Tools Used
BlueChip was built using the tkinter GUI toolkit, the Yahoo Finance API and the OS module. The tkinter toolkit was used to design the GUI, offering an easy, efficient way to produce a simplistic, visually appealing user interface. The Yahoo Finance API was used to fetch live stock data. When the user inputs a stock ticker, that ticker is used to fetch a table known as a quote table, containing all financial data pertaining to that stock. From this table, the price to earning ratio and earnings per share are retrieved for use in the intrinsic value calculation. The OS module is used to produce the path to an image file that is used as the background for the user interface. 

## Features

## Usage

## Potential Extensions

## License
