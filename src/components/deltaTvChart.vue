<template>
	<div></div>
</template>

<script>

var Highcharts = require('highcharts');
export default {
	name: "deltaTvChart",
	props: {
		courbePpdDeltaTv: {
			required: false
		}, 
		pointPpdDeltaTv: {
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
            max: 8,
            tickInterval: 1,
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
			positions.push(Math.log10(1))
            for (var tick = 10; tick <= 100; tick += 10)
                positions.push(Math.log10(tick))
            return positions
			}
        },
        series: [{
			name: 'pointPpdDeltaTv',
			line: {
				visible: false,
			},
			data: this.pointPpdDeltaTv,
			color: '#3498db'
			},{name: 'courbePpdDeltaTv',
			marker: {
				enabled: false,
			},
			data: this.courbePpdDeltaTv,
			color: '#3498db'
			}]
		});
	},
	beforeDestroy: function() {
		this.target.destroy()
	},
	methods:{
		redraw(){
			this.target.series[0].setData(this.pointPpdDeltaTv, true)
		}
	},
	watch:{
		pointPpdDeltaTv(){
			this.redraw()
		},
		courbePpdDeltaTv(){
			this.target.series[1].setData(this.courbePpdDeltaTv, true)
		}
	}
}
</script>

<style scoped>
div {
        width: 340px;
        height: 510px;
        margin: 6px 0px;
}
</style>