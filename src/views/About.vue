<template>
  <div class="wrapper">
  <div id="about-div">

    <img id="couv" src="images/Couverture_Dossier.jpg" alt="Couverture dossier Confort climatique" title="Couverture dossier Confort climatique" width="349" height="493"/>
    <div id="texte">
      <h1>Simulateur de confort climatique</h1>
      <p>Pour faire suite à la publication du dossier technique sur le confort climatique, Cylergie met à disposition ce petit simulateur permettant de mieux appréhender la théorie exposée dans ce document.</p>
      <br/>
      <p>Celui-ci se décompose en 3 parties dont l'utilisation est similaire, reprenant toutes des algorithmes et formules de la norme NF EN ISO 7730.</p>
      <br/>
      <h2>Confort climatique</h2>
      <p>On évalue ici le taux de personnes mécontentes sous les conditions climatiques définies. Les résultats sont présentés sous la forme de 2 graphiques, l'un de l'ASHRAE, l'autre issu de la norme NF EN ISO 7730.</p>
      <br/>
      <h2>Inconfort thermique local</h2>
      <p>Cette seconde partie permet de prendre en compte l'influence de différences de températures très localisées.</p>
      <br/>
      <h2>Courant d'air</h2>
      <p>On quantifie finalement l'effet sur le confort d'un courant d'air (vitesse moyenne et turbulence).</p>
      <br/>
      <p>Dans chaque partie, accessible en cliquant sur le bouton correspondant en haut de l'application, il suffit de faire varier les paramètres à l'aide des glissières et observer les résultats sous forme graphique. Un clic sur le bouton tout en haut à droite de l'application permet de faire apparaître (puis disparaître) des explications issues de la norme.</p>
    </div>
  </div>
  </div>
</template>

<style scoped>
.wrapper {
  display: flex;
  width: 100%;
  justify-content: center;
}
#about-div {
  display: flex;
	font-size:16px;
	text-align:justify;
  width: 1078px;
}
h1,h2,h3,h4,h5,h6 {
	font-size:100%;
	font-weight:bold;
	color: #3498db;
}
h1 {
	font-size:45px;
	margin:0px 0px 12px 0px;
}
#couv {
	padding-top: 12px;
}
#texte {
	font-size:16px;
	padding:12px 12px;
}
h2 {
	font-size:20px;
	margin:0px;
}
p {
	font-size:16px;
	margin:0px;
}
</style>