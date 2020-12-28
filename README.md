# BlueChip
BlueChip is a simplistic stock evaluation service that calculates the intrinsic value of any stock that trades on any American stock exchange using the PE Ratio and EPS method. Users can input the ticker of the stock of their choice, and will receive a brief evaluation that includes the intrinsic value of the stock, the live market value of the stock, and a brief statement on if the stock presents a good investment opportunity.
BlueChip is currently only available Windows 10 64-bit. 

## Motivation
When I first began learning to trade stocks, I had no idea how to determine if a stock was a solid buy. I also remember struggling to grasp the meaning of values like EPS, PE Ratio and other confusing acronyms that only served to make the stock market seem all the more daunting. In an attempt to make up for my lack of knowledge, I turned to various stock analysts offering stock ratings. 
As I traded more and more, I realized that relying on analysts could only get me so far. While there seemed to be an unending number of ratings for stocks like AAPL, AMZN, and TSLA, there were almost none for more niche stocks I was interested in. I recall trying to find ratings for CSOD (Cornerstone OnDemand), an online employee training service. There were only two ratings published for the stock, and the most recent one had been published several months before. I realized, there had to be a better way for novices like myself to get some guidance when navigating the markets.
After looking into the methods used by many analysts, I realized that while they do take into account external factors when evaluating a stock, the majority of their work is done analyzing the company's financials to produce an intrinsic value estimate. From further research I realized how many methods there are to calculate a stock's intrinsic value. I decided to use the PE Ratio and EPS method. Not only is it an incredibly reliable method, having been used in stock evaluation for a long time, but I appreciated its focus on company earnings in its evaluation process. From my experience trading I'm of the belief that stocks prices tend not to deviate much from the financial data backing them.
With BlueChip, beginner traders won't have to wait weeks or months for an analyst to provide an evaluation of a stock they are interested in. They can simply enter the ticker of the stock they're interested in into the system and receive a response immediately! I hope this tool helps anyone getting into trading for the first time, and I hope it makes the prospect of trading stocks much less frightening! 

## Screenshots
What users are greeted with when they first open BlueChip:

<img width="377" alt="bluechip1" src="https://user-images.githubusercontent.com/55059833/103178415-a489a600-4850-11eb-85fa-505aec071efa.PNG">

An example of an evaluation of AAPL stock:

<img width="376" alt="bluechip2" src="https://user-images.githubusercontent.com/55059833/103178435-c2570b00-4850-11eb-8b97-e7ca7cb56132.PNG">

## Packages and Tools Used
BlueChip was built using the tkinter GUI toolkit, the Yahoo Finance API and the OS module. pyinstaller was used to produce the executable version of the source code.
The tkinter toolkit was used to design the GUI. tkinter is a Python interface to the Tk GUI toolkit, and is the standard Python GUI. tkinter itself was used to create design elements that could be manipulated to produce the GUI, while tkinter.font was used to customize the font of text elements to produce a more visually appealing GUI.
The Yahoo Finance API was used to access stock data to produce an evaluation for the user. yahoo_fin.stock_info was used to access this information. The Yahoo Finance API allows access to any data present in the Yahoo Finance financial database, and allows for live data to be easily retrieved. 
The OS module was used to create a path to locate the image file used as the GUI background. First, a path to the base folder was created, and then this base folder was searched for the specified image file.
pyinstaller was used to produce an executable version of the source code. pyinstaller was also used to assign an icon to the executable file.

## Usage
BlueChip is an incredibly easy service to use. The only part of this repository that must be downloaded onto your local machine is the distributable folder, but feel free to download anything else you would like. Within the distributable folder there are two files. One is an executable file called BlueChip.exe. This is the file you will need to open to actually use BlueChip. The other file is called blueback.gif and is a gif file that is used as the background for the GUI. This file must be in the same folder as the executable file, and as such, it is advised that you don't move any files into or out of the distributable folder. 
Once you have the distributable folder downloaded onto your local machine, open the executable file by double clicking it. After a short wait, you will be greeted with the initial screen. For reference, please view the first image under the Screenshots heading. Simply type a ticker into the entry box and click the submit button and an evaluation of the stock you inputted will appear. If you do not input a valid ticker, the return box will inform you of this. After submitting a ticker, you may continue to submit more if you wish.
In some cases, there may not be enough data to produce an evaluation. There are two causes for this. One would be that data for the given stock is simply not available on Yahoo Finance. In this case, BlueChip will not be able to produce an evaluation of the stock until the data becomes available. The second reason for this would be that the Yahoo Finance API is in the midst of updating its data. If this is the case, simply wait a short period of time and resubmit the ticker of the stock you would like evaluated, and the evaluation will be provided to you.

## Potential Extensions
There are a number of extensions to this project that are still in development. One is the collection of user data to enhance the user experience. Specifically, tickers that users search for will be saved to a data file saved on the users local machine. This data file will be used in a number of manners. 
First, BlueChip will be able to offer users a selection of other stocks they may be interested in based on the types of stocks they have been searching for. For instance, if a user has been searching for evaluations of TSLA and AAPL stock, the system may offer them other tech stocks they may be interested in like MSFT or UBER. While they may not trade on the same exchange, the point stands that they're part of the same industry and as such, may be of interest to a user based on their search history. 
Furthermore, BlueChip will be able to track the difference between the intrinsic value and market value of stocks found in the user data file to produce a sort of pseudo portfolio. Users will be able to track this difference to determine a general trend with the stocks they're interested in, and will be able to estimate the optimal time to make a purchase.
While BlueChip is certainly functional at the moment and provides a valuable service, there is still more that can be added to it to enhance the user experience.

## License
BlueChip is MIT licensed.
