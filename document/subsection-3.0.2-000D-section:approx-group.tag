<h3 class="tex-subsection" id="section:approx-group"><span data-tag="000D">3.0.2</span> Approximate group representations</h3>

<p>
We first make a little detour through the theory of group representations. For $d$-dimensional matrices $A,B$ and $\sigma $ such that $\sigma $ is positive semidefinite, write 
</p>
<div class="equation">
  \[ \langle A,B\rangle _\sigma = \mathrm{Tr}(AB^* \sigma )\; , \]
</div>
<p>
 where we use $B^*$ to denote the conjugate-transpose. This is an extension of our earlier notation for the matrix inner product, which is recovered for $\sigma = \ensuremath{\mathop{\rm Id}\nolimits }$. If $\sigma $ is the totally mixed state, then we obtain a dimension-normalized variant of the trace inner product. We will also write $\| A\| _\sigma = \langle A,A\rangle _\sigma ^{1/2}$. 
</p>
<p>
Given an arbitrary finite group $G$ (not necessarily abelian), a group representation of $G$ is a map $f:G \to U_ d(\ensuremath{\mathbb {C}})$, the group of $d\times d$ unitary matrices, such that $f$ is a homomorphism: for any $x,y\in G$, $f(x^{-1}y)=f(x)^* f(y)$, where we used $^*$ to denote the conjugate transpose (which, for unitary matrices, corresponds to taking the inverse). The following definition introduces a notion of <em>approximate</em> group representation. 
</p>
<p>
<article class="env-definition" id="000E">
<p><a class="environment-identifier" href="/tag/000E">Definition <span data-tag="000E">3.0.3</span>.</a> Given a finite group $G$, an integer $d\geq 1$, $\varepsilon \geq 0$, and a $d$-dimensional positive semidefinite matrix $\sigma $ with trace $1$, an $(\varepsilon ,\sigma )$-representation of $G$ is a function $f: G \to U_ d(\ensuremath{\mathbb {C}})$, the unitary group of $d\times d$ matrices, such that </p>
<div class="equation" id="000F">
<span class="equation-label"><a data-tag="000F" href="/tag/000F">3.0.3.1</a></span>
<div>\begin{equation} \label{eq:gh-condition} \textsc{E}_{x,y\in G} \, \Re \big (\big \langle f(x)^*f(y) ,f(x^{-1}y) \big \rangle _\sigma \big ) \, \geq \,  1-\varepsilon \; , \end{equation}</div>
</div>
<p> where the expectation is taken under the uniform distribution over $G$. </p>
</article>
</p>
<p>
<article class="env-remark" id="">
<p><a class="environment-identifier" href="/tag/">Remark <span data-tag="">3.0.4</span>.</a>The condition eq:gh-condition in the definition is very closely related to Gowers' $U^2$ norm </p>
<div class="equation">
  \[ \| f\| _{U^2}^4 \, =\,  \textsc{E}_{xy^{-1}=zw^{-1}}\,  \big \langle f(x)f(y)^* ,f(z)f(w)^* \big \rangle _\sigma . \]
</div>
<p> While a large Gowers norm implies closeness to an affine function, we are interested in testing homomorphisms, and the condition eq:gh-condition will arise naturally from our calculations in the next section. </p>
</article>
</p>
