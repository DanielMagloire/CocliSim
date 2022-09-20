<template>
	<div></div>
</template>

<script>

var Highcharts = require('highcharts');
export default {
	name: "asymTChart",
	props: {
		courbePpdAsymT: {
			required: false
		}, 
		pointPpdAsymT: {
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
				max: 35,
				tickInterval: 5,
				gridLineWidth: 1,
			},
        yAxis: {
			type: 'logarithmic',
            min: 1,
            max: 100,
			title: {
				text: null
			},
            tickPositioner: function () {
            var positions = [];
            for (var tick = 0; tick <= 100; tick += 10)
                positions.push(Math.log10(tick))
            return positions
			}
        },
			series: [{
				name: 'pointPpdAsymT',
				line: {
					visible: false,
				},
				data: this.pointPpdAsymT,
				color: '#3498db'
			}],
		}),
		this.initSeries()
	},
	beforeDestroy: function() {
		this.target.destroy();
	},
	methods:{
		initSeries(){
			for (var i = 0 ; i < 3; i++) {
				this.target.addSeries({
					name: 'courbePpdAsymT' + i,
					data: this.courbePpdAsymT[i],
					marker: {
						enabled: false,
					}
				}, false)
			}
			this.target.addSeries({	
				name: 'courbePpdAsymT3',
				data: this.courbePpdAsymT[3],
				marker: {
					enabled: false,
				}
			}, true)
		},
		redraw(){
			this.target.series[0].setData(this.pointPpdAsymT, true)
		}
	},
	watch:{
		pointPpdAsymT(){
			this.redraw()
		},
		courbePpdAsymT(){
			for(var i=0;i<4;i++)
				this.target.series[i+1].setData(this.courbePpdAsymT[i], true)
		}
	}
}
</script>

<style scoped>
div {
	width: 340px;
	height: 445px;
	margin: 6px 12px;
}
</style>