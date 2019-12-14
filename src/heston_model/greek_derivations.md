# Greek Derivations

The purpose of this document is to go through the derivation process of the greeks for a European Call option using the Heston model. 

## Delta 

#### Define call value
The value of a call is the following: 
U = S * P<sub>1</sub> - Ke<sup>(-rt)</sup> * P<sub>2</sub> 

#### Define Delta
Delta is the change in the price of the call, U with respect the the change in the underlying price S.

<a href="https://www.codecogs.com/eqnedit.php?latex=Delta&space;=&space;\frac{\partial&space;U}{\partial&space;S}&space;=&space;\frac{\partial}{\partial&space;S}&space;\left&space;(&space;S&space;*&space;P_{1}&space;-&space;K*e^{-rt}*P_{2}\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Delta&space;=&space;\frac{\partial&space;U}{\partial&space;S}&space;=&space;\frac{\partial}{\partial&space;S}&space;\left&space;(&space;S&space;*&space;P_{1}&space;-&space;K*e^{-rt}*P_{2}\right&space;)" title="Delta = \frac{\partial U}{\partial S} = \frac{\partial}{\partial S} \left ( S * P_{1} - K*e^{-rt}*P_{2}\right )" /></a>

We can rearrange it to the following: 

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;U}{\partial&space;S}&space;=&space;P_{1}&space;&plus;&space;S*\frac{\partial&space;P_{1}}{\partial&space;S}&space;&plus;&space;K*e^{-rt}&space;*&space;\frac{\partial&space;P_{2}}{\partial&space;S}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;U}{\partial&space;S}&space;=&space;P_{1}&space;&plus;&space;S*\frac{\partial&space;P_{1}}{\partial&space;S}&space;&plus;&space;K*e^{-rt}&space;*&space;\frac{\partial&space;P_{2}}{\partial&space;S}" title="\frac{\partial U}{\partial S} = P_{1} + S*\frac{\partial P_{1}}{\partial S} + K*e^{-rt} * \frac{\partial P_{2}}{\partial S}" /></a>

#### Define P<sub>j</sub> and f<sub>j</sub>
Where P<sub>j</sub> and f<sub>j</sub> are the following: 

<a href="https://www.codecogs.com/eqnedit.php?latex=P_{j}&space;=&space;\frac{1}{2}&space;&plus;&space;\frac{1}{\pi}&space;*&space;\int_{0}^{\infty&space;}&space;Re&space;(\frac{e^{-i\phi&space;ln(K)}*f_{j}}{i\phi&space;}&space;)d\phi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P_{j}&space;=&space;\frac{1}{2}&space;&plus;&space;\frac{1}{\pi}&space;*&space;\int_{0}^{\infty&space;}&space;Re&space;(\frac{e^{-i\phi&space;ln(K)}*f_{j}}{i\phi&space;}&space;)d\phi" title="P_{j} = \frac{1}{2} + \frac{1}{\pi} * \int_{0}^{\infty } Re (\frac{e^{-i\phi ln(K)}*f_{j}}{i\phi } )d\phi" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=f_{j}&space;=&space;e^{C&space;&plus;&space;D.v&space;&plus;&space;ln(S)\phi&space;i&space;}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_{j}&space;=&space;e^{C&space;&plus;&space;D.v&space;&plus;&space;ln(S)\phi&space;i&space;}" title="f_{j} = e^{C + D.v + ln(S)\phi i }" /></a>

#### Get derivative of P<sub>j</sub> and f<sub>j</sub> wrt S

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;f_{j}}{\partial&space;S}&space;=&space;\frac{i\phi&space;}{S}&space;f_{j}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;f_{j}}{\partial&space;S}&space;=&space;\frac{i\phi&space;}{S}&space;f_{j}" title="\frac{\partial f_{j}}{\partial S} = \frac{i\phi }{S} f_{j}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;P_{j}}{\partial&space;S}&space;=&space;\frac{1}{\pi}&space;\int_{0}^{\infty}&space;Re(\frac{e^{-i&space;\phi&space;ln(K)&space;}f_{j}}{S})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;P_{j}}{\partial&space;S}&space;=&space;\frac{1}{\pi}&space;\int_{0}^{\infty}&space;Re(\frac{e^{-i&space;\phi&space;ln(K)&space;}f_{j}}{S})" title="\frac{\partial P_{j}}{\partial S} = \frac{1}{\pi} \int_{0}^{\infty} Re(\frac{e^{-i \phi ln(K) }f_{j}}{S})" /></a>

