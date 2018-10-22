clc
NN=[];
c=0;
e=0;
C=0;
E=0;
N=input('Input N:');
I=input('Input No. of Iterations:');
for i=1:N
    NN=[NN,i];
end
for i=1:I
    S=rand(N,1)*100;
    X=awgn(S,1);
    SS=zeros(N,1);
    XX=awgn(SS,1);

    if  transpose(X)*S> 0.5*(transpose(S)*S)
        disp("Target Detected!");
        disp("Sent Signal:");
        disp(transpose(S));
        disp("Received Signal:");
        disp(transpose(X));
        c=c+1;

    else
        disp("Target not Detected!");
        disp("Sent Signal:");
        disp(transpose(S));
        disp("Received Signal:");
        disp(transpose(X));
        e=e+1;
    end


    if  transpose(XX)*S> 0.5*(transpose(S)*S)
        disp("Target Detected!");
        disp("Sent Signal:");
        disp(transpose(S));
        disp("Received Signal:");
        disp(transpose(XX));
        E=E+1;

    else
        disp("Target not Detected!");
        disp("Sent Signal:");
        disp(transpose(S));
        disp("Received Signal:");
        disp(transpose(XX));
        C=C+1;
    end
end
P=((C+c)/(2*I))*100;
disp('Performance of the Target Detection System (%):');
disp(P);
