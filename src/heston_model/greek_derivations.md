# Greek Derivations

The purpose of this document is to go through the derivation process of the greeks for the Heston model. 

## Delta 

#### Define call value
The value of a call is the following: 
C = S * P<sub>1</sub> - Ke<sup>(-rt)</sup> 

#### Define Delta
Delta is the change in the price of the call, C with respect the the change in the underlying price S.

<a href="https://www.codecogs.com/eqnedit.php?latex=Delta&space;=&space;\frac{\partial&space;C}{\partial&space;S}&space;=&space;\frac{\partial}{\partial&space;S}&space;\left&space;(&space;S&space;*&space;P_{1}&space;-&space;K*e^{-rt}*P_{2}\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Delta&space;=&space;\frac{\partial&space;C}{\partial&space;S}&space;=&space;\frac{\partial}{\partial&space;S}&space;\left&space;(&space;S&space;*&space;P_{1}&space;-&space;K*e^{-rt}*P_{2}\right&space;)" title="Delta = \frac{\partial C}{\partial S} = \frac{\partial}{\partial S} \left ( S * P_{1} - K*e^{-rt}*P_{2}\right )" /></a>

We can rearrange it to the following: 

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;C}{\partial&space;S}&space;=&space;P_{1}&space;&plus;&space;S*\frac{\partial&space;P_{1}}{\partial&space;S}&space;&plus;&space;K*e^{-rt}&space;*&space;\frac{\partial&space;P_{2}}{\partial&space;S}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;C}{\partial&space;S}&space;=&space;P_{1}&space;&plus;&space;S*\frac{\partial&space;P_{1}}{\partial&space;S}&space;&plus;&space;K*e^{-rt}&space;*&space;\frac{\partial&space;P_{2}}{\partial&space;S}" title="\frac{\partial C}{\partial S} = P_{1} + S*\frac{\partial P_{1}}{\partial S} + K*e^{-rt} * \frac{\partial P_{2}}{\partial S}" /></a>

#### Define P<sub>j</sub> and f<sub>j</sub>
Where P<sub>j</sub> and f<sub>j</sub> are the following: 

<a href="https://www.codecogs.com/eqnedit.php?latex=P_{j}&space;=&space;\frac{1}{2}&space;&plus;&space;\frac{1}{\pi}&space;*&space;\int_{0}^{\infty&space;}&space;Re&space;(\frac{e^{-i\phi&space;ln(K)}*f_{j}}{i\phi&space;}&space;)d\phi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P_{j}&space;=&space;\frac{1}{2}&space;&plus;&space;\frac{1}{\pi}&space;*&space;\int_{0}^{\infty&space;}&space;Re&space;(\frac{e^{-i\phi&space;ln(K)}*f_{j}}{i\phi&space;}&space;)d\phi" title="P_{j} = \frac{1}{2} + \frac{1}{\pi} * \int_{0}^{\infty } Re (\frac{e^{-i\phi ln(K)}*f_{j}}{i\phi } )d\phi" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=f_{j}&space;=&space;e^{C&space;&plus;&space;D.v&space;&plus;&space;ln(S)\phi&space;i&space;}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_{j}&space;=&space;e^{C&space;&plus;&space;D.v&space;&plus;&space;ln(S)\phi&space;i&space;}" title="f_{j} = e^{C + D.v + ln(S)\phi i }" /></a>

#### Get derivative of P<sub>j</sub> and f<sub>j</sub> wrt S

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;f_{j}}{\partial&space;S}&space;=&space;\frac{i\phi&space;}{S}&space;f_{j}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;f_{j}}{\partial&space;S}&space;=&space;\frac{i\phi&space;}{S}&space;f_{j}" title="\frac{\partial f_{j}}{\partial S} = \frac{i\phi }{S} f_{j}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;P_{j}}{\partial&space;S}&space;=&space;\frac{1}{\pi}&space;\int_{0}^{\infty}&space;Re(\frac{e^{-i&space;\phi&space;ln(K)&space;}f_{j}}{S})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;P_{j}}{\partial&space;S}&space;=&space;\frac{1}{\pi}&space;\int_{0}^{\infty}&space;Re(\frac{e^{-i&space;\phi&space;ln(K)&space;}f_{j}}{S})" title="\frac{\partial P_{j}}{\partial S} = \frac{1}{\pi} \int_{0}^{\infty} Re(\frac{e^{-i \phi ln(K) }f_{j}}{S})" /></a>

#### Subbing in the derivatives of P<sub>j</sub> and f<sub>j</sub> 

<a href="https://www.codecogs.com/eqnedit.php?latex=Delta&space;=&space;\frac{1}{2}&space;&plus;&space;\frac{1}{\pi}\int_{0}^{\infty&space;}&space;Re(e^{-i\phi&space;ln(K)}&space;*((1&plus;\frac{1}{i\phi})f_{j}-\frac{Ke^{-rt}}{S}f_{2}))d\phi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Delta&space;=&space;\frac{1}{2}&space;&plus;&space;\frac{1}{\pi}\int_{0}^{\infty&space;}&space;Re(e^{-i\phi&space;ln(K)}&space;*((1&plus;\frac{1}{i\phi})f_{j}-\frac{Ke^{-rt}}{S}f_{2}))d\phi" title="Delta = \frac{1}{2} + \frac{1}{\pi}\int_{0}^{\infty } Re(e^{-i\phi ln(K)} *((1+\frac{1}{i\phi})f_{j}-\frac{Ke^{-rt}}{S}f_{2}))d\phi" /></a>
