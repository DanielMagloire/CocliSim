<template>
    <div id="divConfort">
        <div id="divConfortControls">
            <div class=wrapper>
            <div class="valueControlBox">
                <label for="tAir">Température sèche de l'air</label>
                <input type="range" id="tAir" name="tAir" min="10" max="30" step="0.1" v-model.number="tAir">
                <span class="valueDisplay" >
                    <span id="valTair" >{{ tAir }}</span>
                    <span>°C</span>
                </span>
            </div>

            <div class="valueControlBox">
                <label for="hRel">Humidité relative</label>
                <input type="range" id="hRel" name="hRel" min="0" max="100" step="1" v-model.number="hRel">
                <span class="valueDisplay" >
                    <span id="valHrel">{{ hRel }}</span>
                    <span>%</span>
                </span>
            </div>

            <div class="valueControlBox">
                <label for="clo">Isolation des vêtements</label>
                <input type="range" id="clo" name="clo" min="0" max="2" step="0.1" v-model.number="clo" v-on:change="updateClo">
                <span class="valueDisplay" >
                    <span id="valClo">{{ clo }}</span>
                    <span>clo</span>
                </span>
            </div>

            <img id="img_clo10" class="activeImgClo" src="images/CLO10.JPG" alt="Slip, chemise, pantalon, veste, chaussettes, chaussures." title="Slip, chemise, pantalon, veste, chaussettes, chaussures." />
            <img id="img_clo00" class="hidden" src="images/CLO00.JPG" alt="Rien..." title="Rien..." />
            <img id="img_clo01" class="hidden" src="images/CLO01.JPG" alt="Maillot de bain, slip." title="Maillot de bain, slip." />
            <img id="img_clo03" class="hidden" src="images/CLO03.JPG" alt="Slip, T-shirt, shorts, chaussettes fines, sandales." title="Slip, T-shirt, shorts, chaussettes fines, sandales." />
            <img id="img_clo05" class="hidden" src="images/CLO05.JPG" alt="Caleçon, chemise à manches courtes, pantalon léger, chaussettes fines, chaussures." title="Caleçon, chemise à manches courtes, pantalon léger, chaussettes fines, chaussures." />
            <img id="img_clo07" class="hidden" src="images/CLO07.JPG" alt="Slip, jupon, bas, robe, chaussures / Sous-vêtements, chemise, pantalon, chaussettes, chaussures." title="Slip, jupon, bas, robe, chaussures / Sous-vêtements, chemise, pantalon, chaussettes, chaussures." />
            <img id="img_clo13" class="hidden" src="images/CLO13.JPG" alt="Sous-vêtements à manches et jambes longues, chemise, pantalon, tricot col en V, veste, chaussettes, chaussures." title="Sous-vêtements à manches et jambes longues, chemise, pantalon, tricot col en V, veste, chaussettes, chaussures." />
            <img id="img_clo15" class="hidden" src="images/CLO15.JPG" alt="Sous-vêtements à manches et jambes courtes, chemise, pantalon, gilet, veste, manteau, chaussettes, chaussures." title="Sous-vêtements à manches et jambes courtes, chemise, pantalon, gilet, veste, manteau, chaussettes, chaussures." />
            <img id="img_clo20" class="hidden" src="images/CLO20.JPG" alt="Sous-vêtements à manches et jambes courtes, chemise, pantalon, veste, veste et pantalon isolants, chaussettes, chaussures." title="Sous-vêtements à manches et jambes courtes, chemise, pantalon, veste, veste et pantalon isolants, chaussettes, chaussures." />

        </div>

        <div class="wrapper">

            <div class="valueControlBox">
                <label for="tRay">Température moyenne de rayonnement</label>
                <input type="range" id="tRay" name="tRay" min="10" max="40" step="0.1" v-model.number="tRay" >
                <span class="valueDisplay" >
                    <span id="valTray">{{ tRay }}</span>
                    <span>°C</span>
                </span>
            </div>

            <div class="valueControlBox">
                <label for="vAir">Vitesse moyenne de l'air</label>
                <input type="range" id="vAir" name="vAir" min="0" max="1" step="0.1" v-model.number="vAir">
                <span class="valueDisplay" >
                    <span id="valVair">{{ vAir }}</span>
                    <span>m/s</span>
                </span>
            </div>

            <div class="valueControlBox">
                <label for="met">Métabolisme</label>
                <input type="range" id="met" name="met" min="0.8" max="3.5" step="0.1" v-model.number="met" v-on:change="updateMet">
                <span class="valueDisplay" >
                    <span id="valMet">{{ met }}</span>
                    <span>met</span>
                </span>
            </div>
					
            <img id="img_met12" class="activeImgMet" src="images/MET12.JPG" alt="Activité sédentaire (bureau, école, domicile, laboratoire)." title="Activité sédentaire (bureau, école, domicile, laboratoire)." />
            <img id="img_met08" class="hidden" src="images/MET08.JPG" alt="Repos, couché." title="Repos, couché." />
            <img id="img_met10" class="hidden" src="images/MET10.JPG" alt="Repos, assis." title="Repos, assis." />
            <img id="img_met14" class="hidden" src="images/MET14.JPG" alt="Station debout." title="Station debout." />
            <img id="img_met16" class="hidden" src="images/MET16.JPG" alt="Activité légère, debout (achats, laboratoire, industrie légère)." title="Activité légère, debout (achats, laboratoire, industrie légère)." />
            <img id="img_met20" class="hidden" src="images/MET20.JPG" alt="Activité moyenne, debout (vendeur, travail ménager, travail sur machine)." title="Activité moyenne, debout (vendeur, travail ménager, travail sur machine)." />
            <img id="img_met24" class="hidden" src="images/MET24.JPG" alt="Marche à plat." title="Marche à plat." />
        
        </div>

        </div>

        <div id="divConfortGraphs">
            <div id="containerPpd">
                <confortChart :courbePpd="initPlotConfort" :pointPpd="updatePlotConfort"/>
            </div>
            <div id="containerAshrae">
                <ashraeChart :courbeAshrae="initPlotAshrae" :pointAshrae="updatePlotAshrae"/>
            </div>
        </div>

    </div>
