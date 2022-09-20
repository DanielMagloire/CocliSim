<template>
	<div></div>
</template>

<script>

var Highcharts = require('highcharts');
export default {
	name: "tSolChart",
	props: {
		courbePpdTsol: {
			required: false
		}, 
		pointPpdTsol: {
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
            min: 5,
            max: 45,
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
			positions.push(Math.log10(1))
            for (var tick = 10; tick <= 100; tick += 10)
                positions.push(Math.log10(tick))
            return positions
			}
        },
        series: [{
			name: 'pointPpdTsol',
			line: {
				visible: false,
			},
			data: this.pointPpdTsol,
			color: '#3498db'
			},{name: 'courbePpdTsol',
			marker: {
				enabled: false,
			},
			data: this.courbePpdTsol,
			color: '#3498db'
			}]
		});
	},
	beforeDestroy: function() {
		this.target.destroy();
	},
	methods:{
		redraw(){
			this.target.series[0].setData(this.pointPpdTsol, true)
		}
	},
	watch:{
		pointPpdTsol(){
			this.redraw()
		},
		courbePpdTsol(){
			this.target.series[1].setData(this.courbePpdTsol, true)
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