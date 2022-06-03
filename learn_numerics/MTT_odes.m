function Ydot = MTT_odes(z,y)
global alpha N g_prime

Ydot = [2*alpha*y(1).*y(2).^-0.5
        g_prime.*y(1).^2.*y(2)^-1
        -N^2*y(1)];

% dWdz=2*alpha*V^0.25;
% dVdz=2*F*W;
% dFdz=-N^2*W;