#### Subbing in the derivatives of P<sub>j</sub> and f<sub>j</sub> 

<a href="https://www.codecogs.com/eqnedit.php?latex=Delta&space;=&space;\frac{1}{2}&space;&plus;&space;\frac{1}{\pi}\int_{0}^{\infty&space;}&space;Re(e^{-i\phi&space;ln(K)}&space;*((1&plus;\frac{1}{i\phi})f_{j}-\frac{Ke^{-rt}}{S}f_{2}))d\phi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Delta&space;=&space;\frac{1}{2}&space;&plus;&space;\frac{1}{\pi}\int_{0}^{\infty&space;}&space;Re(e^{-i\phi&space;ln(K)}&space;*((1&plus;\frac{1}{i\phi})f_{j}-\frac{Ke^{-rt}}{S}f_{2}))d\phi" title="Delta = \frac{1}{2} + \frac{1}{\pi}\int_{0}^{\infty } Re(e^{-i\phi ln(K)} *((1+\frac{1}{i\phi})f_{j}-\frac{Ke^{-rt}}{S}f_{2}))d\phi" /></a>


## Gamma

#### Define call value
The value of a call is the following: 
U = S * P<sub>1</sub> - Ke<sup>(-rt)</sup> * P<sub>2</sub> 

#### Define Gamma
Gamma is the second derivative in the price of the call, U with respect the the change in the underlying price S.
Since Delta is the first derivative, we can also look at Gamma as the first derivative of Delta with respect to S. 

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial^{2}&space;U}{\partial&space;S^{2}}&space;=&space;\frac{\partial&space;}{\partial&space;S}&space;(Delta)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial^{2}&space;U}{\partial&space;S^{2}}&space;=&space;\frac{\partial&space;}{\partial&space;S}&space;(Delta)" title="\frac{\partial^{2} U}{\partial S^{2}} = \frac{\partial }{\partial S} (Delta)" /></a>

Subbing in the final value of delta solved above: 

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial^{2}&space;U}{\partial&space;S^{2}}&space;=&space;\frac{\partial&space;}{\partial&space;S}&space;(\frac{1}{2}&space;&plus;&space;\frac{1}{\pi}&space;\int_{0}^{\infty}&space;Re(e^{-i\phi&space;ln(K)}&space;((1&plus;\frac{1}{i\phi})f_{i}&space;-&space;\frac{Ke^{-rt}}{S}f_{2}))d\phi)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial^{2}&space;U}{\partial&space;S^{2}}&space;=&space;\frac{\partial&space;}{\partial&space;S}&space;(\frac{1}{2}&space;&plus;&space;\frac{1}{\pi}&space;\int_{0}^{\infty}&space;Re(e^{-i\phi&space;ln(K)}&space;((1&plus;\frac{1}{i\phi})f_{i}&space;-&space;\frac{Ke^{-rt}}{S}f_{2}))d\phi)" title="\frac{\partial^{2} U}{\partial S^{2}} = \frac{\partial }{\partial S} (\frac{1}{2} + \frac{1}{\pi} \int_{0}^{\infty} Re(e^{-i\phi ln(K)} ((1+\frac{1}{i\phi})f_{i} - \frac{Ke^{-rt}}{S}f_{2}))d\phi)" /></a>

#### Get derivative of f<sub>j</sub> wrt S
<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;f_{j}}{\partial&space;S}&space;=&space;\frac{i\phi&space;}{S}&space;f_{j}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;f_{j}}{\partial&space;S}&space;=&space;\frac{i\phi&space;}{S}&space;f_{j}" title="\frac{\partial f_{j}}{\partial S} = \frac{i\phi }{S} f_{j}" /></a>

#### Differentiate 
<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial^{2}&space;U}{\partial&space;S^{2}}&space;=&space;(\frac{1}{\pi}&space;\int_{0}^{\infty}&space;Re(e^{-i\phi&space;ln(K)}&space;((1&plus;\frac{1}{i\phi})f_{i}*\frac{i\phi}{S}&space;-&space;\frac{Ke^{-rt}}{S}f_{2}*\frac{i\phi}{S}&plus;&space;\frac{Ke^{-rt}}{S^2}f_{2}))d\phi)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial^{2}&space;U}{\partial&space;S^{2}}&space;=&space;(\frac{1}{\pi}&space;\int_{0}^{\infty}&space;Re(e^{-i\phi&space;ln(K)}&space;((1&plus;\frac{1}{i\phi})f_{i}*\frac{i\phi}{S}&space;-&space;\frac{Ke^{-rt}}{S}f_{2}*\frac{i\phi}{S}&plus;&space;\frac{Ke^{-rt}}{S^2}f_{2}))d\phi)" title="\frac{\partial^{2} U}{\partial S^{2}} = (\frac{1}{\pi} \int_{0}^{\infty} Re(e^{-i\phi ln(K)} ((1+\frac{1}{i\phi})f_{i}*\frac{i\phi}{S} - \frac{Ke^{-rt}}{S}f_{2}*\frac{i\phi}{S}+ \frac{Ke^{-rt}}{S^2}f_{2}))d\phi)" /></a>

