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
# TIPE: Application de la théorie des graphes pour la gestion de Foules. 
Cas du Stade de France pendant les Jeux Olympiques
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

<img src="map_rot.png"  height="450"> 

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

<img src="image-1.png"  > 

<span style="font-size:0.5em;"> Issu de: These are the warning signs that a crowd is dangerously dense - @CNN</span>

</div>
</div>

---

# 2. Modélisation: Graphe de Capacité

---
# Graphes de capacité
Soit $G_c = (V,E, C)$ un graphe non orienté pondéré par:

$C : E \rightarrow \mathbb{N}$ la capacité de chaque arête.

Le graphe des capacités.

---
# Modélisation de la capacité
<div class="columns">
<div>
Modélisation de piétons dans le pire des cas :

$\delta = 5 pers./m²$

Capacité d'une rue: débit maximal en pers./s

$c = \delta * w * v$
- $w$ la largeur de la rue 
- $v$ la vitesse de la foule
- $\delta$ la  densité de la  foule
</div>
<div>

![Speed/density](images/v_over_delta.png)
<span style="font-size:0.5em;"> Étude expérimentale et modélisation des déplacements collectifs de piétons @Mehdi Moussaid </span>

</div>
</div>



---
# 4. Une methode optimale :  Le flot maximal

---
Soit $\varphi = (V,E,\phi)$ un graphe orienté pondéré par 
$\phi : E\rightarrow \mathbb{N}$ le flux passant dans chaque arètes.
Le graphe de flot.

---

# Propriétés des flots
$\forall a \in E,\phi(a)\le C(a)$
On définit:
$\phi⁺: u \in V \rightarrow \sum_{v|(u,v)\in E} \phi(u,v)$
$\phi^-: u \in V \rightarrow \sum_{v|(v,u)\in E} \phi(v,u)$
$\forall u \in V, \phi⁺(u) = \phi^-(u)$

---


