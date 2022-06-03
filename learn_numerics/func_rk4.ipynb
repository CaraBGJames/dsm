{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#    RK4.M   Use 4th order Runge Kutta Method for Numerical Solution of IVPs\n",
    "\n",
    "# The inputs to the function are:\n",
    "#         fxy = the name of the function containing f(x,y) (e.g. oneode, twoode)\n",
    "#         xo,xf = initial and final values of the independent variable (integers or floats)\n",
    "#         yo = initial value of dependent variable at xo (numpy array)\n",
    "#         N = number of intervals to use between xo and xf (integer)\n",
    "\n",
    "# The outputs to the function are:\n",
    "#         X = numpy array containing values of the independent variable\n",
    "#         Y = the estimated dependent variable at each value of the independent variable\n",
    "#         --> this variable is a 1D numpy array if only one equation is solved\n",
    "#         --> it is an M-D numpy array [y1(x) y2(x) ... ] for multiple (M) equations "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "def rk4(fxy, x0, xf, y0, N):\n",
    "\n",
    "    #compute step size and size of output variables\n",
    "    if N < 2:\n",
    "        N = 2 #set minimum number for N\n",
    "    h = (xf - x0) / N\n",
    "    X = np.zeros((N+1, 1))\n",
    "    M = np.max(np.shape(y0))\n",
    "    Y = np.zeros((N+1, M))*1j #make complex by multiplying by 1j; this way can add complex values to this during integration\n",
    "\n",
    "    #set initial conditions\n",
    "    x = x0\n",
    "    X[0] = x\n",
    "    y = [complex(val) for val in y0]  #make complex\n",
    "    Y[0,:] = y\n",
    "    \n",
    "    #begin computational loop\n",
    "    for ii in range(N):\n",
    "        \n",
    "        k1 = np.array([h * val for val in fxy(x,y)]) #evaluate function fxy; depending on equation, k1-4 can be complex; this is why we make Y and y complex as well\n",
    "        k2 = np.array([h * val for val in fxy(x+h/2, y+k1/2)])\n",
    "        k3 = np.array([h * val for val in fxy(x+h/2, y+k2/2)])\n",
    "        k4 = np.array([h * val for val in fxy(x+h, y+k3)])\n",
    "        \n",
    "        y += (k1 + 2*k2 + 2*k3 + k4) / 6.\n",
    "        x += h\n",
    "        X[ii+1] = x\n",
    "        Y[ii+1,:] = y\n",
    "    \n",
    "    return X, Y"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
