<template>
    <div id="divInconfortLocal">
        <div id="divInconfortLocalDeltaTc">
            <div class="valueControlBox" id="valueControlBoxLocalDeltaTc">
                <label for="deltaTv">Différence T° tête/chevilles</label>
                <input type="range" id="deltaTv" name="deltaTv" min="1.4" max="8" step="0.1" v-model.number="deltaTv">
                <span class="valueDisplay" >
                    <span id="valDeltaTv">{{ deltaTv }}</span>
                    <span > °C</span>
                </span>
            </div>

            <div class="containerInconfortLocal">
                    <div id="placeholderDeltaTv" class="placeholder">
                        <deltaTvChart :courbePpdDeltaTv = "initPlotDeltaTv" :pointPpdDeltaTv = "updatePlotDeltaTv"/>
                    </div>
            </div>
        </div>

        <div id="divInconfortLocalTsol">
            <div class="valueControlBox" id="valueControlBoxLocalTsol">
                <label for="tSol" >Température du sol</label>
                <input type="range" id="tSol" name="tSol" v-model="tSol" min="5" max="45" step="1">
                <span class="valueDisplay" >
                    <span id="valTsol">{{ tSol }}</span>
                    <span > °C</span>
                </span>
            </div>

            <div class="containerInconfortLocal">
                    <div id="placeholderTsol" class="placeholder">
                        <tSolChart :courbePpdTsol = "initPlotTsol" :pointPpdTsol = "updatePlotTsol"/>
                    </div>
            </div>
        </div>

        <div id="divInconfortLocalAsymT">

            <div class="valueControlBox" id="valueControlBoxLocalAsymT">
                <label for="tAsym">Asymétrie de température</label>
                <input type="range" id="tAsym" name="tAsym" v-model.number="tAsym" :min="min" :max="max" step="0.1">
                <span class="valueDisplay" >
                    <span id="valTasym">{{ tAsym }}</span>
                    <span > °C</span>
                </span>
            </div>

            <div class="valueControlBox" id="valueControlBoxChoixTypeParoi">
                <label for="choixTypeParoi">Type de paroi</label>
                <select id="choixTypeParoi" v-model.number="typeParoi" v-on:change="updateTypeParoi()">
                    <option value="0" >Plafond chaud</option>
                    <option value="1" >Mur froid</option>
                    <option value="2" >Plafond froid</option>
                    <option value="3" >Mur chaud</option>
                </select>
            </div>

            <div id="containerInconfortAsymT">
                    <div id="placeholderAsymT" class="placeholder">
                        <asymTChart :courbePpdAsymT = "initPlotAsymT" :pointPpdAsymT = "updatePlotAsymT"/>
                    </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
    #divInconfortLocal {
        display: flex;
        justify-content: center;
    }
    #divInconfortLocalDeltaTc {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    #divInconfortLocalTsol {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    #divInconfortLocalAsymT {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .valueControlBox {
        margin: 6px 3px 6px 29px;
    }    

</style>

<script>

import deltaTvChart from '../components/deltaTvChart.vue'
import tSolChart from '../components/tSolChart.vue'
import asymTChart from '../components/asymTChart.vue'
import { getAPI } from '../axios-api'

