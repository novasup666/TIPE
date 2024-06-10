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
  .article {
  display: grid;
  grid-template-columns: 1fr 2fr;}
  .deuxcinquiemes {
  display: grid;
  grid-template-columns: 2fr 3fr;}

---


<!-- header: 'TIPE - Noé VINCENT - 32226' -->
# TIPE: Gestions des flux de spectateurs autour du Stade de France par la théorie des graphes.
Définition d'itinéraires sécurisés pour évacuer le Stade de France lors des Jeux Olympiques.
Noé VINCENT

---
## Comment utiliser la théorie des graphes pour définir les itinéraires piétons aux alentours du stade  de France ?
- maintenir la sécurité des spectateurs.
- le plus efficacement.

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
# Critère de sécurité:
<div class="columns">
<div>
À partir de 6 personnes/m²,
-> Potentiel danger

On place la limite à 5 personnes/m²

Helbing & Mukerji -> trop grande densité: 
l'une des causes du drame de la Love Parade.
</div>
<div>

<img src="images/cnn.png"  > 

<span style="font-size:0.5em;"> Issu de: These are the warning signs that a crowd is dangerously dense - @CNN</span>

</div>
</div>



---

# 2. Modélisation: Graphe de capacité

---
### Graphe de capacité
Soit $G_c = (V,E, C)$ un graphe non orienté pondéré par:

$C : E \rightarrow \mathbb{N}$ la capacité de chaque arête.

Le graphe des capacités.

---
### Modélisation de la capacité

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
<img src="images/map.png" width = "690" >

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
![s-1000](images/M.png)

---
### Proposition de solution
Chemin le plus large entre le stade et le RER B, largeur 7

![s-1001](images/B.png)

---
### Proposition de solution
Chemin le plus large entre le stade et le RER D, largeur 4
![s-1002](images/D.png)

---
## Analyse de la solution  
<div class="article">
<section> Goulot d'étranglement  </section>
<section>  <img src="images/zoom.png"> </section>
<section> Zoom sur le sud-est du graphe  </section>
<section> <img src="images/zoomB.png"></section>
</div class="article">


---

## Analyse de la solution
<div class="article">
<section> Cannibalisme  </section>
<section>  <img src="images/zoomD.png"> </section>
<section> Zoom sur le sud-est du graphe </section>
<section> <img src="images/zoomB.png"></section>
</div class="article">

---

## Analyse de la solution
Largeur théorique : $3+4+7 = 14$
Débit théorique : $28 pers/s$


Largeur réelle: $10$
Débit réel : $20 pers/s$
Temps d'évacuation : 1h08

---
# 4. Une méthode optimale :  Le flot maximal
Algorithme d'Edmond-Karp

---
## Graphe d'éxemple
<img src="images/ex.png">

---
## Graphe de flot

Soit $\varphi = (V,E,\phi,s,t)$ un graphe orienté pondéré par 
$\phi : E\rightarrow \mathbb{N}$ le flot passant dans chaque arètes.

Le graphe de flot avec $s$ : la source, $t$ : le puit
<div style="text-align:center;">
<img src="images/ex_flot.png" width = "600" ></div>



---
### Propriétés des flots: conservation du flot
![ex_flot](images/ex_flot.png)

---
### Propriétés des flots: valeur du flot
![ex_flot](images/ex_flot.png)
$V_{\phi} =$ le flot total sortant de s

---

### Chemin augmentant
![ex_ap](images/ex_ap.png)

$(p,d_{\phi}), p\subset E, d_{\phi}\in \mathbb{N}$

---

### Flot saturé
![ex_flot_sat](images/ex_flot_sat.png)

---
### Flot maximal
![ex_flot_max](images/ex_flot_max.png)

---
### Graphe des augmentations
<div class="deuxcinquiemes">
<div>

Soit $G_a = (V,E,C_r)$ un graphe orienté pondéré.



</div>
<div>
<img src="images/ex_flot.png">
</div>
<div>

$C_r : E \rightarrow \mathbb{N}$ 
la capacité restante de chaque arête.
</div>
<div>
<img src="images/ex_ag.png">
</div>
</div>


---
### Arcs avant, Arcs arrières
![ex_ag](images/ex_ag.png)

---
### Flot saturé
![ex_flot_sat](images/ex_flot_sat.png)

---
### Nouveau graphe des augmentations
![alt text](images/ex_ag2.png)

---
### Nouveau chemin augmentant
![ex_ap2](images/ex_ap2.png)

---
### Flot maximal
![ex_flot_max](images/ex_flot_max.png)

