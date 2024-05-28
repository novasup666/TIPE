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
2. Proposition de modélisation: Graphe de flot
3. Analyse des Algorithmes : Dijkstra (Widest Path) et Edmonds-Karp
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
</div>
<div>

<img src="image-1.png"  > 

<span style="font-size:0.5em;"> Issu de: These are the warning signs that a crowd is dangerously dense - @CNN</span>

</div>
</div>

---

![Speed/density](image.png)