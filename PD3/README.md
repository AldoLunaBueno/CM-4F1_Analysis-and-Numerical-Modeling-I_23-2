# Problema 19

_The circle given by the equation $x^2 + y^2 + ax + by +c = 0$ passes through the points $(-2,0)$, $(-1,7)$ and $(5,-1)$. Find $a$, $b$ and $c$._

Modelemos el problema. Reemplazamos los puntos en la ecuación del círculo para obtener las 3 ecuaciones que nos permitan calcular a, b y c.

$$ -2a + c = -4 $$
$$ -a + 7b + c = -50 $$
$$ 5a + 7b + c = -26 $$

Y construimos el sistema lineal $Ax=b$ correspondiente:

$$
\begin{pmatrix}
-2 & 0 & 1\\\
-1 & 7 & 1\\\
5 & 7 & 1
\end{pmatrix}
$$

$$
\begin{pmatrix}
-2 & 0 & 1\\\
-1 & 7 & 1\\\
5 & 7 & 1
\end{pmatrix}
\cdot
\begin{pmatrix}
a\\\
b\\\
c
\end{pmatrix}
=
\begin{pmatrix}
-4\\\
-50\\\
-26
\end{pmatrix}
$$

