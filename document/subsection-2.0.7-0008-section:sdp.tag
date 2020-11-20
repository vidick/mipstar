<h3 class="tex-subsection" id="section:sdp"><span data-tag="0008">2.0.7</span> An SDP formulation and Tsirelson's bound</h3>

<p>
Is there any limit to how well quantum players can do in the CHSH game, or more generally in an XOR game? Recall that the optimal expected payoff for quantum players is given by eq:def-qval: 
</p>
<div class="equation" id="0009">
<span class="equation-label"><a data-tag="0009" href="/tag/0009">2.0.7.1</a></span>
<div>\begin{equation} \label{eq:qval-2} \beta ^*(G)=\sup _{\substack {A_ i,B_ j\in \ensuremath{\mathbb {C}}^{d\times d}\\ A_ i^2=B_ j^2=\mathbb {I}\\ A_ i=A_ i^\dagger \\ B_ j=B_ j^\dagger }}\sum _{i,j} G_{ij}\cdot \langle \psi | A_ i\otimes B_ j|\psi \rangle  \le \sup _{\substack {\vec{u}_ i,\vec{v}_ j\in \ensuremath{\mathbb {R}}^{d^2}\\ \| \vec{u}_ i\| =\| \vec{v}_ j\| =1}}\sum _{i,j} G_{ij}\vec{u}_ i\cdot \vec{v}_ j = \text{SDP}(G)\; . \end{equation}</div>
</div>
<p>
 This inequality holds because we can set $\vec{u}_ i=A_ i \otimes \ensuremath{\mathop{\rm Id}\nolimits }|\psi \rangle $ and $\vec{v}_ j=\ensuremath{\mathop{\rm Id}\nolimits }\otimes B_ j |\psi \rangle $. Under such choice, one can verify that 
</p>
<div class="equation">
  \[  \| \vec{u}_ i\| =\| \vec{v}_ i\| =1,\qquad u_ i\cdot v_ j=\langle \psi | A_ i \otimes B_ j |\psi \rangle \; .  \]
</div>
<p>
 The expression on the right-hand side of eq:qval-2 is nice because it is directly analogous to the expression eq:opt-1 for the classical value: the only difference is that we now optimize over inner products of unit vectors in any dimension, instead of just products of $\pm 1$ values. Although we will not show explicitly why, those of you familiar with semidefinite program will easily recognize that $\text{SDP}(AG)$ is, indeed, an SDP. In particular, the quantity can be approximated to within $\pm \varepsilon $ in time polynomial in $n$, $m$, and $\log (1/\varepsilon )$. 
</p>
<p>
Note that eq:qval-2 is only an upper bound. How good is it? Let's first use it to prove <em>Tsirelson's theorem</em>, which states that the lower bound of $\frac{\sqrt{2}}{2}$ on the quantum bias of the CHSH game obtained earlier is tight. 
</p>
<p>
<article class="env-theorem" id="000A">
<p><a class="environment-identifier" href="/tag/000A">Theorem <span data-tag="000A">2.0.8</span> <span class="named">(Tsirelson)</span>.</a> For $G$ the CHSH game, it holds that $\beta ^*(G) \leq \frac{\sqrt{2}}{2}$. </p>
</article>
</p>
<article class="env-proof">
<p>
<strong>Proof.</strong>
      For the CHSH game we can write 
    <p>
