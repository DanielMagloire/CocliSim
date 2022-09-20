<template>
	<div></div>
</template>

<script>

var Highcharts = require('highcharts');
export default {
	name: "turbulenceChart",
	props: {
		courbePpdTurbulence: {
			required: false
		}, 
		pointPpdTurbulence: {
			required: false
		},
	},
	data: function() {
		return {
			target: undefined
		}
	},
	created: function () {

	},
    mounted: function() {
		this.target = Highcharts.chart(this.$el, {
		title: {
			text: ''
        },
		chart: {
			reflow: true
		},
		legend: {
			enabled: false,
        },
        xAxis: {
            min: 0,
            max: 0.5,
            tickInterval: 0.1,
			gridLineWidth: 1,
        },
        yAxis: {
            type: 'logarithmic',
            min: 1,
            max: 100,
			title: {
				text: null
			},
            accessibility: {
                rangeDescription: 'Range: 1 to 100'
            },
            tickPositioner: function () {
            var positions = [];
			positions.push(Math.log10(1));
            for (var tick = 10; tick <= 100; tick += 10) {
                positions.push(Math.log10(tick));
            }
            return positions;
        }
        },
        series: [{
			name: 'pointPpdTurbulence',
			line: {
				visible: false,
			},
			data: this.pointPpdTurbulence,
			color: '#3498db'
			}, {name: 'courbePpdTurbulence',
			marker: {
				enabled: false,
			},
			data: this.courbePpdTurbulence,
			color: '#3498db'
			}]
		});
	},
	beforeDestroy: function() {
		this.target.destroy();
	},
	methods:{
		redrawPoint(){
			this.target.series[0].setData(this.pointPpdTurbulence, true)
		}
	},
	watch:{
		pointPpdTurbulence(){
			this.redrawPoint()
		},
        courbePpdTurbulence(){
            this.target.series[1].setData(this.courbePpdTurbulence, true)
        }
	}
}
</script>

<style scoped>
div {
	width: 1078px;
	height: 506px;
	margin: 6px 12px;
}
</style>