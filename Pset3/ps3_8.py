import math

def approx_ode(h, t0, y0, tn):
    t = t0
    y_old = y0
    y_new = y0
    while t < tn:
        y_new = y_old + h*(3+math.exp(-t)-0.5*y_old)
        y_old = y_new
        t = round(t + h, 1)
        
    return y_new


print ('approx_ode (0.1, 0, 1, 5) ')
ans = approx_ode (0.1, 0, 1, 5)
print ('Output : ', ans)
print ('approx_ode (0.1, 0, 1, 2.5) ')
ans = approx_ode (0.1, 0, 1, 2.5)
print ('Output : ', ans)
print ('approx_ode (0.1, 0, 1, 3) ')
ans = approx_ode (0.1, 0, 1, 3)
print ('Output : ', ans)
print ('approx_ode (0.1 , 0, 1, 1) ')
ans = approx_ode (0.1, 0, 1, 1)
print ('Output : ', ans)
print ('approx_ode (0.1 , 0, 1, 0) ')
ans = approx_ode (0.1, 0, 1, 0)
print ('Output : ', ans)