Aim: To determine the performance of Target Detection System.

Methodology:

First of all the code randomly generates a vector of desired size as requested by the user (while inputting N) from uniformly generated distribution between 0 and 1 to simulate the signal sent from the transmitter.

Thereafter for some of the iterations the code adds Additive White Gaussian Noise to the randomly generated signal which was sent to generate the signal received by the receiver and for some of the iterations it just send the Additive White Gaussian Noise as signal received by the receiver.

Thereafter in each iteration Signal Sent and Signal received is sent through Target Detection System which is nothing but a threshold condition on the Signal Sent anf Signal Received by the antenna.

The matrix relation for the same can be found on Page 477 of Intuitive Probability and Random Processes Using MATLAB by Steven M. Kay Reference Book. 

Thereafter to estimate the performance of the system, we check that when the Signal Received by the receiver is juct noise then the system should inform that Target was not detected and when the signal received by the receiver was addition of Signal Sent by the transmitter and AWGN then the system should inform that Target was detected.

Error in the above process would result into a decrease in the performance of the Target Detection System.

Note: As the Problem Statement on the Classroom did not mention about visualizations or Report, I am not attaching the same with the submission.    