</template>


<script>

import confortChart from '../components/confortChart.vue'
import ashraeChart from '../components/ashraeChart.vue'

import { getAPI } from '../axios-api'

export default {
    components: {
        confortChart,
        ashraeChart,
    },
    data: function () {
        return {
            tAir: 20,
            tRay: 22,
            hRel: 50,
            vAir: 0.1,
            clo: 1,
            met: 1.3,
            APICourbeConfort: [],
            APIPointPpd: [],
            APICourbeAshrea: [],
            APIPointAshrae: [],
        }
    },
    created: function () {
        this.getPlotConfort()
        this.getPlotAshrae()
    },
    methods: {
        getPlotConfort: function(){
            getAPI.get('/api/plotconfort/', {
                params:{
                    CLO: this.clo, 
                    MET: this.met, 
                    WME: 0, 
                    TA: this.tAir, 
                    TR: this.tRay, 
                    VEL: this.vAir, 
                    RH: this.hRel, 
                    PA: 0,
                }
            })
            .then(response => {
                console.log('API has emmited plotconfort')
                this.APICourbeConfort = response.data
            })
            .catch(err => {
                console.log(err)
            })
        },
        getPointPpd: function(){
            getAPI.get('/api/pointppd/', {
                params:{
                    CLO: this.clo, 
                    MET: this.met, 
                    WME: 0, 
                    TA: this.tAir, 
                    TR: this.tRay, 
                    VEL: this.vAir, 
                    RH: this.hRel, 
                    PA: 0,
                }
            })
            .then(response => {
                console.log('API has emmited pointppd')
                this.APIPointPpd = response.data
            })
            .catch(err => {
                console.log(err)
            })
        },
        getPlotAshrae: function(){
            getAPI.get('/api/plotashrae/', {
                params:{
                    CLO: this.clo, 
                    MET: this.met, 
                    WME: 0, 
                    TA: this.tAir, 
                    TR: this.tRay, 
                    VEL: this.vAir, 
                    RH: this.hRel, 
                    PA: 0,
                }
            })
            .then(response => {
                console.log('API has emmited plotashrae')
                this.APICourbeAshrea = response.data
            })
            .catch(err => {
                console.log(err)
            })
        },
        getPointAshrae: function(){
            getAPI.get('/api/pointashrae/', {
                params:{
                    CLO: this.clo, 
                    MET: this.met, 
                    WME: 0, 
                    TA: this.tAir, 
                    TR: this.tRay, 
                    VEL: this.vAir, 
                    RH: this.hRel, 
                    PA: 0,
                }
            })
            .then(response => {
                console.log('API has emmited pointashrae')
                this.APIPointAshrae = response.data
            })
            .catch(err => {
                console.log(err)
            })
        },
        updateClo: function () {
            var clo = this.clo
            document.getElementById('valClo').innerHTML = (clo - 0).toFixed(1);
            var images = document.getElementById('divConfortControls').getElementsByClassName('activeImgClo');
            for(var i = 0; i < images.length; i++) {
                images[i].className = 'hidden';
            }
            var valClo = clo - 0;
            if ( valClo >= 0 && valClo < 0.1 ) {
                document.getElementById('img_clo00').className = 'activeImgClo';
            }
            if ( valClo >= 0.1 && valClo < 0.3 ) {
                document.getElementById('img_clo01').className = 'activeImgClo';
            }
            if ( valClo >= 0.3 && valClo < 0.5 ) {
                document.getElementById('img_clo03').className = 'activeImgClo';
            }
            if ( valClo >= 0.5 && valClo < 0.7 ) {
                document.getElementById('img_clo05').className = 'activeImgClo';
            }
            if ( valClo >= 0.7 && valClo < 1 ) {
                document.getElementById('img_clo07').className = 'activeImgClo';
            }
            if ( valClo >= 1 && valClo < 1.3 ) {
                document.getElementById('img_clo10').className = 'activeImgClo';
            }
            if ( valClo >= 1.3 && valClo < 1.5 ) {
                document.getElementById('img_clo13').className = 'activeImgClo';
            }
            if ( valClo >= 1.5 && valClo < 2 ) {
                document.getElementById('img_clo15').className = 'activeImgClo';
            }
            if ( valClo == 2 ) {
                document.getElementById('img_clo20').className = 'activeImgClo';
            }
        },
        updateMet: function () {
            var met = this.met - 0
            document.getElementById('valMet').innerHTML = (met - 0).toFixed(1);
            var images = document.getElementById('divConfortControls').getElementsByClassName('activeImgMet');
            for(var i = 0; i < images.length; i++) {
                images[i].className = 'hidden';
            }
            var valMet = met - 0;
            if ( valMet >= 0.8 && valMet < 1 ) {
                document.getElementById('img_met08').className = 'activeImgMet';
            }
            if ( valMet >= 1 && valMet < 1.2 ) {
                document.getElementById('img_met10').className = 'activeImgMet';
            }
            if ( valMet >= 1.2 && valMet < 1.4 ) {
                document.getElementById('img_met12').className = 'activeImgMet';
            }
            if ( valMet >= 1.4 && valMet < 1.6 ) {
                document.getElementById('img_met14').className = 'activeImgMet';
            }
            if ( valMet >= 1.6 && valMet < 2 ) {
                document.getElementById('img_met16').className = 'activeImgMet';
            }
            if ( valMet >= 2 && valMet < 2.4 ) {
                document.getElementById('img_met20').className = 'activeImgMet';
            }
            if ( valMet >= 2.4 && valMet < 2.8 ) {
                document.getElementById('img_met24').className = 'activeImgMet';
            }
            if ( valMet >= 2.8 && valMet < 3.4 ) {
                document.getElementById('img_met24').className = 'activeImgMet';
            }
            if ( valMet > 3.4 ) {
                document.getElementById('img_met24').className = 'activeImgMet';
            }
        }
    },
    computed: {
        initPlotConfort: function () {
            var courbePpd = []
            for(var i=0;i<61;i++){
                courbePpd.push(this.APICourbeConfort[i])
            }
            return courbePpd
        },
        initPlotAshrae: function () {
            var courbeAshrae = []
            for (var i=0;i<10;i++){
                courbeAshrae.push(this.APICourbeAshrea[i])
            }
            return courbeAshrae
        },
        updatePlotConfort: function() {
            var pointPpd = []    
            pointPpd.push(this.APIPointPpd)
            return pointPpd
        },
        updatePlotAshrae() {
            var pointHumiSpeci = []
            pointHumiSpeci.push(this.APIPointAshrae)
            return pointHumiSpeci
        },
        computedParams(){
            return `${this.tAir}|${this.tRay}|${this.met}|${this.clo}|${this.vAir}|${this.hRel}`
        }
    },
    watch:{
        computedParams: {
            handler: function() {
                this.getPointPpd()
                this.getPointAshrae()
            },
            deep: true,
            immediate: true
        },
    }
}
</script>

<style scoped>
#divConfort {
    display: flex;
    justify-content: center;
}
#divConfort img {
	border: 3px solid #3498db;
	margin: 6px 3px 0px 3px;
	padding: 0px;
	width: 263px;
}
#divConfortControls {
	display: flex;
	margin: 0px;
}
.valueControlBox {
	margin: 6px 3px;
}
#divConfortGraphs {
	display: flex;
    flex-direction: column;
	margin: 0px;
}
.wrapper {
    display: flex;
    flex-direction: column;
}
.activeImgClo {
	display: inline;
}
.activeImgMet {
	display: inline;
}

</style>
