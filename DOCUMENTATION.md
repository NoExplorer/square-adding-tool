# DOCUMENTATION FILE
In this file you will find some info for each tool/command. But first: <p>&nbsp;</p>

# Basic info about this project
## Concept by [Cocoatwix](https://github.com/Cocoatwix)
## "Automated" by [me (NoExplorer)](https://github.com/NoExplorer) and by the cool people who contributed.
## And you! For checking this project out. I hope you enjoy using it and messing around with the code.
Okay, now the real thing.<p>&nbsp;</p>

# Requirements
## **Software**
>Python 3.8 (or newer)

Without this the program WON’T function at all.

>VSCodium (Or Microsoft's Visual Studio Code, if you like telemetry and such) or Notepad++ or Python's own IDE.

Only needed if you want to mess around with the code.
## **Hardware (don't matter much but might help)**
>A decent CPU and 4GB+ of RAM.

Anything better than a Intel Core i3-2120 or an AMD A4-5300 should be enough or even better. As for RAM, 4GB or more of DDR3-2133 or higher spec could be beneficial but I haven’t tested that.

>400KB or more of free storage space.

This shouldn’t be hard, but you will need some storage space. In case I somehow make the code export lists of numbers later on.

>A good APU or GPU.

Not really needed at this current time but when an actual GUI is implemented you will need it.<p>&nbsp;</p>

# Layout / GUI / CLI
![image](https://user-images.githubusercontent.com/37076999/188231436-913e6f1d-51db-439e-8f1f-731424b820a2.png)
****1] Available scripts line**

This part tells you which scripts are currently implemented. All of them are at the moment.

**2] input line (Script selection)**

 Here, you type which script you want to use. They are listed below, but you will need to jump to different pages if you need more info about them.

**1A] chainVerifier**

One of the available scripts. More about it soon.

**1B]numberLocator**

Another script that you can use. More about it soon

**1C]GenerateNumber**

And another one. More about it soon.

**1D]info**

A script that tells you some info about the program. Nothing more

**1E]credits**

The credits are in this command. Should tell you who and how they contributed to this program. Hope I was clear enough. <p>&nbsp;</p>

# chainVerifier Script
Your most commonly visited script. This part of the code will use a specified number (that you might have found) and find which numbers/values come after it. For example:<p>&nbsp;</p>
*Initial number : 98*
![image](https://user-images.githubusercontent.com/37076999/188231405-589aa9e6-bf2d-4b74-9a76-15dbc27e10ae.JPG)
The chain that the number ‘98’ generates is:
`68 -> 56 -> 32 -> 20 -> 8 -> 16 -> 28 -> 40` (before it cycles back to 16)<p>&nbsp;</p>
![image](https://user-images.githubusercontent.com/37076999/188231428-a3054f83-dc54-4fd3-9539-ffae6736b308.png)

**3]’Define number x’ line**

Here you input the number which you want to see the chain of. Any number will work as long as it doesn’t have any decimals. Some numbers might have a small chain, and others a longer one. The entire point of this project is to find which number has the biggest chain.

***The entire point of this project is to find which number has the biggest chain.***

![img](https://user-images.githubusercontent.com/37076999/188231442-b46dc2ac-0274-4606-b1fa-69823d00a568.png)

**4]’Num x y’ line.**

Essentially the chain. Where x is the step and y is the product (68 -> 56 you get the point I hope. I can’t explain this well.)<p>&nbsp;</p>

# numberLocator Script
This script will tell you, after you specify a number, how many Digits and what DigitSum the next number on the chain has. (One thing I would recommend you is to not use any result below 2 or 3 digit numbers that the program spat out. It might not work well). For example:  

*Let’s say that you want to find which number comes after 1001410.*
![img](https://user-images.githubusercontent.com/37076999/188231438-9e38b3b1-4f51-42b9-a963-8ddc19025f2c.png)

From the image above, you can see that the next number can have from `500705` Digits (and digitsum) all the way down to `1`. Although you might think that the lower values are the best, stick to 3 digit results for better luck. After you choose your value of choice, you can use it on the following script.

![img](https://user-images.githubusercontent.com/37076999/188231440-13c281f7-99ae-41c8-9019-cfc24be54613.png)

**5]’x digits’**

Tells you how many digits the next number has.

**6]’sum of those digits must be y’**

Tells you what the sum of the digits should be.

**7]Specify value of ‘’y’’  prompt**

