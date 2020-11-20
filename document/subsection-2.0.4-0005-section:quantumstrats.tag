<h3 class="tex-subsection" id="section:quantumstrats"><span data-tag="0005">2.0.4</span> Quantum strategies</h3>

<p>
Now let's consider quantum players allowed to use shared entanglement to help determine their answers. The game is the same, and in particular the verifier, and the question and answer sets, remain classical. Using that answers in an XOR game are always binary we can represent each player's strategy as a family of observables. 
</p>
<p>
<article class="env-definition" id="">
<p><a class="environment-identifier" href="/tag/">Definition <span data-tag="">2.0.5</span>.</a>A binary observable is a Hermitian matrix $X\in \ensuremath{\mathbb {C}}^{d\times d}$ such that $X=X^\dagger $ and $X^2=\mathbb {I}$ (in other words, all eigenvalues of $X$ are $\in \{ \pm 1\} $). A binary observable $X$ can always be decomposed as $X = X^0 - X^1$ for two projections $X^0$, $X^1$ such that $X^0+X^1 = \ensuremath{\mathop{\rm Id}\nolimits }$, i.e. $\{ X^0,X^1\} $ is a projective measurement. </p>
</article>
</p>
<p>
The laws of quantum mechanics state that if Alice and Bob measure their respective half of an entangled state $|\psi \rangle  \in \ensuremath{\mathbb {C}}^ d \otimes \ensuremath{\mathbb {C}}^ d$ using observables $X$ and $Y$, then the product of the outcomes they obtain has expectation 
</p>
<div class="equation">
  \begin{align*}  \textsc{E}_{}[a\cdot b] &amp; = \Pr \big ( (a,b)=(0,0) \big ) + \Pr \big ( (a,b)=(1,1) \big ) - \Pr \big ( (a,b)=(0,1) \big ) - \Pr \big ( (a,b)=(1,0) \big ) \\ &amp; = \langle \psi | X^0 \otimes Y^0 |\psi \rangle  + \langle \psi | X^1 \otimes Y^1 |\psi \rangle  - \langle \psi | X^0 \otimes Y^1 |\psi \rangle  - \langle \psi | X^1 \otimes Y^0 |\psi \rangle \\ &amp; = \langle \psi | X \otimes Y |\psi \rangle  \, \in \, [-1,1]\; . \end{align*}
</div>
<p>
 You can verify that if we restrict to $d=1$, then the only states are $|\psi \rangle  = (e^{i\theta })$ for some real angle $\theta $, the only observables are $X,Y\in \{ \pm 1\} $, and the computation above just returns the product of the observables — this is basically just a classical deterministic strategy. 
</p>
<p>
With this notation in place we can define the optimal expected payoff for quantum players in an XOR game: 
</p>
<div class="equation" id="0006">
<span class="equation-label"><a data-tag="0006" href="/tag/0006">2.0.5.1</a></span>
<div>\begin{equation} \label{eq:def-qval} \beta ^*(G)=\sup _{\substack {a_ i,b_ j\in \ensuremath{\mathbb {C}}^{d\times d}\\ a_ i^2=b_ j^2=\mathbb {I}\\ a_ i=a_ i^\dagger \\ b_ j=b_ j^\dagger }}\, \sum _{i,j}\,  A_{ij}\cdot \langle \psi | a_ i\otimes b_ j|\psi \rangle \; . \end{equation}</div>
</div>
<p>
 Note that if we restrict the entanglement to $|\phi _{d}\rangle  = d^{-1/2}\sum _{i=1}^ d |i\rangle |i\rangle $, a $d$-dimensional maximally entangled state, we obtain a particularly simple formula, since in this case 
</p>
<div class="equation">
  \[ \langle \psi | X\otimes Y |\psi \rangle  \, =\,  \frac{1}{d} \mbox{\rm Tr}(XY^ T)\; . \]
</div>
<p>
 We will slightly abuse notation and write $\langle X, Y\rangle = \mbox{\rm Tr}(XY^\dagger )$ to denote the matrix trace inner product. 
</p>
<p>
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
</p>
<p>
The example of the CHSH game shows that quantum players can sometimes strictly outperform their classical peers. This already has a pretty neat (and, arguably, deep) consequence: it is possible to use the CHSH game as a “statistical test for information-theoretic randomness”! Indeed, any strategy that succeeds in the test with probability larger than $\frac{1}{2} + \frac{1}{4}$ (a simple condition to verify) cannot be a classical strategy, and in particular it cannot be a deterministic strategy. Thus, any pair of isolated devices (representing the players) that generate an input-output behavior that leads to a sufficiently high success probability in the game is necessarily randomness-generating. Note that this kind of randomness is very different from “pseudo-randomness”: there is no question of computational power here, and the guarantees provided by the test are information-theoretic! 
</p>