#### We can then simplify the equation

<a href="https://www.codecogs.com/eqnedit.php?latex=Gamma=&space;(\frac{1}{\pi}&space;\int_{0}^{\infty}&space;Re(e^{-i\phi&space;ln(K)}&space;((1&plus;i\phi)f_{i}*\frac{1}{S}&space;&plus;&space;\frac{Ke^{-rt}}{S^2}f_{2}*(1-i\phi)))d\phi)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Gamma=&space;(\frac{1}{\pi}&space;\int_{0}^{\infty}&space;Re(e^{-i\phi&space;ln(K)}&space;((1&plus;i\phi)f_{i}*\frac{1}{S}&space;&plus;&space;\frac{Ke^{-rt}}{S^2}f_{2}*(1-i\phi)))d\phi)" title="Gamma= (\frac{1}{\pi} \int_{0}^{\infty} Re(e^{-i\phi ln(K)} ((1+i\phi)f_{i}*\frac{1}{S} + \frac{Ke^{-rt}}{S^2}f_{2}*(1-i\phi)))d\phi)" /></a>

## Vega

#### Define Vega
Vega is the  derivative of the price of the call option, C with respect the the change in the underlying volatility.

<a href="https://www.codecogs.com/eqnedit.php?latex=Vega&space;=&space;\frac{\partial&space;C}{\partial&space;V}&space;=&space;\frac{\partial&space;}{\partial&space;V}&space;(S*P_{1}&space;-&space;Ke^{-rt}*P_{2})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Vega&space;=&space;\frac{\partial&space;C}{\partial&space;V}&space;=&space;\frac{\partial&space;}{\partial&space;V}&space;(S*P_{1}&space;-&space;Ke^{-rt}*P_{2})" title="Vega = \frac{\partial C}{\partial V} = \frac{\partial }{\partial V} (S*P_{1} - Ke^{-rt}*P_{2})" /></a>

#### Get derivative of P<sub>j</sub> and f<sub>j</sub> wrt v
<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;f}{\partial&space;V}&space;=&space;D&space;*&space;f_{j}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;f}{\partial&space;V}&space;=&space;D&space;*&space;f_{j}" title="\frac{\partial f}{\partial V} = D * f_{j}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;P_{j}}{\partial&space;V}&space;=&space;\frac{1}{\pi}\int_{0}^{\infty}&space;Re&space;(\frac{e^{-i\phi&space;ln(K)}}{i\phi}Df_{j})d\phi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;P_{j}}{\partial&space;V}&space;=&space;\frac{1}{\pi}\int_{0}^{\infty}&space;Re&space;(\frac{e^{-i\phi&space;ln(K)}}{i\phi}Df_{j})d\phi" title="\frac{\partial P_{j}}{\partial V} = \frac{1}{\pi}\int_{0}^{\infty} Re (\frac{e^{-i\phi ln(K)}}{i\phi}Df_{j})d\phi" /></a>

#### Subbing these into Vega formula 

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;C}{\partial&space;V}&space;=&space;\frac{S}{\pi}\int_{0}^{\infty}&space;Re&space;(\frac{e^{-i\phi&space;ln(K)}}{i\phi}D_{1}f_{1})d\phi&space;-&space;\frac{Ke^{-rt}}{\pi}\int_{0}^{\infty}&space;Re&space;(\frac{e^{-i\phi&space;ln(K)}}{i\phi}D_{2}f_{2})d\phi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;C}{\partial&space;V}&space;=&space;\frac{S}{\pi}\int_{0}^{\infty}&space;Re&space;(\frac{e^{-i\phi&space;ln(K)}}{i\phi}D_{1}f_{1})d\phi&space;-&space;\frac{Ke^{-rt}}{\pi}\int_{0}^{\infty}&space;Re&space;(\frac{e^{-i\phi&space;ln(K)}}{i\phi}D_{2}f_{2})d\phi" title="\frac{\partial C}{\partial V} = \frac{S}{\pi}\int_{0}^{\infty} Re (\frac{e^{-i\phi ln(K)}}{i\phi}D_{1}f_{1})d\phi - \frac{Ke^{-rt}}{\pi}\int_{0}^{\infty} Re (\frac{e^{-i\phi ln(K)}}{i\phi}D_{2}f_{2})d\phi" /></a>

