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
\theta_e =& \tan^{-1}{\left(\frac{s_\gamma}{c_\gamma} \right)}
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
\theta_e =& \tan^{-1}{ \left( \frac{s_\gamma + s_\delta}{c_\gamma - c_\delta} \right) }
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
## 新たな変数定義
新しく$\gamma$と$\delta$を定義する。
$$
\begin{aligned}
\gamma = \frac{1}{2A} (c_\gamma + js_\gamma) =& ( L_i - L_m \cos{(2 \theta_{\gamma} )}  + jK L_m \sin{(2 \theta_{\gamma} )} ) e^{i\theta_e}\\
\delta = \frac{1}{2A} (c_\delta + js_\delta) =& ( - K(L_i + L_m \cos{(2 \theta_{\gamma} )}) - j L_m \sin{(2 \theta_{\gamma} )} ) e^{-i\theta_e}
\end{aligned}
$$

## 計算の準備
共役により、次の値が計算に利用できる。
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
結論として再掲する。
$$
\begin{aligned}
\gamma - \overline\delta =& ( (K+1)L_i + (K-1) L_m e^{i2\theta_\gamma})e^{i\theta_e}\\
\overline\gamma + \delta =& ( (-K+1)L_i - (K+1) L_m e^{i2\theta_\gamma})e^{-i\theta_e}
\end{aligned}
$$
## 不要な値の除去
ここからは$L_me^{i2\theta_\gamma}$を除去する事を目標にする。
$$
\begin{aligned}
(K+1)(\gamma - \overline\delta) =& ( (K+1)^2L_i + (K+1)(K-1) L_m e^{i2\theta_\gamma})e^{i\theta_e}\\
(K-1)(\overline\gamma + \delta) =& ( -(K-1)^2L_i - (K+1)(K-1) L_m e^{i2\theta_\gamma})e^{-i\theta_e}\\
\\
(K+1)(\gamma - \overline\delta) + (K-1)(\overline\gamma + \delta) =& (K+1)^2L_i e^{i\theta_e} -(K-1)^2L_i e^{-i\theta_e} + (K+1)(K-1)L_m e^{i2\theta_\gamma}(e^{i\theta_e} - e^{-i\theta_e})\\
\end{aligned}
$$
実数係数では、$L_me^{i2\theta_\gamma}$が除去できない。
複素数$e^{i\theta_e}$を乗じて除去する。
$$
\begin{aligned}
(K+1)(\gamma - \overline\delta)e^{-i\theta_e} =& ( (K+1)^2L_i + (K+1)(K-1) L_m e^{i2\theta_\gamma})\\
(K-1)(\overline\gamma + \delta)e^{i\theta_e} =& ( -(K-1)^2L_i - (K+1)(K-1) L_m e^{i2\theta_\gamma})\\
\\
(K+1)(\gamma - \overline\delta)e^{-i\theta_e} + (K-1)(\overline\gamma + \delta)e^{i\theta_e} =& (K+1)^2L_i  -(K-1)^2L_i  = 4KL_i\\
\end{aligned}
$$
この式は実部しか持たない事が分かった。
## 虚部の係数比較
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
虚部が値を持たない事に着目する。
$$
\renewcommand{\Re}{\operatorname{Re}}
\renewcommand{\Im}{\operatorname{Im}}
\begin{aligned}
&\Im ( (K+1)(\gamma - \overline\delta)e^{-i\theta_e} + (K-1)(\overline\gamma + \delta)e^{i\theta_e} ) \\
& = \frac{1}{2A} (K+1) (j((s_\gamma + s_\delta)\cos{\theta_e} - (c_\gamma - c_\delta)\sin{\theta_e} )) \\
+&\frac{1}{2A} (K-1) (j((s_\gamma - s_\delta)\cos{\theta_e} + (c_\gamma + c_\delta)\sin{\theta_e} )) = 0
\end{aligned}
$$

$$
\Leftrightarrow \frac{1}{A} j (Ks_\gamma + s_\delta) \cos{\theta_e} + \frac{1}{A} j (K c_\delta - c_\gamma) \sin{\theta_e} = 0\\
\Leftrightarrow \frac{\sin{\theta_e}}{\cos{\theta_e}} = -\frac{Ks_\gamma + s_\delta}{K c_\delta - c_\gamma}
$$
よって、
$$
\theta_e = \arctan{\left(
 -\frac{Ks_\gamma + s_\delta}{K c_\delta - c_\gamma} \right)}
$$

# python + sympyで検算
```python
print("@calculate 220827-2 my expr")
y = -(K*s_gammat + s_deltat)
x = K*c_deltat + c_gammat
print("@x")
print(simplify_collect(sy,x,sy.cos(theta_e)))
print("@y")
print(simplify_collect(sy,y,sy.sin(theta_e)))
print("@calculate atan my expr")
print(simplify_atan(sy, y, x))
```
## 出力
arctanでθが出るような値にならない、おかしい。どこかで間違っているのだろうか。

@calculate 220827-2 my expr
@x
2*A*(-2*K*Lm*sin(theta_e)*sin(2*theta_gamma) + (-K**2*Li - K**2*Lm*cos(2*theta_gamma) + Li - Lm*cos(2*theta_gamma))*cos(theta_e))
@y
2*A*(-K**2*Lm*sin(2*theta_gamma)*cos(theta_e) - 2*K*Li*sin(theta_e) + Lm*sin(2*theta_gamma)*cos(theta_e))
@calculate atan my expr
atan(K**2*Lm*sin(2*theta_gamma)*cos(theta_e)/(K**2*Li*cos(theta_e) + K**2*Lm*cos(theta_e)*cos(2*theta_gamma) + 2*K*Lm*sin(theta_e)*sin(2*theta_gamma) - Li*cos(theta_e) + Lm*cos(theta_e)*cos(2*theta_gamma)) + 2*K*Li*sin(theta_e)/(K**2*Li*cos(theta_e) + K**2*Lm*cos(theta_e)*cos(2*theta_gamma) + 2*K*Lm*sin(theta_e)*sin(2*theta_gamma) - Li*cos(theta_e) + Lm*cos(theta_e)*cos(2*theta_gamma)) - Lm*sin(2*theta_gamma)*cos(theta_e)/(K**2*Li*cos(theta_e) + K**2*Lm*cos(theta_e)*cos(2*theta_gamma) + 2*K*Lm*sin(theta_e)*sin(2*theta_gamma) - Li*cos(theta_e) + Lm*cos(theta_e)*cos(2*theta_gamma)))
MacBook-Air:calc220827 watashi$ 

# オンライン検証
paizaに簡単に検証できる場所を作った。
https://paiza.io/projects/HXA4KsZ6yvzAVFsMGdVaEQ
ただし、paizaには時間制限があることと、sympyを利用した代数計算は計算量が多いため、複雑な式はタイムアウトしてしまい検証ができない。
そのため、ローカル環境で検証するのがよい。