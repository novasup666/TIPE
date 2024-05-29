---
marp: true
paginate: true
title: TIPE_PRESENTATION
size : 4:3
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
---
<!--
<div class="columns">
<div>

</div>
<div>


<span style="font-size:0.5em;"> Description </span>

</div>
</div>
-->

<!-- header: 'TIPE - Noé VINCENT' -->
# TIPE: Gestions des flux de spectateurs autour du stade de France par la théorie des graphes.
Définition d'itinéraires sécurisés pour évacuer le Stade de France.
Noé VINCENT

---
# Motivation
A voir


---
# Plan
1. Analyse de la situation
2. Modélisation: Graphe de Capacité
3. Une méthode naïve
4. Une méthode optimale: le flot maximal
4. Analyse des résultats
5. Annexe


---
# 1. Analyse de la situation

---
# Situation Géographique

<div class="columns">
<div>


Le stade de France: 81 500 spectateurs 
3 stations de transport en commun aux alentours:
 - Saint-Denis Porte de Paris (M13)
 - La Plaine - Stade de France (RER B)
- Stade de France - Saint-Denis (RER D) 
</div>
<div>

<img src="images/map_rot.png"  height="450"> 

<span style="font-size:0.5em;">Carte des alentours du Stade de France - @OSM</span>

</div>
</div>

---
# Foules et risques
<div class="columns">
<div>
À partir de 6 personnes/m²,
-> Potentiel danger

On place la limite à 5 personnes/m²


</div>
<div>

<img src="images/image-1.png"  > 

<span style="font-size:0.5em;"> Issu de: These are the warning signs that a crowd is dangerously dense - @CNN</span>

</div>
</div>

---

# 2. Modélisation: Graphe de Capacité

---
### Graphes de capacités
Soit $G_c = (V,E, C)$ un graphe non orienté pondéré par:

$C : E \rightarrow \mathbb{N}$ la capacité de chaque arête.

Le graphe des capacités.

---
### Modélisations de la capacité

<div class="columns">
<div>
Modélisation de piétons dans le pire des cas :

$\delta = 5 pers./m²$

Capacité d'une rue: débit maximal en pers./s

$c = \delta * w * v$
- $w$ la largeur de la rue (approximée)
- $v$ la vitesse de la foule
- $\delta$ la  densité de la  foule
</div>
<div>

$v= 0,4m/s$ 

![Speed/density](images/v_over_delta.png)
<span style="font-size:0.5em;"> Étude expérimentale et modélisation des déplacements collectifs de piétons @Mehdi Moussaid </span>

</div>
</div>

---
### Graphe de capacité
<div>
<img src="images/map.png" >

<span style="font-size:0.5em;"> Carte de la zone @OSM </span> 
</div>

---
### Graphe  de capacité

<img src="images/graph.png" >
<span style="font-size:0.5em;"> Graphe représentant la zone
</span> 

---
# 3. Une méthode naïve
$\rightarrow$ les chemins de plus grande capacité entre le stade et les stations

---
### Capacité d'un chemin
$p \subset E$
$C(p) = min\left\{C(e), e \in p\right\}$


### L'algorithme de dijkstra
Chemin de poids minimal dans un graphe.

### Algorithme Widest Path
Algorithme de dijkstra modifié $\rightarrow$ chemin de capacité maximale 

---
### Proposition de solution
![graph](images/graph.png)

---
### Proposition de solution
Chemin le plus large entre le stade et le métro, largeur : 3
![s-1000](images/s-1000.png)

---
### Proposition de solution
Chemin le plus large entre le stade et le RER B, largeur 7

![s-1001](images/s-1001.png)

---
### Proposition de solution
Chemin le plus large entre le stade et le RER D, largeur 4
![s-1002](images/s-1002.png)

---

### Proposition de solution
Largeur théorique : $3+4+7 = 14$
Débit théorique : $28 pers/s$
Largeur réelle: $10$
Débit réel : $20 pers/s$
Temps d'évacuation : 1h08

---
# 4. Une methode optimale :  Le flot maximal
Algorithme d'Edmond-Karp

---
## Graphes de Flots

Soit $\varphi = (V,E,\phi,s,t)$ un graphe orienté pondéré par 
$\phi : E\rightarrow \mathbb{N}$ le flot passant dans chaque arètes.
Le graphe de flot.
$s$ : la source
$t$ : le puit

### Flot entrants et sortants dans un noeud
On définit:
$\phi⁻: u \in V \rightarrow \sum_{v|(u,v)\in E} \phi(u,v)$
$\phi⁺: u \in V \rightarrow \sum_{v|(v,u)\in E} \phi(v,u)$

