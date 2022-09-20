<template>
	<div></div>
</template>

<script>

var Highcharts = require('highcharts');
export default {
	name: "confortChart",
	props: {
		courbePpd: {
			required: false
		}, 
		pointPpd: {
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
            min: -3,
            max: 3,
            tickInterval: 1,
            gridLineWidth: 1,
            plotBands: [{
				from: -3,
				to: -2,
				color: '#80ffff'
            }, {
				from: -2,
				to: -1,
				color: '#c0ffff'
            }, {
				from: 1,
				to: 2,
				color: '#ffc0c0'
            }, {
				from: 2,
				to: 3,
				color: '#ff8080'
            }]
        },
        yAxis: {
			title: {
				text: null
			},
            min: 0,
            max: 100,
            tickInterval: 20
        },
        series: [{
			name: 'pointPpd',
			line: {
				visible: false,
			},
			data: this.pointPpd,
			color: '#3498db'
			},{name: 'courbePpd',
			marker: {
				enabled: false,
			},
			pointStart: -3,
			data: this.courbePpd,
			color: '#3498db'
			}]
		});
	},
	beforeDestroy: function() {
		this.target.destroy();
	},
	methods:{
		redraw(){
			this.target.series[0].setData(this.pointPpd, true)
		}
	},
	watch:{
		pointPpd(){
			this.redraw()
		},
		courbePpd(){
            this.target.series[1].setData(this.courbePpd, true)
        }
	}
}
</script>

<style scoped>
div {
	width: 535px;
	height: 260px;
	margin: 0px 3px 0px 3px;
}
</style>