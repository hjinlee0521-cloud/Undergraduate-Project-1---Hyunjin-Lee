import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
import math
import yfinance as yf
import sklearn
from sklearn.metrics import r2_score
np.set_printoptions(suppress=True)



#Function for n * 2 'A' dataframe 
def to_n2_matrix (df, col_name) :
    new_df = {
        'col 1' : 1,
        'Called_Col' : df[col_name]
    }
    generated_df = pd.DataFrame(new_df)
    return generated_df



#Function for converting a data to array (Matrix)
def matrix_conversion (data) :
    df = pd.DataFrame(data)
    array_converted = df.to_numpy()
    return array_converted



#A function for finding x^* via Normal Equation
def normal_equation (A, b) : 
    x_approx = np.linalg.inv((A.T @ A)) @ A.T @ b
    return x_approx


#Gram-Schmidt getting Q
def gram_schmidt_q (A) :
    v1, v2 = np.hsplit(A, [1])
    v1_sqr_add = 0
    #Calculating magnitude of v1
    #iterate through rows
    for i in range(len(v1)):
        #iterate through columns
        for j in range(len(v1[0])):
            v1_sqr_add += (v1[i][j])**2  
    v1_mag = math.sqrt(v1_sqr_add)

    #Calculating u1 (unit vector of v1)
    u1 = v1 * (1/(v1_mag))

    #dot product implementation
    v2_dot_u1 = 0
    for i in range(len(v2)):
        for j in range(len(u1[0])):
            if i == j :
                v2_dot_u1 += v2[i][j] * u1[i][j]
    v2_parr = v2_dot_u1 * u1
    v2_perp = v2 - v2_parr

    #Calculating the magnitude of v2 perpendicular component
    v2_perp_sqr_add = 0
    for i in range(len(v2_perp)):
        for j in range(len(v2_perp[0])):
            v2_perp_sqr_add += (v2_perp[i][j])**2  
    v2_perp_mag = math.sqrt(v2_perp_sqr_add)

    #Calculating u2 (unit vector of v2)
    u2 = v2_perp * (1/(v2_perp_mag))

    #Final Q
    q = np.hstack((u1, u2))

    return q


#Gram-Schmidt getting R
def gram_schmidt_r (A):
    v1, v2 = np.hsplit(A, [1])
    v1_sqr_add = 0
    #Calculating magnitude of v1
    for i in range(len(v1)):
        for j in range(len(v1[0])):
            v1_sqr_add += (v1[i][j])**2  
    v1_mag = math.sqrt(v1_sqr_add)

    u1 = v1 * (1/(v1_mag))

    #dot product 구현
    v2_dot_u1 = 0
    for i in range(len(v2)):
        for j in range(len(u1[0])):
            if i == j :
                v2_dot_u1 += v2[i][j] * u1[i][j]
    v2_parr = v2_dot_u1 * u1
    v2_perp = v2 - v2_parr

    #Calculating the magnitude of v2 perpendicular component
    v2_perp_sqr_add = 0
    for i in range(len(v2_perp)):
        for j in range(len(v2_perp[0])):
            v2_perp_sqr_add += (v2_perp[i][j])**2  
    v2_perp_mag = math.sqrt(v2_perp_sqr_add)

    #making r
    r = np.zeros((2, 2))
    r[0][0] = v1_mag
    r[0][1] = v2_dot_u1
    r[1][1] = v2_perp_mag

    return r



#Function for conducting System of Equations for matrix 'x' in Rx = (Q^T)b
#A = R, B = (Q^T)b
def mat_sys_eq (A, B):
    A = sp.Matrix(A)
    B = sp.Matrix(B)

    x1, x2 = sp.symbols('x1 x2')
    x = sp.Matrix([[x1], [x2]])
    
    rx = A @ x

    #system of equations
    eq1 = rx[0] - B[0]
    eq2 = rx[1] - B[1]
    ans = sp.solve((eq1, eq2), (x1, x2))

    return ans






#Simulation Start
#Data Load + make it as Date Frame
start_data = "2015-01-05"
end_data = "2026-4-23"

#Apple Dataset Load (Close, Volume)
apple_data = yf.download("AAPL", start = start_data, end = end_data, auto_adjust = True)

#Gold Dataset Load (Close)
gold_data = yf.download("GC=F", start = start_data, end = end_data, auto_adjust = True)

#w Dataset Load (Close)
usdkrw_data = yf.download("KRW=X", start = start_data, end = end_data, auto_adjust = True)

