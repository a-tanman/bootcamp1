def position_velocity(u,t):
    G = 9.81
    y = u*t - 0.5*G*(t**2)
    y2 = u - G*t
    return(round(y, 2), round(y2, 2))

def close_enough(num1, num2):
    tol = 1e-10
    return abs(num1 - num2) < tol

print(position_velocity(5.0,10.0))
print(position_velocity(5.0,0.0))
print(position_velocity(0.0,5.0))
ans = position_velocity(5.0, 10.0)
assert close_enough(ans[0],-440.5) and close_enough(ans[1], -93.1)