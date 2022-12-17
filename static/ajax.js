var pagination = Number(document.getElementById('pagination-page').getAttribute('data-page'))
var spinner = document.querySelector('.loader')
var table = document.querySelector('.order-table')

var page = 0
var pageNumber = Number(document.getElementById('page-number').innerText)

var filters = {
	payment: null,
	status: null,
	type: null
}

function changePage(path, token){
	spinner.style.display = 'flex'
	table.style.opacity = '.5'
	if (path == 'next') {
		page += 8
		pageNumber += 1
		filter(page, token)
	} else if (path == 'prev') {
		(page > 0) ? page -= 8 : null;
		if (pageNumber > 1)
			pageNumber -= 1
		filter(page, token)
	}
}


function constructor(data){
	let tree = String()
	let datetime = null
	let json = null

	data.forEach(order => {
		datetime = new Date(order.creationTime)
		json = JSON.stringify(order)
		tree += `
			<tr onclick='showOrder(${json})' class="order-table-row">
				<td><small>${order.id}</small></td>
				<td><small>${order.user}</small></td>
				<td><small class="available-${(order.paid) ? 'True' : 'False'}">${(order.paid) ? 'Да' : 'Нет'}</small></td>
				<td><small>${order.price}</small></td>
				<td><small class="order-status-color-${order.status}">${order.status}</small></td>
				<td><small>${datetime.toDateString()}</small></td>
				<td><small>${order.deliveryTime}</small></td>
				<td><small>${order.paymentMethod}</small></td>
			</tr>
		`
	})
	table.querySelectorAll('.order-table-row').forEach(row => row.remove())
	table.querySelector('tbody').innerHTML += tree
	spinner.style.display = 'none'
	table.style.opacity = '1'
	document.getElementById('page-number').innerText = pageNumber
}


function filter(page, token){
	let data = `{\n  "pageable": {\n    "pageNumber": ${page},\n    "pageSize": 8\n  }\n}`
	data = (filters['payment'] === null) ? data : data.replace('\n}', `,\n  "paymentMethod": "${filters['payment']}"\n}`)
	data = (filters['status'] === null) ? data : data.replace('\n}', `,\n  "status": "${filters['status']}"\n}`)
	data = (filters['type'] === null) ? data : data.replace('\n}', `,\n  "type": "${filters['type']}"\n}`)
	fetch('http://admin.motitashkent.uz/api/v1/order/filter', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'Authorization': token
		},
		body: data
	}).then(response => response.json()).then(data => constructor(data))
}


function segregate(token){
	let type = document.querySelector('#filter-order-type').value
	let status = document.querySelector('#filter-order-status').value
	let payment = document.querySelector('#filter-payment-type').value

	filters['type'] = (type == '-') ? null : type
	filters['status'] = (status == '-') ? null : status
	filters['payment'] = (payment == '-') ? null : payment

	spinner.style.display = 'flex'
	table.style.opacity = '.5'
	pageNumber = 1
	page = 0
	filter(page, token)
}