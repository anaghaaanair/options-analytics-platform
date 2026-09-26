import math
from scipy.stats import norm

#Data
S=50
K=55
T=0.25
sigma=0.30
r=0.05

#Calculate d1 and d2
d1=(math.log(S/K)+(r+sigma**2/2)*T)/(sigma*math.sqrt(T))
d2=d1-sigma*math.sqrt(T)

#Calculating normal distribution values: N(d1) and N(d2)
Nd1=norm.cdf(d1)
Nd2=norm.cdf(d2)

#Calculate call and put prices
call_price=S*Nd1-K*math.exp(-r*T)*Nd2
put_price=K*math.exp(-r*T)*norm.cdf(-d2)-S*norm.cdf(-d1)

#Greeks
call_delta=Nd1
put_delta=Nd1-1

gamma=norm.pdf(d1)/(S*sigma*math.sqrt(T))

vega=S*norm.pdf(d1)*math.sqrt(T)

call_rho=K*T*math.exp(-r*T)*Nd2

call_theta=(
    -(S*norm.pdf(d1)*sigma)/(2*math.sqrt(T))
    -r*K*math.exp(-r*T)*Nd2
)

#Printing everything
print("d1 =", d1)
print("d2 ", d2)

print("N(d1)= ", Nd1)
print("N(d2)= ", Nd2)

print("Call price =", call_price)
print("Put price =", put_price)

print("Call Delta =", call_delta)
print("Put Delta =", put_delta)
print("Gamma =", gamma)
print("Vega =", vega)
print("Call Rho =", call_rho)
print("Call Theta =", call_theta)