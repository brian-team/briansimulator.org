<html><body><p>The latest SVN version of Brian includes a new experimental package, brian.experimental.codegen, which is designed for automatic generation of code for numerical integration in Python, C++ and GPU C++. If the global preference usecodegen is True then it will be used automatically for all nonlinear differential equations. If usecodegenweave is True then C code will be generated, otherwise Python code. In all cases the code runs faster. GPU code is not currently used. Use the <a href="http://www.briansimulator.org/docs/reference-preferences.html#global-configuration-file">brian_global_preferences.py</a> file to activate it for all your code. As an example of how it works, let's use the following Brian Equations object:

[python]
eqs = Equations('''
dV/dt = -W*V/(10*second) : volt
dW/dt = -V**2/(1*second) : volt
''')
[/python]

The codegen module generates the following code for the Euler update scheme. For Python:

[python]
V = _S[0]
W = _S[1]
V__tmp = -0.1*V*W
W__tmp = -1.0*V**2
V += V__tmp*dt
W += W__tmp*dt
[/python]

For C:

[cpp]
double *V__Sbase = _S+0*num_neurons;
double *W__Sbase = _S+1*num_neurons;
for(int _i=0;_i&lt;num_neurons;_i++){
    double &amp;V = *V__Sbase++;
    double &amp;W = *W__Sbase++;
    double V__tmp = -0.1*V*W;
    double W__tmp = -1.0*pow(V, 2);
    V += V__tmp*dt;
    W += W__tmp*dt;
}
[/cpp]

And for the GPU:

[cpp]
__global__ void stateupdate(int num_neurons, double t, double *S)
{
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if(i&gt;=num_neurons) return;
    double &amp;V = S[i+0*num_neurons];
    double &amp;W = S[i+1*num_neurons];
    double &amp;V = *V__Sbase++;
    double &amp;W = *W__Sbase++;
    double V__tmp = -0.1*V*W;
    double W__tmp = -1.0*pow(V, 2);
    V += V__tmp*dt;
    W += W__tmp*dt;
}
[/cpp]

These are all generated from the following template for the Euler integration scheme:

[python]
euler_scheme = [
    (('foreachvar', 'nonzero'),
        '''
        $vartype ${var}__tmp = $var_expr
        '''),
    (('foreachvar', 'nonzero'),
        '''
        $var += ${var}__tmp*dt
        ''')
    ]
[/python]

The other schemes are the RK2 and exponential Euler scheme. For example, the exponential Euler scheme is:

[python]
exp_euler_scheme = [
    (('foreachvar', 'nonzero'),
        '''
        $vartype ${var}__B = @substitute(var_expr, {var:0})
        $vartype ${var}__A = @substitute(var_expr, {var:1})
        ${var}__A -= ${var}__B
        ${var}__B /= ${var}__A
        ${var}__A *= dt
        '''),
    (('foreachvar', 'nonzero'),
        '''
        $var += ${var}__B
        $var *= exp(${var}__A)
        $var -= ${var}__B
        ''')
    ]
[/python]

On the Equations above, this generates the following Python code:

[python]
V = _S[0]
W = _S[1]
V__B = 0
W__B = -1.0*V**2
V__A = -0.1*W
W__A = -1.0*V**2
V__A -= V__B
W__A -= W__B
V__B /= V__A
W__B /= W__A
V__A *= dt
W__A *= dt
V += V__B
W += W__B
V *= exp(V__A)
W *= exp(W__A)
V -= V__B
W -= W__B
[/python]

And similarly for C++ and GPU.

We will be extending the automatic generation of code into other areas, including resets, thresholds, and STDP code.

If you have any comments on the approach, bug reports, etc. please let us know!</p></body></html>