#Bitcoin Dataset Load (Close)
bitcoin_data = yf.download("BTC-USD", start = start_data, end = end_data, auto_adjust = True)


#Date clean
cleaned_set = pd.DataFrame()
cleaned_set["Apple_Close"] = apple_data["Close"]
cleaned_set["Apple_Volume"] = apple_data["Volume"]
cleaned_set["Gold_Close"] = gold_data["Close"]
cleaned_set["Bitcoin_Close"] = bitcoin_data["Close"]
cleaned_set["USD_KRW_Close"] = usdkrw_data["Close"]

cleaned_set = cleaned_set.loc[apple_data.index]
cleaned_set = cleaned_set.ffill()

#Dataframe with percent changes (not the actual prize)
final_set = pd.DataFrame()
final_set["Apple_price_pct"] = cleaned_set["Apple_Close"].pct_change()
final_set["Gold_price_pct"] = cleaned_set["Gold_Close"].pct_change()
final_set["Bitcoin_price_pct"] = cleaned_set["Bitcoin_Close"].pct_change()
final_set["USD_KRW_pct"] = cleaned_set["USD_KRW_Close"].pct_change()
final_set["Apple_Volume_change"] = np.log(cleaned_set["Apple_Volume"]).diff() #used log to deal with the skewness and +1 to take care of 0

final_set = final_set.dropna()


#(1) Close Price Rate of Change vs Trading Volume Rate of Change
#Load each column data
aapl_price_pct = final_set["Apple_price_pct"]
aapl_volume_pct = final_set["Apple_Volume_change"]

#Trading Volume Rate of Change to n * 2 dataframe 
volume_pct_df = to_n2_matrix(final_set, "Apple_Volume_change")

#n * 2 dataframe conversion to matrix
price_pct_mat = matrix_conversion(aapl_price_pct)
volume_pct_mat = matrix_conversion(volume_pct_df)

#Normal Equation Function to find x^* 
x_approximate_normal = normal_equation(volume_pct_mat, price_pct_mat)
#B0 = 0.00102498, B1 = -0.00378235

#Equation plot + add scatter plot
x = aapl_volume_pct
y = (-0.00378235 * x) + 0.00102498
# plt.scatter(aapl_volume_pct, aapl_price_pct, s = 4, c = 'skyblue')
# plt.title('Volume Change Rate vs Price Change Rate', fontweight = 'bold')
# plt.xlabel('Log of Apple Stock Trading Volume', fontweight = 'bold')
# plt.ylabel('Percent Change of Apple Stock Price', fontweight = 'bold')
# plt.plot(x, y, c = 'yellowgreen')
# plt.show()


#normal equation r^2 value
y_hat = y
y_act = aapl_price_pct
r2_price_volume = r2_score(y_act, y_hat)
#r^2 = 0.004199441971209694

#QR Decomp Function (Get Q and R)
q_mat_vol = gram_schmidt_q(volume_pct_mat)
r_mat_vol = gram_schmidt_r(volume_pct_mat)

#(calculate Q^T*b) find x^* via matrix system of equation function 
qtb_mat_vol = q_mat_vol.T @ price_pct_mat
x_approximate_qr = mat_sys_eq(r_mat_vol, qtb_mat_vol)
#B0 = 0.00102738625107218, B1 = -0.00378913407050527

#equation plot + add scatter plot
x = aapl_volume_pct
y = (-0.00378913407050527 * x) + 0.00102738625107218
# plt.scatter(aapl_volume_pct, aapl_price_pct, s = 4, c = 'skyblue')
# plt.title('Volume Change Rate vs Price Change Rate', fontweight = 'bold')
# plt.xlabel('Log of Apple Stock Trading Volume', fontweight = 'bold')
# plt.ylabel('Percent Change of Apple Stock Price', fontweight = 'bold')
# plt.plot(x, y, c = 'coral')
# plt.show()


#QR decomp eq r^2 value
y_hat_qr = y
y_act_qr = aapl_price_pct
r2_price_volume_qr = r2_score(y_act_qr, y_hat_qr)
#r^2 = 0.0041994350805637515


#Normal r^2 value and QR r^2 value
#Normal r^2 : 0.004199441971209694
#QR r^2 : 0.0041994350805637515





#(2) Close Price Rate of Change vs Gold Price Rate of Change
#Load each column data
aapl_price_pct = final_set["Apple_price_pct"]
gold_price_pct = final_set["Gold_price_pct"]


