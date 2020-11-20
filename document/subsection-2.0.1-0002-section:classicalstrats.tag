<h3 class="tex-subsection" id="section:classicalstrats"><span data-tag="0002">2.0.1</span> Classical strategies</h3>

<p>
Given an arbitrary XOR game $G$, introduce a matrix $A\in \ensuremath{\mathbb {R}}^{n\times m}$ with coefficients $G_{ij}=\pi (i,j)c_{ij}$. Then the maximum expected payoff for the players is 
</p>
<div class="equation" id="0003">
<span class="equation-label"><a data-tag="0003" href="/tag/0003">2.0.1.1</a></span>
<div>\begin{equation} \label{eq:opt-1} \beta (G) \, =\,  \max _{a_ i,b_ j\in \{ \pm 1\} }\sum _{i,j} G_{ij}a_ ib_ j \; . \end{equation}</div>
</div>
<p>
 It is not hard to verify that this is related to the value $\omega (G)$ of the game, the maximum propbability for the players to be accepted, as $\omega (G) = \frac{1}{2} + \frac{1}{2}\beta (G)$. 
</p>
<p>
Conversely, for any $A\in \ensuremath{\mathbb {R}}^{m\times n}$, we can define $c_{ij}=\text{sign}(A_{ij})$ and $\pi (i,j)=\frac{A_{ij}}{\sum _{k,l}|A_{kl}|}$ to transform any optimization problem of the form eq:opt-1 into an XOR game. You may already know that computing eq:opt-1, or even approximating it to within a small constant factor, is NP-hard in the worst case; if not, verify that there is a simple reduction from MAXCUT. So approximating the value of a $2$-player XOR game is NP-hard; this is a slightly stronger result than the hardness for “clause-vs-variable”-type games that we discussed earlier. 
</p>
<p>
<article class="env-remark" id="">
<p><a class="environment-identifier" href="/tag/">Remark <span data-tag="">2.0.2</span>.</a>In general one may allow the players to use randomized strategies, including both private and shared randomness, to select their answers. It is easy to see that this cannot help in general: if on average (over their random coin tosses) the players achieve a certain payoff, then there must exist some choice of coins that lets them achieve at least the average payoff, and they might as well fix this choice of coins as part of their strategy. </p>
</article>
</p>
<p>
<article class="env-example" id="0007">
<p><a class="environment-identifier" href="/tag/0007">Example <span data-tag="0007">2.0.3</span>.</a> We let $m=n=2$ and $c_{11}=c_{12}=c_{21}=1$, $c_{22}=-1$. Thus the players “win” if and only if $a_ i \oplus b_ j = i\wedge j$ (interpreting $i,j\in \{ 1,2\} $ as Booleans by mapping $1$ to $0$ and $2$ to $1$). This game is called the CHSH game, after its inventors, Clause, Horne, Shimony, and Holt. We can evaluate the maximum expected payoff exactly: </p>
<div class="equation">
  \[  \beta (G)=\max _{a_ i,b_ j\in \{ \pm 1\} }\sum _{i,j}\pi (i,j)c_{ij}a_ ib_ j=\max \frac{1}{4}(a_1b_1+a_1b_2+a_2b_1-a_2b_2)= \frac{1}{2}\; .\footnote{The quantity $\beta (G)$ is called the ``bias'' of the game, which is twice the largest possible advantage over a random strategy.}  \]
</div>
<p> So the classical value of the game is </p>
<div class="equation">
  \[ \omega (G) \, =\,  \frac{1}{2} + \frac{1}{2}\,  \beta (G) \, =\,  \frac{3}{4}\; . \]
</div>
</article>
</p>