---
### Graphe final des augmentations
![ex_ag_final](images/ex_ag_final.png)

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

    Soit E-K(G_c = (V,E,C)):

      Phi <- Vide;
      G_a <- (V,
              E,
              C_r(u,v) = C_r(v,u)  = C(u,v));

      (P_a, dphi) = Chemin_augmentant(G_a);

      Tant que P_a existe : 
        Mettre à jour G_a avec P_a, dphi;
        Mettre à jour Phi avec P_a, dphi;
        (P_a, dphi) = Chemin_augmentant(G_a);
        
      Renvoyer Phi
<span style="font-size:0.5em;"> Pseudo-Code de l'algorithme d'Edmond Karp </span>

- G_c le graphe des capacités

</div>
</div>

---
## Algorithme d'Edmond-Karp
### Recherche du Chemin augmentant
Parcours en largeur : plus court chemin en nombre d'arc

-> Compléxité en $O(|V|*|E|²)$

Renvoie $(p,d\phi)$ un chemin augmentant

---

### Mise à jour de $\varphi$
$\forall e=(u,v) \in p$ 
si e est un  arc avant:
$\phi(u,v) \leftarrow \phi(u,v)+ d\phi$

si $e=(v,u)$ est un arc arrière :
$\phi(u,v) \leftarrow \phi(u,v)-d\phi$

### Mise à jour de $G_a$
$\forall e =(u,v) \in p, C_r(u,v) \leftarrow C_r(u,v) - d\phi$
$\forall e =(u,v) \in p, C_r(v,u) \leftarrow C_r(v,u) + d\phi$


---
## Dans le cas du stade de France
Capacité proportionnelle à la largeur de la rue.
Le puit: un noeud fictif relié par des arêtes de capacité maximale aux stations de transport en commun.
La source : Le stade de France
Objectif: 
- Le flot (un débit de personne) maximal, pour évacuer le plus éfficacement la foule.
---
### Graphe de capacité
![alt text](images/fin_graph.png)

---
### Résultats expérimentaux
Valeur du flot : $23$, débit : $46 pers/s$, temps :$30min$ 
($WP: 10, 20 pers/s$)
![flot final](images/final_flow.png)

---
# 5. Analyse des résultats

---
## Comparaison W-P v. E-K
- Pas de Cannibalisme.
- Pas de goulot détranglement.
- Performance:
  E-K 2 fois plus rapide pour le même niveau de sécurité

---
## Critique du résultat

![flow with map](images/flow_on_map.png)

---
# 6. Annexe

---
## Idée de preuve pour la correction et la complexité d'Edmond-Karp
Correction: équivalence entre absence de chemin augmentant et flot maximal atteint. 

Complexité : si (u,v) est critique à deux moments distincts alors, u s'est éloigné de s d'au moins 2 entre ces deux moments, or $\delta(s,u)\le|V|$ donc (u,v) n'est critique qu'au plus $\frac{|V|-2} {2}$ fois. D'où nombre d'itération majoré par $|E|*|V|$ or chaque itération a une complexité en $O(|E|)$: parcours en largeur + màj $\varphi$ et màj $G_a$. 
$\rightarrow O(|V|*|E|²)$

---
### Code - Imports et Classe de graphe:
<div class="columns">
<div>

![alt text](code_images/image-22.png)
![alt text](code_images/image-6.png)
</div>
<div>

![alt text](code_images/image-7.png)
</div>

---

### Code - Classe de tas max:
<div class="columns">
<div>

![alt text](code_images/image-8.png)
</div>
<div>

![alt text](code_images/image-9.png)
</div>


---

### Code - Widest-Path, reconstruction du chemin:
<div class="columns">
<div>

![alt text](code_images/image-10.png)
</div>
<div>

![alt text](code_images/image-11.png)</div>

---

### Code - Edmond-Karp et fonctions associées:
<div class="columns">
<div>

![alt text](code_images/image-24.png)

</div>
<div>

![alt text](code_images/image-23.png)

</div>

---

### Code - Edmond-Karp et fonctions associées:
<div class="columns">
<div>

![alt text](code_images/image-14.png)

</div>
<div>

![alt text](code_images/image-15.png)

</div>

---

### Code - Edmond-Karp et fonctions associées:
<div class="columns">
<div>

![alt text](code_images/image-16.png)

</div>

---
### Code - Graphe de capacité
<div class="columns">
<div>

Où DATA est un tableau contenant N triplets $(d,f,c)$ 
- $d,f \in V$ les extremités d'une arète 
- $c \in \mathbb{N}$ sa largeur.

Et Vertices un set contenant les somemts de G.
</div>
<div>

![alt text](code_images/image-17.png)
</div>

---
### Code - Affichage des graphes
Avec Positions un tableau associant à chaque noeud une position sur l'image. 
![alt text](code_images/image-21.png)
![alt text](code_images/image-19.png)

---
### Code - Affichage des graphes

![alt text](code_images/image-20.png)