<div class="equation">
  \begin{align*}  \text{SDP}(G) &amp; = \sup _{\substack {\vec{u}_ i,\vec{v}_ j\in \ensuremath{\mathbb {R}}^{d^2}\\ \begin{bgroup}  \| \vec{u}_ i\| =\| \vec{v}_ j\| =1

\end{bgroup}}} \frac{1}{4} \big (\vec{u}_0 \cdot \vec{v}_0 + \vec{u}_1 \cdot \vec{v}_0 + \vec{u}_0 \cdot \vec{v}_1 - \vec{u}_1 \cdot \vec{v}_1\big )\\ &amp; = \sup _{\substack {\vec{u}_ i,\vec{v}_ j\in \ensuremath{\mathbb {R}}^{d^2}\\ \begin{bgroup}  \| \vec{u}_ i\| =\| \vec{v}_ j\| =1

\end{bgroup}}} \frac{1}{4} \big (\vec{u}_0 \cdot (\vec{v}_0 + \vec{v}_1) + \vec{u}_1 \cdot (\vec{v}_0 -\vec{v}_1)\big )\\ &amp;  = \sup _{\substack {\vec{v}_ j\in \ensuremath{\mathbb {R}}^{d^2}\\ \begin{bgroup}  \| \vec{v}_ j\| =1

\end{bgroup}}} \frac{1}{4} \big (\| \vec{v}_0 + \vec{v}_1\|  + \| \vec{v}_0 -\vec{v}_1\|  \big )\\ &amp;  \leq \sup _{\substack {\vec{v}_ j\in \ensuremath{\mathbb {R}}^{d^2}\\ \begin{bgroup}  \| \vec{v}_ j\| =1

\end{bgroup}}} \frac{\sqrt{2}}{4} \big ( \| \vec{v}_0 + \vec{v}_1\| ^2 + \| \vec{v}_0 -\vec{v}_1\| ^2\big )^{1/2} \\ &amp; = 2\frac{\sqrt{2}}{4} \; . \end{align*}
</div>
<p>
       Here for the third line we used that for any nonzero $\vec{v}$ the supremum over unit $\vec{u}$ of $\vec{u}\cdot \vec{v}$ is $\| \vec{v}\| $, achieved at $\vec{u} = \vec{v}/\| \vec{v}\| $; the fourth line is the Cauchy-Schwarz inequality; the last expands the squares and uses that $\vec{v}_0$ and $\vec{v}_1$ are unit vectors. 
      <span class="qed">$\square$</span>
</p>
</p></p></article>
<p>
Tsirelson's proof of his theorem was a bit different: he worked directly with the operators, and considered the square of the game value. We will revisit his proof a little later. 
</p>
<p>
Theorem <a data-tag="000A" href="/tag/000A">2.0.8</a> shows that the bound eq:qval-2 is tight for the CHSH game. What is amazing is that it is <em>always</em> tight, for any XOR game! This is another result by Tsirelson. 
</p>
<p>
<article class="env-exercise" id="000B">
<p><a class="environment-identifier" href="/tag/000B">Exercise <span data-tag="000B">2.0.9</span>.</a> Show that given a vector solution to SDP($G$) it is always possible to find a quantum strategy that achieves exactly the same value. <em>[Hint: Consider Hermitian matrices $C_1,\ldots ,C_ d \in \ensuremath{\mathbb {C}}^{D\times D}$ that square to identity and pairwise anti-commute. For any vector $u$, consider $u\mapsto C(u) = \sum _ i u_ i C_ i$. What can you say about $C(u)$? And about $\langle \phi _{D}| C(u) \otimes C(v)|\phi _ D\rangle $? ]</em> </p>
</article>
</p>
<p>
The fact that eq:qval-2 is an equality has amazing consequences for the study of XOR games. In particular, it implies that: 
</p>
<ul>
<li><p>
The right-hand size of eq:qval-2 can be expressed as a semidefinite program, hence the maximum expected payoff of quantum players can be computed efficiently (recall that for classical players it is NP-hard);<a class="footnotemark" href="#a0000001144" id="a0000001144-mark"><sup>1</sup></a>
</p>
</li><li><p>
The proof of Tsirelson's theorem in Exercise <a data-tag="000B" href="/tag/000B">2.0.9</a> is explicit, hence an optimal quantum strategy can always be found efficiently; 
</p>
</li><li><p>
Grothendieck's inequality from functional analysis shows that the ratio of $\text{SDP}(G)/\beta ^*(G)$ is always at most a universal constant, Grothendieck's constant $K_ G \leq 1.782\ldots $: this implies that, in XOR games, quantum players can only ever achieve a payoff that is a constant factor larger than the optimal classical payoff. 
</p>
</li>
</ul>
<p>
<article class="env-remark" id="">
<p><a class="environment-identifier" href="/tag/">Remark <span data-tag="">2.0.10</span>.</a>There are many interesting games that are not XOR games. A good example is the <em>Magic Square game</em>. This game is a “pseudo-telepathy” game, which means that the quantum value is $1$ (there is a perfect quantum strategy), while the classical value is strictly below $1$. It is known that XOR games cannot be pseudo-telepathy games. </p>
</article>
</p>
