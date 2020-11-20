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