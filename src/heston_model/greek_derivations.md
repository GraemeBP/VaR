# Greek Derivations

The purpose of this document is to go through the derivation process of the greeks for the Heston model. 

## Delta 
The value of a call is the following: 
C = S * P<sub>1</sub> - Ke<sup>(-rt)</sup> 

Delta is the change in the price of the call, C with respect the the change in the underlying price S.

<a href="https://www.codecogs.com/eqnedit.php?latex=Delta&space;=&space;\frac{\partial&space;C}{\partial&space;S}&space;=&space;\frac{\partial}{\partial&space;S}&space;\left&space;(&space;S&space;*&space;P_{1}&space;-&space;K*e^{-rt}*P_{2}\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Delta&space;=&space;\frac{\partial&space;C}{\partial&space;S}&space;=&space;\frac{\partial}{\partial&space;S}&space;\left&space;(&space;S&space;*&space;P_{1}&space;-&space;K*e^{-rt}*P_{2}\right&space;)" title="Delta = \frac{\partial C}{\partial S} = \frac{\partial}{\partial S} \left ( S * P_{1} - K*e^{-rt}*P_{2}\right )" /></a>

We can rearrange it to the following: 

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;C}{\partial&space;S}&space;=&space;P_{1}&space;&plus;&space;S*\frac{\partial&space;P_{1}}{\partial&space;S}&space;&plus;&space;K*e^{-rt}&space;*&space;\frac{\partial&space;P_{2}}{\partial&space;S}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;C}{\partial&space;S}&space;=&space;P_{1}&space;&plus;&space;S*\frac{\partial&space;P_{1}}{\partial&space;S}&space;&plus;&space;K*e^{-rt}&space;*&space;\frac{\partial&space;P_{2}}{\partial&space;S}" title="\frac{\partial C}{\partial S} = P_{1} + S*\frac{\partial P_{1}}{\partial S} + K*e^{-rt} * \frac{\partial P_{2}}{\partial S}" /></a>
