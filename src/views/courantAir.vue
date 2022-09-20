<template>
    <div id="divCourantAir">
        <div class="wrapper">
            <div class="valueControlBox" id="ctlTair2">
                <label for="tAir2">Température sèche de l'air</label>
                <input type="range" id="tAir2" name="tAir2" min="20" max="26" step="0.1" v-model.number="tAir2">
                <span class="valueDisplay" >
                    <span id="valTair2">{{ tAir2 }}</span>
                    <span > °C</span>
                </span>
            </div>
            <div class="valueControlBox" id="ctlVair2">
                <label for="vAir2">Vitesse moyenne de l'air</label>
                <input type="range" id="vAir2" name="vAir2" min="0.05" max="0.5" step="0.01" v-model.number="vAir2">
                <span class="valueDisplay" >
                    <span id="valVair2">{{ vAir2 }}</span>
                    <span > m/s</span>
                </span>
            </div>
            <div class="valueControlBox" id="ctlTurbulence">
                <label for="turbulence">Turbulence</label>
                <input type="range" id="turbulence" name="turbulence" min="10" max="60" step="1" v-model.number="turbulence">
                <span class="valueDisplay" >
                    <span id="valTurbulence">{{ turbulence }}</span>
                    <span > %</span>
                </span>
            </div>
        </div>
        <div id="containerCourantAir">
                <div id="placeholderTurbulence" class="placeholder">
                    <turbulenceChart :courbePpdTurbulence = "initPlotTurbulence" :pointPpdTurbulence = "updatePlotTurbulence"/>
                </div>
        </div>
    </div>
</template>

<style scoped>
#divCourantAir {
    display: inline-block;
    align-items: center;
    flex-direction: column;
}
.wrapper {
    display: flex;
    width: 100%;
    justify-content: center;
}
.valueControlBox {
	margin: 6px 50px;
}

</style>

<script>

import turbulenceChart from '../components/turbulenceChart.vue'
import { getAPI } from '../axios-api'

export default {
    components: {
        turbulenceChart,
    },
    data: function () {
        return {
            tAir2: 20,
            vAir2: 0.1,
            turbulence: 40,
            APICourbeTurbulence: [],
            APIPointTurbulence: [],
        }
    },
    methods: {
        getPlotTurbulence: function(){
            getAPI.get('/api/plotturbulence/', {
                params:{
                    tAir2: this.tAir2, 
                    vAir2: this.vAir2, 
                    turbulence: this.turbulence,
                }
            })
            .then(response => {
                console.log('API has emmited plotturbulence')
                this.APICourbeTurbulence = response.data
            })
            .catch(err => {
                console.log(err)
            })
        },
        getPointTurbulence: function(){
            getAPI.get('/api/pointturbulence/', {
                params:{
                    tAir2: this.tAir2, 
                    vAir2: this.vAir2, 
                    turbulence: this.turbulence,
                }
            })
            .then(response => {
                console.log('API has emmited pointturbulence')
                this.APIPointTurbulence = response.data
            })
            .catch(err => {
                console.log(err)
            })
        },
    },
    computed: {
        initPlotTurbulence: function () {
            var courbePpdTurbulence = []
            for (var i=0;i<46;i++){
                courbePpdTurbulence.push(this.APICourbeTurbulence[i])
            }

            return courbePpdTurbulence
        },
        updatePlotTurbulence: function () {
            var pointPpdTurbulence = []
            pointPpdTurbulence = this.APIPointTurbulence
            return pointPpdTurbulence
        },
        computedParams(){
            return `${this.tAir2}|${this.vAir2}|${this.turbulence}`
        }
    },
    watch:{
        computedParams: {
            handler: function() {
                this.getPlotTurbulence()
                this.getPointTurbulence()
            },
            deep: true,
            immediate: true
        },
    }
}
</script>