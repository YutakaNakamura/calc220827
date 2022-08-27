# θを計算したい
次の$c_\gamma$,$s_\gamma$,$c_\delta$,$s_\delta$と$tan^{-1}$を使って$\theta_e$を計算したい。
$$
\begin{aligned}
c_\gamma =& 2 A (- K L_m \sin{(2 \theta_{\gamma} )} \sin{(\theta_{e} )} + (L_i - L_m \cos{(2 \theta_{\gamma} )}) \cos{(\theta_{e} )})\\

s_\gamma =& 2 A (K L_m \sin{(2 \theta_{\gamma} )} \cos{(\theta_{e} )} + (L_i - L_m \cos{(2 \theta_{\gamma} )}) \sin{(\theta_{e} )})\\


c_\delta =& 2 A (- L_m \sin{(2 \theta_{\gamma} )} \sin{(\theta_{e} )} - ( K L_i + K L_m \cos{(2 \theta_{\gamma} )}) \cos{(\theta_{e} )})\\

s_\delta =& 2 A (- L_m \sin{(2 \theta_{\gamma} )} \cos{(\theta_{e} )} + (K L_i + K L_m \cos{(2 \theta_{\gamma} )}) \sin{(\theta_{e} )})
\end{aligned}
$$
条件を付与すると計算できた。

K=0のとき
$$
\begin{aligned}
c_\gamma =& 2 A ((L_i - L_m \cos{(2 \theta_{\gamma} )}) \cos{(\theta_{e} )})\\

s_\gamma =& 2 A ((L_i - L_m \cos{(2 \theta_{\gamma} )}) \sin{(\theta_{e} )})\\

\theta_e =& \tan^{-1}{\frac{s_\gamma}{c_\gamma}}
\end{aligned}
$$
K=1のとき
$$
\begin{aligned}
c_\gamma =& 2 A (- L_m \sin{(2 \theta_{\gamma} )} \sin{(\theta_{e} )} + (L_i - L_m \cos{(2 \theta_{\gamma} )}) \cos{(\theta_{e} )})\\

s_\gamma =& 2 A ( L_m \sin{(2 \theta_{\gamma} )} \cos{(\theta_{e} )} + (L_i - L_m \cos{(2 \theta_{\gamma} )}) \sin{(\theta_{e} )})\\


c_\delta =& 2 A (- L_m \sin{(2 \theta_{\gamma} )} \sin{(\theta_{e} )} - ( L_i + L_m \cos{(2 \theta_{\gamma} )}) \cos{(\theta_{e} )})\\

s_\delta =& 2 A (- L_m \sin{(2 \theta_{\gamma} )} \cos{(\theta_{e} )} + ( L_i + L_m \cos{(2 \theta_{\gamma} )}) \sin{(\theta_{e} )})\\

c_\gamma - c_\delta =& 2 A ( ( 2 L_i ) \cos{(\theta_{e} )})\\
s_\gamma + s_\delta =& 2 A ( ( 2 L_i ) \sin{(\theta_{e} )})\\

\theta_e =& \tan^{-1}{\frac{s_\gamma + s_\delta}{c_\gamma - c_\delta}}
\end{aligned}
$$


# 220827
なるほど、回転の変換の積が作用してるように見えるのか！書き直してみる。
$$
\begin{aligned}
c_\gamma =& 2 A ( (L_i - L_m \cos{(2 \theta_{\gamma} )}) \cos{(\theta_{e} )} + K L_m \sin{(2 \theta_{\gamma} )} (-\sin{(\theta_{e} )}))\\

s_\gamma =& 2 A ((L_i - L_m \cos{(2 \theta_{\gamma} )}) \sin{(\theta_{e} )}+K L_m \sin{(2 \theta_{\gamma} )} \cos{(\theta_{e} )}  )\\


c_\delta =& 2 A (- K ( L_i + L_m \cos{(2 \theta_{\gamma} )}) \cos{(\theta_{e} )}- L_m \sin{(2 \theta_{\gamma} )} \sin{(\theta_{e} )} )\\

s_\delta =& 2 A (- K (L_i + L_m \cos{(2 \theta_{\gamma} )}) (-\sin{(\theta_{e} )}) - L_m \sin{(2 \theta_{\gamma} )} \cos{(\theta_{e} )} )
\end{aligned}
$$
$$
\begin{aligned}
\gamma = \frac{1}{2A} (c_\gamma + js_\gamma) =& ( L_i - L_m \cos{(2 \theta_{\gamma} )}  + jK L_m \sin{(2 \theta_{\gamma} )} ) e^{i\theta_e}\\

\delta = \frac{1}{2A} (c_\delta + js_\delta) =& ( - K(L_i + L_m \cos{(2 \theta_{\gamma} )}) - j L_m \sin{(2 \theta_{\gamma} )} ) e^{-i\theta_e}
\end{aligned}
$$

共役
$$
\begin{aligned}
\overline\gamma =& ( L_i - L_m \cos{(2 \theta_{\gamma} )}  - jK L_m \sin{(2 \theta_{\gamma} )} ) e^{-i\theta_e}\\

\overline\delta =& ( - K(L_i + L_m \cos{(2 \theta_{\gamma} )}) + j L_m \sin{(2 \theta_{\gamma} )} ) e^{i\theta_e}
\end{aligned}
$$