#Make n * 2 dataframe 
gold_pct_df = to_n2_matrix(final_set, "Gold_price_pct")


#n * 2 dataframe conversion to matrix
price_pct_mat = matrix_conversion(aapl_price_pct)
gold_pct_mat = matrix_conversion(gold_pct_df)


#Normal Equation Function to find x^* 
x_approximate_normal2 = normal_equation(gold_pct_mat, price_pct_mat)
#B0 = 0.00100981, B1 = 0.03277638

#Equation plot + add scatter plot
x2 = gold_price_pct
y2 = (0.03277638 * x2) + 0.00100981
# plt.scatter(gold_price_pct, aapl_price_pct, s = 4, c = 'skyblue')
# plt.title('Gold Price Change Rate vs Stock Price Change Rate', fontweight = 'bold')
# plt.xlabel('Percent Change of Gold Price', fontweight = 'bold')
# plt.ylabel('Percent Change of Apple Stock Price', fontweight = 'bold')
# plt.plot(x2, y2, c = 'yellowgreen')
# plt.show()


#normal equation r^2 value
y_hat2 = y2
y_act2 = aapl_price_pct
r2_price_gold = r2_score(y_act2, y_hat2)
#r^2 = 0.00034778283525294107

#QR Decomp Function (Get Q and R)
q_mat_vol2 = gram_schmidt_q(gold_pct_mat)
r_mat_vol2 = gram_schmidt_r(gold_pct_mat)

#(calculate Q^T*b) find x^* via matrix system of equation function
qtb_mat_vol2 = q_mat_vol2.T @ price_pct_mat
x_approximate_qr2 = mat_sys_eq(r_mat_vol2, qtb_mat_vol2)
#B0 = 0.00102718498139251, B1 = 0.0378153848812961

#equation plot + add scatter plot
x2 = gold_price_pct
y2 = (0.0378153848812961 * x2) + 0.00102718498139251
# plt.scatter(gold_price_pct, aapl_price_pct, s = 4, c = 'skyblue')
# plt.title('Gold Price Change Rate vs Stock Price Change Rate', fontweight = 'bold')
# plt.xlabel('Percent Change of Gold Price', fontweight = 'bold')
# plt.ylabel('Percent Change of Apple Stock Price', fontweight = 'bold')
# plt.plot(x2, y2, c = 'coral')
# plt.show()


#QR decomp eq r^2 value
y_hat_qr2 = y2
y_act_qr2 = aapl_price_pct
r2_price_gold_qr = r2_score(y_act_qr2, y_hat_qr2)
#r^2 = 0.00033831859971034106


#Normal r^2 value and QR r^2 value
#Normal r^2 : 0.00034778283525294107
#QR r^2 : 0.00033831859971034106





#(3) Close Price Rate of Change vs Change of USD-KRW Exchange Rate
#Load each column data
aapl_price_pct = final_set["Apple_price_pct"]
usd_krw_pct = final_set["USD_KRW_pct"]


#Change of USD-KRW Exhange rate to n * 2 dataframe
usd_krw_pct_df = to_n2_matrix(final_set, "USD_KRW_pct")


#n * 2 dataframe conversion to matrix
price_pct_mat = matrix_conversion(aapl_price_pct)
usd_krw_mat = matrix_conversion(usd_krw_pct_df)


#Normal Equation Function to find x^* 
x_approximate_normal3 = normal_equation(usd_krw_mat, price_pct_mat)
#B0 = 0.00101864, B1 = 0.07312977


#Equation plot + add scatter plot
x3 = usd_krw_pct
y3 = (0.07312977 * x3) + 0.00101864
# plt.scatter(usd_krw_pct, aapl_price_pct, s = 4, c = 'skyblue')
# plt.title('Change Rate of USD-KRW Exchange Rate vs Stock Price Change Rate', fontweight = 'bold')
# plt.xlabel('Change Rate of USD-KRW Exchange Rate', fontweight = 'bold')
# plt.ylabel('Percent Change of Apple Stock Price', fontweight = 'bold')
# plt.plot(x3, y3, c = 'yellowgreen')
# plt.show()


#normal equation r^2 value
y_hat3 = y3
y_act3 = aapl_price_pct
r2_price_USDKRW = r2_score(y_act3, y_hat3)
#r^2 = 0.0005462027414886439


#QR Decomp Function (Get Q and R)
q_mat_vol3 = gram_schmidt_q(usd_krw_mat)
r_mat_vol3 = gram_schmidt_r(usd_krw_mat)