export default {
    components: {
        deltaTvChart,
        tSolChart,
        asymTChart,
    },
    data: function () {
        return {
            deltaTv: 4,
            tSol: 24,
            tAsym: 1,
            typeParoi: 0,
            min: 1,
            max: 23,
            APICourbeDeltaTv: [],
            APIPointDeltaTv: [],
            APICourbeTsol: [],
            APIPointTsol: [],
            APICourbeAsymT: [],
            APIPointAsymT: [],
        }
    },
    created: function() {
        this.getPlotDeltaTv()
        this.getPlotTsol()
        this.getPlotAsymT()
    },
    methods: {
        getPlotDeltaTv: function(){
            getAPI.get('/api/plotdeltatv/', {
                params:{
                    deltaTv: this.deltaTv, 
                    tSol: this.tSol, 
                    tAsym: this.tAsym,
                    typeParoi: this.typeParoi,
                }
            })
            .then(response => {
                console.log('API has emmited plotdeltatv')
                this.APICourbeDeltaTv = response.data
            })
            .catch(err => {
                console.log(err)
            })
        },
        getPointDeltaTv: function(){
            getAPI.get('/api/pointdeltatv/', {
                params:{
                    deltaTv: this.deltaTv, 
                    tSol: this.tSol, 
                    tAsym: this.tAsym,
                    typeParoi: this.typeParoi,
                }
            })
            .then(response => {
                console.log('API has emmited pointdeltatv')
                this.APIPointDeltaTv = response.data
            })
            .catch(err => {
                console.log(err)
            })
        },
        getPlotTsol: function(){
            getAPI.get('/api/plottsol/', {
                params:{
                    deltaTv: this.deltaTv, 
                    tSol: this.tSol, 
                    tAsym: this.tAsym,
                    typeParoi: this.typeParoi,
                }
            })
            .then(response => {
                console.log('API has emmited plottsol')
                this.APICourbeTsol = response.data
            })
            .catch(err => {
                console.log(err)
            })
        },
        getPointTsol: function(){
            getAPI.get('/api/pointtsol/', {
                params:{
                    deltaTv: this.deltaTv, 
                    tSol: this.tSol, 
                    tAsym: this.tAsym,
                    typeParoi: this.typeParoi,
                }
            })
            .then(response => {
                console.log('API has emmited pointtsol')
                this.APIPointTsol = response.data
            })
            .catch(err => {
                console.log(err)
            })
        },
        getPlotAsymT: function(){
            getAPI.get('/api/plotasymt/', {
                params:{
                    deltaTv: this.deltaTv, 
                    tSol: this.tSol, 
                    tAsym: this.tAsym,
                    typeParoi: this.typeParoi,
                }
            })
            .then(response => {
                console.log('API has emmited plotasymt')
                this.APICourbeAsymT = response.data
            })
            .catch(err => {
                console.log(err)
            })
        },
        getPointAsymT: function(){
            getAPI.get('/api/pointasymt/', {
                params:{
                    deltaTv: this.deltaTv, 
                    tSol: this.tSol, 
                    tAsym: this.tAsym,
                    typeParoi: this.typeParoi,
                }
            })
            .then(response => {
                console.log('API has emmited pointasymt')
                this.APIPointAsymT = response.data
            })
            .catch(err => {
                console.log(err)
            })
        },
        updateTypeParoi: function() {
            var typeParoi = this.typeParoi
            switch (typeParoi - 0) {
                case 0: // Plafond chaud : 1 < Tasym < 23
                    this.min = 1
                    this.max = 23
                    this.tAsym = 1
                    break
                case 1: // Mur froid : 6.8 < Tasym < 17
                    this.min = 6.8
                    this.max = 17
                    this.tAsym = 6.8
                    break
                case 2: // Plafond froid : 7.5 < Tasym < 17
                    this.min = 7.5
                    this.max = 17
                    this.tAsym = 7.5
                    break
                case 3: // Mur chaud : 7.5 < Tasym < 31
                    this.min = 7.5
                    this.max = 31
                    this.tAsym = 7.5
                    break
            }
        }
    },
    computed: {
        initPlotDeltaTv: function() {
            var courbePpdDeltaTv = []
            for (var i=0;i<41;i++)
                courbePpdDeltaTv.push(this.APICourbeDeltaTv[i])
            return courbePpdDeltaTv
        },
        initPlotTsol: function() {
            var courbePpdTsol = []
            for (var i=0;i<201;i++)
                courbePpdTsol.push(this.APICourbeTsol[i])
            return courbePpdTsol
        },
        initPlotAsymT: function() {
            var courbeAsymT = []
            for(var i = 0; i < 4; i++)
                courbeAsymT.push(this.APICourbeAsymT[i])
            return courbeAsymT
        },
        updatePlotDeltaTv: function() {
            var pointPpdDeltaTv = []
            pointPpdDeltaTv = this.APIPointDeltaTv
            return pointPpdDeltaTv
        },
        updatePlotTsol: function() {
            var pointPpdTsol = []
            pointPpdTsol = this.APIPointTsol
            return pointPpdTsol
        },
        updatePlotAsymT: function() {
             var pointPpdAsymT = this.APIPointAsymT
            var plotDataAsymT = []
            plotDataAsymT.push(pointPpdAsymT);
            return plotDataAsymT
        },
        computedParams(){
            return `${this.tAsym}|${this.tSol}|${this.deltaTv}`
        }
    },
    watch:{
        computedParams: {
            handler: function() {
                this.getPointDeltaTv()
                this.getPointTsol()
                this.getPointAsymT()
            },
            deep: true,
            immediate: true
        },
    }

}
</script>