$$
\begin{aligned}
\gamma - \overline\delta =& ( L_i - L_m \cos{(2 \theta_{\gamma} )}  + jK L_m \sin{(2 \theta_{\gamma} )} ) e^{i\theta_e}\\ 
& +  (  K(L_i + L_m \cos{(2 \theta_{\gamma} )}) - j L_m \sin{(2 \theta_{\gamma} )} ) e^{i\theta_e} \\
=&( (K+1)L_i + (K-1) L_m(\cos{2 \theta_\gamma}+j\sin{2\theta_\gamma}))e^{i\theta_e}\\
=&( (K+1)L_i + (K-1) L_m e^{i2\theta_\gamma})e^{i\theta_e}\\
\\
\overline\gamma + \delta =& ( L_i - L_m \cos{(2 \theta_{\gamma} )}  - jK L_m \sin{(2 \theta_{\gamma} )} ) e^{-i\theta_e}\\
& +  ( - K(L_i + L_m \cos{(2 \theta_{\gamma} )}) - j L_m \sin{(2 \theta_{\gamma} )} ) e^{-i\theta_e}\\

=&( (-K+1)L_i - (K+1) L_m(\cos{2 \theta_\gamma}+j\sin{2\theta_\gamma}))e^{-i\theta_e}\\
=&( (-K+1)L_i - (K+1) L_m e^{i2\theta_\gamma})e^{-i\theta_e}\\

\end{aligned}
$$
$L_m(e^{i2\theta_\gamma})$を除去する。

(再掲)
$$
\begin{aligned}
\gamma - \overline\delta =& ( (K+1)L_i + (K-1) L_m e^{i2\theta_\gamma})e^{i\theta_e}\\
\overline\gamma + \delta =& ( (-K+1)L_i - (K+1) L_m e^{i2\theta_\gamma})e^{-i\theta_e}\\
\\
\end{aligned}
$$
より、
$$
\begin{aligned}
(K+1)(\gamma - \overline\delta) =& ( (K+1)^2L_i + (K+1)(K-1) L_m e^{i2\theta_\gamma})e^{i\theta_e}\\
(K-1)(\overline\gamma + \delta) =& ( -(K-1)^2L_i - (K+1)(K-1) L_m e^{i2\theta_\gamma})e^{-i\theta_e}\\
\\
(K+1)(\gamma - \overline\delta) + (K-1)(\overline\gamma + \delta) =& (K+1)^2L_i e^{i\theta_e} -(K-1)^2L_i e^{-i\theta_e} + (K+1)(K-1)L_m e^{i2\theta_\gamma}(e^{i\theta_e} - e^{-i\theta_e})\\
\end{aligned}
$$

# 再計算
$$
\begin{aligned}
(K+1)(\gamma - \overline\delta)e^{-i\theta_e} =& ( (K+1)^2L_i + (K+1)(K-1) L_m e^{i2\theta_\gamma})\\
(K-1)(\overline\gamma + \delta)e^{i\theta_e} =& ( -(K-1)^2L_i - (K+1)(K-1) L_m e^{i2\theta_\gamma})\\
\\
(K+1)(\gamma - \overline\delta)e^{-i\theta_e} + (K-1)(\overline\gamma + \delta)e^{i\theta_e} =& (K+1)^2L_i  -(K-1)^2L_i  = 4KL_i\\
\end{aligned}
$$
この式は実部しか持たない事が分かる。展開する。
$$
\begin{aligned}
\gamma = \frac{1}{2A} (c_\gamma + js_\gamma)\\
\delta = \frac{1}{2A} (c_\delta + js_\delta)\\
\overline\gamma = \frac{1}{2A} (c_\gamma - js_\gamma)\\
\overline\delta = \frac{1}{2A} (c_\delta - js_\delta)\\
\end{aligned}
$$
より、
$$
\begin{aligned}
& (K+1)(\gamma - \overline\delta)e^{-i\theta_e} + (K-1)(\overline\gamma + \delta)e^{i\theta_e} \\
& = \frac{1}{2A} (K+1) ( (c_\gamma - c_\delta) + j(s_\gamma + s_\delta) ) e^{-i\theta_e} + 
\frac{1}{2A} (K-1) ((c_\gamma + c_\delta) + j(s_\delta - s_\gamma) )e^{i\theta_e} \\
& = \frac{1}{2A} (K+1) ( (c_\gamma - c_\delta) + j(s_\gamma + s_\delta) ) (\cos{\theta_e} - j\sin{\theta_e}) + 
\frac{1}{2A} (K-1) ((c_\gamma + c_\delta) + j(s_\delta - s_\gamma) ) (\cos{\theta_e} + j\sin{\theta_e}) \\

& = \frac{1}{2A} (K+1) ( ( (c_\gamma - c_\delta)\cos{\theta_e} + (s_\gamma + s_\delta)\sin{\theta_e} ) + j((s_\gamma + s_\delta)\cos{\theta_e} - (c_\gamma - c_\delta)\sin{\theta_e} ) ) \\
&+ \frac{1}{2A} (K-1) ( ( (c_\gamma + c_\delta)\cos{\theta_e} - (s_\gamma - s_\delta)\sin{\theta_e} ) + j((s_\gamma - s_\delta)\cos{\theta_e} + (c_\gamma + c_\delta)\sin{\theta_e} ) ) \\
\end{aligned}
$$

$$
\begin{aligned}
& \frac{1}{2A} (K+1) (j((s_\gamma + s_\delta)\cos{\theta_e} - (c_\gamma - c_\delta)\sin{\theta_e} )) \\
+ & \frac{1}{2A} (K-1) (j((s_\gamma - s_\delta)\cos{\theta_e} + (c_\gamma + c_\delta)\sin{\theta_e} )) = 0
\end{aligned}
$$

$$
\frac{1}{A} j (Ks_\gamma + s_\delta) \cos{\theta_e} + \frac{1}{A} j (K c_\delta - c_\gamma) \cos{\theta_e} = 0
$$