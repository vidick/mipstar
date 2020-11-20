<article class="env-example" id="0007">
<p><a class="environment-identifier" href="/tag/0007">Example <span data-tag="0007">2.0.6</span>.</a> Consider </p>
<div class="equation">
  \begin{equation*}  A_0=\left(\begin{array}{cc}1&amp; 0\\ 0&amp; -1\end{array}\right),\qquad B_0=\frac{1}{\sqrt{2}}\left(\begin{array}{cc}1&amp; 1\\ 1&amp; -1\end{array}\right),\qquad A_1=\left(\begin{array}{cc}0&amp; 1\\ 1&amp; 0\end{array}\right),\qquad B_1=\frac{1}{\sqrt{2}}\left(\begin{array}{cc}1&amp; -1\\ -1&amp; -1\end{array}\right)\; . \end{equation*}
</div>
<p> Then you can verify that $A_0,A_1,B_0,B_1$ are observables; in fact, you can recognize some standard matrices from quantum information. Moreover, </p>
<div class="equation">
  \[ \frac{1}{2} \langle A_0, B_0\rangle = \frac{1}{2}\langle A_0, B_1\rangle = \frac{1}{2} \langle A_1, B_0\rangle =\frac{\sqrt{2}}{2}\; ,\quad \text{and}\quad \frac{1}{2}\langle A_1,B_1\rangle = -\frac{\sqrt{2}}{2}\; . \]
</div>
<p> Plugging these calculations into the definition of the CHSH game (Example <a data-tag="0007" href="/tag/0007">2.0.6</a>), we see that these observables, together with a maximally entangled state in dimension $d=2$, achieve a bias of </p>
<div class="equation">
  \[  \frac{1}{4}\cdot 4\cdot \frac{\sqrt{2}}{2} =\frac{\sqrt{2}}{2} \approx 0.73\; ,  \]
</div>
<p> which is strictly larger than the bias $1/2$ that we proved optimal for classical players. </p>
</article>