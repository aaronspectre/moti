let panel = document.getElementById('add-form')
let orderf = document.getElementById('create-form')
let covers = document.querySelectorAll('.add-form-cover')
let form = document.querySelector('add-product-form')
let canvas = document.getElementById('qr')
let list = document.getElementById('add-form-section-order-list')


covers.forEach(cover => {
	cover.addEventListener('click', event => {
		panel.style.display = 'none'
		panel.style.opacity = 0

		orderf.style.display = 'none'
		orderf.style.opacity = 0

		list.querySelectorAll('li').forEach(li => li.remove())
	})
})


function showOrder(order) {
	panel.style.display = 'flex'
	panel.style.opacity = 1

	products = Array()
	for (var i = order.products.length - 1; i >= 0; i--) {
		products.push(`x${order.products[i].count} ${order.products[i].productName}`)
	}


	dateOptions = {day: 'numeric', month: 'short', hour: 'numeric', minute: 'numeric', hour12: false}

	document.getElementById('order-view-phone').innerText = order.user
	document.getElementById('order-view-price').innerText = order.price
	document.getElementById('order-view-status').innerText = order.status
	document.getElementById('order-view-date').innerText = new Date(order.creationTime).toLocaleDateString('en-US', dateOptions)
	document.getElementById('order-view-phone').innerText = order.user
	document.getElementById('order-view-delivery').innerText = order.deliveryTime
	document.getElementById('order-view-address').innerText = order.addressRes
	document.getElementById('order-view-comment').innerText = order.comments
	document.getElementById('order-view-order').innerText = products.join('\n')
	document.getElementById('order-view-type').innerText = order.orderType
	document.getElementById('order-view-pay').innerText = order.paymentMethod

	document.getElementById('order-cancel-button').setAttribute('href', `${window.origin}/update/${order.id}/CANCELLED`)
	document.getElementById('order-deliver-button').setAttribute('href', `${window.origin}/update/${order.id}/DELIVER`)

	qrcode = new QRious({
		element: canvas,
		background: 'white',
		foreground: '#292929',
		level: 'H',
		size: 182,
		value: String(order.id)
	})
}


function callForm(){
	orderf.style.display = 'flex'
	orderf.style.opacity = 1

	orderf.querySelector('#orders').removeAttribute('value')
}


function addProduct(){
	if (orderf.querySelector('#amount').value != '' && orderf.querySelector('#amount').value > 0){
		product = orderf.querySelector('#product').value.split('-')
		count = orderf.querySelector('#amount').value
		li = document.createElement('li')
		item = document.createElement('small')
		item.appendChild(document.createTextNode(`x${count} ${product[0]}`))
		li.appendChild(item)
		list.appendChild(li)

		orders = orderf.querySelector('#orders').value.split('?')
		orders = orders[0] == '' ? [] : orders
		orders.push(`{"productId": ${product[1]}, "count": ${count}}`)
		orderf.querySelector('#orders').value = orders.join('?')
	}
}


function clearProducts(){
	list.querySelectorAll('li').forEach(li => li.remove())
}


function submitOrder(){
	orders = orderf.querySelector('#orders').value.split('?')
	orderf.querySelector('#orders').value = `[${orders.join(',')}]`
	console.log(orderf.querySelector('#orders').value)
	orderf.querySelector('.add-product-form').submit()
}