This is where you type what number you want to find the values for. Cannot explain it well enough but I hope you got the point.

# GenerateNumber Script
This script, when combined with the values you got from the `numberLocator` script, will generate for you pseudorandom numbers which might go after the initial number. For example:

*From the previous script, the values that should lead us to the next number are 239 (for the digits) and 239 (for the digitsum).*
![img](https://user-images.githubusercontent.com/37076999/188231419-6c04ff30-5010-440b-8281-dd8e8832775a.jpg)

![img](https://user-images.githubusercontent.com/37076999/188231425-7840f72c-3ee0-492f-bd65-8cb65bcda93b.jpg)

**8]Some warnings**

The first line is telling you to run the `numberLocator` script, if you haven’t already. The other one is telling you that high values might/will take longer to generate a number.

**9]Amount of Digits prompt**

Here you should specify the amount of digits that you got from the `numberLocator` script.

**10]Digitsum prompt**

Here you should specify the digitsum that you got from the `numberLocator` script.

**11]Delay before each generation prompt**

Here you should specify your desired amount of time you want to wait before the script generates an output. 0 counts as none.

**12]Output**

This is your output. Size will matter depending on how many digits you want your number to have. If you want to copy it, select it and press Ctrl+C.

**13]Info**

This here is the info about the specific output. Do not fear as it is quite simple. Length is, well, the length of your output (it should be same as the one you specified). And Sum of digits is the sum of all the digits in the output (this too should be the same as the one you specified). <p>&nbsp;</p>

# credits Script
This script just rolls the credits. Simple enough. You might not need this function very frequently but if you want to know who helped and how, just use this script.

![img](https://user-images.githubusercontent.com/37076999/188231429-c6c68e97-b8bd-4985-bf2c-070914fbbbfb.png)

Self-explanatory. The program will exit by itself after 30 seconds pass. Should be enough for you to read them.<p>&nbsp;</p>
# info Script
Should be easy to understand what this one does. Just displays some info about the program, and the inspiration.

![img](https://user-images.githubusercontent.com/37076999/188231437-1772bbc9-5ef0-4475-878b-45400b604624.png)

Program will quit by itself after 30 seconds. Should be enough for you to scan the QR Code or copy the link and read the text.

# ***IMPORTANT! DO NOT SCAN QR CODE OR VISIT LINK FROM 3RD PARTY CLONE! YOU COULD EXPOSE YOUR SYSTEM TO POTENTIAL VIRUSES! ONLY TRUST THIS ONE.*** <p>&nbsp;</p>

# Credits and Info.
If the previous two parts didn’t say much, here are the people who helped:

>Ratery on StackOverflow. They made the 'GenerateNumber' script. And many others in the question I made.

>kite.com . They provided to me the 'sum_of_digits' code.

>BigTeePee on PCMR Discord. Helped fix an issue on the 'numberLocator' script.
    
>scares009 / Cocoatwix . Original creator of this concept.

>JZGonzales. Fixed by either introducing or removing a floating point delay

>And YOU. For testing this program, and using it!

>Version: 0.0.1eg <p>
>Script date: 23rd November 2021 <p>
>Finish date: 5th December 2021 <p>
>Most recent change: 30th June 2022 <p>
>Project status: Early Beta

# License
GPL-3.0-or-later
(https://www.gnu.org/licenses/gpl-3.0-standalone.html)