<h3 class="tex-subsection" id="section:chsh"><span data-tag="000L">3.0.8</span> Rigidity for the CHSH game</h3>

<p>
Now let's see what this all has to do with the CHSH game. We will use the theory of approximate group representations to prove the following theorem, originally due to <span class="cite">[<a href="/bibliography/summers1988maximal">summers1988maximal</a>]</span> (with slightly weaker bounds; see also <span class="cite">[<a href="/bibliography/mckague2012robust">mckague2012robust</a>]</span> for the $O(\sqrt{\varepsilon })$ dependence). 
</p>
<p>
<article class="env-theorem" id="000M">
<p><a class="environment-identifier" href="/tag/000M">Theorem <span data-tag="000M">3.0.9</span>.</a> Let $\varepsilon &gt;0$, and suppose that a strategy for the players in the CHSH game, using a bipartite state $|\psi \rangle \in \ensuremath{\mathbb {C}}^ d\otimes \ensuremath{\mathbb {C}}^ d$ and observables $A_0,A_1$ for Alice and $B_0,B_1$ for Bob, achieves a bias at least $\sqrt{2}/2-\varepsilon $ in the game. Then there are local isometries $V_ A,V_ B:\ensuremath{\mathbb {C}}^ d \to \ensuremath{\mathbb {C}}^2 \otimes \ensuremath{\mathbb {C}}^{d'}$ such that </p>
<div class="equation" id="000N">
<span class="equation-label"><a data-tag="000N" href="/tag/000N">3.0.9.1</a></span>
<div>\begin{equation} \label{eq:chsh-state} \big \|  V_ A \otimes V_ B |\psi \rangle  - \frac{1}{\sqrt{2}}\big (|00\rangle +|11\rangle \big ) \otimes |\psi '\rangle  \big \| ^2 = O(\sqrt{\varepsilon }) \; , \end{equation}</div>
</div>
<p> and </p>
<div class="equation" id="000P">
<span class="equation-label"><a data-tag="000P" href="/tag/000P">3.0.9.2</a></span>
<div>\begin{equation} \label{eq:chsh-alice} \big \| ( V_ A \otimes V_ B)( A_0 \otimes \ensuremath{\mathop{\rm Id}\nolimits })|\psi \rangle  - (\sigma _ X \otimes \ensuremath{\mathop{\rm Id}\nolimits })\frac{1}{\sqrt{2}}(|00\rangle +|11\rangle ) \otimes |\psi '\rangle  \big \|  \, =\,  O\big (\sqrt{\varepsilon }\big )\; , \end{equation}</div>
</div>
<p> and a similar relation holds with $A_0$ replaced by $A_1$ and $\sigma _ X$ replaced by $\sigma _ Z$. Moreover, analogous relations hold for Bob's observables. </p>
</article>
</p>
<p>
It is important to note what the theorem says, and what it does not say. It does not say that the state $|\psi \rangle $ shared by the players must be close to an EPR pair — it says that, <em>up to local rotations</em>, the state must be close to an EPR pair <em>tensored with an ancilla state</em>. Since local unitaries have no effect on the Schmidt coefficients, it does imply that the original state shared by the players have Schmidt coefficients that can be split into two roughly even batches — and in particular, that there are at least two of them. 
</p>
<p>
The theorem also does not say anything about the observables $A_0$, $A_1$ themselves. Eq. eq:chsh-alice only talks about the action of the observable <em>on the state</em>. This is inevitable, as the game only “observes” this action. In particular, it is perfectly possible for $A_0$ to look like something completely arbitrary in a portion of space in which the reduced density of $|\psi \rangle $ on Alice's space is zero, or very small. But the theorem does say that, in terms of “observable consequences” only, the action of $A_0$ on $|\psi \rangle $ is comparable to the action of $\sigma _ X$ on one half of an EPR pair. Although this may sound relatively weak, we will see that it can be exploited all the way into a complete “leash” for an arbitrary computation. 
</p>
<article class="env-proof">
<p>
<strong>Proof.</strong>
      For the first step of the proof we follow Tsirelson's argument showing a bound of $\frac{\sqrt{2}}{2}$ on the quantum value of the CHSH game. Tsirelson's idea was to consider the square 
    <p>
<div class="equation" id="000Q">
<span class="equation-label"><a data-tag="000Q" href="/tag/000Q">3.0.9.3</a></span>
<div>\begin{align}  (A_0\otimes B_0 + A_0\otimes B_1 + A_1\otimes B_0 - A_1\otimes B_1 )^2 &amp; =( (A_0+A_1)\otimes B_0 + (A_0-A_1)\otimes B_1 )^2\label{eq:bellop}\\ &amp; = 4\ensuremath{\mathop{\rm Id}\nolimits }\otimes \ensuremath{\mathop{\rm Id}\nolimits }+ (A_1A_0-A_0A_1)\otimes (B_0B_1-B_1B_0)\; .\notag \end{align}</div>
</div>
<p>
       This last term has operator norm at most $8$, and as a result the CHSH operator $A_0\otimes B_0 + A_0\otimes B_1 + A_1\otimes B_0 - A_1\otimes B_1$ has operator norm at most $\sqrt{8}$; Tsirelson's bound on the quantum value of CHSH follows by dividing by $4$ and observing that the players' choice of entangled state cannot beat the largest eigenvector. 
    <p>
      Furthermore, under the assumption that the strategy achieves a bias of at least $\sqrt{2}/2-\varepsilon $ in the game, using $|\langle \psi |X|\psi \rangle |^2 \leq \langle \psi |XX^*|\psi \rangle $ for any Hermitian $X$, the left-hand side of eq:bellop, when evaluated on $|\psi \rangle $, must be at least $8(1-\varepsilon )^2$. Applying the Cauchy-Schwarz inequality it follows that both conditions 
    <p>
<div class="equation">
  \[ \mbox{\rm Tr}((A_1A_0 + A_0A_1)^2\rho _ A) = O({\varepsilon })\qquad \text{and}\qquad \mbox{\rm Tr}((B_0B_1+B_1B_1)^2 \rho _ B) = O({\varepsilon }) \]
</div>
<p>
       must hold, where $\rho _ A$ and $\rho _ B$ are the reduced density matrices of $|\psi \rangle $ on Alice and Bob respectively. Using the notation introduced in Section <a data-tag="" href="/tag/">None</a>, this says that 
    <p>
<div class="equation" id="000R">
<span class="equation-label"><a data-tag="000R" href="/tag/000R">3.0.9.4</a></span>
<div>\begin{equation} \label{eq:a-ac} \| A_0A_1 + A_1A_0\| _{\rho _ A}^2 = O({\varepsilon })\; , \end{equation}</div>
</div>
<p>
       i.e. $A_0$ and $A_1$ approximately commute. 
    <p>
      Now here comes the key observation. Consider the $8$-element group $H$ generated by the Pauli matrices $\sigma _ X$ and $\sigma _ Z$, i.e. 
    <p>
<div class="equation">
  \[ H\, =\, \pm \big \{  \ensuremath{\mathop{\rm Id}\nolimits },\,  \sigma _ X,\, \sigma _ Z,\,  \sigma _ X\sigma _ Z\big \} \; . \]
</div>
<p>
       Then I claim that $A_0$ and $A_1$ induce an approximate representation of $H$, by setting 
    <p>
<div class="equation">
  \[  f(\pm \ensuremath{\mathop{\rm Id}\nolimits })=\pm \ensuremath{\mathop{\rm Id}\nolimits },\quad f(\pm \sigma _ X)=\pm A_0,\quad \quad f(\pm \sigma _ Z)=\pm A_1,\quad f(\pm \sigma _ X\sigma _ Z) = \pm A_0A_1\; . \]
</div>
<p>
       Note that this is a legal definition, since $A_0$, $A_1$, and $A_0A_1$ are all unitary. Moreover, using only eq:a-ac and the fact that $A_0$ and $A_1$ are observables, it is immediate to verify that the conditions of Theorem <a data-tag="000H" href="/tag/000H">3.0.6</a> are satisfied, i.e. $f$ is an $(O({\varepsilon }),\rho _ A)$-representation of $H$. 
    <p>
      Applying the theorem, there must exist an exact representation of $H$ to which $f$ is close. However, the representation theory of $H$ is not complicated. It has four $1$-dimensional representations, but all of them map $-\ensuremath{\mathop{\rm Id}\nolimits }$ to $1$, so they cannot be close to $f$. Hence we are left with the unique irreducible $2$-dimensional representation of $H$, which is precisely given by the Pauli matrices! 
    <p>
      We're almost done. We can apply the same considerations to Bob's operators $B_0$ and $B_1$, except that here we will choose to rotate the representation so that it sends $\sigma _ X$ to the Hadamard matrix $H$ and $\sigma _ Z$ to the matrix $G$. This is another valid representation; it is the same as the standard one, but rotated. 
    <p>
      Finally we need to verify the condition on $|\psi \rangle $. Note that by assumption 
    <p>
<div class="equation">
  \[  \frac{1}{4}\langle \psi | A_0 \otimes B_0 + A_0 \otimes B_1 + A_1 \otimes B_0 - A_1\otimes B_1 |\psi \rangle  \geq \frac{\sqrt{2}}{2} - \varepsilon \; , \]
</div>
<p>
       which then implies 
    <p>
<div class="equation">
  \[  \frac{1}{4} \langle \psi |(V_ A\otimes V_ B)^\dagger \big ( (\sigma _ X \otimes H + \sigma _ X \otimes G + \sigma _ Z \otimes H - \sigma _ Z\otimes G)\otimes \ensuremath{\mathop{\rm Id}\nolimits }\big ) (V_ A\otimes V_ B)|\psi \rangle  \geq \frac{\sqrt{2}}{2} - O({\varepsilon })\; , \]
</div>
<p>
       i.e. 
    <p>
<div class="equation" id="000S">
<span class="equation-label"><a data-tag="000S" href="/tag/000S">3.0.9.5</a></span>
<div>\begin{equation} \label{eq:xz-v} \frac{1}{2}\langle \psi |(V_ A\otimes V_ B)^\dagger \big ( (\sigma _ X \otimes \sigma _ X + \sigma _ Z \otimes \sigma _ Z )\otimes \ensuremath{\mathop{\rm Id}\nolimits }\big )(V_ A\otimes V_ B)|\psi \rangle  \geq 1 - O({\varepsilon })\; . \end{equation}</div>
</div>
<p>
       Now observe that $\frac{1}{2}(\sigma _ X \otimes \sigma _ X + \sigma _ Z \otimes \sigma _ Z )$ is an observable with a single eigenvalue $1$, with associated eigenvector $|\phi _2\rangle $, and all other eigenvalues equal to $0$ or $-1$. Therefore, eq:xz-v implies 
    <p>
<div class="equation">
  \[  \big \| \big (\langle \phi _2|\otimes \ensuremath{\mathop{\rm Id}\nolimits }\big )(V_ A\otimes V_ B)|\psi \rangle \big \| ^2 \, \geq \,  1-O({\varepsilon })\; , \]
</div>
<p>
       which means that $(V_ A\otimes V_ B)|\psi \rangle = |\phi _2\rangle  \otimes |\psi '\rangle  + |\psi ''\rangle $ for some sub-normalized states $|\psi '\rangle $ and $|\psi ''\rangle $ such that $\| |\psi ''\rangle \| ^2 = O(\varepsilon )$. This proves the theorem. 
      <span class="qed">$\square$</span>
</p>
</p></p></p></p></p></p></p></p></p></p></p></p></p></p></p></p></p></p></p></p></p></p></p></article>