#### We can then simplify the formula 

<a href="https://www.codecogs.com/eqnedit.php?latex=Vega&space;=&space;\frac{\partial&space;C}{\partial&space;V}&space;=&space;\frac{1}{\pi}\int_{0}^{\infty}&space;Re&space;(\frac{e^{-i\phi&space;ln(K)}}{i\phi}&space;*&space;(D_{1}*f_{1}*S&space;-&space;D_{2}*f_{2}*Ke^{-rt}))d\phi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Vega&space;=&space;\frac{\partial&space;C}{\partial&space;V}&space;=&space;\frac{1}{\pi}\int_{0}^{\infty}&space;Re&space;(\frac{e^{-i\phi&space;ln(K)}}{i\phi}&space;*&space;(D_{1}*f_{1}*S&space;-&space;D_{2}*f_{2}*Ke^{-rt}))d\phi" title="Vega = \frac{\partial C}{\partial V} = \frac{1}{\pi}\int_{0}^{\infty} Re (\frac{e^{-i\phi ln(K)}}{i\phi} * (D_{1}*f_{1}*S - D_{2}*f_{2}*Ke^{-rt}))d\phi" /></a>

## Rho 

#### Define Rho 

Rho is the  derivative of the price of the call option, C with respect the the change in the underlying interest rate.

<a href="https://www.codecogs.com/eqnedit.php?latex=Rho=&space;\frac{\partial&space;C}{\partial&space;r}&space;=&space;\frac{\partial&space;}{\partial&space;r}&space;(S*P_1&space;-&space;Ke^{-rt}P_2)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Rho=&space;\frac{\partial&space;C}{\partial&space;r}&space;=&space;\frac{\partial&space;}{\partial&space;r}&space;(S*P_1&space;-&space;Ke^{-rt}P_2)" title="Rho= \frac{\partial C}{\partial r} = \frac{\partial }{\partial r} (S*P_1 - Ke^{-rt}P_2)" /></a>

#### We know what P<sub>j</sub> and f<sub>j</sub> are from above, however interest rate is also apart of C (not the call) within f<sub>j</sub>. C is defined as the following:

<a href="https://www.codecogs.com/eqnedit.php?latex=C&space;=&space;r&space;\phi&space;i&space;t&space;&plus;&space;\frac{\alpha&space;}{\sigma&space;^2}(b_j&space;-&space;\rho&space;\sigma&space;\phi&space;i)t&space;-&space;2ln(\frac{1-ge^{-dt}}{1-g})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C&space;=&space;r&space;\phi&space;i&space;t&space;&plus;&space;\frac{\alpha&space;}{\sigma&space;^2}(b_j&space;-&space;\rho&space;\sigma&space;\phi&space;i)t&space;-&space;2ln(\frac{1-ge^{-dt}}{1-g})" title="C = r \phi i t + \frac{\alpha }{\sigma ^2}(b_j - \rho \sigma \phi i)t - 2ln(\frac{1-ge^{-dt}}{1-g})" /></a>

#### Now lets get the derivatives of C, P<sub>j</sub> and f<sub>j</sub>

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;C}{\partial&space;r}&space;=&space;\phi&space;it" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;C}{\partial&space;r}&space;=&space;\phi&space;it" title="\frac{\partial C}{\partial r} = \phi it" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;f_j}{\partial&space;r}&space;=&space;\phi&space;i&space;t&space;f_j" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;f_j}{\partial&space;r}&space;=&space;\phi&space;i&space;t&space;f_j" title="\frac{\partial f_j}{\partial r} = \phi i t f_j" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;P_j}{\partial&space;r}&space;=&space;\frac{1}{\pi}&space;\int_{0}^{\infty}&space;Re(e^{-i&space;\phi&space;ln(K)}f_j&space;t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;P_j}{\partial&space;r}&space;=&space;\frac{1}{\pi}&space;\int_{0}^{\infty}&space;Re(e^{-i&space;\phi&space;ln(K)}f_j&space;t)" title="\frac{\partial P_j}{\partial r} = \frac{1}{\pi} \int_{0}^{\infty} Re(e^{-i \phi ln(K)}f_j t)" /></a>

