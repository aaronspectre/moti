function mostSelling(report){
	let series = Array()
	let categories = Array()
	report.forEach(item => {
		series.push({x: 'x', y: item.count})
		categories.push(item.name)
	})
	let mostSellingOptions = {
		chart: {
			type: 'bar'
		},
		plotOptions: {
			bar: {
				borderRadius: 4,
				horizontal: true
			}
		},
		series: [{
			name: 'Products',
			data: series
		}],
		xaxis: {
			categories: categories,
			label: {
				text: 'Product'
			}
		},
		labels: categories
	}

	let mostSellingChart = new ApexCharts(document.getElementById('most-selling-chart'), mostSellingOptions)
	mostSellingChart.render()
}

function paymentMethods(report){
	let series = [report.paymeAmount, report.clickAmount, report.cashAmount]
	let paymentMethodsOptions = {
		chart: {
			width: 480,
			type: 'pie'
		},
		series: [12000, 10000, 11200],
		labels: ['Payme', 'Click', 'Cash']
	}

	let paymentMethodsChart = new ApexCharts(document.getElementById('payment-methods-chart'), paymentMethodsOptions)
	paymentMethodsChart.render()
}

function last30Orders(report){
	let series = Array()
	let categories = Array()

	report.forEach(item => {
		series.push(item.count)
		categories.push(item.day)
	})

	let last30OrdersOptions = {
		chart: {
			type: 'line',
			height: 500
		},
		series: [{
			name: 'Orders',
			data: series
		}],
		dataLabels: {
			enabled: true
		},
		stroke: {
			curve: 'smooth'
		},
		xaxis: {
			categories: categories
		}
	}

	let last30OrdersChart = new ApexCharts(document.getElementById('last-30-orders-chart'), last30OrdersOptions)
	last30OrdersChart.render()
}

function downloadReport(){
	let form = document.querySelector('#download-report form')
	let start = String(form.querySelector('input[name="start-date"]').value)
	let end = String(form.querySelector('input[name="end-date"]').value)
	start = new Date(start.split('-'))
	end = new Date(end.split('-'))
	form.querySelector('input[name="start"]').value = start.getTime()
	form.querySelector('input[name="end"]').value = end.getTime()
	form.submit()
}