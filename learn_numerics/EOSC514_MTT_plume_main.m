

clear all
close all
%clc
%Bsic MTT(56) plume model; CV analysis; steady; boussinesq
%Mass (volume): d/dz(R^2w) = 2*alpha*w*R
%Momentum: d/dz(R^2w^2) = g'*R^2
%Buoyancy: d/dz(R^2*w*g') = -N^2*R^2*w
%Simplify equations: W = w*R^2 ; V = w*R ; F = w*R^2*g'

% define constants
global alpha N g_prime;;

alpha = 0.1; %entrainment coefficient
g_prime = 0.05;



% specify initial value

Q0=0.1;
M0=0.1;
F0=1;
N=0.1; %% Buoyancy frequency; vary this


Zmax = (abs(F0)^0.25/N^(3/4));
Zmom = abs(F0)^-0.5 * M0^0.75;
Z_int =5*Zmax;



%Vector of initial values
Yo =[Q0
    M0
    F0];

z=linspace(0,Z_int,1000);
z=z';
[z,y] = ode45(@MTT_odes,z,Yo);
figure(10),plot(y,z/Zmax)
legend('volume flux','momentum flux','buoyancy flux',4);
ylabel('Height z / ( F^{1/4} N^{-3/4})'); xlabel('Plume parameter');
axis([-1 10 0 5])

hold on
plot(0,z(1:20:end),'k .')
plot(0,Zmom,'r square')
