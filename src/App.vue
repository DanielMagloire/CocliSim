<template>
  <div id="app">
    <div id="nav">
      <img id="logo-engie" src="images/Logo_Engie_Solutions.png" alt="Logo ENGIE"/>
      <router-link to="/">a propos</router-link>
      <router-link to="/confort-climatique">confort</router-link>
      <router-link to="/inconfort-thermique">inconfort</router-link>
      <router-link to="/courant-air">courant d'air</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>

</script>

<style>
* {
	margin:0;
	padding:0;
	box-sizing: border-box;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.hidden {
	display: none;
}
/****** Barre de navigation ******/

#logo-engie {
    height: 8vh;
	filter: brightness(0) invert(1);
}
#nav {
  display: flex;
	justify-content: space-around;
	height: 8vh;
	background-color: #3498db;
  margin-bottom: 50px;
}
#nav a {
	line-height: 8vh;
	text-align: center;
	text-decoration: none;
	text-transform: uppercase;
	transition: 0.5s;
	color: #fff;
	font-size:14px;
	letter-spacing: 3px;
	font-weight:bold;
	width: 100%;
}
#nav a:hover {
	color: #3498db;
	background-color: #fff;
}

#nav a.router-link-exact-active {
  color: #3498db;
  background-color: #fff;
}

/****** Elements interactifs ******/

.valueControlBox {
	border: 1px solid #b0a6ba;
	width: 264px;
	padding: 0px 0px 3px 0px;
	margin: 3px;
	display: inline-block;
}
.valueControlBox label {
	background: #3498db;
	font-size: 11px;
	font-weight: bold;
	color: #fff;
	text-align: center;
	display: block;
	padding: 3px;
	margin: 0px 0px 3px 0px;
}
.valueControlBox input[type=range] {
	width: 200px;
	margin: 3px 0px 3px 6px;
  float: left;
}
.valueControlBox select {
	width: 258px;
	margin: 3px;
}
.valueControlBox .valueDisplay {
	font-size: 12px;
	float: right;
	margin: 3px 6px 0px 0px;
}
</style>
