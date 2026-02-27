# Lab 5

## Team Members
Selena Zhang - 2575286626

## Part 1 Question Answers

 # Question 1: What is dBm? What values are considered good and bad for WiFi signal strength?
    dBm represents decibel-milliwatts, which is a unit for power with respect to a milliwatt. A good signal is -30 dBm (max), and it starts getting bad at around -70 dBm. 
    
 # Question 2: Why do we need to check the OS? What is the difference between the commands for each OS?
    We need to check the OS because each system uses a different command to get the wifi signal strength. The difference between commands is in the command name and also the format of the output. For example, the Linux commands displays signal strenth as "Signal Level: ..." while Darwin displays it as "RSSI: ...".
    
 # Question 3: In your own words, what is subprocess.check_output doing? What does it return?
    subprocess.check_output basically spits the string you input into the terminal as a command. It returns the output that command has in the terminal, as a string of bytes.
    
 # Question 4: In your own words, what is re.search doing? What does it return?
    re.search is parsing through a decoded form of the check_output output, looking specifically for a key word/phrase, which we set as "RSSI = ", with some variations. It returns a specified part right after the key phrase, which we set as the dBM value.
    
 # Question 5: In the Windows case, why do we need to convert the signal quality to dBm?
    We need to convert in the Windows function because the command outputs the signal strength as a percentage from 0 to 100 of the maximum signal strength.

 # Question 6: What is the standard deviation? Why is it useful to calculate it?
     The standard deviation is measure of variance; how your data points distribute themselves around the center value. It is useful to calculate so you get an idea of your data's fluctuation and noise.

 # Question 7: What is a dataframe? Why is it useful to use a dataframe to store the data?
     A dataframe is a type of 2-D structure that is mutable and can hold tabular data. It's useful because it can hold various types of data in each row/column, which we used in this code to combine the location, signal mean, and signal std values together.
 
 # Question 8: Why is it important to plot the error bars? What do they tell us?
     Error bars are important to tell us about the variation of the data and also shows overlap between group. This information of overlaps is important in telling us if a seeming difference is actually significant or not.

 # Question 9: What did you observe from the plot? How does the signal strength change as you move between locations?
    #          Why do you think signal strength is weaker in certain locations?
    From the plot, I saw that the signal was strongest in the bathroom and bedroom, and weakest in the kitchen and living room. This makes sense because the bathroom and bedroom are just down the hallway of the router, while the kitchen and living room are downstairs. They are farther + more objects in between.
    


# Part 2 Question Answers

1. How does distance affect TCP and UDP throughput?
      Distance should theoretically decrease TCP throughput, although that wasn't too apparent from the graphs I collected. For UDP, it remained constant at 10 mBps.

2. At what distance does significant packet loss occur for UDP?
      None of the distances I tested showed any sort of packet loss for UDP.

3. Why does UDP experience more packet loss than TCP?
      UDP experiences more packet loss than TCP due to the nature of the protocol, which doesn't prioritize reliability. If UDP is overwhelmed, then it will just toss packets rather than slowing down.

4. What happens if we increase the UDP bandwidth (-b 100M)?
      If we increase the UDP bandwidth, there would be less package loss and higher throughput. Although in our case, I imagine there would be similar performance since we have 0 packet loss anyways.

5. Would performance be different on 5 GHz Wi-Fi vs. 2.4 GHz?
      Performance would be different on 5 GHz vs. 2.4 GHz. On the former, we would expect higher throughput for shorter distances, but worse performance at farther distances. For the latter, peak throughput would be less, but it would have less loss as distance increases.