#(calculate Q^T*b) find x^* via matrix system of equation function
qtb_mat_vol3 = q_mat_vol3.T @ price_pct_mat
x_approximate_qr3 = mat_sys_eq(r_mat_vol3, qtb_mat_vol3)
#B0 = 0.00102741598045608, B1 = 0.0767748100587355


#equation plot + add scatter plot
x3 = usd_krw_pct
y3 = (0.0767748100587355 * x3) + 0.00102741598045608
# plt.scatter(usd_krw_pct, aapl_price_pct, s = 4, c = 'skyblue')
# plt.title('Change Rate of USD-KRW Exchange Rate vs Stock Price Change Rate', fontweight = 'bold')
# plt.xlabel('Change Rate of USD-KRW Exchange Rate', fontweight = 'bold')
# plt.ylabel('Percent Change of Apple Stock Price', fontweight = 'bold')
# plt.plot(x3, y3, c = 'coral')
# plt.show()


#QR decomp eq r^2 value
y_hat_qr3 = y3
y_act_qr3 = aapl_price_pct
r2_price_usdkrw_qr = r2_score(y_act_qr3, y_hat_qr3)
#r^2 = 0.0005446057138297489


#Normal r^2 value and QR r^2 value 
#Normal r^2 : 0.0005462027414886439
#QR r^2 : 0.0005446057138297489





#(4) Close Price Rate of Change vs Bitcoin Price Rate of Change
#Load each column data
aapl_price_pct = final_set["Apple_price_pct"]
bitcoin_price_pct = final_set["Bitcoin_price_pct"]


#Make n * 2 dataframe
bitcoin_price_pct_df = to_n2_matrix(final_set, "Bitcoin_price_pct")


#n * 2 dataframe conversion to matrix
price_pct_mat = matrix_conversion(aapl_price_pct)
bitcoin_price_mat = matrix_conversion(bitcoin_price_pct_df)


#Normal Equation Function to find x^* 
x_approximate_normal4 = normal_equation(bitcoin_price_mat, price_pct_mat)
#B0 = 0.00082841, B1 = 0.06925924


#Equation plot + add scatter plot
x4 = bitcoin_price_pct
y4 = (0.06925924 * x3) + 0.00082841
# plt.scatter(bitcoin_price_pct, aapl_price_pct, s = 4, c = 'skyblue')
# plt.title('Bitcoin Price Change Rate vs Stock Price Change Rate', fontweight = 'bold')
# plt.xlabel('Bitcoin Price Change Rate', fontweight = 'bold')
# plt.ylabel('Percent Change of Apple Stock Price', fontweight = 'bold')
# plt.plot(x4, y4, c = 'yellowgreen')
# plt.show()


#normal equation r^2 value
y_hat4 = y4
y_act4 = aapl_price_pct
r2_price_bitcoin = r2_score(y_act4, y_hat4)
#r^2 = 0.0004337419392221875


#QR Decomp Function (Get Q and R)
q_mat_vol4 = gram_schmidt_q(bitcoin_price_mat)
r_mat_vol4 = gram_schmidt_r(bitcoin_price_mat)


#(calculate Q^T*b) find x^* via matrix system of equation function
qtb_mat_vol4 = q_mat_vol4.T @ price_pct_mat
x_approximate_qr4 = mat_sys_eq(r_mat_vol4, qtb_mat_vol4)
#B0 = 0.00102629409813729, B1 = 0.0706065974055978


#equation plot + add scatter plot
x4 = bitcoin_price_pct
y4 = (0.0706065974055978 * x3) + 0.00102629409813729
# plt.scatter(bitcoin_price_pct, aapl_price_pct, s = 4, c = 'skyblue')
# plt.title('Bitcoin Price Change Rate vs Stock Price Change Rate', fontweight = 'bold')
# plt.xlabel('Bitcoin Price Change Rate', fontweight = 'bold')
# plt.ylabel('Percent Change of Apple Stock Price', fontweight = 'bold')
# plt.plot(x4, y4, c = 'coral')
# plt.show()


#QR decomp eq r^2 value
y_hat_qr4 = y4
y_act_qr4 = aapl_price_pct
r2_price_bitcoin_qr = r2_score(y_act_qr4, y_hat_qr4)
#r^2 = 0.0005453862233224527


#Normal r^2 value and QR r^2 value
#Normal r^2 : 0.0004337419392221875
#QR r^2 : 0.0005453862233224527