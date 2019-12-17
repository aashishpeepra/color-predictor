# color-predictor
It uses some mathematical equations (which I wrote from scratch) to figure out what kind of background either black or white suits the color that you pass to it.
This is written purely in Python without the use of many other machine learning library.

<h2>API version</h2>
<br/>
The api.py is the API version of the Machine Learning code i wrote so you can use the API anywhere by simply hosting it on platforms like heroku (no promotion)

<h2>How to use?</h2>
<br/>
I tried to comment description of every function which should be helpfull. You can directly run the withoutML1.py through your console and that will train from the text file containing the color data set with their corresponding suitable background value. After traiing an infinite loop will trigger prompting to enter hexadecimal color value (remember not to pass # with the color, just pass the hexadecimal color value in for RRGGBB)