---
## Propriétés des Flots

### Sources et puits
$\phi⁺(s) = 0$
$\phi⁻(t)) = 0$

### Valeur du flot
$V_{\phi} = \phi⁻(s)$


### Conservation du flot

$\forall u \in V\backslash\left\{s,t \right\}, \phi⁺(u) = \phi^-(u)$

---
### Graphe des augmentations
Soit $G_A = (V,E,C_r)$ un graphe orienté pondéré par:

$C_r : E \rightarrow \mathbb{N}$ la capacité restante de chaque arête.

Le graphe des augmentation.

### Chemin augmentant
$P = (p,d\phi)\in \mathbb{P}(E) * \mathbb{N}$

$p$ : ensemble d'arcs débutant à $s$ et finissant en $t$

$d\phi$ : variation du flot

---
## Algorithme d'Edmond-Karp

<div class="columns">
<div>

$EK :G_c \rightarrow \varphi_{max}$


### Objectif
Maximiser $V_{\phi}$

### Fonctionnement
Trouver des chemins augmentants dans $G_a$ afin d'augmenter le flux.
</div>
<div>

    Soit E-K(G_c = (V,E,C),pr):
      Phi <- Vide
      G_a <- (V+{t},
              E + {{puit ,t} pr},
              C_r(u,v) = C_r(v,u)  = C(u,v)
              )
      (P_a, dphi) = Chemin_augmentant(G_a)
      Tant P_a != Vide : 
        Mettre à jour G_a avec P_a, dphi
        Mettre à jour Phi avec P_a, dphi
      Renvoyer Phi
<span style="font-size:0.5em;"> Pseudo-Code de l'algorithme d'Edmond Karp </span>

- G_c le graphe des capacités
- pr les puits réels

</div>
</div>

---
## Algorithme d'Edmond-Karp
### Recherche du Chemin augmentant
Parcours en largeur : plus court chemin en nombre d'arc

### Arc avant 
Arc de $G_r$ dans le sens initial, le sens du flot


### Arc arrière
Arc de $G_r$ de sens inverse au flot, de capacité égale au flot.

---

### Mise à jour de $\varphi$
$\forall e=(u,v) \in p$ 
si e est un  arc avant:
$\phi(u,v) \leftarrow \phi(u,v)+ d\phi$

si e=(v,u) est un arc arrière :
$\phi(u,v) \leftarrow \phi(u,v)-d\phi$

### Mise à jour de $G_r$
$\forall e =(u,v) \in p, C_r(u,v) \leftarrow C_r(u,v) - d\phi$
$\forall e =(u,v) \in p, C_r(v,u) \leftarrow C_r(v,u) + d\phi$



---
### Exemple
Graphe de Capacité, graphe d'augmentation
![ex_graph](images/example_graph.png)

---
### Exemple
Graphe de flot
![ex_f0](images/ex_f0.png)

---
### Exemple
Graphe d'augmentation, chemin augmentant
![alt text](images/ex_agp0.png)

---
### Exemple
Graphe de flot
![ex_f1](images/ex_f1.png)

---
### Exemple
Graphe d'augmentation
![ag1](images/ex_ag1.png)

---
### Exemple
Graphe d'augmentation, chemin augmentant
![agp1](images/ex_agp1.png)

---
### Exemple
Graphe de flot
![ex_f2](images/ex_f2.png)

---
### Exemple
Graphe d'augmentation
![ag2](images/ex_ag2.png)

---
### Exemple
Graphe d'augmentation, chemin augmentant
![agp2](images/ex_agp2.png)

---
### Exemple
Graphe de flot
![ex_f3](images/ex_f3.png)

---
### Exemple
Graphe d'augmentation
![ag3](images/ex_ag3.png)

---
### Exemple
Graphe d'augmentation, chemin augmentant
![agp3](images/ex_agp3.png)

---
### Exemple
Graphe de flot
![ex_f4](images/ex_f4.png)

---
### Exemple
Graphe d'augmentation
![ag4](images/ex_ag4.png)

---
### Exemple
Graphe d'augmentation, chemin augmentant
![agp4](images/ex_agp4.png)

---
### Exemple
Graphe de flot
![ex_f5](images/ex_f5.png)

---
### Exemple
Graphe d'augmentation final
![ag5](images/ex_ag5.png)

---
### Exemple
Graphe de flot final
![ex_f5(final)](images/ex_f5.png)

---
### Résultats expérimentaux
Largeur : 23, débit : 46 pers/s, temps :30min
![final flow](images/final_flow.png)