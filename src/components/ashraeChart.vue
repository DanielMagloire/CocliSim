<template>
	<div></div>
</template>

<script>

var Highcharts = require('highcharts');
export default {
	name: "ashraeChart",
	props: {
		courbeAshrae: {
			required: false
		}, 
		pointAshrae: {
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
				min: 15,
				max: 35,
				tickInterval: 5,
				gridLineWidth: 1,
			},
			yAxis: {
				title: {
					text: null
				},
				min: 0,
				max: 15,
				tickInterval: 5
				
			},
		}),
		this.initSeries()
	},
	beforeDestroy: function() {
		this.target.destroy();
	},
	methods:{
		initSeries(){
			for (var i = 0 ; i < 10; i++) {
				if (i < 2) {
					this.target.addSeries({	
						name: 'zoneHiver'+(i+1),
						type: 'polygon',
						data: this.courbeAshrae[i],
						marker: {
							enabled: false,
						},
						color: '#56c4e3',
						opacity: 0.5
					}, false)
				}
				else if (i < 5) {
					this.target.addSeries({	
						name: 'zoneEte'+(i-1),
						type: 'polygon',
						data: this.courbeAshrae[i],
						marker: {
							enabled: false,
						},
						color: '#b91432',
						opacity: 0.5
					}, false)
				}
				else {
					this.target.addSeries({
						name: 'courbeAshrae'+(i-4),
						data: this.courbeAshrae[i],
						marker: {
							enabled: false,
						}
					}, false)
				}								
			}
			this.target.addSeries({
				name: 'pointAshrae',
				line: {
					visible: false,
				},
				data: this.pointAshrae,
				color: '#3498db'
			}, true)
		},
		redraw(){
			this.target.series[10].setData(this.pointAshrae, true)
		}
	},
	watch:{
		pointAshrae(){
			this.redraw()
		},
		courbeAshrae(){
			for (var i=0; i<10; i++){
				this.target.series[i].setData(this.courbeAshrae[i], true)
			}

		}
	}
}
</script>

<style scoped>
div {
	width: 535px;
	height: 315px;
	margin: 12px 3px 6px 3px;
}
</style>