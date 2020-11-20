<h1 class="tex-chapter" id="chapter:xorgames"><span data-tag="0001">2</span> XOR games</h1>

<p>
The simplest kind of games to think about are XOR games. An XOR game has the following form: 
</p>
<ol>
<li><p>
The referee selects a pair of questions $(i,j)\in \{ 1,\ldots , m\} \times \{ 1,\ldots , n\} $ according to a distribution $\pi $. 
</p>
</li><li><p>
The referee sends $i$ to Alice and $j$ to Bob. Alice and Bob reply with signs $a_ i,b_ j\in \{ \pm 1\} $ respectively. 
</p>
</li><li><p>
The payoff to the players is $a_ ib_ jc_{ij}$, where $c_{ij}\in \{ \pm 1\} $. (Note that the payoff is a number in $\{ \pm 1\} $. The interpretation is that, if the payoff is $+1$ the players “win”, and if it is $-1$ they “loose”. More general real-valued payoffs may be considered.) 
</p>
</li>
</ol>
<p>
 Given questions $i$ and $j$ respectively, the goal of the players is to provide answers whose product equals the target value $c_{ij}$. However, Alice only knows $i$ and Bob only knows $j$, which is what can make the game challenging. The following example introduces the famous CHSH game as an XOR game. 
</p>
